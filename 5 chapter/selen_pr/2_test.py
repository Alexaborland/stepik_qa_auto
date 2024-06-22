from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login import LoginPage


class Shop:
    def select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print('Test starts')

        login_standard_user = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user',
                               'error_user', 'visual_user']
        password_all = 'secret_sauce'

        login_page = LoginPage(driver)

        for login_name in login_standard_user:
            try:
                login_page.authorization(login_name=login_name, login_password=password_all)
                if login_page.is_login_successful():
                    print('Success')
                    login_page.logout()
                else:
                    print(f"Login failed for {login_name}, retrying with the next account.")
            except Exception as e:
                print(f"An error occurred during login: {e}")

            driver.refresh()

        driver.quit()

shop = Shop()
shop.select_product()


