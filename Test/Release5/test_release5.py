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


    @pytest.mark.tags("TS055")
    def test_ts055(self):
        test_scenario = "TS055"
        Functions().create_document(self.driver, module, test_scenario)
        TC118(self.driver, test_scenario, SAMO['firstname'], SAMO['lastname'], SAMO['emailaddress'],
              SAMO['mobilenumber'], SAMO['CAN'], SAMO['SIN'])
        #TC014(self.driver, test_scenario, SAMO['emailaddress'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS060")
    def test_ts060(self):
        test_scenario = "TS060"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC088a(self.driver, test_scenario, Concern['sacxe_single_can'], Concern['sacxe_single_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS061")
    def test_ts061(self):
        test_scenario = "TS061"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC089a(self.driver, test_scenario, Concern['sacxe_multiple_can'], Concern['sacxe_multiple_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS062")
    def test_ts062(self):
        test_scenario = "TS062"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC088b(self.driver, test_scenario, Concern['sacxe_single_can'], Concern['sacxe_single_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS063")
    def test_ts063(self):
        test_scenario = "TS063"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC089b(self.driver, test_scenario, Concern['sacxe_multiple_can'], Concern['sacxe_multiple_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS064")
    def test_ts064(self):
        test_scenario = "TS064"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC088c(self.driver, test_scenario, Concern['sacxe_single_can'], Concern['sacxe_single_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS065")
    def test_ts065(self):
        test_scenario = "TS065"
        Functions().create_document(self.driver, module, test_scenario)
        Precondition_Login_CXE(self.driver, test_scenario, Concern['cxe_email'], Concern['cxe_password'])
        TC089c(self.driver, test_scenario, Concern['sacxe_multiple_can'], Concern['sacxe_multiple_sin'])
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

    @pytest.mark.tags("TS095")
    def test_ts095(self):
        test_scenario = "TS095"
        Functions().create_document(self.driver, module, test_scenario)
        TC079(self.driver, test_scenario, Concern['concern_email'], Concern['password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS096")
    def test_ts096(self):
        test_scenario = "TS096"
        Functions().create_document(self.driver, module, test_scenario)
        TC080(self.driver, test_scenario, Concern['concern_email'], Concern['password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS097")
    def test_ts097(self):
        test_scenario = "TS097"
        Functions().create_document(self.driver, module, test_scenario)
        TC080(self.driver, test_scenario, Concern['business_account_email'], Concern['business_account_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")


