import pytest

from Test.Release5.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestConcern:
    module = "Release5"
    function = Functions()

    @pytest.mark.tags("TS001")
    def test_ts001(self):
        test_scenario = "TS001"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC036(self.driver, test_scenario)

        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS002")
    def test_ts002(self):
        test_scenario = "TS002"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC037(self.driver, test_scenario)

        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS003")
    def test_ts003(self):
        test_scenario = "TS003"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC038(self.driver, test_scenario)

        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS006", "User_Concern")
    def test_ts006(self):
        test_scenario = "TS006"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario, 'Inquiry')
        TC005(self.driver, test_scenario, 'Inquiry')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_single_service'])
        #TC111(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS007", "User_Concern")
    def test_ts007(self):
        test_scenario = "TS007"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC003(self.driver, test_scenario, 'Inquiry')
        TC005(self.driver, test_scenario, 'Inquiry')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS008", "User_Concern")
    def test_ts008(self):
        test_scenario = "TS008"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario, 'Inquiry')
        TC005(self.driver, test_scenario, 'Inquiry')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_can'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS009", "User_Concern")
    def test_ts009(self):
        test_scenario = "TS009"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC004(self.driver, test_scenario, 'Inquiry')
        TC005(self.driver, test_scenario, 'Inquiry')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_can_multiple_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS010", "User_Concern")
    def test_ts010(self):
        test_scenario = "TS010"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario, 'Feedback')
        TC005(self.driver, test_scenario, 'Feedback')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_single_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS011", "User_Concern")
    def test_ts011(self):
        test_scenario = "TS011"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC003(self.driver, test_scenario, 'Feedback')
        TC005(self.driver, test_scenario, 'Feedback')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS012", "User_Concern")
    def test_ts012(self):
        test_scenario = "TS012"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario, 'Feedback')
        TC005(self.driver, test_scenario, 'Feedback')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_can'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS013", "User_Concern")
    def test_ts013(self):
        test_scenario = "TS013"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC004(self.driver, test_scenario, 'Feedback')
        TC005(self.driver, test_scenario, 'Feedback')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_can_multiple_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS014", "User_Concern")
    def test_ts014(self):
        test_scenario = "TS014"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario, 'Request')
        TC005(self.driver, test_scenario, 'Request')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_single_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS015", "User_Concern")
    def test_ts015(self):
        test_scenario = "TS015"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC003(self.driver, test_scenario, 'Request')
        TC005(self.driver, test_scenario, 'Request')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS016", "User_Concern")
    def test_ts016(self):
        test_scenario = "TS016"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario, 'Request')
        TC005(self.driver, test_scenario, 'Request')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_can'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS017", "User_Concern")
    def test_ts017(self):
        test_scenario = "TS017"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC004(self.driver, test_scenario, 'Request')
        TC005(self.driver, test_scenario, 'Request')
        TC006(self.driver, test_scenario)
        TC111a(self.driver, test_scenario, Concern['username_multiple_can_multiple_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS018")
    def test_ts018(self):
        test_scenario = "TS018"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, 'Inquiry')
        TC001a(self.driver, test_scenario)
        TC005a(self.driver, test_scenario, Concern['can_single_sin'], Concern['first_name'], Concern['last_name'], Concern['username_single_service'], Concern['mobile'], Concern['remarks'])
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111a(self.driver, test_scenario, Concern['username_single_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS019")
    def test_ts019(self):
        test_scenario = "TS019"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, 'Inquiry')
        TC003a(self.driver, test_scenario, Concern['can_single_sin'])
        TC005b(self.driver, test_scenario, Concern['can_single_sin'], Concern['sin_multiple'] , Concern['first_name'], Concern['last_name'], Concern['username_single_service'], Concern['mobile'], Concern['remarks'])
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111a(self.driver, test_scenario, Concern['username_single_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS020")
    def test_ts020(self):
        test_scenario = "TS020"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, 'Feedback')
        TC001a(self.driver, test_scenario)
        TC005b(self.driver, test_scenario, Concern['can_single_sin'], Concern['sin_multiple'] , Concern['first_name'], Concern['last_name'], Concern['username_single_service'], Concern['mobile'], Concern['remarks'])
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111a(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS021")
    def test_ts021(self):
        test_scenario = "TS021"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, 'Feedback')
        TC003a(self.driver, test_scenario, Concern['can_single_sin'])
        TC005b(self.driver, test_scenario, Concern['can_single_sin'], Concern['sin_multiple'] , Concern['first_name'], Concern['last_name'], Concern['username_single_service'], Concern['mobile'], Concern['remarks'])
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111a(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")
    @pytest.mark.tags("TS022")
    def test_ts022(self):
        test_scenario = "TS022"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, 'Request')
        TC001a(self.driver, test_scenario)
        TC005b(self.driver, test_scenario, Concern['can_single_sin'], Concern['sin_multiple'] , Concern['first_name'], Concern['last_name'], Concern['username_single_service'], Concern['mobile'], Concern['remarks'])
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111a(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS023")
    def test_ts023(self):
        test_scenario = "TS023"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, 'Request')
        TC003a(self.driver, test_scenario, Concern['can_single_sin'])
        TC005b(self.driver, test_scenario, Concern['can_single_sin'], Concern['sin_multiple'] , Concern['first_name'], Concern['last_name'], Concern['username_single_service'], Concern['mobile'], Concern['remarks'])
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111a(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS032")
    def test_ts032(self):
        test_scenario = "TS032"
        Functions().create_document(self.driver, module, test_scenario)
        TC012(self.driver, test_scenario)
        TC087(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS033")
    def test_ts033(self):
        test_scenario = "TS033"
        Functions().create_document(self.driver, module, test_scenario)
        TC012(self.driver, test_scenario)
        TC087(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS034")
    def test_ts034(self):
        test_scenario = "TS034"
        Functions().create_document(self.driver, module, test_scenario)
        TC020(self.driver, test_scenario)
        TC013(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS035")
    def test_ts035(self):
        test_scenario = "TS035"
        Functions().create_document(self.driver, module, test_scenario)
        TC021(self.driver, test_scenario)
        TC013(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS036")
    def test_ts036(self):
        test_scenario = "TS036"
        Functions().create_document(self.driver, module, test_scenario)
        TC022(self.driver, test_scenario)
        TC013(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS037")
    def test_ts037(self):
        test_scenario = "TS037"
        Functions().create_document(self.driver, module, test_scenario)
        TC023(self.driver, test_scenario)
        TC013(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS038")
    def test_ts038(self):
        test_scenario = "TS038"
        Functions().create_document(self.driver, module, test_scenario)
        TC023(self.driver, test_scenario)
        TC013(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS039")
    def test_ts039(self):
        test_scenario = "TS039"
        Functions().create_document(self.driver, module, test_scenario)
        TC024(self.driver, test_scenario)
        TC013(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS040")
    def test_ts040(self):
        test_scenario = "TS040"
        Functions().create_document(self.driver, module, test_scenario)
        TC024(self.driver, test_scenario)
        TC013(self.driver, test_scenario)
        TC014(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")


    @pytest.mark.tags("TS055")
    def test_ts055(self):
        test_scenario = "TS055"
        Functions().create_document(self.driver, module, test_scenario)
        TC118(self.driver, test_scenario, SAMO['firstname'], SAMO['lastname'], SAMO['emailaddress'],
              SAMO['mobilenumber'], SAMO['CAN'], SAMO['SIN'])
        #TC014(self.driver, test_scenario, SAMO['emailaddress'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS066")
    def test_ts066(self):
        test_scenario = "TS066"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC090(self.driver, test_scenario)
        TC091(self.driver, test_scenario, Concern['alphanumeric_can'])
        TC092(self.driver, test_scenario, Concern['nonexisting_can'])
        TC093(self.driver, test_scenario, Concern['less_character_can'])
        TC094(self.driver, test_scenario, Concern['multiple_service_can'])
        TC095(self.driver, test_scenario, Concern['multiple_service_can'], Concern['incorrect_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS067")
    def test_ts067(self):
        test_scenario = "TS067"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC090b(self.driver, test_scenario)
        TC091b(self.driver, test_scenario, Concern['alphanumeric_can'])
        TC092b(self.driver, test_scenario, Concern['nonexisting_can'])
        TC093b(self.driver, test_scenario, Concern['less_character_can'])
        TC094b(self.driver, test_scenario, Concern['multiple_service_can'])
        TC095b(self.driver, test_scenario, Concern['multiple_service_can'], Concern['incorrect_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS068")
    def test_ts068(self):
        test_scenario = "TS068"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC090c(self.driver, test_scenario)
        TC091c(self.driver, test_scenario, Concern['alphanumeric_can'])
        TC092c(self.driver, test_scenario, Concern['nonexisting_can'])
        TC093c(self.driver, test_scenario, Concern['less_character_can'])
        TC094c(self.driver, test_scenario, Concern['multiple_service_can'])
        TC095c(self.driver, test_scenario, Concern['multiple_service_can'], Concern['incorrect_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

