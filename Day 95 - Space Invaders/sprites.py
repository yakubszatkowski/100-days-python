import pygame

class PlayerShip(pygame.sprite.Sprite):

    SHIP_WIDTH, SHIP_HEIGHT = 61, 50
    VELOCITY = 10

    def __init__(self, core):
        pygame.sprite.Sprite.__init__(self)
        self.core = core

        self.spaceship_img = self.core.find_img('img/spaceship_player.png')
        self.image = pygame.Surface((self.SHIP_WIDTH, self.SHIP_HEIGHT), pygame.SRCALPHA)
        self.image.blit(self.spaceship_img, (0,0))
        self.rect = self.image.get_rect()

        self.START_X, self.START_Y = (self.core.WIDTH/2 - self.SHIP_WIDTH/2), 820
        self.rect.topleft = (self.START_X, self.START_Y)


    def update(self):
        self.move()


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 10:
            self.rect.x -= self.VELOCITY
        if keys[pygame.K_RIGHT] and self.rect.right < 790:
            self.rect.x += self.VELOCITY
