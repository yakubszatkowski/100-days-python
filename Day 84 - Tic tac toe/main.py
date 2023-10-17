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


class PvPWindow(Screen):
    alternate_xo = itertools.cycle(['O', 'X'])

    def on_enter(self):
        game_board = self.ids.game_board
        game_board.clear_widgets()


        for n in range(9):
            button = Button(text="", on_press=self.clicked)
            game_board.add_widget(button)

    def clicked(self, button):
        button.text = next(self.alternate_xo)

class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
