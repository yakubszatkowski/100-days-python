# Both projects are rather me having fun and learning with selectors that's why its inconsistent
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

email = 'rtyrtyqweqwe39@gmail.com'
password = os.environ.get('D32_gmail_pass')
phone_number = '123 123 123'

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3403355181&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)
driver.maximize_window()

time.sleep(1)
log_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
log_in.click()

time.sleep(1)
mail_input = driver.find_element(By.CSS_SELECTOR, '#username')
pass_input = driver.find_element(By.CSS_SELECTOR, '#password')
submit_button = driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button')
mail_input.send_keys(email)
pass_input.send_keys(password)
submit_button.click()

time.sleep(3)
list_of_jobs = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')

for job in list_of_jobs[0:1]:
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", job)
    job.click()

    time.sleep(1)
    apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
    apply_button.click()

    time.sleep(1)
    phone_input = driver.find_element(By.CSS_SELECTOR, '.jobs-easy-apply-modal .jobs-easy-apply-form-section__grouping '
                                                       '.artdeco-text-input--input')
    phone_input.send_keys(phone_number)
    next_button = driver.find_element(By.XPATH, '//*[text() = "Next"]')
    next_button.click()

    time.sleep(1)
    choose_button = driver.find_element(By.XPATH, '//*[text() = "Next"]')
    choose_button.click()
    next_button = driver.find_element(By.XPATH, '//*[text() = "Next"]')
    next_button.click()
    # I've ended here because project's requirements are outdated and can't be met because of LinkedIn changing
    # its application process and sending empty resumes is pretty 'assholish' anyway
