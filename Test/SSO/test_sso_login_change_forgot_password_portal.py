import pytest
from Test.SSO.test_cases import *


@pytest.mark.usefixtures("setup")
class TestSSOLoginChangeForgotPass:
    module = "SSO"

    @pytest.mark.tags("TS003")
    def test_ts003(self):
        test_scenario = "TS003"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, SSO['normal_account_email'], SSO['normal_account_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS004")
    def test_ts004(self):
        test_scenario = "TS004"
        Functions().create_document(self.driver, module, test_scenario)
        TC007(self.driver, test_scenario, "Invalid@yopmail.com", "InvalidPass")
        Functions().tag_status(self.module, test_scenario, "Passed")
