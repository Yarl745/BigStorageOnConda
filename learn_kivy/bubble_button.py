from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class ButtonApp(App):
    def build(self):
        return FloatLayout().add_widget(BWidget())


class BWidget(Widget):
    def do_action(self):
        self.ids.bb.text = "I'm activated"


if __name__ == '__main__':
    ButtonApp().run()
