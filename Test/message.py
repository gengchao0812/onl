# import re
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# import time
# import random
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import cx_Oracle
# # personal={}

from Config import config
import os
print(os.path)
print('*************')
print(os.listdir())
print('*************')
db = config.Config_Db().return_db(onl=1)
cursor = db.cursor()
tsql = "select appi_app_id from apply_main_appi where appi_mc_id_number='110107195612205380'"
cursor.execute(tsql)
data = cursor.fetchone()
cursor.close()
db.close()
print(data)
# # firstname1 = '张'
# # familyname1 = '三'
# # phone = 13011111111
# # idnumber = 110101197203180494
# # personal.update(firstname1 = firstname1, familyname1 = familyname1,phone = phone,idnumber = idnumber,a = '03' , b = 3)
# # print(personal)
# # print(personal['firstname1'])
# # print(type(personal['a']))
# # print(type(personal['b']))
# #
# # appiMcEducation = random.randint(1,3)
# # a = "%02d"%appiMcEducation
# # print(a)
# # c = random.randint(801,805)
# # print(c)
#
# # db = cx_Oracle.connect('ops_uat/ops_uat')
# def get_random_phone_state():
#     phone = '0'
#     i = 0
#     while (i < 3):
#         num = random.choice('123456789')
#         phone += num
#         i += 1
#     return phone
#
#
#
# def get_random_phone_no():
#     phone = '6'
#     i = 0
#     while (i < 7):
#         num = random.choice('123456789')
#         phone += num
#         i += 1
#     return phone
#
# def return_data_pc_new(appid):
#     import cx_Oracle
#     a='ops_uat'
#     b='Bb_11111'
#     c='22.188.44.190:1521/apsonl'
#     # db = cx_Oracle.connect('ops_uat/Bb_11111@22.188.44.190:1521/apsonl')
#     db = cx_Oracle.connect(a,b,c)
#     cursor = db.cursor()
#     tsql = "select pi.appi_app_id,pi.appi_mc_first_name,pi.appi_mc_family_name,pi.appi_mc_id_number,pi.appi_mc_addr_1,pi.appi_mc_contact_name,pi.appi_mc_contact_m_phone,pi.appi_mc_employer_name,pi.appi_mc_empl_addr_1,pi.appi_mc_empl_phone_state, pi.appi_mc_empl_phone_no,pi.appi_mc_empl_posi_year,pi.appi_mc_empl_year_earn from apply_main_appi pi where pi.appi_app_id='%s'  order by pi.update_date desc" % appid
#     cursor.execute(tsql)
#     data = cursor.fetchone()
#     cursor.close()
#     db.close()
#     return data
#
# def func(x):
#     assert 1==x,'这里断言不过'
#     print('没问题')
# #
# # if __name__ == '__main__':
# #     appid='0220210002502779'
# #     c = return_data_pc_new(appid)
# #     print(c)
# #
#
#
#
#     # assert c[0] == str(dia['id'])
# #
# # # _base_url = "https://22.188.180.205/udid/c1?"
# # _driver = webdriver.Chrome()
# # _driver.maximize_window()
# # newwindow='window.open("https://22.188.180.205/udid/c1?")'
# # # newwindow='window.open("http://22.188.46.140/apply/pc/index")'
# # _driver.execute_script(newwindow)
# # time.sleep(2)
# # all_handles = _driver.window_handles
# # _driver.switch_to.window(all_handles[-1])
# # _driver.find_element_by_xpath('//*[@id="details-button"]').click()
# # # _driver.find_element_by_xpath('//*[@class="nav-wrapper"]/button[3]').click()
# # # _driver.find_element_by_xpath("//*[@class='top-up']/a[5]").click()
# # _driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
# # time.sleep(1)
# # # _driver.switch_to_window(_driver.window_handles[0])
# # _driver.switch_to.window(all_handles[0])
# # time.sleep(10)
# #
# # def func(idnumber):
# #     import cx_Oracle
# #
# # # db = cx_Oracle.connect('ops_uat/ops_uat')
# # # appid = '0120210001059881'
# #     db = cx_Oracle.connect('ops_uat/ops_uat@22.188.46.141:1521/apsonl')
# #     cursor = db.cursor()
# #     tsql = "select pi.appi_app_id,pi.appi_mc_first_name,pi.appi_mc_family_name,pi.appi_mc_id_number,pi.appi_mc_addr_1,pi.appi_mc_contact_name,pi.appi_mc_contact_m_phone,pi.appi_mc_employer_name,pi.appi_mc_empl_addr_1,pi.appi_mc_empl_phone_state, pi.appi_mc_empl_phone_no,pi.appi_mc_empl_posi_year,pi.appi_mc_empl_year_earn from apply_main_appi pi where pi.appi_mc_id_number='%s'" % idnumber
# #     print(tsql)
# #     cursor.execute(tsql)
# #     data = cursor.fetchone()
# #     cursor.close()
# #     db.close()
# #     return data
# # if __name__ == '__main__':
# #     idnumber = '110101197002131098'
# #     data = func(idnumber)
# #     print(data[0])
# #     print(data[1])
# #     print(data[2])
# #     print(data[3])
# #     print(data[4])
# #     print(data[5])
# #     print(data[6])
# #     print(data[7])
# #     print(data[8])
# #     print(data[9])
# #     print(data[10])
# #     print(data[11])
# #     print(data[12])
# # # mobile = '130'
# # i = 0
# # while (i < 7):
# #     num = random.choice('0123456789')
# #     mobile += num
# #     i += 1
# # mobile += random.choice('1234')
# # print(mobile)
#
#
