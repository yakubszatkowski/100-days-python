from game import Game

g = Game()

if __name__ == '__main__':
    while g.run:
        g.current_display.display()

#TODO Improvements ideas
# tidy the code
# more gameplay elements - ball going through blocks boost, multiple balls boost etc.

# pyinstaller --windowed --icon=img\icon.ico main.py