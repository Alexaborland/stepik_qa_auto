import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input login')

'''Clear the field'''
# time.sleep(3)
# user_name.clear()
# time.sleep(3)
# user_name.send_keys(login_standard_user)

'''Deleting symbols imitating the backspace button'''
# user_name.send_keys(Keys.BACKSPACE * 3)
# time.sleep(3)
# user_name.send_keys('ser')

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('Input password')
password.send_keys(Keys.ENTER) # click the enter button


'''Scrolling the list "filters" on the main page by hands'''
# filter = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
# filter.click()
# print('Click filters')
# time.sleep(3)
# filter.send_keys(Keys.DOWN)
# time.sleep(3)
# filter.send_keys(Keys.ENTER)
# button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
# button_login.click()
# print('Click login button')
