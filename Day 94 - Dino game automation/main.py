import os, time, win32gui, cv2
from ctypes import windll
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from screen_capture import get_game_screen
from game_object import GameObject
from utils import find_img

def jump():
    actions.send_keys(Keys.UP).perform()


def squat():
    actions.key_down(Keys.DOWN).perform()
    time.sleep(0.333)
    actions.key_up(Keys.DOWN).perform()


def main_script():

    # Entering the game
    privacy_popout_window_agree_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'button.css-47sehv')))
    privacy_popout_window_agree_button.click()
    jump()
    game_on = True
    region = (370, 820 , 60, 1000)
    
    # Game loop
    while game_on:
        game_screen = get_game_screen(hwnd, region)
        cv2.imshow('screen', game_screen)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':

    # Initialize the driver
    WINDOW_NAME = 'Play Chrome Dinosaur Game Online - elgooG - Google Chrome'
    chrome_driver_path = os.environ.get('D48_chrome_driver_path')
    options = Options()
    options.add_experimental_option("detach", True)  # for dev
    driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
    driver.get('https://elgoog.im/dinosaur-game/')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    actions = ActionChains(driver)

    player = [
        GameObject(find_img('dino_day.png')), GameObject(find_img('dino_night.png'))
        ]
    enemies = [
        GameObject(find_img('big_cacti_day.png')), GameObject(find_img('big_cacti_night.png')), 
        GameObject(find_img('small_cacti_day.png')), GameObject(find_img('small_cacti_night.png')), 
        GameObject(find_img('bird_day.png')), GameObject(find_img('bird_night.png'))
        ]

    # Initialize main script
    main_script()

