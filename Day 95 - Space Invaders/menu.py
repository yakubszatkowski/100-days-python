import pygame

class MainMenu():
    BLACK = (40, 40, 43)

    def __init__(self, core):
        self.core = core

    def display(self):
        self.run_display = True
        while self.run_display:
            self.core.window.fill(self.BLACK)