from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_page import LoginPage


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

        login_standard_user = 'standard_user'
        password_all = 'secret_sauce'

        login = LoginPage(driver)
        login.authorisation(login_name=login_standard_user, login_password=password_all)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button['
                                                                                               '@id="add-to-cart'
                                                                                               '-sauce-labs-backpack"]')))
        select_product.click()
        print('Product is added to cart')

        cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
        cart.click()
        print('Clicked to the cart button')

        successes_add_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Your Cart")]'))).text
        assert successes_add_product == 'Your Cart'
        print('Test is successful')


shop = Shop()
shop.select_product()
