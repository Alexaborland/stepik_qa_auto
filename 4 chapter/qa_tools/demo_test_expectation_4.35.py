

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
# base_url = 'https://demoqa.com/dynamic-properties'
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()
# driver.implicitly_wait(10)


def hide_ads(driver):
    driver.execute_script("""
        var elements = document.querySelectorAll('div[id^="google_ads_iframe"]');
        elements.forEach(function(element) {
            element.style.display = 'none';
        });
    """)


time.sleep(2)
hide_ads(driver)

# print('Test starts')
# visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
# visible_button.click()
# print('Test finished')

print('Test starts')
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="visibleAfter"]')))
visible_button.click()
print('Test finished')