from selenium import webdriver
from selenium.webdriver.common.by import By
import time


LINK = "http://suninjuly.github.io/find_xpath_form"
FIRST_NAME_TAG = "input"
LAST_NAME_NAME = "last_name"
CITY_CLASS_NAME = "city"
COUNTRY_ID = "country"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    input1 = browser.find_element(By.TAG_NAME, FIRST_NAME_TAG)
    input1.send_keys("Lexa")
    input2 = browser.find_element(By.NAME, LAST_NAME_NAME)
    input2.send_keys("Alekseev")
    input3 = browser.find_element(By.CLASS_NAME, CITY_CLASS_NAME)
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.ID, COUNTRY_ID)
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, '//*/button[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
