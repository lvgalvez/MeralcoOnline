import pytest

from Test.Concern.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestConcern:

    module = "Concern"
    function = Functions()



    @pytest.mark.tags("TS016")
    def test_ts016(self):
        test_scenario = "TS016"
        Functions().create_document(self.driver, self.module, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS018")
    def test_ts018(self):
        test_scenario = "TS018"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario)
        TC001(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS019")
    def test_ts019(self):
        test_scenario = "TS019"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario)
        TC003(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS020")
    def test_ts020(self):
        test_scenario = "TS020"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario)
        TC001(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS021")
    def test_ts021(self):
        test_scenario = "TS021"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario)
        TC003(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS022")
    def test_ts022(self):
        test_scenario = "TS022"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario)
        TC001(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS023")
    def test_ts023(self):
        test_scenario = "TS023"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario)
        TC003(self.driver, test_scenario)
        TC005(self.driver, test_scenario)
        TC110(self.driver, test_scenario, Concern['reference_number'], Concern['last_name'])
        TC111(self.driver, test_scenario, Concern['concern_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")