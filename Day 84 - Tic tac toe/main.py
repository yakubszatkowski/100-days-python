from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.properties import *
from kivy.clock import Clock
import itertools


LabelBase.register(name='Montserrat', fn_regular='styling/Montserrat-Light.ttf')

win_conditions = [
    (0, 1, 2),
    (3, 4 ,5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (2, 4, 6),
    (0, 4, 8),
]


class MainWindow(Screen):
    pass


class Game(Screen):
    score_x = NumericProperty()
    score_o = NumericProperty()
    winner = StringProperty()

    def on_enter(self):
        self.alternate_xo = itertools.cycle(['O', 'X'])  # consider different colors?
        self.game_board = self.ids.game_board
        self.game_board.clear_widgets()
        self.score_x = 0
        self.score_o = 0

        for n in range(9):
            button = Button(text="", font_size=80, on_press=self.clicked)
            self.game_board.add_widget(button)


    def clicked(self, button):
        if button.text:
            pass
        else:
            button.text = next(self.alternate_xo)
            self.check_if_win()


    def check_if_win(self):

        def win(winner):
            for button in self.game_board.children:
                button.disabled=True
            self.winner = f'{winner} won!'
            Clock.schedule_once(self.on_leave, 1)

        empty_board = self.game_board.children[::-1]
        board_state = [element.text for element in empty_board]

        for win_condition in win_conditions:
            x_count = sum(True for position in win_condition if board_state[position] == 'X')
            o_count = sum(True for position in win_condition if board_state[position] == 'O')

            if x_count == 3:
                self.score_x += 1
                win('X')
            elif o_count == 3:
                self.score_o += 1
                win('O')


    def on_leave(self, dt=None):
        self.winner = ""
        for button in self.game_board.children:
            button.disabled = False
        for element in self.game_board.children[::-1]:  # this is supposed to iterate backwards
            element.text = ''


class PvP(Game):
    pass


class VsComputerOption(Screen):
    pass


class VsComputerEasy(Game):
    pass


class VsComputerHard(Game):
    pass


class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
