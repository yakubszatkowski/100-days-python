import pygame

class GamePlay:
    def __init__(self, game):
        self.right_border = None
        self.left_border = None
        self.player_block = None
        self.gameplay = None
        self.game = game
        self.VEL = 5
        self.BLOCK_DIMENSIONS = 50, 15
        self.clock = pygame.time.Clock()
        self.color_list = [
            (0, 255, 0),
            (255, 0, 0),
            (0, 0, 255),
            (255, 192, 203),
            (255, 255, 0),
            (128, 0, 128),
            (255, 165, 0),
            (0, 255, 255),
            (255, 69, 0)
        ]

    def blit_screen(self):
        self.game.window.blit(self.game.window, (0, 0))
        pygame.display.update()

    def display(self):
        self.gameplay = True
        board_objects = self.init_board()
        blocks_list = self.init_blocks()
        while self.gameplay:
            self.clock.tick(60)
            self.game.check_events()
            self.board(board_objects, blocks_list)
            self.check_input()
            self.blit_screen()

    def init_board(self):
        self.left_border = pygame.Rect(27, 0, 10, self.game.HEIGHT)
        self.right_border = pygame.Rect(self.game.WIDTH - 30, 0, 10, self.game.HEIGHT)
        self.player_block = pygame.Rect(self.game.WIDTH / 2, 700, 100, 35)
        return self.player_block, self.left_border, self.right_border

    def init_blocks(self):
        blocks_list = []
        start_x = self.left_border.x + 13
        start_y = 10
        for i in range(60):
            block = pygame.Rect(start_x, start_y, self.BLOCK_DIMENSIONS[0], self.BLOCK_DIMENSIONS[1])
            blocks_list.append(block)
            start_x += self.BLOCK_DIMENSIONS[0] + 3
            if len(blocks_list) % 10 == 0:
                start_x = self.left_border.x + 13
                start_y += 20

        return blocks_list

    def board(self, board_objects, blocks_list):
        self.game.window.fill(self.game.BLACK)
        for board_object in board_objects:
            pygame.draw.rect(self.game.window, self.game.WHITE, board_object)
        for block in blocks_list:
            pygame.draw.rect(self.game.window, self.game.WHITE, block)

    def check_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_block.x > self.left_border.x + 10:
            self.player_block.x -= self.VEL
        if keys[pygame.K_RIGHT] and self.player_block.x + 100 < self.right_border.x:
            self.player_block.x += self.VEL
        if self.game.BACK_KEY:
            self.game.current_display = self.game.main_menu
            self.gameplay = False
