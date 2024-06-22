from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def authorisation(self, login_name, login_password):
        user_name = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_name)
        print('Input login')

        password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(login_password)
        print('Input password')

        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        button_login.click()
        print('Clicked login button')

    def is_login_successful(self):
        try:
            products_title = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//span[text()="Products"]')))
            print('Login successful, Products page is displayed.')
            return True
        except:
            try:
                error_message = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//h3[@data-test="error"]')))
                print('Login error message displayed:', error_message.text)
            except:
                print('Login failed, no error message displayed.')
            return False

    def logout(self):
        menu_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
        menu_button.click()

        logout = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
        logout.click()
