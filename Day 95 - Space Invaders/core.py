import pygame
from menu import *

class Core:

    WIDTH = 1000
    HEIGHT = 800
    FPS = 60

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Space Invaders by yakubszatkowski')

        self.run = True
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.main_menu = MainMenu(self)
        self.current_display = self.main_menu

