import pytest
from selenium.webdriver.common.by import By

@pytest.mark.web
def test_login_sucesso(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    assert "Logged In Successfully" in driver.page_source

@pytest.mark.web
def test_login_email_invalido(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    assert "Your username is invalid!" in driver.page_source

@pytest.mark.web
def test_login_senha_incorreta(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("WrongPassword")
    driver.find_element(By.ID, "submit").click()

    assert "Your password is invalid!" in driver.page_source

@pytest.mark.web
def test_login_sem_campos(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "submit").click()
    assert "Your username is invalid!" in driver.page_source or "Your password is invalid!" in driver.page_source
