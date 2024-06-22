from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):

        user_name = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_name)
        print('Login input')

        user_password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        user_password.send_keys(login_password)
        print('Password input')

        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        login_button.click()
        print('Password input')

    def is_login_successful(self):
        try:
            product_title = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//span[text()="Products"]')))
            print('The title exists')
            return True
        except:
            try:
                error_message = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//h3[@data-test="error"]')))
                print('The error message exists')
            except:
                return False

    def logout(self):
        menu_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
        menu_button.click()

        logout = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
        logout.click()



