from selenium import webdriver
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = 'c:\\webdrivers\\chromedriver.exe'

is_prime = lambda n: False if n == 1 else not 0 in [n%i for i in range(2, n)]

driver = webdriver.Chrome(DRIVER_PATH)
driver.get('https://isthisprime.com/game/')
driver.find_element_by_id('start').click()
start_time = time.time()

while time.time() - start_time < 60:
    number = driver.find_element_by_id('n').text
    if is_prime(int(number)):
        driver.find_element_by_id('yes').click()
    else:
        driver.find_element_by_id('no').click()


