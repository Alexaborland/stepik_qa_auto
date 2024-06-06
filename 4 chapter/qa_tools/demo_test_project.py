from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

current_date = datetime.now()
current_date_format = current_date.strftime('%m/%d/%Y')
print(f'Today date is {current_date_format}')
new_date = current_date + timedelta(days=10)
date = new_date.strftime('%m/%d/%Y')
print(f'New date is {date}')

date_put_in_field = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
date_put_in_field.click()
date_put_in_field.click()
date_value = date_put_in_field.get_attribute('value')
clear_symbol = (len(date_value))
date_put_in_field.send_keys(Keys.BACKSPACE*clear_symbol)
date_put_in_field.send_keys(date)

