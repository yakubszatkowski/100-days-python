from typing import Any
import pygame
from time import sleep

class PlayerShip(pygame.sprite.Sprite):

    SHIP_WIDTH, SHIP_HEIGHT = 61, 50
    MOVEMENT_VELOCITY = 10

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
            self.rect.x -= self.MOVEMENT_VELOCITY
        if keys[pygame.K_RIGHT] and self.rect.right < 790:
            self.rect.x += self.MOVEMENT_VELOCITY


class EnemyShip(pygame.sprite.Sprite):

    SHIP_WIDTH, SHIP_HEIGHT = 53, 53
    MOVEMENT_VELOCITY, MISSLE_VELOCITY = 1, 3
    

    def __init__(self, core, start_x, start_y, movement_range):
        pygame.sprite.Sprite.__init__(self)
        self.core = core

        self.ufo_img = self.core.find_img('img/enemy_1.png')
        self.image = pygame.Surface((self.SHIP_WIDTH, self.SHIP_HEIGHT), pygame.SRCALPHA)
        self.image.blit(self.ufo_img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)

        self.range_x = [start_x + movement_range[0], start_x + movement_range[1]]
        self.range_y = [start_y + movement_range[0], start_y + movement_range[1]]
        self.direction_x = 1
        self.direction_y = 1


    def update(self):
        self.rect.x += self.MOVEMENT_VELOCITY * self.direction_x
        self.rect.y += self.MOVEMENT_VELOCITY * self.direction_y

        if self.rect.x <= self.range_x[0]:
            self.direction_x *= -1
        elif self.rect.x >= self.range_x[1]:
            self.direction_x *= -1
        elif self.rect.y <= self.range_y[0]:
            self.direction_y *= -1
        elif self.rect.y >= self.range_y[1]:
            self.direction_y *= -1

        
#TODO 
    # enemy spaceships circular motion
    # enemy spaceships left and right ease out motion
    # player spaceship ease out motion after control
    # player spaceship init - fly in from bottom
    # enemy spaceships init - fly in from top

        