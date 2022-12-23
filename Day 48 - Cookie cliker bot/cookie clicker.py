from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

URL = 'http://orteil.dashnet.org/experiments/cookie/'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)

cookie = driver.find_element(By.ID, 'cookie')
store = driver.find_elements(By.CSS_SELECTOR, '#store div')
store_items = [item.get_attribute('id') for item in store][::-1]

time_to_stop = time.time() + 5 * 60
while time_to_stop > time.time():
    time_to_shop = time.time() + 5
    while time_to_shop > time.time():
        cookie.click()
    else:
        for item in store_items:
            try:
                driver.find_element(By.ID, item).click()
            except:
                pass
