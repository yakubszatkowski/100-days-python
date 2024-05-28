from core import Core

core = Core()

if __name__ == '__main__':
    while core.core_run:
        # core.current_display.display()
        core.game_loop()

# Create a menu that uses event.type == pygame.KEYDOWN