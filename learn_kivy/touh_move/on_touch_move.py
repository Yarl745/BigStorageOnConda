from kivy.app import App
from kivy.uix.widget import Widget


class MyW(Widget):
    def on_touch_move(self, touch):
        if 'pos' in touch.profile:
            self.ids.label.text = str(touch.pos)


class kv2App(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    kv2App().run()
