from typing import Optional, List
from order.menu import Menu, get_menu_items

class Session:
    def __init__(self):
        self.menu = Menu([])

        # order section
        self.order: list = []

        # nav position
        self.target_item = None
        self.pos_item_by_menu = None


    def __str__(self):
        return f"Session(menu={self.menu}, order={self.order}, pos_item_by_menu={self.pos_item_by_menu})"

    def update_menu(self) -> None:
        self.menu.update_menu()

    def clear_position(self):
        self.pos_item_by_menu = None
        self.target_item = None
        print("Position cleared")

