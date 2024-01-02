import pygame
from random import choice
import numpy as np
class GamePlay:
    def __init__(self, game):
        self.ball, self.right_border, self.left_border, self.player_block, self.gameplay = None, None, None, None, None
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
        directions = np.arange(-1,1,0.25)
        directions = np.delete(directions, 4)  # deletes 0
        x_dir, y_dir = choice(directions).item(), choice(directions).item()
        directions_vector = pygame.Vector2(x_dir, y_dir)
        normalized_directions_vector = directions_vector.normalize()
        while self.gameplay:
            self.clock.tick(60)
            self.game.check_events()
            self.board(board_objects, blocks_list)
            self.check_input()
            normalized_directions_vector = self.handle_ball(normalized_directions_vector, blocks_list)
            self.blit_screen()

    def init_board(self):
        self.left_border = pygame.Rect(27, 0, 10, self.game.HEIGHT)
        self.right_border = pygame.Rect(self.game.WIDTH - 30, 0, 10, self.game.HEIGHT)
        self.player_block = pygame.Rect(self.game.WIDTH / 2 - 50, 700, 100, 15)
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

    def handle_ball(self, directions_vector, blocks):

        def advanced_collision(block, ball, x_dir, y_dir):  #TODO research alternatives!
            collision_vector = pygame.Vector2(ball.center) - pygame.Vector2(block.center)
            normalized_collision_vector = collision_vector.normalize()

            reflection_vector = pygame.Vector2(x_dir, y_dir).reflect(normalized_collision_vector)
            x_dir, y_dir = reflection_vector.x, reflection_vector.y

            return x_dir, y_dir


        x_dir, y_dir = directions_vector
        self.ball.x += x_dir * 3
        self.ball.y += y_dir * 3

        if self.right_border.colliderect(self.ball) or self.left_border.colliderect(self.ball):
            x_dir *= -1
        elif self.ball.y <= 0:
            y_dir *= -1
        elif self.ball.y == self.game.HEIGHT:
            print('loser hahah')
        elif self.player_block.colliderect(self.ball):
            x_dir, y_dir = advanced_collision(self.player_block, self.ball, x_dir, y_dir)
        #     y_dir *= -1
        # for block in blocks:
        #     if block[0].colliderect(self.ball):
        #         y_dir *= -1
        #         print(pygame.Vector2(self.ball.center), pygame.Vector2(block[0].center))
        #         print(pygame.Vector2(self.ball.center).normalize(), pygame.Vector2(block[0].center).normalize())
        #         print(type(pygame.Vector2(self.ball.center)))
        #         blocks.remove(block)

        directions_vector = x_dir, y_dir
        return directions_vector


