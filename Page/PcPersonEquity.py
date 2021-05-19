from Page.BasePage import BasePage
from Page.PcPersonOther import PcPersonOther
from selenium.webdriver.common.by import By


class PcPersonEquity(BasePage):
    """
    PC权益页面
    """
    def goto_persion_other(self):
        self.find(By.XPATH, '//*[@id="equityNext"]')
        self.find_and_click(By.XPATH, '//*[@id="equityNext"]')
        return PcPersonOther(self._driver)