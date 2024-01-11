import pygame
import math

class PlayerBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width, self.height = 100, 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (x, y)
        self.VELOCITY = 5

        # self.top = self.rect.y
        # self.left = self.rect.x
        # self.bottom = self.rect.y + self.height
        # self.right = self.rect.x + self.width

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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (x, y)
        self.velocity = pygame.Vector2(0,5)
        # self.BALL_SPEED = 5
        # self.ball_direction = 180

        self.top = self.rect.y
        self.left = self.rect.x
        self.bottom = self.rect.y + self.height
        self.right = self.rect.x + self.width


    def update(self):
        def bounce(block):
            offset = self.rect.x - block.rect.x, self.rect.y - block.rect.y
            if p := block.mask.overlap(self.mask, offset):
                v = pygame.Vector2(p) - (block.width / 2, block.height / 2)
                self.velocity.reflect_ip(v)

        self.rect.center += self.velocity

        bounce(self.player)

        if self.rect.y <= 0 + 10:
            self.rect.y += 10
            self.velocity[1] *= -1
        elif self.rect.y >= self.game.HEIGHT - 10: # losing condition
            self.rect.y -= 10
            self.velocity[1] *= -1
        elif self.rect.colliderect(self.gameplay.right_border):
            self.rect.x -= 10
            self.velocity[0] *= -1
        elif self.rect.colliderect(self.gameplay.left_border):
            self.rect.x += 10
            self.velocity[0] *= -1

        # direction_radians = math.radians(self.ball_direction)
        # x_dir = math.sin(direction_radians)
        # y_dir = math.cos(direction_radians)
        # self.rect.x += self.BALL_SPEED * x_dir
        # self.rect.y -= self.BALL_SPEED * y_dir


#TODO Implement masks
