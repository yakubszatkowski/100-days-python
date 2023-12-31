import pygame

class Menu:
    def __init__(self, game):
        self.run_display = None
        self.game = game
        self.mid_w, self.mid_h = self.game.WIDTH/2, self.game.HEIGHT/2

        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
        self.titlex, self.titley = self.mid_w, self.mid_h - 100
        self.startx, self.starty = self.mid_w, self.mid_h

    def draw_cursor(self):
        self.game.draw_text('*', 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.window, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = 'Start'
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 50
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.window.fill(self.game.BLACK)
            self.check_input()
            self.game.draw_text('Breakout Game', 60, self.titlex, self.titley)
            self.game.draw_text('Start Game', 20, self.startx, self.starty)
            self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Start':
                self.state = 'Credits'
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
            elif self.state == 'Credits':
                self.state = 'Start'
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.current_display = self.game.game
            elif self.state == 'Credits':
                self.game.current_display = self.game.credits
        self.run_display = False

class CreditsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

    def display(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.window.fill(self.game.BLACK)
            self.check_input()
            self.game.draw_text('Credits', 60, self.titlex, self.titley)
            self.game.draw_text('Author: yakubszatkowski', 20, self.startx, self.starty)
            self.blit_screen()

    def check_input(self):
        if self.game.START_KEY or self.game.BACK_KEY:
            self.game.current_display = self.game.main_menu
            self.run_display = False
