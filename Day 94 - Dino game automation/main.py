import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = os.environ.get('D48_chrome_driver_path')


def main_script():
    # Initialize driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
    driver.get('https://elgoog.im/dinosaur-game/')
    driver.maximize_window()


if __name__ == '__main__':
    main_script()