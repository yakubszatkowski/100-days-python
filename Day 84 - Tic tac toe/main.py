from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.properties import *
import itertools

LabelBase.register(name='Montserrat',
                   fn_regular='styling/Montserrat-Light.ttf')

win_conditions = {  # this can be changed to list
    1: (0, 1, 2),
    2: (3, 4 ,5),
    3: (6, 7, 8),
    4: (0, 3, 6),
    5: (1, 4, 7),
    6: (2, 5, 8),
    7: (2, 4, 6),
    8: (0, 4, 8),
}


class MainWindow(Screen):
    pass


class GameWindow(Screen):
    score_x = NumericProperty()
    score_o = NumericProperty()

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
        empty_board = self.game_board.children[::-1]
        board_state = [element.text for element in empty_board]

        for win_condition in win_conditions.values():  # ↓ this can be done more efficiently with list comprehension
            x_count = 0
            o_count = 0
            for position in win_condition:
                if board_state[position] == 'X':
                    x_count += True
                    if x_count == 3:
                        self.score_x += 1
                        self.on_leave()
                if board_state[position] == 'O':
                    o_count += True
                    if o_count == 3:
                        self.score_o += 1
                        self.on_leave()

        # after match is over (when point is being assigned) buttons should get disabled for 1 second and a
        # label should appear telling who was the winner of the match

        # print('X won!')
        # print('O won!')
        # print(f'{board_state[:3]}\n{board_state[3:6]}\n{board_state[6:9]}\n')  # testing


    def on_leave(self):
        for element in self.game_board.children[::-1]:  # this is supposed to iterate backwards
            element.text = ''


class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
