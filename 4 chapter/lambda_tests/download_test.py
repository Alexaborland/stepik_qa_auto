import glob
import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path_downloaded = 'C:\\Users\\HP\\PycharmProjects\\stepik_qa_auto\\4 chapter\\lambda_tests\\downloaded_files\\'
#
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': path_downloaded}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

click_download = driver.find_element(By.XPATH, '//button[contains(text(), "Download File")]')
click_download.click()
print('download clicked')
time.sleep(3)

'''The directory is not empty'''
# if os.listdir(path_downloaded):
#     print('The file is downloaded')
# else:
#     print('There is nothing')

'''The file exists in this directory'''
file_name = 'LambdaTest.pdf'
file_path = path_downloaded + file_name
assert os.access(file_path, os.F_OK)
print('The file exists in this directory')
time.sleep(3)



# files = glob.glob(os.path.join(path_downloaded, '*.*'))
# for file in files:
#     i = os.path.getsize(file)
#     if i > 10:
#         print('The file is not empty')
#     else:
#         print('The file is empty')

'''directory cleaning'''
files = glob.glob(os.path.join(path_downloaded, '*.*'))
for file in files:
    os.remove(file)
