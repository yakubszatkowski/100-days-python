import pygame
from menu import *

class Core:

    WIDTH = 1000
    HEIGHT = 800
    FPS = 60
    BLACK = (40, 40, 43)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Space Invaders by yakubszatkowski')

        self.core_run = True
        
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.main_menu = MainMenu(self)
        
        self.current_display = self.main_menu


    def game_loop(self):
        while self.core_run:
            self.check_events()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.core_run = False
