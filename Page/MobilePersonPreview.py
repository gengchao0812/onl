from Page.BasePage import BasePage
from Page.MobilePersonEnd import MobilePersonEnd
from selenium.webdriver.common.by import By
import time

class MobilePersonPreview(BasePage):
    """
    手机预览页面
    """
    def goto_end_page_mobile(self):
        time.sleep(6)
        self.find(By.XPATH, '//*[@id="nextStep"]')
        self._driver.find_element_by_xpath('//*[@id="nextStep"]').click()
        return MobilePersonEnd(self._driver)