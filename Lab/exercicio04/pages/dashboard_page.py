from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    WELCOME_LOCATOR = (By.TAG_NAME, "h1")

    def esta_logado(self):
        try:
            txt = self.obter_texto(self.WELCOME_LOCATOR)
            return "Logged In Successfully" in txt or "Logged In" in txt
        except Exception:
            return False

    def obter_mensagem_boas_vindas(self):
        try:
            return self.obter_texto(self.WELCOME_LOCATOR)
        except Exception:
            return ""
