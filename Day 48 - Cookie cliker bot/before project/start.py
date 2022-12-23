from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
URL = 'https://www.python.org/'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)

# To check price of rice cooker on amazon
# price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# print(price.text)

# # Finding elements by HTML
# search_bar = driver.find_element(by=By.NAME, value='q')
# print(search_bar)  # names the element
# print(search_bar.tag_name)  # says what elemet it is
# print(search_bar.get_attribute('placeholder'))
# logo = driver.find_element(by=By.CLASS_NAME, value='python-logo')
# print(logo.size) # prints size of logo

# # Finding elements by CSS
# documentation = driver.find_element(by=By.CSS_SELECTOR, value='.documentation-widget a')
# print(documentation.text)

# # Finding emelets by XPATH
# submit_bug = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug.etg)

driver.close()
