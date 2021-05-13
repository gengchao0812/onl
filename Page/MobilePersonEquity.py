from Page.BasePage import BasePage
from Page.MobilePersonOther import MobilePersonOther
from selenium.webdriver.common.by import By


class MobilePersonEquity(BasePage):
    """
    手机权益页面
    """
    def goto_persion_other_mobile(self):
        # target = self._driver.find_element(By.XPATH,'//*[@id="equityNext"]')
        # self._driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find(By.XPATH, '//*[@id="equitySubmit"]')
        self.find_and_click(By.XPATH, '//*[@id="equitySubmit"]')
        return MobilePersonOther(self._driver)