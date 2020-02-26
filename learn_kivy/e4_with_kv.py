import kivy

from kivy.app import App
from kivy.uix.label import Label


class e4_with_kvApp(App):
    def build(self):
        return Label()


if __name__ == '__main__':
    e4_with_kvApp().run()
