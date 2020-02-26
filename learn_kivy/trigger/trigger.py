from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


class MyW(Widget):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def my_callback(self, dt):
        self.ids.label.text = "-{}---{}-".format(self.counter, str(dt))
        self.counter += 1

    def on_touch_down(self, touch):
        trigger = Clock.create_trigger(self.my_callback)
        if touch.is_double_tap:
            trigger()


class triggerApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    triggerApp().run()
