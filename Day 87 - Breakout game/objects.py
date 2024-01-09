import pygame

class PlayerBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width, self.height = 100, 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.VELOCITY = 5

    def update(self, *args, **kwargs):
        self.move()
        # self.check_collision()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.VELOCITY
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.VELOCITY


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width, self.height = 10, 10
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.BALL_SPEED = 5

        pygame.draw.circle(self.image, 'white', (self.width // 2, self.height // 2), 5)

    def update(self):
        self.rect.y += self.BALL_SPEED
        self.rect.x += self.BALL_SPEED