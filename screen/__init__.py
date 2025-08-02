# from kivymd.uix.screenmanager import MDScreenManager
# from kivymd.uix.screen import MDScreen
# from kivymd.app import MDApp
# from kivy.lang.builder import Builder
#
# class MenuWaiterScreen(MDScreen):
#     pass
#
# class MenuScreen(MDScreen):
#     pass
#
# class ItemScreen(MDScreen):
#     pass
#
# class OrderScreen(MDScreen):
#     pass
#
# class SummaryScreen(MDScreen):
#     pass
#
# class EditOrderScreen(MDScreen):
#     pass
#
#
# class WaiterScreen(MDScreen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#         self.inner_waiter_manager = MDScreenManager()
#         self.inner_waiter_manager.add_widget(MenuWaiterScreen(name="menu_waiter"))
#         self.inner_waiter_manager.add_widget(MenuScreen(name="menu"))
#         self.inner_waiter_manager.add_widget(ItemScreen(name="item"))
#         self.inner_waiter_manager.add_widget(OrderScreen(name="order"))
#         self.inner_waiter_manager.add_widget(SummaryScreen(name="summary"))
#         self.inner_waiter_manager.add_widget(EditOrderScreen(name="order_view"))
#         self.inner_waiter_manager.current = "menu_waiter"
#
#
#     def add_order(self):
#         self.manager.current = "order"
#
#     def edit_order(self):
#         self.manager.current = "order_view"
#
