from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MyW(Widget):
    counter = 0

    def on_touch_down(self, touch):
        if touch.button == 'left':
            self.add_widget(Button(text=str(touch.pos), pos=touch.pos, id = str(self.counter)))
            self.counter += 1
        elif touch.button == 'right':
            print(touch)


class addwidgApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    addwidgApp().run()
