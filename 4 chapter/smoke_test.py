
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
print('Click login button')


'''Info product 1'''
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

'''Info product 2'''
product_2 = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[3]')
value_price_product_2 = price_product_2.text
print(value_price_product_2)

'''Adding products to cart'''
add_to_cart_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
add_to_cart_product_1.click()
print('Add the Product 1 to the cart')

add_to_cart_product_2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
add_to_cart_product_2.click()
print('Add the Product 2 to the cart')

cart = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
cart.click()
print('Click to the cart button')

'''Info Cart Product 1'''
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
cart_value_product_1 = cart_product_1.text
print(cart_value_product_1)
assert value_product_1 == cart_value_product_1
print('Cart name info for product 1 is correct')

cart_price_product_1 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]')
cart_value_price_product_1 = cart_price_product_1.text
print(cart_value_price_product_1)
assert value_price_product_1 == cart_value_price_product_1
print('Cart price info for product 1 is correct')

'''Info Cart Product 2'''
cart_product_2 = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
cart_value_product_2 = cart_product_2.text
print(cart_value_product_2)
assert value_product_2 == cart_value_product_2
print('Cart name info for product 2 is correct')

cart_price_product_2 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]')
cart_value_price_product_2 = cart_price_product_2.text
print(cart_value_price_product_2)
assert value_price_product_2 == cart_value_price_product_2
print('Cart price info for product 2 is correct')

'''Checkout'''
checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print('Click Checkout button')

'''Fill out the delivery info'''
user_first_name = 'Alexa'
user_last_name = 'Borland'
user_zip_code = 'MP6 A8T'
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys(user_first_name)
print('Filling out the First Name')

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys(user_last_name)
print('Filling out the Last Name')

zip_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip_code.send_keys(user_zip_code)
print('Filling out Zip Code')

continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
continue_button.click()
print('Click Continue button')

'''Info Delivery Product 1'''
delivery_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
delivery_value_product_1 = delivery_product_1.text
print(delivery_value_product_1)
assert value_product_1 == delivery_value_product_1
print('Delivery name info is correct')

delivery_price_product_1 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]')
delivery_value_price_product_1 = delivery_price_product_1.text
print(delivery_value_price_product_1)
assert value_price_product_1 == delivery_value_price_product_1
print('Delivery price info is correct')

'''Info Delivery Product 2'''
delivery_product_2 = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
delivery_value_product_2 = delivery_product_2.text
print(delivery_value_product_2)
assert value_product_2 == delivery_value_product_2
print('Delivery name info for product 2 is correct')

delivery_price_product_2 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]')
delivery_value_price_product_2 = delivery_price_product_2.text
print(delivery_value_price_product_2)
assert value_price_product_2 == delivery_value_price_product_2
print('Delivery price info for product 2 is correct')


price_1 = float(delivery_value_price_product_1.replace('$', ''))
price_2 = float(delivery_value_price_product_2.replace('$', ''))
sum_products = price_1 + price_2

total_price = driver.find_element(By.XPATH, '//div[@data-test="subtotal-label"]')
value_total_price = total_price.text
print(value_total_price)
value_total_price_num = float(value_total_price.replace('Item total: $', ''))
print(sum_products)
assert value_total_price_num == sum_products
print('The price is same')


finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
finish_button.click()

'''Gratitude page'''
gratitude_for_order = driver.find_element(By.XPATH, '//h2[@class="complete-header"]').text
assert gratitude_for_order == 'Thank you for your order!'
print('The gratitude is correct')