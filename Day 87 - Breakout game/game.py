import pygame

class Game:

    def __init__(self):
        # Constants
        self.game = True
        self.WIDTH, self.HEIGHT = 600, 800
        self.FPS = 60

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def game_loop(self):
        while self.game:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                    pygame.quit()
