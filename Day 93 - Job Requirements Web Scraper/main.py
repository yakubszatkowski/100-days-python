import os, time, re
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


def find_job_titles(job_list):
    return job_list.find_elements(By.CSS_SELECTOR, 'li.jobs-search-results__list-item div.job-card-container div.artdeco-entity-lockup__content div.artdeco-entity-lockup__title a strong')


def load_job_listing(driver, job_list):
    time.sleep(2)
    is_full_list = False
    while not is_full_list:
        job_titles = find_job_titles(job_list)
        job_titles_amount = len(job_titles)
        driver.execute_script("arguments[0].scrollIntoView();", job_titles[-1])
        time.sleep(0.5)
        new_job_titles_amount = len(find_job_titles(job_list))
        if new_job_titles_amount == job_titles_amount:
            is_full_list = True
    return job_titles


def main_script(error_count, analyzed_job_titles):
    # Check error count
    print('Current error count: ', error_count)

    # Initialize driver
    options = Options()
    options.add_argument('-headless=new')  # for prod
    # options.add_experimental_option("detach", True) # for dev
    driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
    exceptions_to_ignore = (NoSuchElementException, StaleElementReferenceException)
    wait = WebDriverWait(driver, 5, ignored_exceptions=exceptions_to_ignore)
    driver.get('https://www.linkedin.com/login')
    driver.maximize_window()
    time.sleep(2)

    # Login
    mail_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, r'button[aria-label="Sign in"]')))
    mail_input.send_keys(email)
    password_input.send_keys(password)
    submit_button.click()


    # Start scraping listed job titles
    while analyzed_job_titles:
        analyzed_job_title = analyzed_job_titles[0]
        print('Job titles to analyze left:', analyzed_job_titles)
        print('Started scraping:', analyzed_job_title)

        # Getting to job listing
        jobs = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')))
        jobs.click()

        time.sleep(1)
        search_bar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav-search"]/div/div[2]')))
        search_bar.click()

        time.sleep(1)
        search_bar_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.jobs-search-box__inner input.jobs-search-box__keyboard-text-input')))
        search_bar_input.send_keys(analyzed_job_title)
        search_bar_input.send_keys(Keys.ENTER)
        experience_level_options = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="searchFilter_experience"]')))
        experience_level_options.click()
        time.sleep(1)
        internship_checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="experience-1"]')))
        entry_checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="experience-2"]')))
        internship_checkbox.click()
        entry_checkbox.click()
        time.sleep(1)
        show_results_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="hoverable-outlet-experience-level-filter-value"] div.reusable-search-filters-buttons button[aria-label*="Apply current filter to show"]')))
        show_results_button.click()
        time.sleep(1)

        # Load all the job listings by scrolling down as much as possible
        job_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.scaffold-layout__list-container')))
        job_titles = load_job_listing(driver, job_list)
        driver.execute_script("arguments[0].scrollIntoView();", job_titles[0])
        time.sleep(1)

        # Scrape job requirements
        job_requirements = ''
        for job_title in job_titles:
            job_title.click()
            time.sleep(1)
            job_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#job-details div.mt4')))
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
            
        # Filtering and counting technology keywords
        most_common_words = keyword_count(job_requirements)
        print('Technologies scraped:', most_common_words)

        # Saving technology keywords in google sheets
        update_worksheet(analyzed_job_title, most_common_words)

        # Removing job title from the list after finishing scraping it
        analyzed_job_titles.pop(0)
        print('Scraping', analyzed_job_title, 'finished.\n\n')


if __name__ == '__main__':

    # Variables
    email = 'rtyrtyqweqwe39@gmail.com'
    password = os.environ.get('D32_gmail_pass')
    chrome_driver_path = os.environ.get('D48_chrome_driver_path')
    error_count = 0
    analyzed_job_titles = [
        '"machine learning"', '"data science"', '"data engineer"', '"data analyst"',  '"software engineer"', 
        '"web developer"', '"devops engineer"', '"automation engineer"', '"mobile developer"',
    ]
    
    # Handling rare errors; running main script
    while error_count <= 5:
        if not analyzed_job_titles:
            break
        else:
            try:
                main_script(error_count, analyzed_job_titles)
            except Exception as e:  
                print('Error occured:', e)
                error_count += 1

# TODO
    # Try deploying to cloud service to run once a day - AWS Lambda
