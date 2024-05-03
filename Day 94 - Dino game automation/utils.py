import os, time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


main_directory = os.path.dirname(os.path.realpath(__file__))
img_game_directory = os.path.join(main_directory, 'img_game')

def find_img(name):
    return os.path.join(img_game_directory, name)

def privacy_button_press(wait):
    time.sleep(1)
    privacy_popout_window_agree_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'button.css-47sehv')))
    privacy_popout_window_agree_button.click()

def jump(actions):
    actions.send_keys(Keys.UP).perform()


def squat(actions):
    actions.key_down(Keys.DOWN).perform()
    time.sleep(0.333)
    actions.key_up(Keys.DOWN).perform()
