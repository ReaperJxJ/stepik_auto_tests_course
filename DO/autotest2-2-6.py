from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import math
import time


LINK = 'https://SunInJuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    answer_field = browser.find_element(By.ID,'answer')
    answer_field.send_keys(y)
    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.location_once_scrolled_into_view
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    # robot_radio.location_once_scrolled_into_view
    robot_radio.click()
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
