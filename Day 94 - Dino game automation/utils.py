import os

main_directory = os.path.dirname(os.path.realpath(__file__))
img_game_directory = os.path.join(main_directory, 'img_game')

def find_img(name):
    return os.path.join(img_game_directory, name)
