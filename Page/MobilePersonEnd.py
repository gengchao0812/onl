from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
import re
import time

class MobilePersonEnd(BasePage):
    """
    手机结束页面
    """
    def goto_index_mobile(self):
        time.sleep(3)
        message = self.find(By.XPATH,'//*[@class="describe_p').text
        appid = re.findall(r'您的申请件编号是"(.*)"', message)
        return appid
