from kivy.app import App
from kivy.uix.widget import Widget


class MyW(Widget):
    def on_touch_move(self, touch):
        if 'pos' in touch.profile:
            self.ids.button.pos = touch.pos


class move_buttonApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    move_buttonApp().run()
