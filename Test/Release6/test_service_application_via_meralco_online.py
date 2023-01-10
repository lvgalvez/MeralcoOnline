import pytest

from Test.SAMO.test_cases import *
from Test.Release6.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestServiceApplicationMeralcoOnline:
    module = "SAMO"
    serviceApplicationModule = "Release6"

    @pytest.mark.tags("TS035")
    def test_ts035(self):
        test_scenario = "TS035"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC051(self.driver, test_scenario, SAMO['business_company_name'], SAMO['business_trade_name'], SAMO['business_company_email'], SAMO['business_company_landline'],
              SAMO['business_first_name'], SAMO['business_last_name'], SAMO['business_emailaddress'], SAMO['business_mobile_number'], SAMO['business_designation'], SAMO['service_add'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS036")
    def test_ts036(self):
        test_scenario = "TS036"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC054(self.driver, test_scenario, SAMO['contractor_firstName'], SAMO['contractor_lastName'],
              SAMO['contractor_middlename'],
              SAMO['contractor_businessName'], SAMO['contractor_emailAddress'], SAMO['contractor_mobileNumber'],
              SAMO['contractor_birthday'], SAMO['service_add'])
        Functions().tag_status(self.module, test_scenario, "Passed")