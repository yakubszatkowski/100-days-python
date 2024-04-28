import os, time, win32gui, win32ui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ctypes import windll
from PIL import Image


def jump():
    actions.send_keys(Keys.UP).perform()


def squat():
    actions.key_down(Keys.DOWN).perform()
    time.sleep(0.333)
    actions.key_up(Keys.DOWN).perform()


def get_game_screen():
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
   
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, 1936, 1056)  # figure a way to capture only a part of the screen instead
    saveDC.SelectObject(saveBitMap)    
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return im
    

def main_script():

    # Entering the game
    privacy_popout_window_agree_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'button.css-47sehv')))
    privacy_popout_window_agree_button.click()
    time.sleep(1)
    jump()
    game_on = True
    time.sleep(1)
    squat()


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

