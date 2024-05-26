import os, win32gui, cv2, time, mss, numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from utils import privacy_button_press, jump, squat, print_fps

# day   object = [ 83  83  83 255]; background [255 255 255 255]
# night object = [172 172 172 255]; background [ 36  33  32 255]

def main_script():

    # np.set_printoptions(threshold=np.inf)

    # Local variables
    loop_time = 0.00001
    fps_list = []
    day_bg = np.array([255, 255, 255])
    night_bg = np.array([36, 32, 32])
    day_object = np.array([83, 83, 83])
    night_object = np.array([172, 172, 172])

    # Start the game
    jump(actions)

    with mss.mss() as sct:
        monitor = {"top": 700, "left": 250, "width": 300, "height": 1}

        # Game loop
        while 1:
            
            # FPS print for testing
            print_fps(fps_list, loop_time)
            loop_time = time.time()

            # Update game screen
            screen_capture = sct.grab(monitor)
            screen_capture_array = np.array(screen_capture)
            screen_capture_array_3_channels = screen_capture_array[0][..., :3]

            # Check if day or night
            unique_rows, counts = np.unique(screen_capture_array_3_channels, axis=0, return_counts=True)
            most_common_index = np.argmax(counts)
            most_common_vector = unique_rows[most_common_index]

            # Actions
            if night_bg in most_common_vector:
                if night_object in screen_capture_array_3_channels:
                    jump(actions)
            elif day_bg in most_common_vector:
                if day_object in screen_capture_array_3_channels:
                    jump(actions)



if __name__ == '__main__':

    # Initialize the driver
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
    actions = ActionChains(driver)
    
    # Initialize main script
    main_script()





