from selenium import webdriver
from Page.BasePage import BasePage
from Page.MobileFamilyCard import MobileFamilyCard
from selenium.webdriver.common.by import By
from Page.PcAuthentication import PcAuthentication

class MobileIndexPage(BasePage):
    _base_url = "http://22.188.46.142/apply/mobile/index"
    """
    手机首页点击事件
    定义了界面按钮
    goto_young -- 年轻时尚
    goto_family -- 卡片全家福
    goto_card -- 我要办卡
    """

    def goto_yonug(self):
        #年轻时尚点击事件
        self.find_and_click(By.XPATH,'//*[@class="top-up"]/a[1]')

    def goto_family_mobile(self):
        #卡片全家福点击事件
        self.find_and_click(By.XPATH, "//*[@id='family']")
        self._driver.implicitly_wait(3)
        return MobileFamilyCard(self._driver)

    def goto_card(self):
        #我要办卡点击事件
        self.find_and_click('//*[@id="mchot"]')
        # return PcAuthentication(self._driver)


