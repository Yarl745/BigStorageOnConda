from kivy.app import App
from kivy.uix.widget import Widget


class MyW(Widget):
    def on_touch_down(self, touch):
        print(touch.profile)
        if 'button' in touch.profile:
            # self.ids.button1.text = touch.button
            self.ids.button1.text = str(touch.pos)
            self.ids.label1.text = str(touch.profile)


class mykvApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    mykvApp().run()
