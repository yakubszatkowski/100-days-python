import os, time, win32gui, win32con, win32api, win32ui
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
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_UP, 0)


def squat():
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_DOWN, 0)
    time.sleep(0.333)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_DOWN, 0)


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
    print(bmpstr)
    print(len(bmpstr))
    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return im
    

def main_script():

    # Entering the game
    time.sleep(1)
    privacy_popout_window_agree_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'button.css-47sehv')))
    privacy_popout_window_agree_button.click()
    jump()
    game_on = True
    time.sleep(3)

    # Automation
    game_screen = get_game_screen()
    # game_screen.save('pic.png')
    

if __name__ == '__main__':

    # Initialize the driver
    WINDOW_NAME = 'Play Chrome Dinosaur Game Online - elgooG - Google Chrome'
    chrome_driver_path = os.environ.get('D48_chrome_driver_path')
    options = Options()
    options.add_experimental_option("detach", True)  # for dev
    driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
    driver.get('https://elgoog.im/dinosaur-game/')
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    win32gui.SetForegroundWindow(hwnd)

    print(driver.get_window_size)

    # Initialize main script
    main_script()
