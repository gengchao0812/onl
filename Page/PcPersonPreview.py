from Page.BasePage import BasePage
from Page.PcPersonEnd import PcPersonEnd
from selenium.webdriver.common.by import By
import time

class PcPersonPreview(BasePage):
    """
    PC预览页面
    """
    def goto_end_page(self):
        time.sleep(6)
        self.find(By.XPATH, '//*[@id="confirmNext"]')
        self._driver.find_element_by_xpath('//*[@id="confirmNext"]').click()
        return PcPersonEnd(self._driver)