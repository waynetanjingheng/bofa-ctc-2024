from order_queue import Order, OrderQueue
from datetime import datetime as dt

""" 
        self.order_id = order_id
        self.client_id = client_id
        self.rating = rating
        self.arrival_time = arrival_time
        self.price = price
        self.quantity = quantity
"""


def _format_time(arrival_time):
    return dt.strptime(arrival_time, "%H:%M:%S").time()


data = [
    Order(1, "B", 1, _format_time("09:30:00"), 101, 500),
    Order(2, "C", 2, _format_time("09:30:01"), 100, 100),
    Order(3, "A", 2, _format_time("09:31:00"), 100, 150),
    Order(4, "B", 1, _format_time("09:35:00"), 100, 50),
    Order(5, "E", 3, _format_time("09:40:00"), "Market", 10),
]

order_queue = OrderQueue(bids=data)

order_queue.match()
