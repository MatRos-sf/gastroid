from kivy.lang import Builder

from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingActionButton
KV = '''
<WaiterMenuScreen>:
    MDRoundFlatIconButton:
        text: "Dodaj"
        icon: "plus"
        pos_hint: {"center_x": .5, "center_y": .6}
        on_press: app.custom_change_screen("current_menu")
        
    MDRoundFlatIconButton:
        text: "Edytuj"
        icon: "playlist-edit"
        pos_hint: {"center_x": .5, "center_y": .4}
        
'''

Builder.load_string(KV)

class WaiterMenuScreen(MDScreen):
    pass

