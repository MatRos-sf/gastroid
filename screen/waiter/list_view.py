from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, OneLineListItem

KV = """
<MenuListView>:
    BoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            size_hint_y: .1
            id: MDTopAppBar
            left_action_items: [["keyboard-backspace", lambda x: root.go_back(x)]]
            title: "Menu"
            elevation: 1   # shadow
        
        BoxLayout:
            orientation: "vertical"
            size_hint_y: .9
            MDLabel:
                size_hint_y: .1
                text: "Menu"
                halign: "center"
            
            MDScrollView:
                id: scroll_menu
                MDList:
                    id: menu

        
<MenuItemListView>:
    BoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            size_hint_y: .1
            id: MDTopAppBar
            left_action_items: [["keyboard-backspace", lambda x: root.go_back(x)]]
            title: "Menu"
            elevation: 1   # shadow
        
        BoxLayout:
            orientation: "vertical"
            size_hint_y: .9
            MDLabel:
                id: menu_name
                size_hint_y: .1
                text: "Menu"
                halign: "center"
            
            MDScrollView:
                id: scroll_menu
                MDList:
                    id: menu
    
"""
Builder.load_string(KV)

class MenuListView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session_data = None
        self.theme_cls.material_style = "M2"

    def refresh(self):
        """Czyści listę i ponownie ładuje dane."""
        self.ids.menu.clear_widgets()
    #     #self.on_enter()    #TODO: powtarzające menu coś jest nie tak

    def on_enter(self, *args):
        super().on_enter(*args)
        self.session_data = MDApp.get_running_app().session_data

        for m in self.session_data.menu.menu:
            self.ids.menu.add_widget(OneLineListItem(
                text=m,
                on_press=lambda x, m=m: self.on_press_menu(m)
            ))
    def on_leave(self, *args):
        super().on_leave(*args)
        self.ids.menu.clear_widgets()

    def on_press_menu(self, item_by_menu: str):
        self.session_data.pos_item_by_menu = item_by_menu
        MDApp.get_running_app().custom_change_screen("menu_items")

    def go_back(self, obj):
        self.session_data = MDApp.get_running_app().session_data
        if self.session_data.order:
            raise NotImplementedError()

        self.session_data.clear_position()
        self.manager.current = "waiter_menu"

class MenuItemListView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self, *args):
        super().on_enter(*args)
        session_data = MDApp.get_running_app().session_data
        menu_type = session_data.pos_item_by_menu
        self.ids.menu_name.text = menu_type.title()
        for m in session_data.menu.get_items_by_menu(menu_type):
            self.ids.menu.add_widget(OneLineListItem(
                text=m.name
            ))
    def on_leave(self, *args):
        super().on_leave(*args)
        self.ids.menu.clear_widgets()

    def go_back(self, obj):
        session_data = MDApp.get_running_app().session_data

        session_data.clear_position()
        app = MDApp.get_running_app()
        app.custom_change_screen("current_menu")