import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.maximize_window()

'''Switch between tabs'''
# click_tab_button = driver.find_element(By.XPATH, '//button[@id="tabButton"]')
# click_tab_button.click()
# time.sleep(2)
# print(driver.current_url)
#
# header_1 = driver.find_element(By.XPATH, '//h1[@class="text-center"]')
# print(header_1.text)
#
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)
#
# header_2 = driver.find_element(By.XPATH, '//h1[@id="sampleHeading"]')
# print(header_2.text)
#
# driver.switch_to.window(driver.window_handles[0])
# print(driver.current_url)
time.sleep(2)  # Подождем, чтобы реклама успела загрузиться
driver.execute_script("""
    var elements = document.querySelectorAll('div[id^="google_ads_iframe"]');
    elements.forEach(function(element) {
        element.style.display = 'none';
    });
""")

time.sleep(2)
action = ActionChains(driver)
click_windows_button = driver.find_element(By.XPATH, '//button[@id="windowButton"]')
action.move_to_element(click_windows_button).perform()
time.sleep(3)
click_windows_button.click()
time.sleep(2)
print(driver.current_url)

windows_1 = driver.window_handles[0]
windows_2 = driver.window_handles[1]
driver.switch_to.window(windows_2)
print(driver.current_url)
# header_1 = driver.find_element(By.XPATH, '//h1[@class="text-center"]')
# print(header_1.text)
driver.switch_to.window(windows_1)
print(driver.current_url)

