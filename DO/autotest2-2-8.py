from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time

LINK = 'https://suninjuly.github.io/file_input.html'

try: 
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'fl.txt')
    browser = webdriver.Chrome()
    browser.get(LINK)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Name')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Surname')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('megamail@mail.com')
    add_file = browser.find_element(By.ID, 'file')
    add_file.send_keys(file_path)
    submit_btn = browser.find_element(By.CLASS_NAME,'btn')
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
