import pytest

from Test.Outage.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestOutage:
    module = "Outage"

    @pytest.mark.tags("TS027")
    def test_ts027(self):
        test_scenario = "TS027"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061a(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'], "temperature", 8)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS028")
    def test_ts028(self):
        test_scenario = "TS028"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061a(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'], "rainfall", 15)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS029")
    def test_ts029(self):
        test_scenario = "TS029"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061a(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'], "wind_speed", 12)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS030")
    def test_ts030(self):
        test_scenario = "TS030"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061a(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'], "clouds", 13)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS031")
    def test_ts031(self):
        test_scenario = "TS031"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061b(self.driver, test_scenario, "temperature", 8)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS032")
    def test_ts032(self):
        test_scenario = "TS032"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061b(self.driver, test_scenario, "rainfall", 10)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS033")
    def test_ts033(self):
        test_scenario = "TS033"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061b(self.driver, test_scenario, "wind_speed", 11)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS034")
    def test_ts034(self):
        test_scenario = "TS034"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061b(self.driver, test_scenario, "clouds", 16)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS050")
    def test_ts050(self):
        test_scenario = "TS050"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC124(self.driver, test_scenario)
        TC125(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS051")
    def test_ts051(self):
        test_scenario = "TS051"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC126(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        TC127(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")
    @pytest.mark.tags("TS061")
    def test_ts061(self):
        test_scenario = "TS061"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC143(self.driver, test_scenario)
        TC144(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS062")
    def test_ts062(self):
        test_scenario = "TS062"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC145(self.driver, test_scenario)
        #TC146(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")