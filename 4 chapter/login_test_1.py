import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

'''Headless mode'''
# options.add_argument('--headless')

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input login')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('Input password')
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click login button')

'''Opening the Menu'''
menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print('Click Menu button')
time.sleep(2)
link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()

'''Scrolling'''
# driver.execute_script('window.scrollTo(0, 200)')

'''Finding element'''
# action = ActionChains(driver)
# red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
# action.move_to_element(red_t_shirt).perform()

'''Find element on the main page'''
# text_products = driver.find_element(By.XPATH, '//span[@class="title"]')
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == 'Products'
# print('Good')
# driver.close()

'''Checking the url'''
# url = "https://www.saucedemo.com/inventory.html"
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('Good url')
