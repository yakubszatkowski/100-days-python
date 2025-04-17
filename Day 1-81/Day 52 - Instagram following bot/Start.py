from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

URL = 'https://www.instagram.com/'
INSTA_NICK = os.environ.get('D52_insta_nick')
INSTA_PASS = os.environ.get('D52_insta_pass')
TARGET_AUDIENCE = 'mmorpgrs'


class InstaFollower:
    def __init__(self):
        chrome_driver_path = os.environ.get('D48_chrome_driver_path')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options,
                                       service=Service(executable_path=chrome_driver_path, log_path="NUL"))

    def login(self):
        self.driver.get(URL)
        time.sleep(3)
        # this works but i decided to try something else
        # cookies_accept = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie')]")
        cookies_accept = self.driver.find_element(By.CSS_SELECTOR, '.xs83m0k .x7r02ix ._a9_0')
        cookies_accept.click()
        time.sleep(5)
        login_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        pass_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_input.send_keys(INSTA_NICK)
        pass_input.send_keys(INSTA_PASS)
        try:
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        except NoSuchElementException:
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[4]/button/div')
        submit_button.click()
        time.sleep(10)
        # having fun with different methods'
        # notification_popup = self.driver.find_element(By.CSS_SELECTOR, '.x1ja2u2z .x7r02ix ._a9-v ._a9_1')
        notification_popup = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Nie teraz')]")
        notification_popup.click()

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{TARGET_AUDIENCE}/')
        time.sleep(3)
        # Why does Xpath doesn't always work?
        followers = self.driver.find_element(By.CSS_SELECTOR, '._aa_z .x78zum5 .x1quol0o .xieb3on .x1uw6ca5 .xkhd6sd ._aade')
        followers.click()
        time.sleep(3)
        scrollable_window_popup = self.driver.find_element(By.CSS_SELECTOR, '.x47corl .xw8ag78 .x5fp0pe ._ab9f ._aano')
        for _ in range(3):
            time.sleep(3)
            # may be worth finding different methods
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_window_popup)

    def follow(self):
        people_to_follow = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Obserwuj')]")
        time.sleep(5)
        for person in people_to_follow:
            try:
                person.click()
            except ElementClickInterceptedException:
                pass  # if I didn't use xpath by text i would have to find cancel button and click it
            time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()