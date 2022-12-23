import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# URL = 'https://en.wikipedia.org/wiki/Main_Page'
URL = 'https://www.appbrewery.co/p/newsletter'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)

# article_count = driver.find_element(By.CSS_SELECTOR, value='.mw-parser-output #articlecount a')
# article_count.click()

# wikipedia_article = driver.find_element(By.LINK_TEXT, value='Wikipedia')
# wikipedia_article.click()

# search_bar = driver.find_element(By.NAME, value='search')
# search_bar.send_keys('Python')
# search_bar.send_keys(Keys.ENTER)

sub_type_in = driver.find_element(By.NAME, 'email')
sub_type_in.send_keys('randomemail@gmail.com')
sub_type_in.send_keys(Keys.ENTER)
