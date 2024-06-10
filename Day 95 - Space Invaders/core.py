import pygame, os
from interface import *
from game import *

class Core:

    WIDTH = 800
    HEIGHT = 900
    FPS = 60
    WHITE = (240, 240, 255)
    BLACK = (40, 40, 43)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Cosmic Assault by yakubszatkowski')
        mixer.init()
        self.core_run = True
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.main_directory = os.path.dirname(os.path.realpath(__file__))

        self.draw_text_outline("Loading...", 50, self.WIDTH // 2, self.HEIGHT // 2)
        pygame.display.update()

        self.menu_music = mixer.Sound(os.path.join(self.main_directory, 'sound/menu_music.mp3'))
        self.game_music = mixer.Sound(os.path.join(self.main_directory, 'sound/game_music.mp3'))
        self.shoot_sound = mixer.Sound(os.path.join(self.main_directory, 'sound/shoot_sound.mp3'))
        self.being_shoot_sound = mixer.Sound(os.path.join(self.main_directory, 'sound/being_shoot_sound.mp3'))

        self.main_menu = MainMenu(self)
        self.credit_menu = CreditsMenu(self)
        self.options_menu = OptionsMenu(self)
        self.game = Game(self)
        self.current_display = self.main_menu


    def game_loop(self):
        while self.core_run:
            self.current_display.check_events()
            self.current_display.display()

            pygame.display.update()
            self.clock.tick(self.FPS)


    def find_img(self, path):
        img_path = os.path.join(self.main_directory, path)
        loaded_img = pygame.image.load(os.path.join(img_path))
        return loaded_img


    def draw_text(self, text, size, x, y, color):
        font = pygame.font.SysFont('comicsans', size)
        text_surface = font.render(text, 1, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)


    def draw_text_outline(self, text, size, x, y):
        self.draw_text(text, size, x-3, y-3, self.BLACK)
        self.draw_text(text, size, x+3, y-3, self.BLACK)
        self.draw_text(text, size, x-3, y+3, self.BLACK)
        self.draw_text(text, size, x+3, y+3, self.BLACK)
        self.draw_text(text, size, x, y, self.WHITE)
