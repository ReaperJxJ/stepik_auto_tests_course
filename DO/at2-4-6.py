from selenium import webdriver
from selenium.webdriver.common.by import By

import time


LINK = 'http://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    btn = browser.find_element(By.ID,"button")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
