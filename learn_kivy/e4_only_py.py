import kivy
kivy.require('1.9.0') # Kivy ver where the code has been tested!

from kivy.app import App
from kivy.uix.label import Label


class OpaApp(App):
    def build(self):
        self.title = "It's my title MZFK"
        return Label(text='Ohhhh, shit')
    pass


if __name__ == '__main__':
    OpaApp().run()
