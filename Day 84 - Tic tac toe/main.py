from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase

LabelBase.register(name='Montserrat',
                   fn_regular='styling/Montserrat-Light.ttf')


class MainWindow(Screen):
    pass


class PvPWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class TicTacToe(App):
    def build(self):
        return Builder.load_file('tictactoe.kv')


if __name__ == '__main__':
    TicTacToe().run()
