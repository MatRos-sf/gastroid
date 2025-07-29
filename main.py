from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = """
<ChoiceScreen>:
    BoxLayout:
        orientation: "vertical"
        
        BoxLayout:
            size_hint_y: 0.1
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
        
        AnchorLayout:
            canvas.before:
                Color:
                    rgba: 1, 0, 0, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
    
            BoxLayout:
                orientation: "vertical"
                size_hint: None, None
                spacing: "10dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                adaptive_size: True
    
                MDRaisedButton:
                    text: "Waiter"
                    on_release: app.root.current = "waiter"
                    style: "filled"

                MDRaisedButton:
                    text: "Chef"
                    on_release: app.root.current = "chef"
    
                MDRaisedButton:
                    text: "Cashier"
                    on_release: app.root.current = "cashier"
<WaiterScreen>:
    BoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back"
            on_release: app.root.current = "choice"
<ChefScreen>:
    BoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back"
            on_release: app.root.current = "choice"
<CashierScreen>:
    BoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back"
            on_release: app.root.current = "choice"
"""
Builder.load_string(KV)

class ChoiceScreen(MDScreen):
    pass


class WaiterScreen(MDScreen):
    pass


class ChefScreen(MDScreen):
    pass


class CashierScreen(MDScreen):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        sm = MDScreenManager()
        sm.add_widget(WaiterScreen(name="waiter"))
        sm.add_widget(ChefScreen(name="chef"))
        sm.add_widget(CashierScreen(name="cashier"))
        sm.add_widget(ChoiceScreen(name="choice"))
        sm.current = "choice"
        return sm


if __name__ == "__main__":
    MainApp().run()
