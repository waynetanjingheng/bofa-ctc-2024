import pandas as pd
import numpy as np
from data_fetch import get_initial_data
from open_auction import get_open_auction_trades, find_open_price
from continuous_trading import get_continuous_trading_trades
from close_auction import get_close_auction_trades, find_close_price
from trades import get_all_failed_trades
from reports import (
    generate_client_report,
    generate_exchange_report,
    generate_instrument_report,
)


def main():
    initial_data, CLIENT_RATINGS = get_initial_data()

    """OPEN AUCTION"""
    # Filter out only orders that arrived strictly before 09:30:00 and are valid. These will be used for the open auction.
    open_auction_passed_trades = get_open_auction_trades(df=initial_data)
    open_price = find_open_price(trades=open_auction_passed_trades)
    # TODO: simulate open auction trades

    """CONTINUOUS TRADING"""
    continuous_trading_passed_trades = get_continuous_trading_trades(
        df=open_auction_passed_trades
    )
    # TODO: simulate trading

    """CLOSE AUCTION"""
    close_auction_passed_trades = get_close_auction_trades(df=initial_data)
    close_price = find_close_price(trades=close_auction_passed_trades)
    # TODO: simulate trading

    """Generate Exchange Report"""
    failed_trades = get_all_failed_trades()
    generate_exchange_report()
    generate_client_report()
    generate_instrument_report()


if __name__ == "__main__":
    main()
