import pygame

class Interface():

    BLACK = (40, 40, 43)
    TRANSPARERT_BLACK = (0, 0, 0, 180)
    WHITE = (240, 240, 255)

    def __init__(self, core):
        self.core = core
        self.mid_w, self.mid_h = self.core.WIDTH/2, self.core.HEIGHT/2

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.SysFont('comicsans', size)
        text_surface = font.render(text, 1, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.core.window.blit(text_surface, text_rect)

    def draw_text_outline(self, text, size, x, y):
        self.draw_text(text, size, x-3, y-3, self.BLACK)
        self.draw_text(text, size, x+3, y-3, self.BLACK)
        self.draw_text(text, size, x-3, y+3, self.BLACK)
        self.draw_text(text, size, x+3, y+3, self.BLACK)
        self.draw_text(text, size, x, y, self.WHITE)

    def draw_transparent_rect(self, x, y, width, height):
        rect = (x - width/2, y - height/2, width, height)
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, self.TRANSPARERT_BLACK, shape_surf.get_rect())
        self.core.window.blit(shape_surf, rect)


class MainMenu(Interface):

    def __init__(self, core):
        super().__init__(core)
        self.background_img = self.core.find_img('img/menu_background.png')
        self.scaled_bg = pygame.transform.scale(self.background_img, (self.core.WIDTH, self.core.HEIGHT))

    def display(self):
        self.core.window.blit(self.scaled_bg, (0,0))
        self.draw_transparent_rect(self.mid_w, self.mid_h-30, 500, 600)
        self.draw_text_outline('Cosmic Assault', 60, self.mid_w, self.mid_h-250)
        self.draw_text_outline('Start Game', 40, self.mid_w, self.mid_h-100)
        self.draw_text_outline('Options', 40, self.mid_w, self.mid_h)
        self.draw_text_outline('Credits', 40, self.mid_w, self.mid_h+100)
