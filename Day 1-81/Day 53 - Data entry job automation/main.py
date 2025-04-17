from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

DATA_SHEET = 'https://docs.google.com/spreadsheets/d/1aYadW8eTEwzn1Re-7T3VMjsnPQtrsAvKZ9IeL9bNbZ8/edit?resourcekey#gid=1899136292'
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScNvA9uFLvfZRfc1LHizRIvX7yfpVTAMrlmkoNGlZfgYu8YPg/viewform'
RENTING_WEBSITE = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.65786208105469%2C%22east%22%3A-122.20879591894531%2C%22south%22%3A37.56005507446884%2C%22north%22%3A37.989903032322125%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

# Opens zillo website with rent offers
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
driver = webdriver.Chrome()
driver.get(RENTING_WEBSITE)
time.sleep(1)

# Scrolls through page so every offer will be loaded
y = 1000
for n in range(5):
    driver.execute_script(f"window.scrollTo(0, {y});")
    y += 800
    time.sleep(0.5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extracts data and puts it into the lists
addresses = soup.find_all(attrs={'data-test': 'property-card-addr'})
prices = soup.find_all(attrs={'data-test': 'property-card-price'})
links = soup.find_all(attrs={'data-test': 'property-card-link'}, href=True)
addresses_list = [address.getText().split('|')[-1].strip() for address in addresses]
prices_list = [price.getText().split('+')[0] for price in prices]
links_list = [f'https://www.zillow.com{link["href"]}' for link in links[::2]]

# Fill in forms and submits them into data sheet
for n in range(len(addresses_list)):
    driver.get(FORM_URL)
    time.sleep(1)
    # Locates inputs and button
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    # Fills in extracted data and submits it
    address_input.send_keys(addresses_list[n])
    price_input.send_keys(prices_list[n])
    link_input.send_keys(links_list[n])
    submit_button.click()

    time.sleep(1)
