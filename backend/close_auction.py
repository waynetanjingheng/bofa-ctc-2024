import pandas as pd
import numpy as np
from checking import check_trade
from trades import PassedTrades
from helper import _format_time

"""From the dataframe consisting of passed orders strictly after 16:00, calculate the open price and execute the trades.
"""


def get_close_auction_trades(df: pd.DataFrame) -> pd.DataFrame:
    """From the entire list of trades, obtain only those that are strictly after 16:00 AND are valid orders."""
    close_auction_passed_trades = PassedTrades()

    for _, trade in df.iterrows():
        if _format_time(trade["Time"]) >= _format_time("16:00:00"): # Ensure trade is within valid time window.
            check_trade(row=trade, passed_trades=close_auction_passed_trades)

    return close_auction_passed_trades.passed_trades


def find_close_price(trades: pd.DataFrame) -> float:
    # matching algo for wayne to add
    trades.groupby(["Quantity", "Price"], axis=0, as_index=False).sum()
    i = trades.iloc[trades["Quantity"].idxmax()]
    return i["Price"]
