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


class VsComputerOption(Screen):
    pass


class Game(Screen):

    score_1 = NumericProperty()
    score_2 = NumericProperty()
    winner = StringProperty()

    def on_enter(self):
        self.game_board = self.ids.game_board
        self.game_board.clear_widgets()
        self.score_1 = 0
        self.score_2 = 0
        self.turn = 'player_1'

        for n in range(9):
            self.button = Button(text="", font_size=80, on_press=self.player_moves)
            self.game_board.add_widget(self.button)

    def on_leave(self, dt=None):
        self.winner = ''
        for button in self.game_board.children:
            button.disabled = False
        for element in self.game_board.children[::-1]:
            element.text = ''

    def is_win(self, figure):
        board_objects = self.game_board.children[::-1]
        board = [element.text for element in board_objects]
        for win_condition in win_conditions:
            count = sum(True for position in win_condition if board[position] == figure)
            if count == 3:
                print(f'{figure} win')
                return True
        return False


class PvP(Game):

    def player1_move(self, button):
        if button.text:
            pass
        else:
            button.text = 'O'
            self.is_win('O')

    def player2_move(self, button):
        if button.text:
            pass
        else:
            button.text = 'X'
            self.is_win('X')

    def player_moves(self, button):
        if self.turn == 'player_1':
            self.player1_move(button)
            self.turn = 'player_2'
        elif self.turn == 'player_2':
            self.player2_move(button)
            self.turn = 'player_1'


class VsComputerHard(Game):
    pass


class VsComputerEasy(Game):
    pass


class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
