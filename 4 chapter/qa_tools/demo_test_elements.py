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
# base_url = 'https://demoqa.com/checkbox'
# base_url = 'https://demoqa.com/radio-button'
# base_url = 'https://demoqa.com/buttons'
base_url = 'https://www.mvideo.ru/brand/apple-685?categoryId=10'
driver.get(base_url)
driver.maximize_window()

'''Checkbox'''
# checkbox = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
# checkbox.click()
# button_list = driver.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]')
# button_list.click()

'''Radiobutton'''
# radiobutton = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
# radiobutton.click()
# text_about_selection = radiobutton.text
# result = 'Yes'
# assert result == text_about_selection
# print('Passed')

'''Double click'''
# action = ActionChains(driver)
#
# doubleclick_button = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
# action.double_click(doubleclick_button).perform()
#
# right_click_button = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
# action.context_click(right_click_button).perform()

'''Slider'''
time.sleep(5)
action = ActionChains(driver)

slider_square = driver.find_element(By.XPATH, '//a[@class="ui-slider-handle ui-state-default ui-corner-all"]')

action.click_and_hold(slider_square).move_by_offset(200, 0).release().perform()

