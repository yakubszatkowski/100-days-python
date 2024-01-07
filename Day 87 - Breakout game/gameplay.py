import pygame
from random import choice
import math

class GamePlay:
    def __init__(self, game):
        self.ball, self.right_border, self.left_border, self.player_block = None, None, None, None
        self.countdown_flag, self.gameplay, self.direction_radian = None, None, None
        self.board_objects, self.blocks_list = None, None
        self.ball_direction = 0
        self.game = game
        self.VEL = 5
        self.BLOCK_DIMENSIONS = 50, 20
        self.BALL_SPEED = 5
        self.BALL_SAFEGUARD = self.BALL_SPEED + 10
        self.clock = pygame.time.Clock()
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

    def blit_screen(self):
        self.game.window.blit(self.game.window, (0, 0))
        pygame.display.update()

    def display(self):
        self.gameplay = True
        self.board_objects = self.init_board()
        self.blocks_list = self.init_blocks()
        self.ball_direction = 180
        while self.gameplay:
            self.clock.tick(60)
            self.game.check_events()
            self.board()
            self.check_input()
            self.ball_movement()
            self.blit_screen()

    def init_board(self):
        self.left_border = pygame.Rect(27, 0, 10, self.game.HEIGHT)
        self.right_border = pygame.Rect(self.game.WIDTH - 30, 0, 10, self.game.HEIGHT)
        self.player_block = pygame.Rect(self.game.WIDTH / 2 - 50, 700, 100, 20)
        self.ball = pygame.Rect(self.game.WIDTH / 2 - 42, self.game.HEIGHT / 2, 10, 10)
        return self.player_block, self.left_border, self.right_border

    def init_blocks(self):
        blocks_list = []
        start_x = self.left_border.x + 37
        start_y = 30
        for i in range(90):
            block = pygame.Rect(start_x, start_y, self.BLOCK_DIMENSIONS[0], self.BLOCK_DIMENSIONS[1])
            blocks_list.append((block, choice(self.color_list)))
            start_x += self.BLOCK_DIMENSIONS[0] + 5
            if len(blocks_list) % 9 == 0:
                start_x = self.left_border.x + 37
                start_y += 30
        return blocks_list

    def board(self):
        self.game.window.fill(self.game.BLACK)
        for board_object in self.board_objects:
            pygame.draw.rect(self.game.window, self.game.WHITE, board_object)
        for block, color in self.blocks_list:
            pygame.draw.rect(self.game.window, color, block)
        pygame.draw.circle(self.game.window, self.game.WHITE, self.ball.center, 5)

    def check_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_block.left > self.left_border.right:
            self.player_block.x -= self.VEL
        if keys[pygame.K_RIGHT] and self.player_block.right < self.right_border.left:
            self.player_block.x += self.VEL
        if self.game.BACK_KEY:
            self.game.current_display = self.game.main_menu
            self.gameplay = False

    def ball_movement(self):
        def bounce(diff):
            if -25 <= diff <= 25:
                diff *= -1
            self.ball_direction = (180 - self.ball_direction) % 360
            self.ball_direction += diff
            if 80 < self.ball_direction < 100 or 260 < self.ball_direction < 280:
                self.ball_direction += 20
            if self.player_block.colliderect(self.ball):
                print(diff)

        def bounce_of_block(block):
            if block.colliderect(self.ball):
                diff = (block.x + block.width / 2) - (self.ball.x + self.ball.width / 2)
                if block.top <= self.ball.bottom < block.top + self.BALL_SAFEGUARD and y_dir < 0:
                    # print('top hit', block.top, self.ball.bottom)
                    bounce(diff)
                    # self.ball.y -= 10
                elif block.bottom >= self.ball.top > block.bottom - self.BALL_SAFEGUARD and y_dir > 0:
                    # print('bottom hit', block.bottom, self.ball.top)
                    bounce(-diff)
                    self.ball.y += 10
                elif block.right >= self.ball.left:
                    # print('right hit', block.right, self.ball.left)
                    bounce(180)
                elif block.left <= self.ball.right:
                    # print('right hit', block.left, self.ball.right)
                    bounce(180)
                # else:
                #     bounce(180)
                #     # print('bounce')
                return True

        direction_radians = math.radians(self.ball_direction)

        x_dir = math.sin(direction_radians)
        y_dir = math.cos(direction_radians)

        self.ball.x += self.BALL_SPEED * x_dir
        self.ball.y -= self.BALL_SPEED * y_dir

        bounce_of_block(self.player_block)

        for block in self.blocks_list:
            if bounce_of_block(block[0]):
                self.blocks_list.remove(block)

        if self.ball.y <= 0 + 10:
            self.ball.y += 10
            bounce(0)
        elif self.ball.y >= self.game.HEIGHT - 10: # losing condition
            bounce(0)
            self.ball.y -= 10
            # self.countdown()
        elif self.ball.colliderect(self.right_border):
            self.ball.x -= 10
            bounce(180)
        elif self.ball.colliderect(self.left_border):
            self.ball.x += 10
            bounce(180)

    def countdown(self, lost=None):
        self.countdown_flag = True
        while self.countdown_flag:
            for i in range(3, 0, -1):
                self.game.draw_text(f'{i}', 40 ,self.game.WIDTH / 2, self.game.HEIGHT / 2)
                self.blit_screen()
                pygame.time.delay(1000)

            self.countdown_flag = False


#TODO
# Game countdown
# Score
# Lose condition
