import pygame

class Menu:

    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.WIDTH/2, self.game.HEIGHT/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100