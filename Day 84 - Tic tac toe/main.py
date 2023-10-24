from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.properties import *
from kivy.clock import Clock

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
    player_1_current_figure = StringProperty()
    player_2_current_figure = StringProperty()
    winner = StringProperty()

    def on_enter(self):
        self.game_board = self.ids.game_board
        self.game_board.clear_widgets()
        self.score_1 = 0
        self.score_2 = 0
        self.turn = 'player_1'
        self.players = { 'Player 1': 'X', 'Player 2': 'O' }
        self.player_1_current_figure = self.players['Player 1']
        self.player_2_current_figure = self.players['Player 2']

        for n in range(9):
            self.button = Button(text="", font_size=80, on_press=self.player_moves)
            self.game_board.add_widget(self.button)

    def on_leave(self, dt=None):
        self.winner = ''
        for button in self.game_board.children:
            button.disabled = False
        for element in self.game_board.children[::-1]:
            element.text = ''
        self.players['Player 1'], self.players['Player 2'] = self.players['Player 2'], self.players[
            'Player 1']
        self.player_1_current_figure = self.players['Player 1']
        self.player_2_current_figure = self.players['Player 2']


    def is_win(self, figure):
        board_objects = self.game_board.children[::-1]
        board = [element.text for element in board_objects]

        for win_condition in win_conditions:
            count = sum(True for position in win_condition if board[position] == figure)
            if count == 3:
                for player, player_figure in self.players.items():
                    if player_figure == figure:
                        return True
        return False

    def is_draw(self):
        board_objects = self.game_board.children[::-1]
        board = [element.text for element in board_objects]
        if '' in board:
            return False
        else:
            return True


    def win(self, player):
        for button in self.game_board.children:
            button.disabled = True
        if player == 'Player 1':
            self.score_1 += 1
        else:
            self.score_2 += 1
        self.winner = f'{player} won!'
        Clock.schedule_once(self.on_leave, 1)

    def draw(self):
        for button in self.game_board.children:
            button.disabled = True
        self.winner = f'Draw!'
        Clock.schedule_once(self.on_leave, 1)


    def player_moves(self, button):
        if self.turn == 'Player_1':
            self.player1_move(button)
        elif self.turn == 'Player_2':
            self.player2_move(button)

    def player1_move(self, button):
        if button.text:
            pass
        else:
            button.text = self.players['Player 1']
            self.turn = 'Player_2'
            if self.is_draw():
                self.draw()
            if self.is_win(self.players['Player 1']):
                self.win('Player 1')


class PvP(Game):
    def player2_move(self, button):
        if button.text:
            pass
        else:
            button.text = self.players['Player 2']
            self.turn = 'Player_1'
            if self.is_draw():
                self.draw()
            if self.is_win(self.players['Player 2']):
                self.win('Player 2')


class VsComputerHard(Game):

    def player_moves(self, button):
        self.player1_move(button)
        self.npc_move()

    def npc_move(self):
        best_score = -800
        best_move = None

        board_objects = self.game_board.children[::-1]
        board_copy = board_objects[:]
        for position, cell in enumerate(board_copy):
            if cell.text == '':
                cell.text = self.players['Player 2']
                score = self.minimax(board_copy, False)
                cell.text = ''
                if score > best_score:
                    best_score = score
                    best_move = position
        board_objects[best_move].text = self.players['Player 2']


    def minimax(self, board, is_maxing):
        if self.is_win(self.players['Player 2']):
            return 1
        if self.is_win(self.players['Player 1']):
            return -1
        if self.is_draw():
            return 0

        if is_maxing:
            best_val = -800
            for position, cell in enumerate(board):
                if cell.text == '':
                    cell.text = self.players['Player 2']
                    value = self.minimax(board, not is_maxing)
                    cell.text = ''
                    best_val = max(best_val, value)
            return best_val
        else:
            best_val = 800
            for position, cell in enumerate(board):
                if cell.text == '':
                    cell.text = self.players['Player 1']
                    value = self.minimax(board, not is_maxing)
                    print(value)
                    cell.text = ''
                    best_val = min(best_val, value)
            return best_val


class VsComputerEasy(Game):
    pass


class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
