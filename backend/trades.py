import pandas as pd

"""Define the dataframes for failed and passed trades, and the helper functions that interact with these dataframes."""

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

passed_trades = pd.DataFrame(
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
completed_buys = {}  # hash map storing (client, stock): quantity


def add_failed_trade(row: pd.core.series.Series, reason: str) -> None:
    row["REASON"] = reason
    failed_trades.loc[len(failed_trades)] = row


def add_passed_trade(row: pd.core.series.Series) -> None:
    passed_trades.loc[len(passed_trades)] = row
