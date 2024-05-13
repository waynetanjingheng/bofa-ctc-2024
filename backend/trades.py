import pandas as pd

"""Define the dataframes for failed and passed trades, and the helper functions that interact with these dataframes.
Failed trades are intended to be global for logging and reporting purposes at the end of the trading day.
Passed trades are meant to have separate class instances for open auction, continuous trading, and close auction.
"""

failed_trades = pd.DataFrame(
    columns=[
        "REASON",
        "ClientID",
        "Currencies",
        "PositionCheck",
        "Rating",
        "Time",
        "OrderID",
        "Quantity",
        "Side",
        "InstrumentID",
        "Currency",
        "LotSize",
    ]
)


def add_failed_trade(row: pd.core.series.Series, reason: str) -> None:
    row["REASON"] = reason
    failed_trades.loc[len(failed_trades)] = row


def get_all_failed_trades() -> pd.DataFrame:
    return failed_trades


class PassedTrades:

    def __init__(self):
        self.passed_trades = pd.DataFrame(
            columns=[
                "ClientID",
                "Rating",
                "Time",
                "OrderID",
                "Quantity",
                "Side",
                "InstrumentID",
                "Currency",
                "LotSize",
            ]
        )
        self.completed_buys = {}  # hash map storing (client, stock): quantity

    def add_passed_trade(self, row: pd.core.series.Series) -> None:
        self.passed_trades.loc[len(self.passed_trades)] = row
