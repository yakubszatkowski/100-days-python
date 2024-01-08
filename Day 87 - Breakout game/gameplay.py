from objects import *
import math

class GamePlay:
    def __init__(self, game):
        self.right_border, self.left_border, self.board_objects, self.player_block, self.ball = None, None, None, None, None
        self.gameplay = False
        self.game = game
        self.clock = pygame.time.Clock()

    def blit_screen(self):
        self.game.window.blit(self.game.window, (0, 0))
        pygame.display.update()

    def display(self):
        self.gameplay = True
        self.init_board()
        while self.gameplay:
            self.clock.tick(60)
            self.game.check_events()
            self.draw_board()
            self.check_input()
            self.blit_screen()

    def init_board(self):
        self.left_border = pygame.Rect(27, 0, 10, self.game.HEIGHT)
        self.right_border = pygame.Rect(self.game.WIDTH - 30, 0, 10, self.game.HEIGHT)
        self.player_block = PlayerBlock(self.game.WIDTH / 2 - 50, 700, 100, 20)
        self.ball = Ball(self.game.WIDTH / 2 - 5, self.game.HEIGHT / 2, 10, 10)

    def draw_board(self):
        self.game.window.fill(self.game.BLACK)
        pygame.draw.rect(self.game.window, self.game.WHITE, self.left_border)
        pygame.draw.rect(self.game.window, self.game.WHITE, self.right_border)
        pygame.draw.rect(self.game.window, self.game.WHITE, self.player_block)
        pygame.draw.circle(self.game.window, self.game.WHITE, self.ball.center, 5)

    def check_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print('left')
        if keys[pygame.K_RIGHT]:
            print('right')
        if self.game.BACK_KEY:
            self.game.current_display = self.game.main_menu
            self.gameplay = False





