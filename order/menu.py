import requests
from dataclasses import dataclass, field
from typing import Optional, List

URL = "http://127.0.0.1:8000"

@dataclass
class Addition:
    id: int
    name: str
    price: float
    is_available: bool


@dataclass
class Item:
    id: int
    menu: str
    sub_menu: Optional[str]
    name: str
    description: str
    additions: List[Addition]
    is_available: bool
    price: float

    @classmethod
    def from_dict(cls, data):
        # capture additions
        addition_collection = data.get("additions")
        additions = [Addition(**addition) for addition in addition_collection] if addition_collection else []
        return cls(
            id=data["id"],
            menu=data["menu"],
            sub_menu=data["sub_menu"],
            name=data["name"],
            description=data["description"],
            additions=additions,
            is_available=data["is_available"],
            price=data["price"],
        )


class Menu:
    ITEMS_ENDPOINT = URL + "/api/items/"

    def __init__(self, items: List[Item]):
        self.items = items
        self.menu: set[str] = self.extract_menu()
        print(f"{self.menu = }")

    def extract_menu(self) -> set[str]:
        menu = [item.menu for item in self.items]
        return set(menu)

    def get_items_by_menu(self, menu: str) -> List[Item]:
        return [item for item in self.items if item.menu == menu]

    def find_item_by_id(self, item_id: int) -> Item:
        #TODO: Warning this is slow and dangerous because lista can be empty
        return [item for item in self.items if item.id == item_id][0]

    def update_menu(self):
        self.items = get_menu_items(self.ITEMS_ENDPOINT)
        self.menu = self.extract_menu()
        print(self.menu)

def get_menu_items(url: str) -> List[Item]:
    get_response = requests.get(url, timeout=10)
    items = [Item.from_dict(item) for item in get_response.json()]
    return items
