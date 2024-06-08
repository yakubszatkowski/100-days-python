from typing import Any
import pygame
from time import sleep

class PlayerShip(pygame.sprite.Sprite):

    SHIP_WIDTH, SHIP_HEIGHT = 61, 50
    MOVEMENT_VELOCITY, MISSLE_VELOCITY = 10, 6

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


    # def shoot(self):


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 10:
            self.rect.x -= self.MOVEMENT_VELOCITY
        if keys[pygame.K_RIGHT] and self.rect.right < 790:
            self.rect.x += self.MOVEMENT_VELOCITY



class EnemyShip(pygame.sprite.Sprite):

    SHIP_WIDTH, SHIP_HEIGHT = 53, 53
    ROTATION_VELOCITY, MISSLE_VELOCITY = 8, 2
    

    def __init__(self, core, start_x, start_y, rotation_dir):
        pygame.sprite.Sprite.__init__(self)
        self.core = core
        self.ufo_img = self.core.find_img('img/enemy_1.png')
        self.image = pygame.Surface((self.SHIP_WIDTH, self.SHIP_HEIGHT), pygame.SRCALPHA)
        self.image.blit(self.ufo_img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)

        self.pos = self.rect.topleft
        self.rotation_dir = rotation_dir
        self.angle = 0
        self.radius = 2


    def update(self):
        center = self.pos + pygame.math.Vector2(0, self.radius).rotate(self.angle*self.rotation_dir) 
        self.rect = self.image.get_rect(center=(round(center.x), round(center.y)))
        self.angle = (self.angle + self.ROTATION_VELOCITY) % 360 

