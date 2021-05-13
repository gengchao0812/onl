import pytest
import yaml
# from Page.PcIndexPage import PcIndexPage
from Page.MobileIndexPage import MobileIndexPage


class TestAddMember():
    def setup(self):
        self.main = MobileIndexPage()


    @pytest.mark.skip
    # @pytest.mark.parametrize('firstname1,familyname1,appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn',yaml.safe_load(open("..//Data/PcNew.yaml",encoding="utf-8")).values())
    @pytest.mark.parametrize('firstname1,familyname1,idnumber,appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn',[('张', '三','110101196902130491', '这里是住宅地址某某大街四号院', '李菲菲', 13022233331, '天阳宏业科技发展有限公司', '这里是单位地址某某某大街八十三楼', '1234', '88885555', '15', '80')])
    # @pytest.mark.parametrize('firstname1,familyname1,appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn',a)
    def test_add_mobile_new_member(self, firstname1, familyname1, idnumber, appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo, appiMcEmplPosiYear, appiMcEmplYearEarn):
        appid = self.main.goto_family_mobile().goto_number_card_mobile().goto_authentication_mobile().goto_personal_information_mobile(firstname1,familyname1,idnumber).goto_equity_mobile(appiMcAddr1, appiMcContactName, appiMcContactPhone, appiMcEmployerName, appiMcEmplAddr1, appiMcEmplPhoneState, appiMcEmplPhoneNo).goto_persion_other_mobile().goto_preview_page_mobile().goto_end_page_mobile().goto_index_mobile()
        import cx_Oracle
        # db = cx_Oracle.connect('ops_uat/ops_uat')
        db = cx_Oracle.connect('ops_uat/ops_uat@22.188.46.141:1521/apsonl')
        cursor = db.cursor()
        tsql = "select appi_app_id from apply_main_appi where appi_mc_id_number='%s'" % idnumber
        cursor.execute(tsql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
        assert data == appid


    def teardown(self):
        self.main.close()