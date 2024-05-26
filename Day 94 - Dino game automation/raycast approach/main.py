import os, cv2, time, numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from utils import privacy_button_press, jump, print_fps
from screen_capture import WindowCaputre

def main_script(actions, wincap):
    # Local variables
    loop_time = 0.00001
    fps_list = []

    day_bg = np.array([255, 255, 255])
    night_bg = np.array([36, 32, 32])
    day_object = np.array([83, 83, 83])
    night_object = np.array([172, 172, 172])

    action_threshold = 300

    # Start the game
    jump(actions)
    wincap.start()

    # Game loop
    while True:

        if wincap.screenshot is None:
            continue

        print_fps(fps_list, loop_time)
        loop_time = time.time()

        unique_rows, counts = np.unique(wincap.screenshot, axis=0, return_counts=True)
        most_common_index = np.argmax(counts)
        most_common_vector = unique_rows[most_common_index]

        # Actions
        if night_bg in most_common_vector:
            if night_object in wincap.screenshot:
                jump(actions)
        elif day_bg in most_common_vector:
            if day_object in wincap.screenshot:
                jump(actions)


        cv2.imshow('screen', wincap.screenshot)
        if cv2.waitKey(1) == ord('q'):
            wincap.stop()
            break


if __name__ == '__main__':

    # Initialize the driver
    chrome_driver_path = os.environ.get('D48_chrome_driver_path')
    options = Options()
    driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))

    # Open browser
    while True:
        try:
            driver.get('https://elgoog.im/dinosaur-game/')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)
            privacy_button_press(wait)
            break
        except:
            driver.quit()

    # Core variables
    actions = ActionChains(driver)
    wincap = WindowCaputre('Play Chrome Dinosaur Game Online - elgooG - Google Chrome')
    
    # Initialize main script
    main_script(actions, wincap)


# # FPS print for testing
#         print_fps(fps_list, loop_time)
#         loop_time = time.time()

#         cv2.imshow('screen', wincap.screenshot)
#         if cv2.waitKey(1) == ord('q'):
#             wincap.stop()
#             cv2.destroyAllWindows()
#             break