import os, win32gui, cv2, time, mss, numpy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from game_object import GameObject
from utils import find_img, privacy_button_press, jump, squat, print_fps


def main_script():

    # Local variables
    loop_time = 0.00001
    fps_list = []
    action_threshold = 280
    # Start the game
    jump(actions)
    
    # Game loop
    with mss.mss() as sct:
        monitor = {"top": 600, "left": 250, "width": 550, "height": 150}
        while 1:
            # FPS print for testing
            print_fps(fps_list, loop_time)
            loop_time = time.time()

            # Update game screen
            img = numpy.array(sct.grab(monitor))
            game_screen = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            for key in dodge_objects:
                dodge_object = dodge_objects[key]
                if dodge_object.match(game_screen):
                    dodge_object_left_x = dodge_object.location[0][0]
                    dodge_object_left_y = dodge_object.location[0][1]
                    cv2.rectangle(game_screen, dodge_object.location[0], dodge_object.location[1], (0,0,255), 2)

                    # Action
                    if dodge_object_left_y == 20:
                        print(key, 'x:', dodge_object_left_x, 'y:', dodge_object_left_y)
                        squat(actions)
                    elif dodge_object_left_x < action_threshold:
                        print(key, 'x:', dodge_object_left_x, 'y:', dodge_object_left_y)
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
        'big_cacti_day': GameObject(find_img('big_cacti_day.png')),
        'big_cacti_night': GameObject(find_img('big_cacti_night.png')),
        'bird_day': GameObject(find_img('bird_day.png')),
        'bird_night': GameObject(find_img('bird_night.png')),
        'small_cacti_day': GameObject(find_img('small_cacti_day.png')),
        'small_cacti_night': GameObject(find_img('small_cacti_night.png')),
    }

    # Initialize main script
    main_script()



# from screen_capture import get_game_screen
# region = (250, 625, 800, 750)
# game_screen = get_game_screen(hwnd, region)
