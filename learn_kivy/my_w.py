import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class MyW(Widget):
    def b_smash(self):
        self.ids.b1.text = 'Smashed'


class MyW1(Widget):
    pass


class MyW2(Widget):
    pass


class MyWApp(App):
    def build(self):
        b = BoxLayout()
        b.add_widget(MyW(), MyW1(), MyW2())
        return b


if __name__ == '__main__':
    MyWApp().run()
