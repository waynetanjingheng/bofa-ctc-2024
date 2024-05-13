from heapq import *
from datetime import datetime as dt


def _format_time(arrival_time):
    return dt.strptime(arrival_time, "%H:%M:%S").time()


class Order:
    def __init__(self, order_id, client_id, rating, arrival_time, price, quantity):
        self.order_id = order_id
        self.client_id = client_id
        self.rating = rating
        self.arrival_time = _format_time(arrival_time)
        self.price = price
        self.quantity = quantity

    def __lt__(self, other):
        """Determines how to compare priority between 2 Order objects"""
        if self.price == "Market" and other.price != "Market":
            return True  # Market orders have higher priority
        if self.price != "Market" and other.price == "Market":
            return False
        return (self.price, self.rating, self.arrival_time) < (
            other.price,
            other.rating,
            other.arrival_time,
        )

    def __eq__(self, other):
        return (self.price, self.rating, self.arrival_time) == (
            other.price,
            other.rating,
            other.arrival_time,
        )

    def __repr__(self):
        return f"{self.order_id, self.client_id, self.rating, self.arrival_time.strftime('%H:%M:%S'), self.price, self.quantity}"


class OrderQueue:
    def __init__(self, bids=[], asks=[]):
        self.bid_heap = bids
        self.ask_heap = asks
        heapify(self.bid_heap)
        heapify(self.ask_heap)

    def get_bid_count(self):
        return len(self.bid_heap)

    def get_ask_count(self):
        return len(self.ask_heap)

    def add_bid_order(self, new_bid):
        heappush(self.bid_heap, new_bid)

    def add_ask_order(self, new_ask):
        heappush(self.ask_heap, new_ask)

    def match(self):
        matches = 0
        
        while self.bid_heap:
            best_bid = heappop(self.bid_heap)
            print(best_bid)
