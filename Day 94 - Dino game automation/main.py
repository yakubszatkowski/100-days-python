import os, time, win32gui, cv2
from ctypes import windll
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from game_object import GameObject
from screen_capture import get_game_screen
from utils import find_img, privacy_button_press, jump, squat


def main_script():

    # Start the game    
    jump(actions)
    region = (625, 750, 250, 800)

    # Game loop
    while 1:

        # Update game screen
        game_screen = get_game_screen(hwnd, region)

        # Detection of objects to dodge
        for key in dodge_objects:
            dodge_object = dodge_objects[key][0]
            action_threshold = dodge_objects[key][1]
            if dodge_object.match(game_screen):
                dodge_object_left_x = dodge_object.location[0][0]
                cv2.rectangle(game_screen, dodge_object.location[0], dodge_object.location[1], (0,0,255), 2)

                # Action
                if dodge_object_left_x < action_threshold:
                    print('jump over', key, dodge_object_left_x)
                    jump(actions)


        # Show recorded region
        cv2.imshow('screen', game_screen)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':

    # Initialize the driver
    WINDOW_NAME = 'Play Chrome Dinosaur Game Online - elgooG - Google Chrome'
    chrome_driver_path = os.environ.get('D48_chrome_driver_path')
    options = Options()
    driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
    
    # Open browser
    while 1:
        try:
            driver.get('https://elgoog.im/dinosaur-game/')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)
            privacy_button_press(wait)
            break
        except:
            driver.quit()

    # Core variables
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    actions = ActionChains(driver)
    rect = win32gui.GetWindowRect(hwnd)
    dodge_objects = {
        'big_cacti_day': [GameObject(find_img('big_cacti_day.png')), 360],
        'big_cacti_night': [GameObject(find_img('big_cacti_night.png')), 300],
        'big_double_cacti_day': [GameObject(find_img('big_double_cacti_day.png')), 350],
        'big_quadruple_cacti_day': [GameObject(find_img('big_quadruple_cacti_day.png')), 300],
        'bird_day': [GameObject(find_img('bird_day.png')), 400],
        'bird_night': [GameObject(find_img('bird_night.png')), 400],
        'small_cacti_day': [GameObject(find_img('small_cacti_day.png')), 520],
        'small_cacti_night': [GameObject(find_img('small_cacti_night.png')), 300],
        'small_double_cacti_day': [GameObject(find_img('small_double_cacti_day.png')), 350],
        'small_triple_cacti': [GameObject(find_img('small_triple_cacti.png')), 350]
    }
    

    # Initialize main script
    main_script()

#TODO
    # Get back to old pictures and trim the dodge_objects dict to the revelant picture