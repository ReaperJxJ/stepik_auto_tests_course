from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time


LINK = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    butn = browser.find_element(By.CLASS_NAME, 'btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    answer_field = browser.find_element(By.ID,'answer')
    answer_field.send_keys(y)
    submit_button = browser.find_element(By.CLASS_NAME, 'btn').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
