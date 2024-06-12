from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

'''Headless mode'''
# options.add_argument('--headless')

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

'''Sigh in'''
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input login')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('Input password')
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Clicked login button')


def pick_the_product():
    while True:
        try:
            print('Welcome to the shop!')
            print('1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs '
                  'Fleece'
                  'Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)')
            product_number = int(input("Pick the product and print number from 1 to 6: "))

            if product_number == 1:
                add_to_cart_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
                add_to_cart_product_1.click()
                product_name = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]').text
                product_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]').text
                print(f'{product_name} was picked')
            elif product_number == 2:
                add_to_cart_product_2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
                add_to_cart_product_2.click()
                product_name = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]').text
                product_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]').text
                print(f'{product_name} was picked')
            elif product_number == 3:
                add_to_cart_product_3 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
                add_to_cart_product_3.click()
                product_name = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]').text
                product_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[3]').text
                print(f'{product_name} was picked')
            elif product_number == 4:
                add_to_cart_product_4 = driver.find_element(By.XPATH,
                                                            '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
                add_to_cart_product_4.click()
                product_name = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]').text
                product_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[4]').text
                print(f'{product_name} was picked')
            elif product_number == 5:
                add_to_cart_product_5 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
                add_to_cart_product_5.click()
                product_name = driver.find_element(By.XPATH, '//a[@id="item_2_title_link"]').text
                product_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[5]').text
                print(f'{product_name} was picked')
            elif product_number == 6:
                add_to_cart_product_6 = driver.find_element(By.XPATH,
                                                            '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
                add_to_cart_product_6.click()
                product_name = driver.find_element(By.XPATH, '//a[@id="item_3_title_link"]').text
                product_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[6]').text
                print(f'{product_name} was picked')
            else:
                print("Incorrect number. Print the number from 1 to 6.")
                continue

            print(f'Product: {product_name}, Price: {product_price}')

            '''Click the cart button'''
            cart = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
            cart.click()
            print('Clicked to the cart button')

            '''Info Cart Product'''
            cart_product_name = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
            cart_product_price = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]').text
            print(f'Product: {cart_product_name}, Price: {cart_product_price}')
            assert product_name == cart_product_name
            assert product_price == cart_product_price
            print('Cart name info for product is correct')

            '''Checkout'''
            checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
            checkout.click()
            print('Clicked Checkout button')

            '''Fill out the delivery info'''
            user_first_name = 'Alexa'
            user_last_name = 'Borland'
            user_zip_code = 'MP6 A8T'
            first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
            first_name.send_keys(user_first_name)
            print('First Name is printed')

            last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
            last_name.send_keys(user_last_name)
            print('Last Name is printed')

            zip_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
            zip_code.send_keys(user_zip_code)
            print('Zip Code is printed')

            continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
            continue_button.click()
            print('Clicked Continue button')

            '''Info Delivery Product'''
            delivery_product = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
            print(delivery_product)
            assert product_name == delivery_product
            print('Delivery name info is correct')

            delivery_price_product = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]').text
            print(delivery_price_product)
            assert product_price == delivery_price_product
            print('Delivery price info is correct')

            finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
            finish_button.click()

            '''Gratitude page'''
            gratitude_for_order = driver.find_element(By.XPATH, '//h2[@class="complete-header"]').text
            assert gratitude_for_order == 'Thank you for your order!'
            print('The gratitude is correct')

            break

        except ValueError:
            print("Print the correct number.")
        except Exception as e:
            print(f"An error occurred: {e}")


pick_the_product()
