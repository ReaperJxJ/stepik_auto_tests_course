from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time



LINK = 'https://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input_field = browser.find_element(By.CLASS_NAME,'form-control')
    input_field.send_keys(y)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = bool(people_radio.get_attribute("checked"))
    print("value of people radio: ", people_checked)
    if people_checked == True :
       print('checked')
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_checked = bool(robot_radio.get_attribute("checked"))
    print("value of robot radio: ", robot_checked, type(robot_checked))
    if robot_checked == True :
       print('checked')
    elif robot_checked == False:
       print('Unchecked')
    robot_radio.click()
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
