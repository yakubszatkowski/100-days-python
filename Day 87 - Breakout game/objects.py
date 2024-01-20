import pygame
import math

class PlayerBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width, self.height = 100, 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.VELOCITY = 5

    def update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.VELOCITY
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.VELOCITY


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, game, gameplay, player):
        super().__init__()
        self.game, self.gameplay = game, gameplay
        self.player = player
        self.width, self.height = 10, 10
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, 'white', (self.width // 2, self.height // 2), 5)
        self.rect.topleft = (x, y)

        self.direction = 120
        self.x_dir, self.y_dir = 0, 0
        self.velocity = 5


    def update(self):

        def bounce(angle):
            self.direction = 360 - self.direction
            self.direction += angle
            if self.direction >= 360:
                self.direction -= 360
            if 280 > self.direction > 260:
                self.direction += 25
            elif 100 > self.direction > 80:
                self.direction -= 25

            print(f'current direction: {self.direction}')
            return self.direction

        def player_bounce(block):
            diff = int((block.rect.x + block.rect.width / 2) - (self.rect.x + self.rect.width / 2))
            if block.rect.top <= self.rect.bottom < block.rect.top + 6 and y_dir > 0:
                bounce_angle = 180 - diff
                bounce_angle = bounce(bounce_angle)
                if 270 > bounce_angle > 90:
                    bounce(180)

        x_dir = math.sin(math.radians(self.direction))
        y_dir = -math.cos(math.radians(self.direction))
        self.rect.x += self.velocity * x_dir
        self.rect.y += self.velocity * y_dir

        if self.rect.colliderect(self.player):
            player_bounce(self.player)
        elif self.rect.y <= 0 + 350:  # change to +10 later on
            self.rect.y += 10
            bounce(180)
        elif self.rect.y >= self.game.HEIGHT - 10:  # losing condition
            self.rect.y -= 10
            bounce(180)
        elif self.rect.colliderect(self.gameplay.right_border):
            self.rect.x -= 10
            bounce(0)
        elif self.rect.colliderect(self.gameplay.left_border):
            self.rect.x += 10
            bounce(0)

