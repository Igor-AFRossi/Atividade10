import pytest
import time
from selenium.webdriver.common.by import By

buscas = [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
]

@pytest.mark.web
@pytest.mark.parametrize("termo_busca", buscas)
def test_busca_google(chrome_driver, termo_busca):
    driver = chrome_driver
    driver.get("https://www.google.com")
    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(termo_busca)
        search_box.submit()
    except Exception:
        pytest.skip("Google não disponível ou bloqueado neste ambiente")

    time.sleep(2)
    assert termo_busca.lower() in driver.page_source.lower()
