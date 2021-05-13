from Page.BasePage import BasePage
from Page.PcProductDetails import PcProductDetails
import time
from selenium.webdriver.common.by import By

class FamilyCard(BasePage):

    def goto_number_card(self):
        # 点击数字卡
        self._driver.find_element_by_xpath('//*[@class="screen_family"]/ul/li[6]/a').click()
        self.find_and_click(By.XPATH, '//*[@class="screen_family"]/ul/li[6]/a')
        self._driver.find_element_by_xpath('//*[@id="cardList"]/article[4]/div/div[4]/input').click()
        return PcProductDetails(self._driver)