import pygame
from sprites import *

class Game:

    def __init__(self, core):
        self.core = core
        self.background_img = self.core.find_img('img/game_background.png')
        self.scaled_bg = pygame.transform.scale(self.background_img, (self.core.WIDTH, self.core.HEIGHT))
        self.init_display_bool = True
        self.game_on = False
        

    def display(self):
        if self.init_display_bool:
            self.init_level()
            self.init_display_bool = False
            self.game_on = True

        if self.game_on:
            self.core.window.blit(self.scaled_bg, (0,0))
            for enemy_ship in self.enemy_ships:
                missle = enemy_ship.random_shoot()
                if missle:
                    self.enemy_missles.add(missle)
                    self.sprites.add(self.enemy_missles)

            self.missle_collision()
            self.sprites.update()
            self.sprites.draw(self.core.window)
            self.health_bar.draw(self.player.hitpoints)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.core.core_run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.core.current_display = self.core.main_menu
                    self.init_display_bool = True
                    self.sprites = None
                if event.key == pygame.K_UP:
                    player_missle = Missle(
                        self.player.rect.centerx, 
                        self.player.rect.centery - 35, 
                        self.player.MISSLE_VELOCITY,
                        'yellow'
                    )
                    self.player_missiles.add(player_missle)
                    self.sprites.add(self.player_missiles)

        if self.player.hitpoints <= 0:
            self.game_on = False
            # self.draw_text_outline('You\'ve lost!', 60, self.core.WIDTH, self.core.HEIGHT)
            # self.draw_text_outline('Press esc to return to menu', 60, self.core.WIDTH, self.core.HEIGHT + 50)
        elif len(self.enemy_ships) == 0:
            self.game_on = False
            # self.draw_text_outline('You\'ve won!', 60, self.core.WIDTH, self.core.HEIGHT)
            # self.draw_text_outline('Press esc to return to menu', 60, self.core.WIDTH, self.core.HEIGHT + 50)


    def missle_collision(self):
        pygame.sprite.groupcollide(self.player_missiles, self.enemy_ships, True, True)

        if pygame.sprite.spritecollide(self.player, self.enemy_missles, True):
            self.player.hitpoints -= 1


    def init_level(self):
        self.sprites = pygame.sprite.Group()
        self.enemy_ships = pygame.sprite.Group()
        self.player_missiles = pygame.sprite.Group()
        self.enemy_missles = pygame.sprite.Group()
        self.health_bar = HealthBar(self.core)

        self.player = PlayerShip(self.core)
        self.enemy_ships.add(self.init_enemy_ships())
        self.sprites.add(self.player, self.enemy_ships)


    def init_enemy_ships(self):
        x, y = 60, 50
        enemy_ships = pygame.sprite.Group()
        rotation_dir = 1

        for _ in range(18):
            enemy_ship = EnemyShip(self.core, x, y, rotation_dir)
            enemy_ships.add(enemy_ship)
            x += 85
            if len(enemy_ships) % 9 == 0:
                y += 72
                x = 60
            rotation_dir *= -1

        return enemy_ships
    

class HealthBar:

    WIDTH, HEIGHT = 200, 20

    def __init__(self, core):
        self.core = core
        self.surface = self.core.window
        self.x, self.y = self.core.WIDTH/2 + 100, 860

        self.hp = 5
        self.max_hp = 5


    def draw(self, current_hp):
        ratio = current_hp / self.max_hp
        pygame.draw.rect(self.surface, "white", (self.x-2, self.y-2, self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, "white", (self.x-2, self.y+2, self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, "white", (self.x+2, self.y-2, self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, "white", (self.x+2, self.y+2, self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, "crimson", (self.x, self.y, self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, "darkgreen", (self.x, self.y, self.WIDTH * ratio, self.HEIGHT))


# TODO
    # move draw_text_outline from interface.py to core.py and refactor it in code
    # continue winning/losing condition
    