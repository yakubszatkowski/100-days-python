import pygame
import math
import random

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
        if keys[pygame.K_LEFT] and self.rect.left > 39:
            self.rect.x -= self.VELOCITY
        if keys[pygame.K_RIGHT] and self.rect.right < 566:
            self.rect.x += self.VELOCITY


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color_list = [
            (77, 128, 77),
            (128, 64, 64),
            (77, 77, 128),
            (204, 173, 179),
            (204, 204, 102),
            (89, 0, 89),
            (204, 133, 102),
            (77, 128, 128),
            (204, 46, 0)
        ]
        self.width, self.height = 50, 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(random.choice(self.color_list))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, game, gameplay):
        super().__init__()
        self.game, self.gameplay = game, gameplay
        self.player = self.gameplay.player_block
        self.blocks = self.gameplay.block_group
        self.width, self.height = 10, 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((40, 40, 43))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, 'white', (self.width // 2, self.height // 2), 5)
        self.rect.topleft = (x, y)
        self.direction = 180
        self.velocity = 5
        self.collision_tolerance = 6

    def update(self):
        def bounce(angle):
            self.direction = 360 - self.direction
            self.direction += angle
            if self.direction >= 360:
                self.direction -= 360
            if 285 > self.direction > 255:
                self.direction += 31
            elif 105 > self.direction > 75:
                self.direction -= 31
            return self.direction

        def player_bounce(block):
            diff = int((block.rect.x + block.rect.width / 2) - (self.rect.x + self.rect.width / 2))
            if block.rect.top <= self.rect.bottom < block.rect.top + self.collision_tolerance and y_dir > 0:
                bounce_angle = 180 - diff
                bounce_angle = bounce(bounce_angle)
                if 270 > bounce_angle > 90:
                    bounce(180)

        x_dir = math.sin(math.radians(self.direction))
        y_dir = -math.cos(math.radians(self.direction))
        self.rect.x += self.velocity * x_dir
        self.rect.y += self.velocity * y_dir

        for block in self.blocks:
            if self.rect.colliderect(block):
                if abs(block.rect.top - self.rect.bottom) < self.collision_tolerance and y_dir > 0:
                    bounce(180)
                if abs(block.rect.bottom - self.rect.top) < self.collision_tolerance and y_dir < 0:
                    bounce(180)
                if abs(block.rect.right - self.rect.left) < self.collision_tolerance and x_dir < 0:
                    bounce(0)
                if abs(block.rect.left - self.rect.right) < self.collision_tolerance and x_dir > 0:
                    bounce(0)
                block.kill()

        if self.rect.colliderect(self.player):
            player_bounce(self.player)
        elif self.rect.y <= 0 + 10:
            self.rect.y += 10
            bounce(180)
        elif self.rect.y >= self.game.HEIGHT - 10 and self.gameplay.gameplay == True:
            self.rect.y -= 11
            self.velocity = 0
            self.gameplay.countdown(lost=True)
        elif self.rect.colliderect(self.gameplay.right_border):
            self.rect.x -= 10
            bounce(0)
        elif self.rect.colliderect(self.gameplay.left_border):
            self.rect.x += 10
            bounce(0)

