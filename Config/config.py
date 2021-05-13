import yaml
import os
import sys
import cx_Oracle

class Config_Db():
    def return_db(self,onl):
        a = sys.path[0]+'\Data\DB.yaml'
        f = open(r'%s'%a)
        bb = yaml.safe_load(f)
        if onl == 1:
            usr=(bb['onl1'][0])
            pw=(bb['onl1'][1])
            ip=(bb['onl1'][2])
            return self.DB(usr, pw,ip)
        elif onl == 2:
            usr=(bb['onl2'][0])
            pw=(bb['onl2'][1])
            ip=(bb['onl2'][2])
            return self.DB(usr, pw, ip)
        else:
            print("找不到数据库配置")

    def DB(self,usr, pw, ip):
        conn = cx_Oracle.connect(usr, pw, ip, encoding='UTF-8', nencoding='UTF-8')
        return conn

