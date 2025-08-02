from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem, IconRightWidget
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton
from order.order import OrderItem

KV = """
<OrderItemScreen>:
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
                id: ois_item_name
                size_hint_y: .1
                font_style: "H5"
                halign: "center"
        
            MDLabel:
                id: ois_item_description
                size_hint_y: .1
                font_style: "H6"
                halign: "center"
            MDTextField:
                id: ois_note
                mode: "rectangle"
                hint_text: "Info"

            MDTextField:
                id: ois_quantity
                mode: "rectangle"
                text: "1"
                helper_text: "Ilość"

            
            BoxLayout:
                MDRoundFlatIconButton:
                    text: "Zamów"
                    icon: "plus"
                    on_press: root.do_order()
                MDRoundFlatIconButton:
                    id: ois_item_add
                    text: "Dodatki"
                    icon: "plus"
                    on_press: root.open_addition_dialog()
                

"""
Builder.load_string(KV)
class OrderItemScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item = None
        self.dialog = None
        self.selected_additions = set()

    def on_enter(self, *args):
        super().on_enter(*args)
        session_data = MDApp.get_running_app().session_data
        print("on_enter", session_data.menu.find_item_by_id(session_data.target_item))

        self.item = session_data.menu.find_item_by_id(session_data.target_item)
        self.dialog = None
        self.selected_additions = set()

        self.ids.ois_item_name.text = self.item.name or ""
        self.ids.ois_item_description.text = self.item.description or ""
        if not self.item.additions:
            self.ids.ois_item_add.disabled = True
        else:
            self.ids.ois_item_add.disabled = False

    def open_addition_dialog(self):
        if not self.item or not self.item.additions:
            return

        additions_box = MDBoxLayout(orientation="vertical", adaptive_height=True, spacing=dp(5))

        for addition in self.item.additions:
            list_item = OneLineAvatarIconListItem(text=addition.name)

            checkbox = MDCheckbox()
            # ✅ USTAWIAMY checkbox jako zaznaczony, jeśli już jest w zbiorze
            if addition.name in self.selected_additions:
                checkbox.active = True

            # Powiązanie zmiany stanu z aktualizacją selected_additions
            checkbox.bind(active=lambda cb, val, name=addition.name: self.on_checkbox_change(name, val))

            right_widget = IconRightWidget()
            right_widget.add_widget(checkbox)

            list_item.add_widget(right_widget)
            additions_box.add_widget(list_item)

        self.dialog = MDDialog(
            title="Wybierz dodatki",
            type="custom",
            content_cls=additions_box,
            buttons=[
                MDFlatButton(text="ANULUJ", on_release=lambda x: self.dialog.dismiss()),
                MDFlatButton(text="OK", on_release=lambda x: self.confirm_additions())
            ],
        )
        self.dialog.open()


    def on_checkbox_change(self, name, state):
        """Zapisuje zaznaczenia checkboxów"""
        if state:
            self.selected_additions.add(name)
        else:
            self.selected_additions.discard(name)

    def confirm_additions(self):
        self.dialog.dismiss()

    def go_back(self, obj):
        self.item = None
        self.dialog = None
        self.selected_additions = set()
        MDApp.get_running_app().session_data.target_item = None
        MDApp.get_running_app().custom_change_screen("menu_items")

    def do_order(self):
        _additions = [addition for addition in self.item.additions if addition.name in self.selected_additions]

        MDApp.get_running_app().session_data.order.append(OrderItem(
            item=self.item,
            additions=_additions,
            note=self.ids.ois_note.text,
            quantity=int(self.ids.ois_quantity.text)
        ))
        self.go_back(None)
