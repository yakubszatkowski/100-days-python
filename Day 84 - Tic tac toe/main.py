from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.button import Button
import itertools

LabelBase.register(name='Montserrat',
                   fn_regular='styling/Montserrat-Light.ttf')

win_conditions = {
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


    def check_if_win(self):  # check the logic of win conditions
        empty_board = self.game_board.children[::-1]
        board_state = [element.text for element in empty_board]

        print(f'{board_state[:3]}\n{board_state[3:6]}\n{board_state[6:8]}\n')  # testing

        for win_condition in win_conditions.values():
            x_count = 0
            o_count = 0
            for position in win_condition:
                if board_state[position] == 'X':
                    x_count += True
                    if x_count == 3:
                        print('X won!')
                if board_state[position] == 'O':
                    o_count += True
                    if o_count == 3:
                        print('O won!')


    def on_leave(self):
        for element in self.game_board.children[::-1]:  # this iterates backwards
            element.text = ''


    def clicked(self, button):
        if button.text:
            pass
        else:
            button.text = next(self.alternate_xo)
            self.check_if_win()


class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
