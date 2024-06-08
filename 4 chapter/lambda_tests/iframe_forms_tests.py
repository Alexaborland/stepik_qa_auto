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
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()

iframe = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
driver.switch_to.frame(iframe)
text_frame = driver.find_element(By.XPATH, '//div[@id="__next"]/div/div[2]')
text_frame_text = text_frame.text
print(text_frame_text)

text_frame.send_keys(Keys.CONTROL + 'a')

click_edition_panel_bold = driver.find_element(By.XPATH, '//button[@title="Bold"]')
click_edition_panel_bold.click()
print('The text became bold')

new_text_frame = driver.find_element(By.XPATH, '//div[@id="__next"]/div/div[2]/b')
new_text_frame_text = new_text_frame.text
print(new_text_frame_text)

assert text_frame_text == new_text_frame_text
