import pygame
from sprites import *

class Game:

    def __init__(self, core):
        self.core = core
        self.background_img = self.core.find_img('img/game_background.png')
        self.scaled_bg = pygame.transform.scale(self.background_img, (self.core.WIDTH, self.core.HEIGHT))

        self.sprites = pygame.sprite.Group()
        self.player = PlayerShip(self.core)

        self.sprites.add(self.player)


    def display(self):
        self.core.window.blit(self.scaled_bg, (0,0))
        self.sprites.update()
        self.sprites.draw(self.core.window)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.core.core_run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.core.current_display = self.core.main_menu
