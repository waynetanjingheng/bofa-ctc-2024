import pandas as pd
from helper import _format_time
from checking import check_trade


def test_get_open_auction_trades(df: pd.DataFrame):
    for _, row in df.iterrows():
        if _format_time(row["Time"]) >= _format_time("09:30:00"):
            return False
    return True
