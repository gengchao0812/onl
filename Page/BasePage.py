from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import random


class BasePage:

    _driver = None
    _base_url = ""
    personal = {}
    personalother = {}

    def __init__(self, deiver: WebDriver = None):
        if deiver is None:
            chrome_options = Options()
            # 和浏览器做复用调试
            # Chrome --remote-debugging-port=9222打开调试
            # chrome_options.debugger_address = "127.0.0.1:9222"
            chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
            # chrome_options.add_argument('disable-infobars')
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = deiver
        if self._base_url != "":
            time.sleep(3)
            #打开新标签获取session
            newwindow = 'window.open("https://22.188.180.205/udid/c1?")'
            # newwindow='window.open("http://22.188.46.140/apply/pc/index")'
            self._driver.execute_script(newwindow)
            self._driver.implicitly_wait(3)
            all_handles = self._driver.window_handles
            #切到第二个标签页
            self._driver.switch_to.window(all_handles[-1])
            self._driver.find_element_by_xpath('//*[@id="details-button"]').click()
            # _driver.find_element_by_xpath('//*[@class="nav-wrapper"]/button[3]').click()
            # _driver.find_element_by_xpath("//*[@class='top-up']/a[5]").click()
            self._driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
            time.sleep(1)
            # _driver.switch_to_window(_driver.window_handles[0])
            #切回第一个标签
            self._driver.switch_to.window(all_handles[0])
            time.sleep(1)
            self._driver.maximize_window()
            self._driver.get(self._base_url)
            self._driver.implicitly_wait(10)

    def find(self, by, locator):
        #每次查到都会界面滚动查找
        target = self._driver.find_element(by,locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", target)
        return self._driver.find_element(by, locator)


    def find_and_click(self, by, locator):
        return self._driver.find_element(by, locator).click()

    def find_and_send(self, by, locator, text):
        #先清除数据再送值
        self._driver.find_element(by, locator).clear()
        return self._driver.find_element(by, locator).send_keys(text)

    def finds(self, by, locator):
        target = self._driver.find_elements(by,locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", target)
        return self._driver.find_elements(by,locator)

    def close(self):
        time.sleep(2)
        #close 关闭单个  quit 关闭所有
        self._driver.quit()

    def get_random_phone(self):
        """
        随机通讯运营商正常手机号
        :return:
        """
        mobile = '130'
        i = 0
        while (i < 7):
            num = random.choice('0123456789')
            mobile += num
            i += 1
        mobile += random.choice('1234')
        return mobile

    def get_random_phone_no(self):
        """
        随机8位电话号码
        :return:
        """
        phone = '6'
        i = 0
        while (i<7):
            num = random.choice('123456789')
            phone += num
            i +=1
        return phone

    def get_random_phone_state(self):
        phone = '0'
        i = 0
        while (i < 3):
            num = random.choice('123456789')
            phone += num
            i += 1
        return phone


    def return_data_pc_new(self,appid):
        """
        手机新客户数据比对
        :param appid:
        :return:
        """
        from Config import config
        #链接数据库
        db = config.Config_Db().return_db(onl=1)
        # # db = cx_Oracle.connect('ops_uat/ops_uat')
        # db = cx_Oracle.connect('ops_uat/Bb_11111@22.188.44.190:1521/apsonl')
        #打开游标
        cursor = db.cursor()
        #sql
        tsql = "select appi_app_id,appi_mc_first_name,appi_mc_family_name,appi_mc_id_number, appi_mc_m_phone,appi_Mc_Education , appi_Mc_Marital_Sts ," \
               "appi_Mc_Addr_1 , appi_Mc_Reside_Sts , appi_Mc_Contact_Name,appi_Mc_Contact_Relship , appi_Mc_Contact_M_Phone , appi_Mc_Empl_Industry_Type ," \
               "appi_Mc_Empl_Message ,appi_Mc_Empl_Jobrole ,appi_Mc_Empl_Biz_Type,appi_Mc_Employer_Name,appi_Mc_Empl_Addr_1 , appi_Mc_Empl_Phone_State ," \
               "appi_Mc_Empl_Phone_No,appi_Mc_Empl_Posi_Year,appi_Mc_Empl_Year_Earn from apply_main_appi where appi_app_id='%s'" % appid
        cursor.execute(tsql)
        data = cursor.fetchone()
        #关闭游标
        cursor.close()
        #关闭数据库
        db.close()
        return data

    def return_data_mobile_new(self,appid):
        """
        手机新客户数据比对
        :param appid:
        :return:
        """
        from Config import config
        #链接数据库
        db = config.Config_Db().return_db(onl=1)
        # # db = cx_Oracle.connect('ops_uat/ops_uat')
        # db = cx_Oracle.connect('ops_uat/Bb_11111@22.188.44.190:1521/apsonl')
        #打开游标
        cursor = db.cursor()
        #sql
        tsql = "select appi_app_id,appi_mc_first_name,appi_mc_family_name,appi_mc_id_number, appi_mc_m_phone,appi_Mc_Education , appi_Mc_Marital_Sts ," \
               "appi_Mc_Addr_1 , appi_Mc_Reside_Sts , appi_Mc_Contact_Name,appi_Mc_Contact_Relship , appi_Mc_Contact_M_Phone , appi_Mc_Empl_Industry_Type ," \
               "appi_Mc_Empl_Message ,appi_Mc_Empl_Jobrole ,appi_Mc_Empl_Biz_Type,appi_Mc_Employer_Name,appi_Mc_Empl_Addr_1 , appi_Mc_Empl_Phone_State ," \
               "appi_Mc_Empl_Phone_No,appi_Mc_Empl_Year_Earn from apply_main_appi where appi_app_id='%s'" % appid
        cursor.execute(tsql)
        data = cursor.fetchone()
        #关闭游标
        cursor.close()
        #关闭数据库
        db.close()
        return data