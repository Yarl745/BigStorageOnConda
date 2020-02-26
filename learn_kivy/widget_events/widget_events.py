from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MyW(Widget):
    def __init__(self):
        super().__init__()
        btn = Button(text="Button hleba")
        btn.bind(state=self.state_callback, on_press=self.on_press_callback)
        self.add_widget(btn)
        self.bind(pos=self.on_press_callback)

    def state_callback(self, obj, val):
        print(obj, val)

    def on_press_callback(self, obj):
        self.ids.label.text = "press on button"
        print('ho-ho-ho')


class widget_eventsApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    widget_eventsApp().run()
