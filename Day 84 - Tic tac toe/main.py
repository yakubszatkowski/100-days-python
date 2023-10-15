from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


class TicTacToe(App):
    def __init__(self):
        super().__init__()
        Window.minimum_width = 400
        Window.minimum_height = 600

    def build(self):
        title_label = Label(text='Tic Tac Toe')
        return title_label


if __name__ == '__main__':
    app = TicTacToe()
    app.run()
