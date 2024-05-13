import pandas as pd

"""Parse the input data, perform the necessary joins, and return the final dataframe."""


def get_initial_data():
    clients = pd.read_csv("input_clients.csv")
    orders = pd.read_csv("input_orders.csv")
    instruments = pd.read_csv("input_instruments.csv")

    initial_join = pd.merge(
        clients, orders, how="inner", left_on="ClientID", right_on="Client"
    )

    final_join = pd.merge(
        initial_join,
        instruments,
        how="left",
        left_on="Instrument",
        right_on="InstrumentID",
    )  # keep joins

    final_join.drop(columns="Client", inplace=True)
    final_join.drop(columns="Instrument", inplace=True)

    return final_join
