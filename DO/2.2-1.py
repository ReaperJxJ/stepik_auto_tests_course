import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'
# открываем браузер и переходим по ссылке
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим числа на странице
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    print(num1)
    print(num2)

    # Складываем числа
    result = str(num1 + num2)
    print(result)

    # Находим выпадающий список
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(result)

    # Находим и нажимаем кнопку
    option1 = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    option1.click()

finally:
    # Ждем
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()