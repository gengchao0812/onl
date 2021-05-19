from Page.BasePage import BasePage
from Page.PcPersonEquity import PcPersonEquity
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
# from Page.PcPersonOther import PcPersonOther
class PcPersonInformation(BasePage):
    """
    PC个人信息页
    """

    def goto_equity(self, appiMcAddr1, appiMcContactName,  appiMcEmployerName, appiMcEmplAddr1 ):
        # 省市区
        self.find_and_click(By.XPATH, '//*[@id="appiBranchShow"]')
        self.find_and_click(By.XPATH, '//*[@id="_citys0"]/a[2]')
        self.find_and_click(By.XPATH, '//*[@id="_citys1"]/a[1]')
        self.find_and_click(By.XPATH, '//*[@id="_citys2"]/a[1]')
        #家庭地址省市区
        self.find_and_click(By.XPATH, '//*[@id="appiMcAddrShow"]')
        self.find_and_click(By.XPATH, '//*[@id="_citys0"]/a[2]')
        self.find_and_click(By.XPATH, '//*[@id="_citys1"]/a[1]')
        self.find_and_click(By.XPATH, '//*[@id="_citys2"]/a[1]')
        #证件是否长期有效
        Select(self.find(By.XPATH, '//*[@id="appiMcIdLongFlag"]')).select_by_value("1")
        #教育程度
        appiMcEducation = random.randint(1,3)
        Select(self.find(By.XPATH, '//*[@id="appiMcEducation"]')).select_by_value('%s'%appiMcEducation)
        #婚姻状况
        appiMcMaritalSts = random.randint(1, 3)
        Select(self.find(By.XPATH, '//*[@id="appiMcMaritalSts"]')).select_by_value('%s'%appiMcMaritalSts)
        #住宅详细地址
        self.find_and_send(By.XPATH, '//*[@id="appiMcAddr1"]', appiMcAddr1)
        #住宅性质
        appiMcResideSts = random.randint(1, 3)
        Select(self.find(By.XPATH, '//*[@id="appiMcResideSts"]')).select_by_value('%s'%appiMcResideSts)
        time.sleep(1)
        #行业性质之前先下拉到最底
        target = self._driver.find_element_by_xpath('//*[@class="button_group"]/input[2]')
        self._driver.execute_script("arguments[0].scrollIntoView();", target)
        #联系人姓名
        self.find_and_send(By.XPATH, '//*[@id="appiMcContactName"]', appiMcContactName)
        #与联系人关系
        appiMcContactRelship = random.randint(11, 14)
        Select(self.find(By.XPATH, '//*[@name="appiMcContactRelship"]')).select_by_value('%s'%appiMcContactRelship)
        time.sleep(1)
        # 联系人手机号
        appiMcContactPhone = self.get_random_phone()
        self.find_and_send(By.XPATH, '//*[@id="appiMcContactPhone"]', appiMcContactPhone)
        #行业性质 %2d 格式化补0
        a = random.randint(1, 3)
        appiMcEmplIndustryType = "%02d" % a
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplIndustryType"]')).select_by_value('%s'%appiMcEmplIndustryType)
        time.sleep(1)
        #职位或职级appiMcEmplJobrole
        b = random.randint(1, 3)
        appiMcEmplMessage = "%02d" % b
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplMessage"]')).select_by_value('%s'%appiMcEmplMessage)
        time.sleep(1)
        appiMcEmplJobrole = random.randint(801, 805)
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplJobrole"]')).select_by_value('%s'%appiMcEmplJobrole)
        #经济类型appiMcEmplBizType
        appiMcEmplBizType = random.randint(11, 18)
        Select(self.find(By.XPATH, '//*[@id="appiMcEmplBizType"]')).select_by_value('%s'%appiMcEmplBizType)
        #单位名称
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmployerName"]', appiMcEmployerName)
        #单位详细地址
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplAddr1"]', appiMcEmplAddr1)
        #单位电话区号
        appiMcEmplPhoneState = self.get_random_phone_state()
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPhoneState"]', appiMcEmplPhoneState)
        #单位电话号码
        appiMcEmplPhoneNo = self.get_random_phone_no()
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPhoneNo"]', appiMcEmplPhoneNo)
        #现职已工作时间年
        appiMcEmplPosiYear = random.randint(1, 100)
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplPosiYear"]', appiMcEmplPosiYear)
        #个人年收入万元
        appiMcEmplYearEarn = random.randint(1, 100)
        self.find_and_send(By.XPATH, '//*[@id="appiMcEmplYearEarn"]', appiMcEmplYearEarn)
        #单位地址省市区
        self.find_and_click(By.XPATH, '//*[@id="appiMcEmplAddrShow"]')
        self.find_and_click(By.XPATH, '//*[@id="_citys0"]/a[2]')
        self.find_and_click(By.XPATH, '//*[@id="_citys1"]/a[1]')
        self.find_and_click(By.XPATH, '//*[@id="_citys2"]/a[1]')
        time.sleep(1)
        # 点击下一步
        self.find_and_click(By.XPATH, '//*[@class="button_group"]/input[2]')
        #把界面值都存入字典
        self.personalother.update(appiMcEducation = appiMcEducation, appiMcMaritalSts = appiMcMaritalSts,appiMcAddr1 = appiMcAddr1 , appiMcResideSts = appiMcResideSts , \
                                  appiMcContactName = appiMcContactName,appiMcContactRelship = appiMcContactRelship ,appiMcContactPhone = appiMcContactPhone ,  appiMcEmplIndustryType = appiMcEmplIndustryType , \
                                  appiMcEmplMessage = appiMcEmplMessage , appiMcEmplJobrole = appiMcEmplJobrole , appiMcEmplBizType = appiMcEmplBizType, appiMcEmployerName = appiMcEmployerName, \
                                  appiMcEmplAddr1 = appiMcEmplAddr1 , appiMcEmplPhoneState= appiMcEmplPhoneState , appiMcEmplPhoneNo = appiMcEmplPhoneNo, \
                                  appiMcEmplPosiYear = appiMcEmplPosiYear, appiMcEmplYearEarn= appiMcEmplYearEarn
                                  )
        return PcPersonEquity(self._driver)