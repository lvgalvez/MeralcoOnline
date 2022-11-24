import pytest

from Test.SAMO.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestServiceApplicationMeralcoOnline:
    module = "SAMO"

    @pytest.mark.tags("TS003")
    def test_ts003(self):
        test_scenario = "TS003"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario, SAMO['individual_account_email'], SAMO['individual_account_first'],
              SAMO['individual_account_middle'], SAMO['individual_account_last'], SAMO['individual_account_mobile'], SAMO['default_password'], SAMO['individual_account_birthday'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS001")
    def test_ts001(self):
        test_scenario = "TS001"
        Functions().create_document(self.driver, module, test_scenario)
        TC001(self.driver, test_scenario, SAMO['normal_account_email'], SAMO['normal_account_password'], SAMO['service_add'], SAMO['birthday'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS002")
    def test_ts002(self):
        test_scenario = "TS002"
        Functions().create_document(self.driver, module, test_scenario)
        TC001(self.driver, test_scenario, SAMO['business_account_email'], SAMO['business_account_password'],
              SAMO['service_add'], SAMO['birthday'])
        Functions().tag_status(self.module, test_scenario, "Passed")


    @pytest.mark.tags("TS004")
    def test_ts004(self):
        test_scenario = "TS004"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC003(self.driver, test_scenario, SAMO['business_company_name'], SAMO['business_trade_name'], SAMO['business_company_email'], SAMO['business_company_landline'],
              SAMO['business_first_name'], SAMO['business_last_name'], SAMO['business_emailaddress'], SAMO['business_mobile_number'], SAMO['business_designation'], SAMO['service_add'])
        Functions().tag_status(self.module, test_scenario, "Passed")



    @pytest.mark.tags("TS006")
    def test_ts006(self):
        test_scenario = "TS006"
        Functions().create_document(self.driver, module, test_scenario)
        TC006(self.driver, test_scenario, SAMO['normal_account_email'], SAMO['normal_account_password'],
              SAMO['service_add'])
        Functions().tag_status(self.module, test_scenario, "Passed")


    @pytest.mark.tags("TS007")
    def test_ts007(self):
        test_scenario = "TS007"
        Functions().create_document(self.driver, module, test_scenario)
        TC007(self.driver, test_scenario, SAMO['business_account_email'], SAMO['business_account_password'],
              SAMO['service_add'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS009")
    def test_ts009(self):
        test_scenario = "TS009"
        Functions().create_document(self.driver, module, test_scenario)
        TC011(self.driver, test_scenario, SAMO['CAN'], SAMO['business_company_name'], SAMO['business_company_landline'],SAMO['business_first_name'], SAMO['business_last_name'], SAMO['business_emailaddress'], SAMO['business_designation'], SAMO['business_mobile_number'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS005")
    def test_ts005(self):
        test_scenario = "TS005"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC004(self.driver, test_scenario, SAMO['contractor_firstName'], SAMO['contractor_lastName'],
              SAMO['contractor_middlename'],
              SAMO['contractor_businessName'], SAMO['contractor_emailAddress'], SAMO['contractor_mobileNumber'],
              SAMO['contractor_birthday'], SAMO['service_add'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS010")
    def test_ts010(self):
        test_scenario = "TS010"
        Functions().create_document(self.driver, module, test_scenario)
        TC012(self.driver, test_scenario, SAMO['CAN'], SAMO['contractor_companyName'], SAMO['contractor_landline'],
              SAMO['contractor_firstName'], SAMO['contractor_lastName'], SAMO['contractor_emailAddress'],
              SAMO['contractor_designation'], SAMO['contractor_mobileNumber'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS011")
    def test_ts010(self):
        test_scenario = "TS011"
        Functions().create_document(self.driver, module, test_scenario)
        TC013(self.driver, test_scenario, SAMO['CAN'], SAMO['contractor_companyName'], SAMO['contractor_landline'],
              SAMO['contractor_firstName'], SAMO['contractor_lastName'], SAMO['contractor_emailAddress'],
              SAMO['contractor_designation'], SAMO['contractor_mobileNumber'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS012")
    def test_ts012(self):
        test_scenario = "TS012"
        Functions().create_document(self.driver, module, test_scenario)
        TC009(self.driver, test_scenario, SAMO['normal_account_email'], SAMO['normal_account_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS013")
    def test_ts013(self):
        test_scenario = "TS013"
        Functions().create_document(self.driver, module, test_scenario)
        TC009(self.driver, test_scenario, SAMO['business_account_email'], SAMO['business_account_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS014")
    def test_ts014(self):
        test_scenario = "TS014"
        Functions().create_document(self.driver, module, test_scenario)
        TC014(self.driver, test_scenario, SAMO['firstname'], SAMO['lastname'], SAMO['emailaddress'], SAMO['mobilenumber'], SAMO['CAN'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS015")
    def test_ts015(self):
        test_scenario = "TS015"
        Functions().create_document(self.driver, module, test_scenario)
        TC015(self.driver, test_scenario, SAMO['firstname'], SAMO['lastname'], SAMO['emailaddress'],
              SAMO['mobilenumber'], SAMO['CAN'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS016")
    def test_ts016(self):
        test_scenario = "TS016"
        Functions().create_document(self.driver, module, test_scenario)
        TC016(self.driver, test_scenario, SAMO['firstname'], SAMO['lastname'], SAMO['emailaddress'],
              SAMO['mobilenumber'], SAMO['CAN'], SAMO['contractor_businessName'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS017")
    def test_ts017(self):
        test_scenario = "TS017"
        Functions().create_document(self.driver, module, test_scenario)
        TC010(self.driver, test_scenario, SAMO['normal_account_email'], SAMO['normal_account_password'], SAMO['birthday'])
        Functions().tag_status(self.module, test_scenario, "Passed")



