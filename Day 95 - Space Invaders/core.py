import pygame, os
from interface import *

class Core:

    WIDTH = 800
    HEIGHT = 1000
    FPS = 60

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Cosmic Assault by yakubszatkowski')
        self.core_run = True

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.main_menu = MainMenu(self)
        self.credit_menu = CreditsMenu(self)
        self.options_menu = OptionsMenu(self)
        
        self.current_display = self.main_menu


    def core_game_loop(self):
        while self.core_run:
            self.clock.tick(self.FPS)
            # self.check_core_events()
            self.current_display.check_events()
            self.current_display.display()
            pygame.display.update()
            

    # def check_core_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.core_run = False


    def find_img(self, path):
        main_directory = os.path.dirname(os.path.realpath(__file__))
        img_path = os.path.join(main_directory, path)
        loaded_img = pygame.image.load(os.path.join(img_path))
        return loaded_img