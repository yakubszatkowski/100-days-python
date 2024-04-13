import os, time, re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
# from keywords_list import negative_keywords

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


# INITIALIZE DRIVER
options = Options()
# options.add_argument('-headless=new')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))

driver.get('https://linkedin.com')
driver.maximize_window()
time.sleep(3)


# LOGIN
mail_input = driver.find_element(By.CSS_SELECTOR, '#session_key')
password_input = driver.find_element(By.CSS_SELECTOR, '#session_password')
submit_button = driver.find_element(By.CSS_SELECTOR, r'div[data-test-id="hero__content"] form[data-id="sign-in-form"] button[data-id="sign-in-form__submit-btn"]')
mail_input.send_keys(email)
password_input.send_keys(password)
submit_button.click()
time.sleep(20)


# FILTER FOR INTERNSHIP AND ENTRY LEVEL POSITIONS
analyzed_job_titles = [
    # data related
    '"machine learning"', '"data science"', '"data engineer"', '"data analyst"'
    # web development related
    '"back end developer"', '"front end developer"', '"web developer"', '"full stack developer"', 
    # software related
    '"software engineer"', '"software developer"'
    # mobile app related
    '"android developer"', '"ios developer"', '"mobile app developer"', 
    # other
    '"game developer"', '"blockchain"', '"rpa"', '"cloud engineer"', '"devops"'
    # '"_______"', 
]

for analyzed_job_title in analyzed_job_titles:
    jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
    jobs.click()
    time.sleep(3)

    search_bar = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]')
    search_bar.click()
    time.sleep(3)

    search_bar_input = driver.find_element(By.CSS_SELECTOR, 'div.jobs-search-box__inner input.jobs-search-box__keyboard-text-input')
    search_bar_input.send_keys(analyzed_job_title)
    search_bar_input.send_keys(Keys.ENTER)
    time.sleep(3)

    experience_level_options = driver.find_element(By.CSS_SELECTOR, 'button[id="searchFilter_experience"]')
    experience_level_options.click()
    time.sleep(3)

    internship_checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for=experience-1]')
    entry_checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for=experience-2]')
    internship_checkbox.click()
    entry_checkbox.click()
    time.sleep(3)

    show_results_button = driver.find_element(By.CSS_SELECTOR, 'div[id="hoverable-outlet-experience-level-filter-value"] button[data-control-name="filter_show_results"]')
    show_results_button.click()
    time.sleep(3)

    # LOAD FIRST PAGE JOB LISTINGS
    job_list = driver.find_element(By.CSS_SELECTOR, 'ul.scaffold-layout__list-container')
    job_titles = load_job_listing()
    driver.execute_script("arguments[0].scrollIntoView();", job_titles[0])

    # GRAB JOB REQUIREMENTS OF EACH JOB TITLE IN THE LIST
    job_requirements = ''
    for job_title in job_titles:
        job_title.click()
        time.sleep(1)
        job_description = driver.find_element(By.CSS_SELECTOR, 'div#job-details span')
        job_description_elements = job_description.find_elements(By.CSS_SELECTOR, 'span')

        for element in job_description_elements:
            try:
                html_object = element.get_attribute('innerHTML').lower()
            except StaleElementReferenceException:
                break
            # if any(keyword in html_object for keyword in negative_keywords):
            #     pass
            if '<li>' in html_object:
                html_pattern = re.compile('<.*?>')
                html_object_text_only = re.sub(html_pattern, '', html_object).strip()
                line = html_object_text_only + '\n'
                job_requirements += line 
            
    with open(r'Day 93 - Webscraping job requirements\.misc\job_descriptions.txt', "a", encoding="utf-8") as f:
        f.write(job_requirements)

    time.sleep(2)

#TODO
    # Get counts of each keyword
    # Save results in google spreadsheets - https://www.youtube.com/watch?v=Mz9JG9CUXXY
