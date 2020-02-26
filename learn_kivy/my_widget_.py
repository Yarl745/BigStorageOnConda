import kivy
from kivy.app import App
from kivy.uix.widget import Widget


class MyWidget(Widget):
    def b_smash(self):
        self.ids.f_but.text = 'SMASH'

    pass


class my_widgetApp(App):
    def build(self):
        return MyWidget()

    pass


if __name__ == '__main__':
    my_widgetApp().run()
