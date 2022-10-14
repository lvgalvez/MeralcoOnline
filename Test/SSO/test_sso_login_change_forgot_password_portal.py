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

    @pytest.mark.tags("TS007")
    def test_ts007(self):
        test_scenario = "TS007"
        Functions().create_document(self.driver, module, test_scenario)
        TC003(self.driver, test_scenario, SSO['forgot_pass_email'], SSO['forgot_pass_new_pass'])
        Functions().tag_status(self.module, test_scenario, "Passed")


