from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text='hello world'
        self.pos=(100,100)
        self.size_hint=(.5,.5)


class LanguageLearnerApp(App):
    def build(self):
        return FunkyButton(
            # text='hello world',
            # pos=(100,100),
            # size_hint=(.5,.5)
        )


if __name__ == "__main__":
    LanguageLearnerApp().run()