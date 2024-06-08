import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

click_drop_down = driver.find_element(By.XPATH, '//span[@aria-labelledby="select2-country-container"]')
click_drop_down.click()
print('Dropdown clicked')

# pick_country = driver.find_element(By.XPATH, '(//li[@class="select2-results__option"])[5]')
# pick_country.click()
# time.sleep(3)

write_country = driver.find_element(By.XPATH, '(//input[@class="select2-search__field"])[2]')
write_country.send_keys('India')
time.sleep(2)
write_country.send_keys(Keys.ENTER)
print('The country name was written')
driver.close()