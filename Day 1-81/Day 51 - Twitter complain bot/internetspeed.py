import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TWITTER_USERNAME = 'cxzkldj432osa'  # cxzkldj432osaQQ222
TWITTER_PASSWORD = os.environ.get('D51_twitter_pass')
UPLOAD = 50
DOWNLOAD = 50

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = os.environ.get('D48_chrome_driver_path')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options,
                                       service=Service(executable_path=chrome_driver_path, log_path="NUL"))
        self.down = 0
        self.up = 0

    def get_internet_speed(self, url):
        self.driver.get(url)
        accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies.click()
        time.sleep(1)
        start_test = self.driver.find_element(By.XPATH,
                                              '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_test.click()
        time.sleep(40)
        download = self.driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upload = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(download.text)
        self.up = float(upload.text)
        print(f'upload: {self.up}\ndownload: {self.down}')
        time.sleep(3)

    def tweet_at_provider(self, url):
        if self.down < DOWNLOAD or self.up < UPLOAD:
            self.driver.get(url)
            time.sleep(5)
            username_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            username_input.send_keys(TWITTER_USERNAME)
            next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            next_button.click()
            time.sleep(5)
            password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(TWITTER_PASSWORD)
            log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
            log_in_button.click()
            # sometimes some bs pop-ups appear, you have to click them manually
            time.sleep(5)
            tweet_input_click = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div')
            tweet_input_click.click()
            time.sleep(2)
            tweet_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_input.send_keys(f'Why is my internet speed at {self.down}/{self.up} Mbps, '
                                  f'when i pay for {UPLOAD}/{DOWNLOAD}?')
            # tweet_input.send_keys('Hello twitter')
            time.sleep(2)
            tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet.click()
