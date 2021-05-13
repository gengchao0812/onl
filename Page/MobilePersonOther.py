from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
from Page.MobilePersonPreview import MobilePersonPreview

class MobilePersonOther(BasePage):
    """
    手机其他信息页
    """

    def goto_preview_page_mobile(self):
        """
        不选择任何直接下一步
        :return:
        """
        self.find_and_click(By.XPATH, '//*[@id="nextStep"]')
        return MobilePersonPreview(self._driver)
