import pytest
import yaml
# from Page.PcIndexPage import PcIndexPage
from Page.MobileIndexPage import MobileIndexPage
import allure
import sys

@allure.feature('pc新客户')
class TestAddMember():
    def setup(self):
        self.main = MobileIndexPage()


    @pytest.mark.skip
    # @pytest.mark.parametrize('firstname1,familyname1,appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn',yaml.safe_load(open("..//Data/PcNew.yaml",encoding="utf-8")).values())
    @pytest.mark.parametrize('firstname1,familyname1,idnumber,appiMcAddr1, appiMcContactName, appiMcEmployerName, appiMcEmplAddr1',yaml.safe_load(open(sys.path[0]+'\Data\PcNew.yaml',encoding='utf-8')))
    @allure.story('测试手机新客户流程正确')
    # @pytest.mark.parametrize('firstname1,familyname1,appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn',a)
    def test_add_mobile_new_member(self, firstname1, familyname1, idnumber, appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn):
        appid = self.main.goto_family_mobile().goto_number_card_mobile().goto_authentication_mobile().goto_personal_information_mobile(firstname1,familyname1,idnumber).goto_equity_mobile(appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo).goto_persion_other_mobile().goto_preview_page_mobile().goto_end_page_mobile().goto_index_mobile()
        data = self.main.return_data_mobile_new(appid[0])
        try:
            assert data[0] == appid[0]
        except AssertionError:
            print('申请件编号不一致')
        try:
            assert data[1] == self.main.personal['firstname1']
        except AssertionError:
            print('姓入库不一致，输入值为%s,入库值为%s'%(self.main.personal['firstname1'],data[1]))
        try:
            assert data[2] == self.main.personal['familyname1']
        except AssertionError:
            print('名入库不一致，输入值为%s,入库值为%s'%(self.main.personal['familyname1'],data[2]))
        try:
            assert data[3] == self.main.personal['idnumber']
        except AssertionError:
            print ('身份征号入库不一致，输入值为%s,入库值为%s'%(self.main.personal['idnumber'],data[3]))
        try:
            assert data[4] == self.main.personal['phone']
        except AssertionError:
            print ('手机号入库不一致，输入值为%s，入库值为%s'%(self.main.personal['iphone'],data[4]))
        try:
            assert data[5] == str(self.main.personalother['appiMcEducation'])
        except AssertionError:
            print ('教育程度入库不一致，输入值为%s,入库值为%s'%(self.main.personalother['appiMcEducation'],data[5]))
        try:
            assert data[6] == str(self.main.personalother['appiMcMaritalSts'])
        except AssertionError:
            print ('婚姻情况入库不一致，输入值为%s，入库值为%s'%(self.main.personalother['appiMcMaritalSts'],data[6]))
        try:
            assert data[7] == self.main.personalother['appiMcAddr1']
        except AssertionError:
            print ('住宅详细地址入库不一致,输入值为%s'%(self.main.personalother['appiMcAddr1'],data[7]))
        try:
            assert data[8] == str(self.main.personalother['appiMcResideSts'])
        except AssertionError:
            print ('住宅性质入库不一致,输入值为%s'%(self.main.personalother['appiMcResideSts'],data[8]))
        try:
            assert data[9] == self.main.personalother['appiMcContactName']
        except AssertionError:
            print ('住宅性质入库不一致,输入值为%s' % (self.main.personalother['appiMcContactName'],data[9]))
        try:
            assert data[10] == str(self.main.personalother['appiMcContactRelship'])
        except AssertionError:
            print ('与联系人关系入库不一致,输入值为%s' % (self.main.personalother['appiMcContactRelship'], data[10]))
        try:
            assert data[11] == self.main.personalother['appiMcContactPhone']
        except AssertionError:
            print ('联系人手机号入库不一致,输入值为%s' % (self.main.personalother['appiMcContactPhone'], data[11]))
        try:
            assert data[12] == self.main.personalother['appiMcEmplIndustryType']
        except AssertionError:
            print ('行业性质入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplIndustryType'], data[12]))
        try:
            assert data[13] == self.main.personalother['appiMcEmplMessage']
        except AssertionError:
            print ('职业信息入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplMessage'], data[13]))
        try:
            assert data[14] == str(self.main.personalother['appiMcEmplJobrole'])
        except AssertionError:
            print ('职位或职级入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplJobrole'], data[14]))
        try:
            assert data[15] == str(self.main.personalother['appiMcEmplBizType'])
        except AssertionError:
            print ('经济类型入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplBizType'], data[15]))
        try:
            assert data[16] == self.main.personalother['appiMcEmployerName']
        except AssertionError:
            print ('单位名称入库不一致,输入值为%s' % (self.main.personalother['appiMcEmployerName'], data[16]))
        try:
            assert data[17] == self.main.personalother['appiMcEmplAddr1']
        except AssertionError:
            print ('单位地址入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplAddr1'], data[17]))
        try:
            assert data[18] == self.main.personalother['appiMcEmplPhoneState']
        except AssertionError:
            print ('单位电话区号入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplPhoneState'], data[18]))
        try:
            assert data[19] == self.main.personalother['appiMcEmplPhoneNo']
        except AssertionError:
            print ('单位电话入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplPhoneNo'], data[19]))
        try:
            assert data[20] == str(self.main.personalother['appiMcEmplYearEarn'])
        except AssertionError:
            print ('个人年收入入库不一致,输入值为%s' % (self.main.personalother['appiMcEmplYearEarn'], data[20]))

    def teardown(self):
        self.main.close()