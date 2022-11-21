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
        TC001(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC006(self.driver, test_scenario)
        #TC011(self.driver, test_scenario) #SKIPPED
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS007")
    def test_ts007(self):
        test_scenario = "TS007"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC006(self.driver, test_scenario)
        # TC011(self.driver, test_scenario) #SKIPPED
        Functions().tag_status(self.module, test_scenario, "Passed")

