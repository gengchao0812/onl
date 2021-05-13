import pytest
import yaml
from Page.PcIndexPage import PcIndexPage
from Page.MobileIndexPage import MobileIndexPage
import py
import sys

class TestAddMember():
    def setup(self):
        self.main = PcIndexPage()


    # @pytest.mark.parametrize('firstname1,familyname1,appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn',yaml.safe_load(open("..//Data/PcNew.yaml",encoding="utf-8")).values())
    @pytest.mark.parametrize('firstname1,familyname1,idnumber,appiMcAddr1, appiMcContactName, appiMcEmployerName, appiMcEmplAddr1',yaml.safe_load(open(sys.path[0]+'\Data\PcNew.yaml',encoding='utf-8')))
    # @pytest.mark.parametrize('firstname1,familyname1,appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn',a)
    # @pytest.mark.skipg
    def test_add_pc_new_member(self, firstname1, familyname1,idnumber, appiMcAddr1, appiMcContactName, appiMcEmployerName, appiMcEmplAddr1):
        appid = self.main.goto_family().goto_number_card().goto_authentication().goto_personal_information(firstname1,familyname1,idnumber).goto_equity(appiMcAddr1, appiMcContactName, appiMcEmployerName, appiMcEmplAddr1).goto_persion_other().goto_preview_page().goto_end_page().goto_index()
        data = self.main.return_data_pc_new(appid[0])
        try:
            assert data[0] == appid[0]
        except AssertionError:
            print('申请件编号不一致')
        try:
            assert data[1] == self.main.personal['firstname1']
        except AssertionError:
            print('姓入库不一致，输入值为%s,入库值为%s'%(data[1],self.main.personal['firstname1']))
        try:
            assert data[2] == self.main.personal['familyname1']
        except AssertionError:
            print('名入库不一致，输入值为%s,入库值为%s'%(data[2],self.main.personal['familyname1']))
        assert data[3] == self.main.personal['idnumber']
        assert data[4] == self.main.personal['phone']
        assert data[5] == str(self.main.personalother['appiMcEducation'])
        assert data[6] == str(self.main.personalother['appiMcMaritalSts'])
        assert data[7] == self.main.personalother['appiMcAddr1']
        assert data[8] == str(self.main.personalother['appiMcResideSts'])
        assert data[9] == self.main.personalother['appiMcContactName']
        assert data[10] == str(self.main.personalother['appiMcContactRelship'])
        assert data[11] == self.main.personalother['appiMcContactPhone']
        assert data[12] == self.main.personalother['appiMcEmplIndustryType']
        assert data[13] == self.main.personalother['appiMcEmplMessage']
        assert data[14] == str(self.main.personalother['appiMcEmplJobrole'])
        assert data[15] == str(self.main.personalother['appiMcEmplBizType'])
        assert data[16] == self.main.personalother['appiMcEmployerName']
        assert data[17] == self.main.personalother['appiMcEmplAddr1']
        assert data[18] == self.main.personalother['appiMcEmplPhoneState']
        assert data[19] == self.main.personalother['appiMcEmplPhoneNo']
        assert data[20] == str(self.main.personalother['appiMcEmplPosiYear'])
        assert data[21] == str(self.main.personalother['appiMcEmplYearEarn'])

    def teardown(self):
        self.main.close()