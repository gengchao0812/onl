from Page.BasePage import BasePage
from Page.MobileProductDetails import MobileProductDetails
import time
from selenium.webdriver.common.by import By

class MobileFamilyCard(BasePage):
    """
    全家福选卡界面
    """
    def goto_number_card_mobile(self):
        # 点击数字卡
        self._driver.implicitly_wait(3)
        # self._driver.find_element_by_xpath('//*[@class="family_menu"]/ul/li[8]/a').click()
        self.find_and_click(By.XPATH, '//*[@class="family_menu"]/ul/li[8]/a')
        # self.find(By.XPATH, '//*[@class="card_list"]/div[3]/div[2]/button')
        time.sleep(1)
        self.find_and_click(By.XPATH, '//*[@class="card_list"]/div[3]/div[2]/button')
        return MobileProductDetails(self._driver)