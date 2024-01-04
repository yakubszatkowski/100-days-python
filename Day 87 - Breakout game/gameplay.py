import pygame
from random import choice
import math

class GamePlay:
    def __init__(self, game):
        self.ball, self.right_border, self.left_border, self.player_block, self.gameplay = None, None, None, None, None
        self.horizontal_bounce, self.vertical_bounce, self.direction_radian = 1, 1, math.pi
        self.game = game
        self.VEL = 5
        self.BLOCK_DIMENSIONS = 50, 15
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
        board_objects = self.init_board()
        blocks_list = self.init_blocks()
        self.ball = pygame.Rect(self.game.WIDTH / 2 - 5, self.game.HEIGHT / 2, 10, 10)

        while self.gameplay:
            self.clock.tick(60)
            self.game.check_events()
            self.board(board_objects, blocks_list)
            self.check_input()
            self.handle_ball(blocks_list)
            self.blit_screen()

    def init_board(self):
        self.left_border = pygame.Rect(27, 0, 10, self.game.HEIGHT)
        self.right_border = pygame.Rect(self.game.WIDTH - 30, 0, 10, self.game.HEIGHT)
        self.player_block = pygame.Rect(self.game.WIDTH / 2 - 50, 700, 100, 15) #
        return self.player_block, self.left_border, self.right_border

    def init_blocks(self):
        blocks_list = []
        start_x = self.left_border.x + 13
        start_y = 10
        for i in range(20):
            block = pygame.Rect(start_x, start_y, self.BLOCK_DIMENSIONS[0], self.BLOCK_DIMENSIONS[1])
            blocks_list.append((block, choice(self.color_list)))
            start_x += self.BLOCK_DIMENSIONS[0] + 3
            if len(blocks_list) % 10 == 0:
                start_x = self.left_border.x + 13
                start_y += 18
        return blocks_list

    def board(self, board_objects, blocks_list):
        self.game.window.fill(self.game.BLACK)
        for board_object in board_objects:
            pygame.draw.rect(self.game.window, self.game.WHITE, board_object)
        for block, color in blocks_list:
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

    def handle_ball(self, blocks):


        x_dir = math.sin(self.direction_radian)
        y_dir = -math.cos(self.direction_radian)

        if self.right_border.colliderect(self.ball) or self.left_border.colliderect(self.ball):
            self.horizontal_bounce *= -1
        elif self.ball.y <= 0:
            self.vertical_bounce *= -1
        elif self.ball.y >= self.game.HEIGHT - 10:
            self.vertical_bounce *= -1
        elif self.ball.colliderect(self.player_block):
            self.vertical_bounce *= -1

        self.ball.x += 3 * x_dir * self.horizontal_bounce
        self.ball.y += 3 * y_dir * self.vertical_bounce


