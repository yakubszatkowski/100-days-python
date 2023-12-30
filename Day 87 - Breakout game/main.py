from game import Game

g = Game()

if __name__ == '__main__':
    g.current_menu.display_menu()
    g.game_loop()