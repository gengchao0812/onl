from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
import re
import time
import os

class PcPersonEnd(BasePage):
    """
    PC结束页面
    """
    def goto_index(self):
        time.sleep(3)
        message = self.find(By.XPATH,'//*[@class="col-md-12 col-sm-12"]/p').text
        appid = re.findall(r'您的申请件编号是(.*)，该编号', message)
        #完成页截图
        #年月日时分秒
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        directory_time = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        #获取到当前文件的目录，并检查是否有directory_time文件夹，如果不存在则自动新建directory_time文件
        try:
            File_Path = os.getcwd() + '\\' + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
                print("目录新建成功:%s" %File_Path)
            else:
                print("目录已存在")
        except BaseException as e:
            print("目录创建失败%s"%e)

        try:
            url = self._driver.save_screenshot('.\\'+ directory_time+'\\'+picture_time+'.png')
            print("%s:截图成功！！！"%url)
        except BaseException as pic_msg:
            print("截图失败:%s"%pic_msg)
        return appid
