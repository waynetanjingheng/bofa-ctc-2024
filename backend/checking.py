import pandas as pd
from trades import add_failed_trade, PassedTrades


def check_trade(row: pd.core.series.Series, passed_trades: PassedTrades) -> bool:
    """Determines if a trade should be rejected or not.
    Failed trades should be added to the failed_trades dataframe.
    Passed trades should be added to the passed_trades dataframe.
    """
    if pd.isna(row["InstrumentID"]):
        add_failed_trade(row=row, reason="REJECTED-INSTRUMENT NOT FOUND")
        return False

    currencySet = (
        set(row["Currencies"].split(","))
        if isinstance(row["Currencies"], str)
        else set()
    )
    # Check currency presence
    if row["Currency"] not in currencySet:
        add_failed_trade(row=row, reason="REJECTED-MISMATCH CURRENCY")
        return False

    # Check lot size
    if row["Quantity"] % row["LotSize"] != 0:
        add_failed_trade(row=row, reason="REJECTED-INVALID LOT SIZE")
        return False

    # Check position
    if row["PositionCheck"] == "Y" and row["Side"] == "Sell":
        instrument = row["InstrumentID"]
        client = row["ClientID"]
        sell_size = row["Quantity"]

        # check hash map
        if (client, instrument) in passed_trades.completed_buys:
            buy_size = passed_trades.completed_buys[(client, instrument)]
            if sell_size <= buy_size:
                pass

            else:
                add_failed_trade(row=row, reason="REJECTED-POSITION CHECK FAILED")
                return False

        else:
            add_failed_trade(row=row, reason="REJECTED-POSITION CHECK FAILED")
            return False

        passed_trades.add_passed_trade(row=row)
        return True


# 2. Matching algo

# go into hashmap for instrument and currency which stores the 2 heaps
# if any sell => look at buy
#   - add sell to heap
#   - pop sell and compare to buy until invalid
# if any buy => look at sell
