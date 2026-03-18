import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

link = "http://selenium1py.pythonanywhere.com"
def test_login(browser):
    browser.get(link)
    browser.find_element_by_id("username").send_keys("test")