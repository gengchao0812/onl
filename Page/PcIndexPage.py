from selenium import webdriver
from Page.BasePage import BasePage
from Page.PcFamilyCard import FamilyCard
from selenium.webdriver.common.by import By
from Page.PcAuthentication import PcAuthentication

class PcIndexPage(BasePage):
    _base_url = "http://22.188.44.178/apply/pc/index"
    """
    PC首页点击事件
    定义了界面按钮
    goto_young -- 年轻时尚
    goto_family -- 卡片全家福
    goto_card -- 我要办卡
    """

    def goto_yonug(self):
        #年轻时尚点击事件
        self.find_and_click(By.XPATH,'//*[@class="top-up"]/a[1]')

    def goto_family(self):
        #卡片全家福点击事件
        self.find_and_click(By.XPATH, "//*[@class='top-up']/a[5]")
        self._driver.implicitly_wait(3)
        return FamilyCard(self._driver)

    def goto_card(self):
        #我要办卡点击事件
        self.find_and_click('//*[@class="top-up"]/a[7]')
        return PcAuthentication(self._driver)


