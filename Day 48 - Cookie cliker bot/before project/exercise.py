import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


URL = 'https://www.python.org/'
chrome_driver_path = os.environ.get('D48_chrome_driver_path')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get(URL)
driver.maximize_window()
time.sleep(0.25)

# upcoming_events = driver.find_element(by=By.CSS_SELECTOR, value='.event-widget .shrubbery .menu')
# events_list = upcoming_events.text.split('\n')
# events_dates = events_list[::2]
# events_names = events_list[1::2]
# event_dict = {}
# for num in range(len(events_dates)):
#     event_dict[num] = {'time': events_dates[num], 'name': events_names[num]}
# print(event_dict)

events_dates = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
events_names = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget .menu a')
events_dict = {}
for num in range(len(events_dates)):
    events_dict[num] = {
        'time': events_dates[num].text,
        'name': events_names[num].text,
    }

print(events_dict)
driver.close()
