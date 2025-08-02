from dataclasses import dataclass, field
from order.menu import Item, Addition
from typing import List

@dataclass
class OrderItem:
    item: Item
    additions: List[Addition]
    note: str
    quantity: int


    def additions_str(self):
        return " +".join([addition.name for addition in self.additions]) if self.additions else ""
class Order:
    def __init__(self, items: List[OrderItem]):
        self.items = items

    def total(self):
        raise NotImplementedError

    def payload(self):
        order = []
        raise NotImplementedError





