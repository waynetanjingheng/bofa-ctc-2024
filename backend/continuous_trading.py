import pandas as pd
import numpy as np
from checking import check_trade
from trades import PassedTrades
from helper import _format_time

"""From the dataframe consisting of passed orders between 09:30 and 16:00, execute the trades.
"""


def get_continuous_trading_trades(df: pd.DataFrame) -> pd.DataFrame:
    """From the entire list of trades, obtain only those that are 09:30 < T < 16:00 AND are valid orders."""
    continuous_trading_passed_trades = PassedTrades()

    for _, trade in df.iterrows():
        if (
            _format_time("09:30:00")
            <= _format_time(trade["Time"])
            < _format_time("16:00:00")
        ):  # Ensure trade is within valid time window.
            check_trade(row=trade, passed_trades=continuous_trading_passed_trades)

    return continuous_trading_passed_trades.passed_trades
