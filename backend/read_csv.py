import pandas as pd
from dotenv import load_dotenv
import os
from order_queue import Order, OrderQueue

load_dotenv()

EXAMPLE_INPUT_ORDERS_PATH = os.environ.get("EXAMPLE_INPUT_ORDERS_PATH")
EXAMPLE_INPUT_CLIENTS_PATH = os.environ.get("EXAMPLE_INPUT_CLIENTS_PATH")

order_df = pd.read_csv(EXAMPLE_INPUT_ORDERS_PATH)
client_df = pd.read_csv(EXAMPLE_INPUT_CLIENTS_PATH)

bids = []
asks = []
market_count = 0
limit_count = 0

# Convert orders into Order objects and store them according to side

""" 
        self.order_id = order_id
        self.client_id = client_id
        self.rating = rating
        self.arrival_time = arrival_time
        self.price = price
        self.quantity = quantity
"""

# Generate hashmap of client ratings

CLIENT_RATINGS = {
    client["ClientID"]: client["Rating"] for _, client in client_df.iterrows()
}

for _, order in order_df.iterrows():
    new_order = Order(
        order_id=order["OrderID"],
        client_id=order["Client"],
        rating=CLIENT_RATINGS[order["Client"]],
        arrival_time=order["Time"],
        price=order["Price"],
        quantity=order["Quantity"],
        side=order["Side"],
    )
    if order["Side"] == "Buy":
        bids.append(new_order)
    else:
        asks.append(new_order)
    if order["Price"] == "Market":
        market_count += 1
    else:
        limit_count += 1

# print(bids)
# print(asks)

order_queue = OrderQueue(
    bids=bids, asks=asks, market_count=market_count, limit_count=limit_count
)
