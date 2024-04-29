import os, time, win32gui, win32ui, numpy as np, cv2
from ctypes import windll
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PIL import Image

def jump():
    actions.send_keys(Keys.UP).perform()


def squat():
    actions.key_down(Keys.DOWN).perform()
    time.sleep(0.333)
    actions.key_up(Keys.DOWN).perform()


def get_game_screen(top, bottom, left, right):
    w, h = win32gui.GetWindowRect(hwnd)[2:]
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)    
    windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
    bmpstr = saveBitMap.GetBitmapBits(True)
      
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    img = np.frombuffer(bmpstr, dtype='uint8')
    img.shape = (h, w, 4)
    game_screen_array = img[top:bottom, left:right]

    return game_screen_array
    

def main_script():
    # Entering the game
    privacy_popout_window_agree_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'button.css-47sehv')))
    privacy_popout_window_agree_button.click()
    jump()
    game_on = True

    time.sleep(6)
    pil_img = Image.fromarray(get_game_screen(370, 820 , 60, 1920))
    pil_img.save('omg.png')
    # while game_on:
    #     game_screen = get_game_screen(370, 820 , 60, 1000)
    #     cv2.imshow('screen', game_screen)
    #     if cv2.waitKey(1) == ord('q'):
    #         break



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
    time.sleep(1)
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    actions = ActionChains(driver)

    # Initialize main script
    main_script()

