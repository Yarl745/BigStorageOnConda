from kivy.app import App
from kivy.uix.widget import Widget


class MyW(Widget):
    def on_touch_down(self, touch):
        if self.ids.button.collide_point(*touch.pos):
            touch.grab(self)
            return True

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.ids.label.text = 'You touch button'
            touch.ungrab(self)
            return True
        else:
            self.ids.label.text = "You don't touch button"


class grab_appApp(App):
    def build(self):
        return MyW()


if __name__ == '__main__':
    grab_appApp().run()
