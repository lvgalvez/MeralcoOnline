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
              SAMO['individual_account_middle'], SAMO['individual_account_last'], SAMO['individual_account_mobile'],
              SAMO['default_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")
