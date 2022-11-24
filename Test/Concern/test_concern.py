import pytest

from Test.Concern.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestConcern:
    module = "Concern"
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
    def test_ts002(self):
        test_scenario = "TS003"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC038(self.driver, test_scenario)

        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS006")
    def test_ts006(self):
        test_scenario = "TS006"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario, 'Inquiry')
        TC005(self.driver, test_scenario, 'Inquiry')
        TC006(self.driver, test_scenario)
        #TC111(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS007")
    def test_ts007(self):
        test_scenario = "TS007"
        Functions().create_document(self.driver, self.module, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS010")
    def test_ts010(self):
        test_scenario = "TS010"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario, 'Feedback')
        TC005(self.driver, test_scenario, 'Feedback')
        TC006(self.driver, test_scenario)
        # TC011(self.driver, test_scenario) #SKIPPED
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS011")
    def test_ts011(self):
        test_scenario = "TS011"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC003(self.driver, test_scenario, 'Feedback')
        TC005(self.driver, test_scenario, 'Feedback')
        TC006(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")


    @pytest.mark.tags("TS014")
    def test_ts014(self):
        test_scenario = "TS010"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario, 'Request')
        TC005(self.driver, test_scenario, 'Request')
        TC006(self.driver, test_scenario)
        # TC011(self.driver, test_scenario) #SKIPPED
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS015")
    def test_ts015(self):
        test_scenario = "TS015"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC003(self.driver, test_scenario, 'Request')
        TC005(self.driver, test_scenario, 'Request')
        TC006(self.driver, test_scenario)

    @pytest.mark.tags("TS016")
    def test_ts016(self):
        test_scenario = "TS016"

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