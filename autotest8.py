from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

LINK = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    a = int(browser.find_element(By.ID, 'num1').text)
    b = int(browser.find_element(By.ID, 'num2').text)
    x = str(a + b)
    print(x)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(x)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
