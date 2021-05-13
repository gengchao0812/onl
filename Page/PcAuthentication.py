from Page.BasePage import BasePage
from Page.PcPersonInformation import PcPersonInformation
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from retrying import retry
# from Utils.tracks import GTrace
# from Utils.PicCodeResult import *
from selenium.webdriver.common.action_chains import ActionChains

class PcAuthentication(BasePage):
    """
    PC身份验证页
    """

    def goto_personal_information(self,firstname1,familyname1,idnumber):
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
        # # 滑块提示
        # SlideRemind = self.find(By.XPATH, '//*[text()="拖动下方的滑块"]')
        # # 滑块刷新按钮
        # Reload = self.find(By.ID, 'dx_captcha_basic_btn-refresh_1')
        # # 滑块
        # Slider = self.find(By.ID, "dx_captcha_basic_slider_1")
        # # 画布
        # Bg = self.find(By.TAG_NAME, 'canvas')
        # # 缺口图片
        # Top = self.find(By.ID, "dx_captcha_basic_sub-slider_1")
        # Cut = self.find(By.XPATH, "//div[@id = 'dx_captcha_basic_sub-slider_1']/img")

        self.find_and_click(By.XPATH, '//*[@class="btn btn-bank agree"]')
        #同意窗口点击确定
        self.find_and_click(By.XPATH, '//*[@id="postIndentifyCode"]')
        #获取手机验证码

        #显示等待输入手机号页面，有则流程继续
        WebDriverWait(self._driver,50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="getRandom"]')))
        phone = self.get_random_phone()
        print(phone)
        self.find_and_send(By.XPATH,'//*[@id="NewappiMcMPhone"]',phone)
        self.find_and_click(By.XPATH,'//*[@id="sure_commit"]')
        #取界面验证码
        WebDriverWait(self._driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="verifyCode"]')))
        yanzhengma = self.find(By.XPATH,'//*[@id="verifyCode"]').text
        yanzhengma1 = re.findall(r'验证码是：(.*)',yanzhengma)
        self.find_and_send(By.XPATH, '//*[@id="indentifyCode"]',yanzhengma1)
        # time.sleep(30)
        # self.find_and_click(By.XPATH, '//*[@class="color_red bankcopy"]')
        # self.find_and_send(By.XPATH, '//*[@id="managerPhone"]', managerphone)
        # #输入客户经理手机号
        self.find(By.XPATH, '//*[@id="verifitySubmit"]')
        self.find_and_click(By.XPATH, '//*[@id="verifitySubmit"]')
        #点击下一步
        self.personal.update(firstname1 = firstname1, familyname1 = familyname1,phone = phone,idnumber = idnumber)
        return PcPersonInformation(self._driver)

    """
    点击刷新
    获取背景图
    获取滑块图片
    移动滑块到缺口位置 -- 判断是否验证成功，验证不成功则重试
    """
    # @retry(stop_max_delay = 10000, wait_fixed = 1000)
    # def slide(self,offset):
    #     self.find_element(*self.Bg)  # 等待canvas画布可见
    #     self.find_element(*self.Reload).click()  # 点击刷新
    #     # 拖动提示语可见则刷新结束
    #     self.find_element(*self.SlideRemind)
    #     # 获取canvas画布图片 -- 背景图
    #     # from Utils import slider
    #     js = 'return document.getElementsByTagName("canvas")[0].toDataURL("image/png");'
    #     img_info = self.driver.execute_script(js)
    #     img_b64 = img_info.split(',')[1]
    #     slider.write_bg(img_b64, 'bg.png')
    #
    #     # 通过src获取滑块图片
    #     import requests
    #     Cut = self.find_element(*self.Cut)
    #     link = Cut.get_attribute('0')
    #     time.sleep(1)
    #     req = requests.get(link, verify=False)
    #     cut_img = req.content
    #     if cut_img == '':
    #         print('获取滑块图片失败')
    #         raise IOError
    #     else:
    #         pass
    #     with open('cut.png', 'wb') as f:
    #         f.write(cut_img)
    #
    #     slider_style = self.find_element(*self.Top).get_attribute('style')
    #     top = int(re.findall("margin-top: (.*?)px; display: block;",slider_style)[0])
    #     top = int(top/0.75)
    #     slider.img_cropped('bg.png','bg.png',0,top,400,top+67)
    #
    #     # 匹配滑块和背景图，得到缺口位置坐标
    #     res = slider.find_pic('bg.png', 'cut.png')
    #     # 计算缺口位置（图像识别结果+矫正偏移量）
    #     distance = res + offset
    #     # 极验轨迹方程
    #     tracks = GTrace().get_tracks(distance)
    #     # print(tracks)
    #     time.sleep(0.5)
    #     Slider = self.find_element(*self.Slider)
    #     ActionChains(self.driver).click_and_hold(Slider).perform()
    #     for track in tracks:
    #         x = track[0]
    #         y = track[1]
    #         t = track[2]
    #         ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=y).perform()
    #         if t>0:
    #             time.sleep(t)
    #         else:
    #             time.sleep(0.05)
    #
    #     # 释放滑块
    #     ActionChains(self.driver).release().perform()
    #     time.sleep(1)
    #     self.no_element(*self.SlideRemind)  # 判断是否验证成功，判断逻辑：画布消失则验证成功

