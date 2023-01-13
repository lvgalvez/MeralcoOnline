import pytest
from Test.SSO.test_cases import *


@pytest.mark.usefixtures("setup")
class TestSSOLoginChangeForgotPass:
    module = "SSO"

    @pytest.mark.tags("TS001")
    def test_ts001(self):
        test_scenario = "TS001"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC005(self.driver, test_scenario, SSO['facebook_email'], SSO['facebook_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS002")
    def test_ts002(self):
        test_scenario = "TS002"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC006(self.driver, test_scenario, SSO['google_email'], SSO['google_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS003")
    def test_ts003(self):
        test_scenario = "TS003"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC007(self.driver, test_scenario, SSO['normal_account_email'], "invalid")
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS004")
    def test_ts004(self):
        test_scenario = "TS004"
        Functions().create_document(self.driver, module, test_scenario)
        TC010(self.driver, test_scenario, SSO['lockout_email'], SSO['lockout_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS005")
    def test_ts005(self):
        test_scenario = "TS005"
        Functions().create_document(self.driver, module, test_scenario)
        TC001(self.driver, test_scenario, SSO['facebook_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS006")
    def test_ts006(self):
        test_scenario = "TS006"
        Functions().create_document(self.driver, module, test_scenario)
        TC001(self.driver, test_scenario, SSO['google_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS007")
    def test_ts007(self):
        test_scenario = "TS007"
        Functions().create_document(self.driver, module, test_scenario)
        TC003(self.driver, test_scenario, SSO['forgot_pass_email'], SSO['forgot_pass_new_pass'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS009")
    def test_ts009(self):
        test_scenario = "TS009"
        Functions().create_document(self.driver, module, test_scenario)
        TC002(self.driver, test_scenario, SSO['google_email'], SSO['google_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS010")
    def test_ts010(self):
        test_scenario = "TS010"
        Functions().create_document(self.driver, module, test_scenario)
        TC004(self.driver, test_scenario, SSO['changepass_email'], SSO['changepass_password'], SSO['changepass_new_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS022")
    def test_ts022(self):
        test_scenario = "TS022"
        Functions().create_document(self.driver, module, test_scenario)
        TC009(self.driver, test_scenario, SSO['expired_email'], SSO['expired_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS024")
    def test_ts024(self):
        test_scenario = "TS024"
        Functions().create_document(self.driver, module, test_scenario)
        TC008(self.driver, test_scenario, SSO['google_email'], SSO['google_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS027")
    def test_ts027(self):
        test_scenario = "TS027"
        Functions().create_document(self.driver, module, test_scenario)
        TC013(self.driver, test_scenario, SSO['facebook_email'])
        Functions().tag_status(self.module, test_scenario, "Passed")
