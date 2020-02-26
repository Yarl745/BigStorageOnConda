from kivy.app import App

from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class ImgBtn(Image, ButtonBehavior):
    def __init__(self):
        super().__init__()
        flag = True

    def on_press(self):
        super().on_press()
        if self.flag:
            self.source = 'CIRCLE_PRESSED.png'
        else:
            self.source = 'CIRCLE_DEFAULT.png'
        self.flag = not self.flag
        print('ON_PRESS')

    # def on_touch_down(self, touch):
    #     if self.ids.circle_id.collide_point(*touch.pos):
    #         touch.grab(self)
    #         return True
    #
    # def on_touch_up(self, touch):
    #     if

    # def on_release(self):
    #     self.source = 'CIRCLE_PRESSED_RED.png'
    #     print('ON_RELEASE')


class circleApp(App):
    def build(self):
        w = Widget()
        # w.add_widget(ImgBtn())
        return Widget()


if __name__ == '__main__':
    circleApp().run()
    pass
