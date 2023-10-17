from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.button import Button
import itertools

LabelBase.register(name='Montserrat',
                   fn_regular='styling/Montserrat-Light.ttf')


class MainWindow(Screen):
    pass


class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_board = None
        self.alternate_xo = None

    def on_enter(self):
        self.alternate_xo = itertools.cycle(['O', 'X'])  # consider different colors?
        self.game_board = self.ids.game_board
        self.game_board.clear_widgets()

        for n in range(9):
            button = Button(text="", font_size=80, on_press=self.clicked)
            self.game_board.add_widget(button)

    def on_leave(self):
        for element in self.game_board.children[::-1]:  # this iterates backwards
            element.text = ''
            # print(element.text)

    def clicked(self, button):
        if button.text:
            pass
        else:
            button.text = next(self.alternate_xo)


class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
