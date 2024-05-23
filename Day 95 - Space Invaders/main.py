from core import Core

g = Core()

if __name__ == '__main__':
    while g.run:
        g.current_display.display()