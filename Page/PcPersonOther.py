from Page.BasePage import BasePage
from Page.PcPersonPreview import PcPersonPreview
from selenium.webdriver.common.by import By

class PcPersonOther(BasePage):
    """
    PC其他信息页
    """

    def goto_preview_page(self):
        """
        不选择任何直接下一步
        :return:
        """
        self.find_and_click(By.XPATH,'//*[@id="careerInfoNext"]')
        return PcPersonPreview(self._driver)
