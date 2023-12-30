import pygame

class Game:

    def __init__(self):
        pygame.init()
        self.run = True
        self.WIDTH, self.HEIGHT = 600, 800
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))


    def game_loop(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.check_events()
            self.draw_window()
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def draw_window(self):
        self.window.fill(self.BLACK)
        self.draw_text('Breakout', 80, self.WIDTH/2, self.HEIGHT/2 - 200)

    def draw_text(self, text, size, x, y):
        font = pygame.font.SysFont('comicsans', size)
        text_surface = font.render(text, 1, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)