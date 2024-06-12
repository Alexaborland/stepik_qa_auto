from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
# base_url = 'https://demoqa.com/dynamic-properties'
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()


def hide_ads(driver):
    driver.execute_script("""
        var elements = document.querySelectorAll('div[id^="google_ads_iframe"]');
        elements.forEach(function(element) {
            element.style.display = 'none';
        });
    """)


time.sleep(2)
hide_ads(driver)

# try:
#     visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_button.click()
# except NoSuchElementException as exception:
#     print('NoSuchElementException exception')
#     time.sleep(10)
#     try:
#         visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#         visible_button.click()
#         print('Click visible button')
#     except NoSuchElementException as exception:
#         print('Element still not found after waiting')

checkbox_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
checkbox_yes.click()
try:
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == 'No'
except AssertionError as exception:
    driver.refresh()
    time.sleep(2)
    hide_ads(driver)
    checkbox_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    checkbox_yes.click()
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == 'Yes'
    print('Checkbox YES')
print('Test is over')
