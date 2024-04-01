import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



email = 'rtyrtyqweqwe39@gmail.com'
password = os.environ.get('D32_gmail_pass')
chrome_driver_path = os.environ.get('D48_chrome_driver_path')

options = Options()
# options.add_argument('-headless=new')
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
time.sleep(20)

jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobs.click()
time.sleep(1)

search_bar = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]')
search_bar.click()
time.sleep(1)

search_bar_input = driver.find_element(By.CSS_SELECTOR, 'div.jobs-search-box__inner input.jobs-search-box__keyboard-text-input')
search_bar_input.send_keys('"machine learning"')
search_bar_input.send_keys(Keys.ENTER)
time.sleep(3)

experience_level_options = driver.find_element(By.CSS_SELECTOR, 'button[id="searchFilter_experience"]')
experience_level_options.click()
time.sleep(3)

internship_checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for=experience-1]')
entry_checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for=experience-2]')
internship_checkbox.click()
entry_checkbox.click()
time.sleep(2)

show_results_button = driver.find_element(By.CSS_SELECTOR, 'div[id="hoverable-outlet-experience-level-filter-value"] button[data-control-name="filter_show_results"]')
# print(show_results_button.is_displayed())
show_results_button.click()