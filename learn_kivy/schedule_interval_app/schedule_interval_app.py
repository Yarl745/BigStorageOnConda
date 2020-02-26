from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class MyW(Widget):
    def __init__(self):
        super().__init__()
        self.counter = 1
        self.flag = False

    def my_callback(self, df):
        self.ids.label.text = "{0})  {1}".format(self.counter, str(df))
        self.counter += 1

    def on_touch_down(self, touch):
        if self.flag:
            Clock.unschedule(self.my_callback)
        else:
            Clock.schedule_interval(self.my_callback, 1 )
        self.flag = not self.flag


class schedule_interval_appApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    schedule_interval_appApp().run()
