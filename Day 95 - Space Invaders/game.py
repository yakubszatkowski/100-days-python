import pygame, time
from sprites import *

class Game:

    def __init__(self, core):
        self.core = core
        self.background_img = self.core.find_img('img/game_background.png')
        self.scaled_bg = pygame.transform.scale(self.background_img, (self.core.WIDTH, self.core.HEIGHT))

        self.sprites = pygame.sprite.Group()
        self.init_level()


    def display(self):
        self.core.window.blit(self.scaled_bg, (0,0))
        self.sprites.update()
        self.sprites.draw(self.core.window)

        # print(len(self.sprites))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.core.core_run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.core.current_display = self.core.main_menu
                if event.key == pygame.K_UP:
                    missle = Missle(self.player.rect.centerx, self.player.rect.centery - 35, self.player.MISSLE_VELOCITY)
                    self.sprites.add(missle)
                    


    def init_level(self):
        self.player = PlayerShip(self.core)
        self.enemy_ships = self.init_enemy_ships()
        self.sprites.add(self.player, self.enemy_ships)


    def init_enemy_ships(self):
        x, y = 60, 50
        enemy_ships = pygame.sprite.Group()
        rotation_dir = 1

        for n in range(1):
            enemy_ship = EnemyShip(self.core, x, y, rotation_dir)
            enemy_ships.add(enemy_ship)
            x += 85
            if len(enemy_ships) % 9 == 0:
                y += 72
                x = 60
            rotation_dir *= -1
            
        return enemy_ships
    