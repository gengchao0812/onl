from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
from Page.MobileAuthentication import MobileAuthentication

class MobileProductDetails(BasePage):
    """
    手机产品介绍页
    """

    def goto_authentication_mobile(self):
        self._driver.implicitly_wait(3)
        self.find(By.XPATH, '//*[@class="ui-btn ui-corner-all solo_btn"]').click()
        self._driver.implicitly_wait(3)
        return MobileAuthentication(self._driver)
