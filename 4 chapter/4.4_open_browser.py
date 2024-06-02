from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# user_name = driver.find_element_by_id('user-name')
# user_name.send_keys('standard_user')
# user_name = driver.find_element(By.ID, 'user-name') # ID
# user_name = driver.find_element(By.NAME, 'user-name')   # NAME
# user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')   # full XPATH
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')   # Id XPATH
user_name.send_keys('standard_user')
password = driver.find_element(By.CSS_SELECTOR, '#password')    # css_selector
password.send_keys('secret_sauce')
button_login = driver.find_element(By.XPATH, '//input[@value="Login"]')
button_login.click()


