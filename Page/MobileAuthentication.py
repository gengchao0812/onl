from Page.BasePage import BasePage
from Page.MobilePersonInformation import MobilePersonInformation
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class MobileAuthentication(BasePage):
    """
    手机身份验证页
    """

    def goto_personal_information_mobile(self,firstname1,familyname1,idnumber):
        time.sleep(2)
        self.find_and_send(By.NAME, 'appiFirstName1', firstname1)
        #姓
        self.find_and_send(By.XPATH, '//*[@id="appiFamilyName1"]', familyname1)
        #名
        self._driver.find_element_by_xpath('//*[@id="appiFamilyName1"]').send_keys(Keys.TAB)
        time.sleep(1)
        #拼音--tab键利用前端事件自动填入拼音
        self.find_and_send(By.XPATH, '//*[@id="appiMcIdNumber"]', idnumber)
        #证件号
        self.find_and_click(By.XPATH, '//*[@id="agreement"]')
        #点击同意
        time.sleep(9)
        self.find_and_click(By.XPATH, '//*[@id="agree"]')
        #同意窗口点击确定
        self.find_and_click(By.XPATH, '//*[@id="postIndentifyCode"]')
        #获取手机验证码

        time.sleep(30)
        # self.find_and_click(By.XPATH, '//*[@class="color_red bankcopy"]')
        # self.find_and_send(By.XPATH, '//*[@id="managerPhone"]', managerphone)
        # #输入客户经理手机号
        self.find(By.XPATH, '//*[@id="nextStep"]')
        self.find_and_click(By.XPATH, '//*[@id="nextStep"]')
        #点击下一步
        self.personal.update(firstname1 = firstname1, familyname1 = familyname1)
        print(self.personal)
        return MobilePersonInformation(self._driver)

