from game import Game

g = Game()

if __name__ == '__main__':
    while g.run:
        g.current_display.display_menu()
        g.game_loop()
