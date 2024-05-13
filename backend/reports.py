import pandas as pd
from collections import defaultdict
from trades import get_all_failed_trades

"""Exchange Report"""


def generate_exchange_report() -> None:
    failed_trades = get_all_failed_trades()
    failed_trades.to_csv("reports/output_exchange_report.csv")


"""Client Report"""
client_positions = defaultdict(
    lambda: defaultdict(int)
)  # <str (Client ID), <str (Instrument ID), int (position)>>


def add_client_position(client: str, instrument: str, quantity: int) -> None:
    client_positions[client][instrument] += quantity


def remove_client_position(client: str, instrument: str, quantity: int) -> None:
    client_positions[client][instrument] -= quantity


def generate_client_report():
    client_positions_df = pd.DataFrame(columns=["ClientID", "InstrumentID", "Position"])
    for client in client_positions:
        for instrument in client_positions[client]:
            client_positions_df.loc[len(client_positions_df)] = (
                client,
                instrument,
                client_positions[client][instrument],
            )

    client_positions_df.to_csv("reports/output_client_report.csv")


"""Instrument Report"""
instrument_data = defaultdict(lambda: defaultdict(float))
instrument_matchings = defaultdict(list)  # list: [matched_price, matched_volume]


def set_instrument_open_price(instrument: str, price: float):
    instrument_data[instrument]["open_price"] = price


def set_instrument_close_price(instrument: str, price: float):
    instrument_data[instrument]["close_price"] = price


def add_instrument_quantity(instrument: str, quantity: float):
    instrument_data[instrument]["total_traded_volume"] += quantity


def set_instrument_day_high(instrument: str, price: float):
    instrument_data[instrument]["day_high"] = price


def set_instrument_day_low(instrument: str, price: float):
    instrument_data[instrument]["day_low"] = price


def add_instrument_matching(instrument: str, price: float, volume: float):
    instrument_matchings[instrument].append((price, volume))


def calc_instrument_VWAP(instrument: str) -> float:
    numerator = sum(match[0] * match[1] for match in instrument_matchings[instrument])
    denomenator = sum(match[1] for match in instrument_matchings[instrument])
    return numerator / denomenator


def generate_instrument_report():
    instruments_df = pd.DataFrame(
        columns=[
            "InstrumentID",
            "Open Price",
            "Close Price",
            "Total Traded Volume",
            "Day High",
            "Day Low",
            "Volume Weighted Average Price",
        ]
    )
    for instrument in instrument_data:
        instruments_df.loc[len(instruments_df)] = (
            instrument_data[instrument]["open_price"],
            instrument_data[instrument]["close_price"],
            instrument_data[instrument]["total_traded_volume"],
            instrument_data[instrument]["day_high"],
            instrument_data[instrument]["day_low"],
            calc_instrument_VWAP(instrument),
        )

    instruments_df.to_csv("reports/output_instrument_report.csv")
