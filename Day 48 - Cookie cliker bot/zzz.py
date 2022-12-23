from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

URL = 'http://orteil.dashnet.org/experiments/cookie/'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")

# I think timeout should be set bigger to inscrease the possibility for buying more expensive tool
timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        # get current money
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            current_money = int(money.replace(",", ""))
        else:
            current_money = int(money)

        # buy tool
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for upgrade in store[::-1]:
            upgrade_text = upgrade.text
            if upgrade_text != "":
                detail = upgrade_text.split("-")
                product = detail[0].strip()
                cost = detail[-1].strip()
                if "," in cost:
                    cost = cost.replace(",", "")
                cost_int = int(cost)
                if current_money >= cost_int:
                    driver.find_element(By.ID, f"buy{product}").click()
                    break
                else:
                    continue

        timeout = time.time() + 10

    if time.time() > five_min:
        cookie_per = driver.find_element(By.ID, "cps").text
        print(cookie_per)
        break