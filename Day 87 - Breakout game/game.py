from menu import *
from gameplay import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Breakout game by yakubszatkowski')
        self.run = True
        self.WIDTH, self.HEIGHT = 600, 800
        self.FPS = 60
        self.WHITE, self.BLACK = (255, 255, 255), (0, 0, 0)
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.main_menu = MainMenu(self)
        self.credits = CreditsMenu(self)
        self.game = GamePlay(self)
        self.current_display = self.main_menu

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game.gameplay = False
                self.current_display.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.SysFont('comicsans', size)
        text_surface = font.render(text, 1, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)
