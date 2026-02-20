from selenium import webdriver
from selenium.webdriver.common.by import By

import math, time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

LINK = 'https://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    btn = browser.find_element(By.CLASS_NAME, 'btn')
    btn.click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)
    submit_btn = browser.find_element(By.CLASS_NAME, 'btn')
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
