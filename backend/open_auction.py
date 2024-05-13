import pandas as pd
import numpy as np
from checking import check_trade
from trades import PassedTrades
from helper import _format_time

"""From the dataframe consisting of passed orders strictly before 09:30:00, calculate the open price and execute the trades.
"""


def get_open_auction_trades(df: pd.DataFrame) -> pd.DataFrame:
    """From the entire list of trades, obtain only those that are strictly before 09:30:00 AND are valid orders."""
    open_auction_passed_trades = PassedTrades()

    for _, trade in df.iterrows():
        if _format_time(trade["Time"]) < _format_time("09:30:00"): # Ensure trade is within valid time window.
            check_trade(row=trade, passed_trades=open_auction_passed_trades)

    return open_auction_passed_trades.passed_trades


def find_open_price(trades: pd.DataFrame) -> float:
    # matching algo for wayne to add
    trades.groupby(["Quantity", "Price"], axis=0, as_index=False).sum()
    i = trades.iloc[trades["Quantity"].idxmax()]
    return i["Price"]
