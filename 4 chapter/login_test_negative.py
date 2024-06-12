import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from faker import Faker

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauc'

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input login')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('Input password')
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click login button')

warring_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warring_text = warring_text.text
assert value_warring_text == 'Epic sadface: Username and password do not match any user in this service'
print('Good test')

# driver.refresh()

'''Screenshot'''
base_dir = 'C:\\Users\\HP\\PycharmProjects\\stepik_qa_auto'
sub_dir = '4 chapter\\screenshots\\'
full_path = os.path.join(base_dir, sub_dir)

now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
name_screenshot = 'screenshot_' + now_date + '.png'
driver.save_screenshot(full_path + name_screenshot)