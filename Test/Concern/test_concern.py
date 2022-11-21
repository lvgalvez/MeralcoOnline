import pytest

from Test.Outage.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestConcern:
    module = "Outage"
    function = Functions()

    @pytest.mark.tags("TS016")
    def test_ts016(self):
        test_scenario = "TS016"
        Functions().create_document(self.driver, self.module, test_scenario)

        Functions().tag_status(self.module, test_scenario, "Passed")