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
        self.velocity = pygame.math.Vector2(0, 5)
        self.vector_influence = 0.9


    def update(self):

        def bounce(paddle):
            # https://gamedev.stackexchange.com/questions/20456/a-more-sophisticated-ball-paddle-collision-algorithm-for-breakout
            collision_x =(self.rect.x - paddle.rect.x) / (paddle.rect.width / 2) - 0.9
            speed_xy = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
            self.velocity[0] = speed_xy * collision_x * self.vector_influence
            self.velocity[1] = math.sqrt(speed_xy**2 - self.velocity[0]**2) * (-1 if self.velocity[1] > 0 else 1)
            if paddle.rect.top <= self.rect.bottom < paddle.rect.top + 10:
                self.rect.y -= 6
            elif paddle.rect.bottom >= self.rect.top > paddle.rect.bottom - 10:
                self.rect.y += 6
            elif paddle.rect.right >= self.rect.left:
                self.velocity[1] *= -1
            elif paddle.rect.left <= self.rect.right:
                self.velocity[1] *= -1

        self.rect.center += self.velocity

        if self.rect.colliderect(self.player):
            bounce(self.player)
        elif self.rect.y <= 0 + 400:  # change to +10 later on
            self.rect.y += 10
            self.velocity[1] *= -1
        elif self.rect.y >= self.game.HEIGHT - 10:  # losing condition
            self.rect.y -= 10
            self.velocity[1] *= -1
        elif self.rect.colliderect(self.gameplay.right_border):
            self.rect.x -= 10
            self.velocity[0] *= -1
        elif self.rect.colliderect(self.gameplay.left_border):
            self.rect.x += 10
            self.velocity[0] *= -1


        # def bounce(angle):
        #     self.ball_direction = (360 - self.ball_direction - angle) % 360
        #
        # def paddle_bounce(paddle):
        #     if self.rect.colliderect(paddle):
        #        pass
        #
        # direction_radians = math.radians(self.ball_direction)
        # x_dir = math.sin(direction_radians)
        # y_dir = math.cos(direction_radians)
        # self.rect.x += self.VELOCITY * x_dir
        # self.rect.y -= self.VELOCITY * y_dir
        #
        # paddle_bounce(self.player)
        #
        # if self.rect.y <= 0 + 400:  # change to +10 later on
        #     self.rect.y += 10
        #     bounce(180)
        # elif self.rect.y >= self.game.HEIGHT - 10:  # losing condition
        #     self.rect.y -= 10
        #     bounce(180)
        # elif self.rect.colliderect(self.gameplay.right_border):
        #     self.rect.x -= 10
        #     bounce(0)
        # elif self.rect.colliderect(self.gameplay.left_border):
        #     self.rect.x += 10
        #     bounce(0)


