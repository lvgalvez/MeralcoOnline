import pytest

from Test.Concern.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestConcern:
    module = "Concern"
    function = Functions()

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
        TC003(self.driver, test_scenario, 'Inquiry')
        TC005(self.driver, test_scenario, 'Inquiry')
        TC006(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS008")
    def test_ts008(self):
        test_scenario = "TS008"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario, 'Inquiry')
        TC005(self.driver, test_scenario, 'Inquiry')
        TC006(self.driver, test_scenario)
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

    @pytest.mark.tags("TS012")
    def test_ts012(self):
        test_scenario = "TS012"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario, 'Feedback')
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
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS016")
    def test_ts016(self):
        test_scenario = "TS016"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario, 'Request')
        TC005(self.driver, test_scenario, 'Request')
        TC006(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")