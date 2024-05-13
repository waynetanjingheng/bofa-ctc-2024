import pandas as pd

"""Parse the input data, perform the necessary joins, and return the final dataframe."""


def get_initial_data() -> pd.DataFrame:
    clients = pd.read_csv("input_clients.csv")
    orders = pd.read_csv("input_orders.csv")
    instruments = pd.read_csv("input_instruments.csv")

    CLIENT_RATINGS = {
        client["ClientID"]: client["Rating"] for _, client in clients.iterrows()
    }

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

    final_join.sort_values("Time")  # Ensure that orders arrive in sequence.

    return final_join, CLIENT_RATINGS
