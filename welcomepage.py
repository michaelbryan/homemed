import pdb
import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder


Builder.load_string("""
HomeScreen>:
    id: home_screen
    translateInput: translateInputID
    translateButton: translateButtonID
    translateLabel: labelID
    top_layout: topLayoutID
    dd_btn: btn_ddID
    my_window: my_windowID
    #my_window_2: my_window_2ID

    orientation: 'vertical'
    canvas:
        Color:
            rgb: root.get_background()
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        id: my_windowID
        size_hint: 1, None
        height: root.height
        pos: 0, root.height - self.height
        orientation: 'vertical'
        BoxLayout:
            id: topLayoutID
            size_hint: 1, None
            height: root.get_button_height()
            pos: 0, root.my_window.height-self.height
            Button:
                id: btn_ddID
                size_hint: 1, 1
                text: 'Usage Notes'
                font_size: root.get_button_font_size()
                on_release: root.drop_down.open(self)
                color: root.get_button_text_color()
                background_normal: root.get_button()
                background_down: root.get_button_down()
            Button:
                text: 'About'
                size_hint: 1, 1
                font_size: root.get_button_font_size()
                on_release: root.drop_down2.open(self)
                color: root.get_button_text_color()
                background_normal: root.get_button()
                background_down: root.get_button_down()

        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, None
            height: root.my_window.height-root.top_layout.height

            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                size_hint: 1, 1
                Label:
                    id: labelID
                    size_hint: .9, 1
                    text: 'Jordanian Translator'
                    color: root.get_text_color()
                    text_size: self.size
                    valign: 'middle'
                    halign: 'center'
                    font_size: root.get_title_font_size()
                    font_name: "DejaVuSans.ttf"
                    #font_name: "simpo.ttf"
                    #font_name: "5thgradecursive.ttf"
                    #font_name: "AGA-Rasheeq-Regular.ttf"

            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                size_hint: 1, .5
                TextInput:
                    id: translateInputID
                    text: ''
                    font_name: "DejaVuSans.ttf"
                    background_color: 1, 1, 1, 1
                    size_hint: .75, None
                    height: root.get_TI_height()
                    font_size: root.get_TI_font_size()
                    multiline: False
                    text_size: self.size
                    on_text_validate: root.translateButtonPressed()
                    hint_text: 'English or Arabic'

            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                size_hint: 1, .5
                Button:
                    id: translateButtonID
                    text: 'Translate'
                    font_size: root.get_button_font_size()
                    size_hint: None, None
                    size: root.get_button_width(), root.get_button_height()
                    valign: 'middle'
                    halign: 'center'
                    on_release: root.translateButtonPressed()
                    color: root.get_button_text_color()
                    background_normal: root.get_accent_button()
                    background_down: root.get_accent_button_down()

""")


button = Button(text='Hello world', font_size=14)

sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))

class TransApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    # populate our dictionary before we do anything...
    PopulateDB("jordict.txt")
    TransApp().run()