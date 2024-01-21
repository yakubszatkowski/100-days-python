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
        self.player_block = PlayerBlock(self.game.WIDTH / 2 - 50 + 100, 700) # -50 + 36 for testing
        start_x, start_y = self.left_border.x + 37, 30
        for i in range(90):
            block = Block(start_x, start_y)
            self.block_group.add(block)
            start_x += block.width + 5
            if len(self.block_group) % 9 == 0:
                start_x = self.left_border.x + 37  # 37 originally
                start_y += 30
        self.ball = Ball(self.game.WIDTH / 2 - 5, self.game.HEIGHT / 2, self.game, self)
        self.all_sprites.add(self.player_block, self.block_group, self.ball)

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

    def countdown(self, lost=None):
        self.countdown_flag = True
        while self.countdown_flag:
            for i in range(3, 0, -1):
                if lost:
                    self.game.draw_text(f'You\'ve lost!', 40, self.game.WIDTH / 2, self.game.HEIGHT / 2 - 100)
                if not lost:
                    self.game.draw_text(f'You\'ve won!', 40, self.game.WIDTH / 2, self.game.HEIGHT / 2 - 100)
                else:
                    self.game.draw_text(f'Get ready!', 40, self.game.WIDTH / 2, self.game.HEIGHT / 2 - 100)
                self.game.draw_text(f'{i}', 40 ,self.game.WIDTH / 2, self.game.HEIGHT / 2)
                self.blit_screen()
                self.check_input()
                pygame.time.delay(1000)

            self.countdown_flag = False


#TODO
# countdown
# winning/losing condition

