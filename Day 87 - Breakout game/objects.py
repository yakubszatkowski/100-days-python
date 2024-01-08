import pygame

class PlayerBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.width = width
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.center = (x, y)
        self.BALL_SPEED = 5

