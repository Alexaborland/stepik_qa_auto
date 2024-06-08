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
base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.maximize_window()

# name = 'Alexandra'
#
# input_form = driver.find_element(By.XPATH, '//input[@id="user-message"]')
# input_form.send_keys(name)
#
# get_checked_button = driver.find_element(By.XPATH, '//button[@id="showInput"]')
# get_checked_button.click()
#
# your_message = driver.find_element(By.XPATH, '//p[@id="message"]')
# text_your_message = your_message.text
# print(text_your_message)
# assert text_your_message == name
# print('The name is same')

num_1 = 123
num_2 = 456
num_sum = num_1 + num_2
print(num_sum)

input_field_1 = driver.find_element(By.XPATH, '//input[@id="sum1"]')
input_field_2 = driver.find_element(By.XPATH, '//input[@id="sum2"]')
input_field_1.send_keys(num_1)
input_field_2.send_keys(num_2)

sum_check_button = driver.find_element(By.XPATH, '//button[contains(text(),"Get Sum")]')
sum_check_button.click()

result = driver.find_element(By.XPATH, '//p[@id="addmessage"]')
# result_text = int(result.text)
result_text = result.text
# assert result_text == num_sum
assert result_text == str(num_sum)
