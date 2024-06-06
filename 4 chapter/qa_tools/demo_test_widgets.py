import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

'''Calendar'''
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.click()
time.sleep(3)
# date_value = new_date.get_attribute('value') # получение значения из этого поля
# clear_symbol = (len(date_value)) # подсчет количества символов в значение
# new_date.send_keys(Keys.BACKSPACE*clear_symbol)
# new_date.send_keys('05/10/2024')
# new_date.send_keys(Keys.ENTER)
#
# today_date = driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day") and contains(@class, "--today")]')
# now_date = datetime.datetime.utcnow().strftime('%d')
# print(now_date)
# date = int(now_date) + 10
# locator = '//div[@aria-label="Choose Wednesday, June ' + str(date) + 'th, 2024"]'
# print(locator)


# tomorrow_date = driver.find_element(By.XPATH, locator)
# tomorrow_date.click()
