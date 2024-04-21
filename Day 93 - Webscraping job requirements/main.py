import os, time, re
start_time = time.time()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from keyword_analysis import keyword_count
from google_sheets import update_worksheet

email = 'rtyrtyqweqwe39@gmail.com'
password = os.environ.get('D32_gmail_pass')
chrome_driver_path = os.environ.get('D48_chrome_driver_path')



def find_job_titles():
    return job_list.find_elements(By.CSS_SELECTOR, 'li.jobs-search-results__list-item div.job-card-container div.artdeco-entity-lockup__content div.artdeco-entity-lockup__title a strong')


def load_job_listing():
    is_full_list = False
    while not is_full_list:
        job_titles = find_job_titles()
        job_titles_amount = len(job_titles)
        driver.execute_script("arguments[0].scrollIntoView();", job_titles[-1])
        time.sleep(1)
        new_job_titles_amount = len(find_job_titles())
        if new_job_titles_amount == job_titles_amount:
            is_full_list = True

    return job_titles


# Initialize driver
options = Options()
# options.add_argument('-headless=new')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
wait = WebDriverWait(driver, 10)
driver.get('https://linkedin.com')
driver.maximize_window()
time.sleep(5)


# Login
mail_input = driver.find_element(By.CSS_SELECTOR, '#session_key')
password_input = driver.find_element(By.CSS_SELECTOR, '#session_password')
submit_button = driver.find_element(By.CSS_SELECTOR, r'div[data-test-id="hero__content"] form[data-id="sign-in-form"] button[data-id="sign-in-form__submit-btn"]')
mail_input.send_keys(email)
password_input.send_keys(password)
submit_button.click()

analyzed_job_titles = [
    '"machine learning"', '"data science"', '"data engineer"', '"data analyst"', 
    '"software engineer"', '"web developer"', '"devops engineer"', '"mobile app developer"', 
    '"automation engineer"'
]

for analyzed_job_title in analyzed_job_titles:
    print(analyzed_job_title)
    # Searching for analyzed job title
    # time.sleep(30)
    jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
    jobs.click()
    time.sleep(2)

    search_bar = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]')
    search_bar.click()
    time.sleep(2)

    search_bar_input = driver.find_element(By.CSS_SELECTOR, 'div.jobs-search-box__inner input.jobs-search-box__keyboard-text-input')
    search_bar_input.send_keys(analyzed_job_title)
    search_bar_input.send_keys(Keys.ENTER)
    time.sleep(2)

    experience_level_options = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="searchFilter_experience"]')))
    experience_level_options.click()
    time.sleep(2)

    internship_checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for=experience-1]')
    entry_checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for=experience-2]')
    internship_checkbox.click()
    entry_checkbox.click()
    time.sleep(2)

    show_results_button = driver.find_element(By.CSS_SELECTOR, 'div[id="hoverable-outlet-experience-level-filter-value"] button[data-control-name="filter_show_results"]')
    show_results_button.click()
    time.sleep(2)

    # Load all the job listings by scrolling down as much as possible
    job_list = driver.find_element(By.CSS_SELECTOR, 'ul.scaffold-layout__list-container')
    job_titles = load_job_listing()
    driver.execute_script("arguments[0].scrollIntoView();", job_titles[0])

    # Scrape job requirements
    job_requirements = ''
    for job_title in job_titles:
        job_title.click()
        job_description = driver.find_element(By.CSS_SELECTOR, 'div#job-details div.mt4')
        job_description_elements = job_description.find_elements(By.CSS_SELECTOR, 'span')

        for element in job_description_elements:
            try:
                html_object = element.get_attribute('innerHTML').lower()
            except StaleElementReferenceException:
                break
            if '<li>' in html_object:
                html_pattern = re.compile('<.*?>')
                html_object_text_only = re.sub(html_pattern, '', html_object).strip()
                line = html_object_text_only + '\n'
                job_requirements += line 

            
    time.sleep(2)
    # Filtering and counting technology keywords
    most_common_words = keyword_count(job_requirements)
    print(most_common_words)
    # Saving technology keywords in google sheets
    update_worksheet(analyzed_job_title, most_common_words)


#TODO
    # job search interface changed when 2nd loop of job search starts
    # what to do if selenium object can't be found by the selector, how to repeat searching for selector? - WebDriverWait.until()
    # figure a way to schedule this script once a day on any cloud service

print("--- %s seconds ---" % (time.time() - start_time))