from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

fbmail = os.environ.get('Day50_fbmail')
fbpass = os.environ.get('Day50_fbpass')

URL = 'https://tinder.com/'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)

log_in_button = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div/div/header/'
                                              'div/div[2]/div[2]/a/div[2]/div[2]')
log_in_button.click()
time.sleep(1)
log_via_facebook = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/'
                                                 'button')
log_via_facebook.click()
time.sleep(1)

# In Selenium, each window has an identification handle, we can get all the window handles with:
# driver.window_handles
# The above line of code returns a list of all the window handles. The first window is at position 0 e.g.
base_window = driver.window_handles[0]
# New windows that have popped out from the base_window are further down in the sequence e.g.
fb_login_window = driver.window_handles[1]
# We can switch our Selenium to target the new facebook login window by:
driver.switch_to.window(fb_login_window)
# You can print the driver.title to verify that it's the facebook login window that is currently target:
cookie_button = driver.find_elements(By.CSS_SELECTOR, '._10 ._59s7 ._4t2a ._4-i2 ._9xo5 button')[0]
cookie_button.click()
time.sleep(1)
fb_login_input = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_pass_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_submit = driver.find_element(By.CSS_SELECTOR, '.login_form_container #loginform #buttons .uiButton')
fb_login_input.send_keys(fbmail)
fb_pass_input.send_keys(fbpass)
fb_submit.click()
time.sleep(10)

driver.switch_to.window(base_window)
driver.maximize_window()
first_accept = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
first_accept.click()
second_accept = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
second_accept.click()
time.sleep(10)
popupone = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[2]/button')
popupone.click()
cookies_button_two = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[2]/div/div/div[1]/div[1]/button/'
                                                   'div[2]/div[2]')
cookies_button_two.click()

for _ in range(10):
    try:
        time.sleep(3)
        like_button = driver.find_element(By.CSS_SELECTOR,
                                          '#q888578821 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button')
        like_button.click()
        time.sleep(3)
    except NoSuchElementException:
        print('Waiting to load up more people.')  # Probably won't be ever needed
        time.sleep(10)
    except ElementClickInterceptedException:
        print('Let me deal with that...')
        close_pop_up = driver.find_element(By.CSS_SELECTOR,
                                           '#q1218950022 > main > div > div.CenterAlign.M\(a\).Expand.Pos\(r\).Fx\(\$flx1\) > div > div.Pos\(a\).T\(0\).P\(20px\).P\(12px\)--xs.End\(0\) > button')
        close_pop_up.click()
        time.sleep(3)
