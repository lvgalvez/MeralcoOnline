import pytest

from Test.SAMO.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestServiceApplicationMeralcoOnline:
    module = "SAMO"
    serviceApplicationModule = "Release5"

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

    @pytest.mark.tags("TS032")
    def test_ts032(self):
        test_scenario = "TS032"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC012a(self.driver, test_scenario, SAMO['emailAddNewService'])
        TC087(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, SAMO['emailAddNewService'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS033")
    def test_ts033(self):
        test_scenario = "TS033"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC012a(self.driver, test_scenario, SAMO['business_account_email'])
        TC087(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, SAMO['business_account_email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS034")
    def test_ts034(self):
        test_scenario = "TS034"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC020(self.driver, test_scenario)
        TC013a(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, Concern['username_multiple_service'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS035")
    def test_ts035(self):
        test_scenario = "TS035"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC021(self.driver, test_scenario)
        TC013a(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, SAMO['business_account_email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS036")
    def test_ts036(self):
        test_scenario = "TS036"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC022(self.driver, test_scenario)
        TC013a(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, Concern['username_single_service'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS037")
    def test_ts037(self):
        test_scenario = "TS037"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC023(self.driver, test_scenario, Concern['username_single_service'])
        TC013a(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, Concern['username_single_service'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS038")
    def test_ts038(self):
        test_scenario = "TS038"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC023(self.driver, test_scenario, SAMO['business_account_email'])
        TC013a(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, SAMO['business_account_email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS039")
    def test_ts039(self):
        test_scenario = "TS039"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC024(self.driver, test_scenario, Concern['username_single_service'])
        TC013a(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, Concern['username_single_service'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS040")
    def test_ts040(self):
        test_scenario = "TS040"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC024(self.driver, test_scenario, SAMO['business_account_email'])
        TC013a(self.driver, test_scenario)
        TC014a(self.driver, test_scenario, SAMO['business_account_email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS045")
    def test_ts045(self):
        test_scenario = "TS045"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC028(self.driver, test_scenario, SAMO['CAN_singlesrvc'], SAMO['business_company_name'], SAMO['business_company_landline'],
              SAMO['business_first_name'], SAMO['business_last_name'], SAMO['business_emailaddress'],
              SAMO['business_designation'], SAMO['business_mobile_number'])
        TC014a(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS046")
    def test_ts046(self):
        test_scenario = "TS046"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC029(self.driver, test_scenario, SAMO['CAN_singlesrvc'], SAMO['contractor_companyName'],
              SAMO['contractor_firstName'], SAMO['contractor_lastName'], SAMO['contractor_emailAddress'], SAMO['contractor_mobileNumber'])
        TC014a(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")