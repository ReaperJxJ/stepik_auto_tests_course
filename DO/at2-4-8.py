from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import math
import time


LINK = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    button.click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)
    # submit_btn = WebDriverWait(browser, 1).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, 'btn'))
    # ) 
    submit_btn = browser.find_element(By.ID, 'solve')
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()