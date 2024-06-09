import pygame
from random import randint

class Missle(pygame.sprite.Sprite):

    WIDTH, HEIGHT = 3, 3

    def __init__(self, start_x, start_y, missle_velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)
        self.missle_velocity = missle_velocity


    def update(self):
        self.rect.y += self.missle_velocity

        if self.rect.y <= 0:
            self.kill()


class PlayerShip(pygame.sprite.Sprite):

    SHIP_WIDTH, SHIP_HEIGHT = 61, 50
    MISSLE_VELOCITY = -6


    def __init__(self, core):
        pygame.sprite.Sprite.__init__(self)
        self.core = core

        self.spaceship_img = self.core.find_img('img/spaceship_player.png')
        self.image = pygame.Surface((self.SHIP_WIDTH, self.SHIP_HEIGHT), pygame.SRCALPHA)
        self.image.blit(self.spaceship_img, (0,0))
        self.rect = self.image.get_rect()
        self.START_X, self.START_Y = (self.core.WIDTH/2 - self.SHIP_WIDTH/2), 820
        self.rect.topleft = (self.START_X, self.START_Y)

        self.friction = -0.1
        self.position, self.velocity, self.acceleration, self.posx = 0, 0, 0, self.START_X


    def update(self):
        self.move()


    def move(self):
        self.acceleration = 0
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.acceleration -= 1.2
        if keys[pygame.K_RIGHT]:
            self.acceleration += 1.2

        self.acceleration += self.velocity * self.friction
        self.velocity += self.acceleration
        self.posx += self.velocity + self.acceleration*0.8
        self.rect.x = self.posx

        if self.rect.right >= 790:
            self.posx = 790 - self.SHIP_WIDTH
        elif self.rect.left <= 10:
            self.posx = 10


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
        self.rotation()
        

    def rotation(self):
        center = self.pos + pygame.math.Vector2(0, self.radius).rotate(self.angle*self.rotation_dir) 
        self.rect = self.image.get_rect(center=(round(center.x), round(center.y)))
        self.angle = (self.angle + self.ROTATION_VELOCITY) % 360 


    def random_shooting(self):
        rng = 'x'
        missle = Missle(self.rect.centerx, self.rect.centery)


# TODO:
    # Enemy spaceship shooting at random times
