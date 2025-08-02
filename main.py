from kivymd.app import MDApp
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager

from screen.waiter import WaiterMenuScreen
from screen.waiter.list_view import MenuListView, MenuItemListView
from screen.waiter.order_view import OrderItemScreen, SummaryOrderScreen

from session import Session

if platform == "linux" or platform == "linux2":
    from kivy.core.window import Window
    Window.size = (300, 500)

class Gastroid(MDApp):
    def __init__(self, **kwargs):
        self.session_data = Session()
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.material_style = "M2"
        sm = ScreenManager()
        # waiter screens
        sm.add_widget(WaiterMenuScreen(name="waiter_menu"))
        sm.add_widget(MenuListView(name="current_menu"))
        sm.add_widget(MenuItemListView(name="menu_items"))
        sm.add_widget(OrderItemScreen(name="order_item"))
        sm.add_widget(SummaryOrderScreen(name="summary_order"))

        sm.current = "waiter_menu"

        return sm

    def custom_change_screen(self, screen):
        print("Current session:", self.session_data)
        if self.root.current == "waiter_menu" and screen == "current_menu":
            print("Update menu ...")
            self.session_data.update_menu()

        self.root.current = screen




if __name__ == "__main__":
    Gastroid().run()