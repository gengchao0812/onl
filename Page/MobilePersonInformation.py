from Page.BasePage import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Page.MobilePersonEquity import MobilePersonEquity
import random
class MobilePersonInformation(BasePage):
    """
    手机个人信息页
    """

    def goto_equity_mobile(self, appiMcAddr1, appiMcContactName, appiMcEmployerName, appiMcEmplAddr1):
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

        #教育程度
        appiMcEducation = random.randint(1, 3)
        Select(self.find(By.XPATH, '//*[@id="appiMcEducation"]')).select_by_value("%s"%appiMcEducation)
        #婚姻状况
        appiMcMaritalSts = random.randint(1, 3)
        Select(self.find(By.XPATH, '//*[@id="appiMcMaritalSts"]')).select_by_value("%s" %appiMcMaritalSts)

        # 住宅详细地址
        self.find_and_send(By.XPATH, '//*[@id="appiMcAddr1"]', appiMcAddr1)

        # 住宅性质
        appiMcResideSts = random.randint(1,5)
        Select(self.find(By.XPATH, '//*[@id="appiMcResideSts"]')).select_by_value("%s"%appiMcResideSts)
        time.sleep(1)
        # 联系人姓名
        self.find_and_send(By.XPATH, '//*[@id="appiMcContactName"]', appiMcContactName)
        # 与联系人关系
        appiMcContactRelship = random.randint(11,14)
        Select(self.find(By.XPATH, '//*[@name="appiMcContactRelship"]')).select_by_value("%s"%appiMcContactRelship)
        time.sleep(1)
        # 联系人手机号
        appiMcContactPhone = self.get_random_phone()
        self.find_and_send(By.XPATH, '//*[@id="appiMcContactPhone"]', appiMcContactPhone)

        # 行业性质 %2d 格式化补0
        a = random.randint(1,31)
        appiMcEmplIndustryType = "%2d"%a
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplIndustryType"]')).select_by_value("%s"%appiMcEmplIndustryType)
        time.sleep(1)

        #职业信息
        b = random.randint(1,5)
        appiMcEmplMessage = "%2d"%b
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplMessage"]')).select_by_value("%s"%appiMcEmplMessage)
        time.sleep(1)


        #职位或职级appiMcEmplJobrole
        appiMcEmplJobrole = random.randint(801,805)
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplJobrole"]')).select_by_value("%s"%appiMcEmplJobrole)
        time.sleep(1)
        #经济类型appiMcEmplBizType
        appiMcEmplBizType = random.randint(11,18)
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplBizType"]')).select_by_value("%s"%appiMcEmplBizType)
        time.sleep(1)
        # 单位名称
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmployerName"]', appiMcEmployerName)
        #单位地址省市区
        self.find_and_click(By.XPATH, '//*[@id="appiMcEmplAddrShow"]')
        self.find_and_click(By.XPATH, '//*[@id="_citys0"]/a[2]')
        self.find_and_click(By.XPATH, '//*[@id="_citys1"]/a[1]')
        self.find_and_click(By.XPATH, '//*[@id="_citys2"]/a[1]')
        # 单位详细地址
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplAddr1"]', appiMcEmplAddr1)
        # 单位电话区号
        appiMcEmplPhoneState = self.get_random_phone_state()
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPhoneState"]', appiMcEmplPhoneState)
        # 单位电话号码
        appiMcEmplPhoneNo = self.get_random_phone_no()
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPhoneNo"]', appiMcEmplPhoneNo)


        # 现职已工作时间年
        # self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPosiYear"]', "3")
        self.find_and_click(By.XPATH, '//*[@id="appiMcEmplPosiYear"]')
        self.find_and_click(By.XPATH, '//*[@class="sure"]')


        # 个人年收入万元
        appiMcEmplYearEarn = random.randint(1,200)
        self.find_and_send(By.XPATH,"//*[@id='appiMcEmplYearEarn']",appiMcEmplYearEarn)

        time.sleep(2)
        # target = self._driver.find_element_by_xpath('//*[@class="button_group"]/input[2]')
        # self._driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_and_click(By.XPATH, '//*[@id="nextStep"]')
        self.personalother.update(appiMcEducation = appiMcEducation, appiMcMaritalSts = appiMcMaritalSts,appiMcAddr1 = appiMcAddr1 , appiMcResideSts = appiMcResideSts , \
                                  appiMcContactName = appiMcContactName,appiMcContactRelship = appiMcContactRelship ,appiMcContactPhone = appiMcContactPhone ,  appiMcEmplIndustryType = appiMcEmplIndustryType , \
                                  appiMcEmplMessage = appiMcEmplMessage , appiMcEmplJobrole = appiMcEmplJobrole , appiMcEmplBizType = appiMcEmplBizType, appiMcEmployerName = appiMcEmployerName, \
                                  appiMcEmplAddr1 = appiMcEmplAddr1 , appiMcEmplPhoneState= appiMcEmplPhoneState , appiMcEmplPhoneNo = appiMcEmplPhoneNo, \
                                appiMcEmplYearEarn= appiMcEmplYearEarn
                                  )
        #点击下一步
        return MobilePersonEquity(self._driver)