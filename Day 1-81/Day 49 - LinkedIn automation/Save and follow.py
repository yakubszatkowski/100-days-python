# Both projects are rather me having fun and learning with selectors that's why its inconsistent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

linkedin_mail = os.environ.get('D49_linkedin_mail')
linkedin_pass = os.environ.get('D49_linkedin_pass')

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3403355181&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)
# driver.maximize_window()

time.sleep(1)
log_in = driver.find_element(By.CSS_SELECTOR, '.base-serp-page__header .nav .nav__button-secondary')
log_in.click()
time.sleep(1)

e_mail_box = driver.find_element(By.XPATH, '//*[@id="username"]')
password_box = driver.find_element(By.XPATH, '//*[@id="password"]')
submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

e_mail_box.send_keys(linkedin_mail)
password_box.send_keys(linkedin_pass)
submit_button.click()
time.sleep(20)  # verification bs - pick picture that shows this and that

try:  # verification bs - sometimes element of closing changes ID
    dumb_button = driver.find_element(By.ID, 'ember115')
except NoSuchElementException:
    try:
        dumb_button = driver.find_element(By.ID, 'ember114')
    except NoSuchElementException:
        dumb_button = driver.find_element(By.ID, 'ember116')

dumb_button.click()

jobs_list = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
for job in jobs_list:
    driver.execute_script("arguments[0].scrollIntoView();", job)  # scrolls until the object is visible
    job.click()
    time.sleep(2)
    save_button = driver.find_element(By.CSS_SELECTOR, '.application-outlet .scaffold-layout__detail '
                                                       '.jobs-unified-top-card .jobs-save-button')

    follow_button = driver.find_element(By.CSS_SELECTOR, '.application-outlet .scaffold-layout__detail '
                                                         '.jobs-company .follow')
    try:
        # sometimes button is not visible because of random popup stuff,
        # so I am scrolling slightly below Y coordinate of button
        save_button.click()
    except ElementClickInterceptedException:
        y_cord_save_button = int(save_button.location['y'])
        driver.execute_script(f"window.scrollTo(0, {y_cord_save_button + 450})")
        save_button.click()
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", follow_button)
    follow_button.click()
    time.sleep(1)
