from Page.BasePage import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Page.MobilePersonEquity import MobilePersonEquity

class MobilePersonInformation(BasePage):
    """
    手机个人信息页
    """

    def goto_equity_mobile(self, appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo):
        self.find_and_click(By.XPATH, '//*[@id="appiBranchShow"]')
        self.find_and_click(By.XPATH, '//*[@id="_citys0"]/a[2]')
        self.find_and_click(By.XPATH, '//*[@id="_citys1"]/a[1]')
        self.find_and_click(By.XPATH, '//*[@id="_citys2"]/a[1]')
        # 省市区
        self.find_and_click(By.XPATH, '//*[@id="appiMcAddrShow"]')
        self.find_and_click(By.XPATH, '//*[@id="_citys0"]/a[2]')
        self.find_and_click(By.XPATH, '//*[@id="_citys1"]/a[1]')
        self.find_and_click(By.XPATH, '//*[@id="_citys2"]/a[1]')
        #家庭地址省市区
        # Select(self.find(By.XPATH, '//*[@id="appiMcIdLongFlag"]')).select_by_value("1")
        #证件是否长期有效
        time.sleep(5)
        Select(self.find(By.XPATH, '//*[@id="appiMcEducation"]')).select_by_value("3")
        #教育程度
        Select(self.find(By.XPATH, '//*[@id="appiMcMaritalSts"]')).select_by_value("3")
        #婚姻状况
        self.find_and_send(By.XPATH, '//*[@id="appiMcAddr1"]', appiMcAddr1)
        #住宅详细地址
        Select(self.find(By.XPATH, '//*[@id="appiMcResideSts"]')).select_by_value("3")
        time.sleep(1)
        #住宅性质
        self.find_and_send(By.XPATH, '//*[@id="appiMcContactName"]', appiMcContactName)
        #联系人姓名
        Select(self.find(By.XPATH, '//*[@name="appiMcContactRelship"]')).select_by_value("12")
        time.sleep(1)
        #与联系人关系
        self.find_and_send(By.XPATH, '//*[@id="appiMcContactPhone"]', appiMcContactPhone)
        # 联系人手机号
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplIndustryType"]')).select_by_value("03")
        time.sleep(1)
        #行业性质
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplMessage"]')).select_by_value("03")
        time.sleep(1)
        #职业信息
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplJobrole"]')).select_by_value("803")
        time.sleep(1)
        #职位或职级appiMcEmplJobrole
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplBizType"]')).select_by_value("13")
        time.sleep(1)
        #经济类型appiMcEmplBizType
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmployerName"]', appiMcEmployerName)
        #单位名称
        self.find_and_click(By.XPATH, '//*[@id="appiMcEmplAddrShow"]')
        self.find_and_click(By.XPATH, '//*[@id="_citys0"]/a[2]')
        self.find_and_click(By.XPATH, '//*[@id="_citys1"]/a[1]')
        self.find_and_click(By.XPATH, '//*[@id="_citys2"]/a[1]')
        #单位地址省市区
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplAddr1"]', appiMcEmplAddr1)
        #单位详细地址
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPhoneState"]', appiMcEmplPhoneState)
        #单位电话区号
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPhoneNo"]', appiMcEmplPhoneNo)
        #单位电话号码
        # self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPosiYear"]', "3")
        self.find_and_click(By.XPATH, '//*[@id="appiMcEmplPosiYear"]')
        self.find_and_click(By.XPATH, '//*[@class="sure"]')
        #现职已工作时间年
        self.find_and_click(By.XPATH, '//*[@id="appiMcEmplYearEarn"]')
        self.find_and_click(By.XPATH, '//*[@class="sure"]')
        #个人年收入万元
        time.sleep(2)
        # target = self._driver.find_element_by_xpath('//*[@class="button_group"]/input[2]')
        # self._driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_and_click(By.XPATH, '//*[@id="nextStep"]')
        #点击下一步
        return MobilePersonEquity(self._driver)