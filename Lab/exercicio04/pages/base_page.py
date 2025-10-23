from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def abrir(self, url):
        self.driver.get(url)

    def clicar(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def digitar(self, locator, texto):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(texto)

    def obter_texto(self, locator):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        return elem.text
