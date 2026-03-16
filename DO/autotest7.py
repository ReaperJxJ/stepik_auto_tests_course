import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


LINK = 'https://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    treasure = browser.find_element(By.ID, 'treasure')
    x = int(treasure.get_attribute('valuex'))
    y = calc(x)

    answer_field = browser.find_element(By.ID,'answer')
    answer_field.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()