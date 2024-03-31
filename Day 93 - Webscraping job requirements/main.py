import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

email = 'rtyrtyqweqwe39@gmail.com'
password = os.environ.get('D32_gmail_pass')
chrome_driver_path = os.environ.get('D48_chrome_driver_path')

options = Options()
options.add_argument('-headless=new')
options.add_experimental_option("detach", True)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))

driver.get('https://linkedin.com')
driver.maximize_window()
time.sleep(2)

mail_input = driver.find_element(By.CSS_SELECTOR, '#session_key')
password_input = driver.find_element(By.CSS_SELECTOR, '#session_password')
submit_button = driver.find_element(By.CSS_SELECTOR, r'div[data-test-id="hero__content"] form[data-id="sign-in-form"] button[data-id="sign-in-form__submit-btn"]')

mail_input.send_keys(email)
password_input.send_keys(password)
submit_button.click()
