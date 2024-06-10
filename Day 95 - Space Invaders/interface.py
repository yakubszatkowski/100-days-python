import pygame

class Interface():

    
    TRANSPARERT_BLACK = (0, 0, 0, 180)
    WHITE = (240, 240, 255)
    BLACK = (40, 40, 43)

    def __init__(self, core):
        self.core = core
        self.mid_w, self.mid_h = self.core.WIDTH/2, self.core.HEIGHT/2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.title_x, self.title_y = self.mid_w, self.mid_h-250
        self.background_img = self.core.find_img('img/menu_background.png')
        self.scaled_bg = pygame.transform.scale(self.background_img, (self.core.WIDTH, self.core.HEIGHT))

    def draw_cursor_w_outline(self):
        self.core.draw_text('>', 30, self.cursor_rect.x-3, self.cursor_rect.y-3, self.BLACK)
        self.core.draw_text('>', 30, self.cursor_rect.x+3, self.cursor_rect.y-3, self.BLACK)
        self.core.draw_text('>', 30, self.cursor_rect.x-3, self.cursor_rect.y+3, self.BLACK)
        self.core.draw_text('>', 30, self.cursor_rect.x+3, self.cursor_rect.y+3, self.BLACK)
        self.core.draw_text('>', 30, self.cursor_rect.x, self.cursor_rect.y, self.WHITE)

    def draw_transparent_rect(self, x, y, width, height):
        rect = (x - width/2, y - height/2, width, height)
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, self.TRANSPARERT_BLACK, shape_surf.get_rect())
        self.core.window.blit(shape_surf, rect)


class MainMenu(Interface):

    def __init__(self, core):
        super().__init__(core)
        self.start_x, self.start_y = self.mid_w, self.mid_h-100
        self.options_x, self.options_y = self.mid_w, self.mid_h
        self.credits_x, self.credits_y = self.mid_w, self.mid_h+100
        self.menu_hover = 'Start'
        self.cursor_offset = -125
        self.cursor_rect.midtop = (self.start_x + self.cursor_offset, self.start_y)
        

    def display(self):
        self.core.window.blit(self.scaled_bg, (0,0))
        self.draw_transparent_rect(self.mid_w, self.mid_h-30, 500, 600)
        self.core.draw_text_outline('Cosmic Assault', 60, self.title_x, self.title_y)
        self.core.draw_text_outline('Start Game', 40, self.start_x, self.start_y)
        self.core.draw_text_outline('Options', 40, self.options_x, self.options_y)
        self.core.draw_text_outline('Credits', 40, self.credits_x, self.credits_y)
        self.draw_cursor_w_outline()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.core.core_run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.menu_hover == 'Start':
                        self.cursor_rect.midtop = (self.options_x + self.cursor_offset, self.options_y)
                        self.menu_hover = 'Options'
                    elif self.menu_hover == 'Options':
                        self.cursor_rect.midtop = (self.credits_x + self.cursor_offset, self.credits_y)
                        self.menu_hover = 'Credits'
                    elif self.menu_hover == 'Credits':
                        self.cursor_rect.midtop = (self.start_x + self.cursor_offset, self.start_y)
                        self.menu_hover = 'Start'
                elif event.key == pygame.K_UP:
                    if self.menu_hover == 'Start':
                        self.cursor_rect.midtop = (self.credits_x + self.cursor_offset, self.credits_y)
                        self.menu_hover = 'Credits'
                    elif self.menu_hover == 'Options':
                        self.cursor_rect.midtop = (self.start_x + self.cursor_offset, self.start_y)
                        self.menu_hover = 'Start'
                    elif self.menu_hover == 'Credits':
                        self.cursor_rect.midtop = (self.options_x + self.cursor_offset, self.options_y)
                        self.menu_hover = 'Options'
                if event.key == pygame.K_RETURN:
                    if self.menu_hover == 'Start':
                        pass
                        self.core.current_display = self.core.game
                    elif self.menu_hover == 'Credits':
                        self.core.current_display = self.core.credit_menu
                    elif self.menu_hover == 'Options':
                        self.core.current_display = self.core.options_menu
                    

class OptionsMenu(Interface):

    def __init__(self, core):
        super().__init__(core)
        self.music_vol_option_x, self.music_vol_option_y = self.mid_w, self.mid_h-100
        self.effect_vol_option_x, self.effect_vol_option_y = self.mid_w, self.mid_h


    def display(self):
        self.core.window.blit(self.scaled_bg, (0,0))
        self.draw_transparent_rect(self.mid_w, self.mid_h-30, 500, 600)
        self.core.draw_text_outline('Options', 60, self.title_x, self.title_y)
        self.core.draw_text_outline('Music volume', 20, self.music_vol_option_x, self.music_vol_option_y)
        self.core.draw_text_outline('Effects volume', 20, self.effect_vol_option_x, self.effect_vol_option_y)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.core.core_run = False
            elif event.type == pygame.KEYDOWN:
                self.core.current_display = self.core.main_menu


class CreditsMenu(Interface):
    
    def __init__(self, core):
        super().__init__(core)
        self.credit_1_x, self.credit_1_y = self.mid_w, self.mid_h - 150
        self.credit_2_x, self.credit_2_y = self.mid_w, self.mid_h - 50
        self.name_y_offset = 35


    def display(self):
        self.core.window.blit(self.scaled_bg, (0,0))
        self.draw_transparent_rect(self.mid_w, self.mid_h-30, 500, 600)
        self.core.draw_text_outline('Credits', 60, self.title_x, self.title_y)
        self.core.draw_text_outline('Main developer:', 20, self.credit_1_x, self.credit_1_y)
        self.core.draw_text_outline('yakubszatkowski', 30, self.credit_1_x, self.credit_1_y + self.name_y_offset)
        self.core.draw_text_outline('Game background image:', 20, self.credit_2_x, self.credit_2_y)
        self.core.draw_text_outline('@phaelnogueira (Unsplash)', 30, self.credit_2_x, self.credit_2_y+ self.name_y_offset)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.core.core_run = False
            elif event.type == pygame.KEYDOWN:
                self.core.current_display = self.core.main_menu
