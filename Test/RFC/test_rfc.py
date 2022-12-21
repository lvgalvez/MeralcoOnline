import pytest

from Test.RFC.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestRFC:
    module = "RFC"
    function = Functions()

    @pytest.mark.tags("TS001")
    def test_ts001(self):
        test_scenario = "TS001"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC001(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS002")
    def test_ts002(self):
        test_scenario = "TS002"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC002(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS005")
    def test_ts005a(self):
        test_scenario = "TS005"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC049(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS006")
    def test_ts005b(self):
        test_scenario = "TS005"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC050(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS006")
    def test_ts006(self):
        test_scenario = "TS006"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC051(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

