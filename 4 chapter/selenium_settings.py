from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настройка опций для Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# Использование ChromeService для управления драйвером
service = ChromeService(executable_path='C:/Users/HP/PycharmProjects/stepik_qa_auto/chromedriver/')

# Создание экземпляра драйвера с использованием службы и опций
driver = webdriver.Chrome(service=service, options=options)

# Альтернативный способ установки ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_1 = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Переход на целевой URL
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()