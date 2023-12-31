import pygame

class GamePlay:
    def __init__(self, game):

        self.gameplay = None
        self.game = game
        self.VEL = 5
        self.player_block = pygame.Rect(self.game.WIDTH / 2 - 50, 700, 100, 30)

    def blit_screen(self):
        self.game.window.blit(self.game.window, (0, 0))
        pygame.display.update()
        # self.game.reset_keys()

    def display(self):
        self.gameplay = True
        while self.gameplay:
            self.game.check_events()

            self.board()
            self.check_input()
            self.blit_screen()

    def board(self):
        self.game.window.fill(self.game.BLACK)
        pygame.draw.rect(self.game.window, (255, 0, 0), self.player_block)

    def check_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_block.x -= 1
        if keys[pygame.K_RIGHT]:
            self.player_block.x += 1

