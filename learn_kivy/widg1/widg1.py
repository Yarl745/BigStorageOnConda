from kivy.app import App
from kivy.uix.widget import Widget
# config
from kivy.config import Config


class MyW(Widget):

    def button_callback(self):
        if self.ids.t_input.text != '':
            self.ids.label.text = self.ids.t_input.text + '(by button_callback)'
        else:
            self.ids.label.text = 'Simple click..'

    def input_callback(self, text):
        self.ids.label.text = str(text) + '(by input_callback)'


class widg1App(App):

    def build(self):
        # Config.set('kivy', 'keyboard_mode', 'systemandmulti')
        return MyW()


if __name__ == '__main__':
    widg1App().run()
