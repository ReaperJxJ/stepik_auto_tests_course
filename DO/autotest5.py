from selenium import webdriver
from selenium.webdriver.common.by import By
import time


MANDATORY_ELEMENTS = ['//div[contains(@class, "first_block")]/div/input[contains(@placeholder, "first name")]',
                      '//div[contains(@class, "first_block")]/div/input[contains(@placeholder, "last name")]',
                      '//div[contains(@class, "first_block")]/div/input[contains(@placeholder, "email")]']

try: 
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    elements = []
    for element_xpath in MANDATORY_ELEMENTS:
      elements.append(browser.find_element(By.XPATH, element_xpath))
    for element in elements:
        element.send_keys("Ответ")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()