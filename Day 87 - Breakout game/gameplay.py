from objects import *
import math

class GamePlay:
    def __init__(self, game):
        self.ball, self.player_block = None, None
        self.right_border, self.left_border = None, None
        self.gameplay = False
        self.game = game
        self.clock = pygame.time.Clock()

        self.block_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()


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
        self.player_block = PlayerBlock(210, 700)  # self.game.WIDTH / 2 - 50
        self.ball = Ball(self.game.WIDTH / 2 - 5, self.game.HEIGHT / 2, self.game, self, self.player_block)
        self.all_sprites.add(self.player_block, self.ball, self.block_group)

    def draw_board(self):
        self.game.window.fill(self.game.BLACK)
        pygame.draw.rect(self.game.window, self.game.WHITE, self.left_border)
        pygame.draw.rect(self.game.window, self.game.WHITE, self.right_border)
        self.all_sprites.update()
        self.all_sprites.draw(self.game.window)


    def check_input(self):
        if self.game.BACK_KEY:
            self.game.current_display = self.game.main_menu
            self.gameplay = False
            for sprite in self.all_sprites.sprites():
                sprite.kill()
