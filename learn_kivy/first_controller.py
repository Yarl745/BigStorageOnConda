import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty


class Controller(BoxLayout):
    info = StringProperty()
    label_wid = ObjectProperty()

    def do_action(self):
        self.label_wid.text = 'Button pressed'
        self.info = 'Bye'


class first_controllerApp(App):
    def build(self):
        return Controller(info='Hello, wrld')


if __name__ == '__main__':
    first_controllerApp().run()
