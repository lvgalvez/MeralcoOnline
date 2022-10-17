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

    @pytest.mark.tags("TS052")
    def test_ts052(self):
        test_scenario = "TS052"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC128(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")


    @pytest.mark.tags("TS053")
    def test_ts053(self):
        test_scenario = "TS053"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC129(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS054")
    def test_ts054(self):
        test_scenario = "TS054"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC131(self.driver, test_scenario)
        TC132(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS055")
    def test_ts055(self):
        test_scenario = "TS055"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC133(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS056")
    def test_ts056(self):
        test_scenario = "TS056"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC134(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS057")
    def test_ts057(self):
        test_scenario = "TS057"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC135(self.driver, test_scenario)
        TC136(self.driver, test_scenario)
        TC137(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS058")
    def test_ts058(self):
        test_scenario = "TS058"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC138(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        TC139(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        TC140(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")


    @pytest.mark.tags("TS059")
    def test_ts059(self):
        test_scenario = "TS059"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC141(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")


    @pytest.mark.tags("TS060")
    def test_ts060(self):
        test_scenario = "TS060"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC142(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

