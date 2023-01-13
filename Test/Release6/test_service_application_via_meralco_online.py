import pytest

from Test.Release6.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestServiceApplicationMeralcoOnline:
    module = "SAMO"
    serviceApplicationModule = "Release6"

    @pytest.mark.tags("TS001")
    def test_ts001(self):
        test_scenario = "TS001"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        #TC002a(self.driver, test_scenario)
        TC003a(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS002")
    def test_ts002(self):
        test_scenario = "TS002"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC005a(self.driver, test_scenario)
        TC006a(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS003")
    def test_ts003(self):
        test_scenario = "TS003"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        #TC008a(self.driver, test_scenario)
        TC009a(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS004")
    def test_ts004(self):
        test_scenario = "TS004"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        #TC011a(self.driver, test_scenario)
        TC012a(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS019a")
    def test_ts019a(self):
        test_scenario = "TS019a"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC039a(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS022a")
    def test_ts022a(self):
        test_scenario = "TS022a"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC042a(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS025a")
    def test_ts025a(self):
        test_scenario = "TS025a"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC045a(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

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
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC054(self.driver, test_scenario, SAMO['contractor_firstName'], SAMO['contractor_lastName'],
              SAMO['contractor_middlename'],
              SAMO['contractor_businessName'], SAMO['contractor_emailAddress'], SAMO['contractor_mobileNumber'],
              SAMO['contractor_birthday'], SAMO['service_add'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS028")
    def test_ts028(self):
        test_scenario = "TS028"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC048(self.driver, test_scenario, Outage['first_name'], Outage['middle_name'],
              Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS029")
    def test_ts029(self):
        test_scenario = "TS029"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC048a(self.driver, test_scenario, Outage['first_name'], Outage['middle_name'],
               Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS030") #screenshot DONE
    def test_ts030(self):
        test_scenario = "TS030"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC048b(self.driver, test_scenario, Outage['first_name'], Outage['middle_name'],
               Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS031") #done
    def test_ts031(self):
        test_scenario = "TS031"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC048c(self.driver, test_scenario, Outage['first_name'], Outage['middle_name'],
               Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")\

    @pytest.mark.tags("TS032") #no screenshot
    def test_ts032(self):
        test_scenario = "TS032"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC048d(self.driver, test_scenario, Outage['first_name'], Outage['middle_name'],
               Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'])
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS045")
    def test_ts045(self):
        test_scenario = "TS045"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC062(self.driver, test_scenario)
        TC063(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS046")
    def test_ts046(self):
        test_scenario = "TS046"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC064(self.driver, test_scenario)
        TC065(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS047")
    def test_ts047(self):
        test_scenario = "TS047"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC066(self.driver, test_scenario)
        TC067(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS048")
    def test_ts048(self):
        test_scenario = "TS048"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC068(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS050")
    def test_ts050(self):
        test_scenario = "TS050"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC070(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")

    @pytest.mark.tags("TS054")
    def test_ts054(self):
        test_scenario = "TS054"
        Functions().create_document(self.driver, self.serviceApplicationModule, test_scenario)
        TC074(self.driver, test_scenario)
        Functions().tag_status(self.serviceApplicationModule, test_scenario, "Passed")