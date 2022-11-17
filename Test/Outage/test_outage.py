import pytest

from Test.Outage.test_cases import *
from Utilities.Data import *
from Utilities.Functions import Functions


@pytest.mark.usefixtures("setup")
class TestOutage:
    module = "Outage"
    function = Functions()

    @pytest.mark.tags("TS016")
    def test_ts016(self):
        test_scenario = "TS016"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC053(self.driver, test_scenario, Outage['report_outage_sin'], Outage['first_name'], Outage['middle_name'],
              Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'], Outage['cxe_email'],
              Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS017")
    def test_ts017(self):
        test_scenario = "TS017"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC054(self.driver, test_scenario, Outage['report_outage_sin'], Outage['first_name'], Outage['middle_name'],
              Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'], Outage['cxe_email'],
              Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS018")
    def test_ts018(self):
        test_scenario = "TS018"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC055(self.driver, test_scenario, Outage['report_outage_sin'], Outage['first_name'], Outage['middle_name'],
              Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'], Outage['cxe_email'],
              Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS021")
    def test_ts021(self):
        test_scenario = "TS021"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC058(self.driver, test_scenario, Outage['first_name'], Outage['middle_name'],
              Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS020")
    def test_ts020(self):
        test_scenario = "TS020"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC057(self.driver, test_scenario, Outage['report_outage_sin'], Outage['first_name'], Outage['middle_name'],
              Outage['last_name'], Outage['mobile_number'], Outage['landline'], Outage['email'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS027")
    def test_ts027(self):
        test_scenario = "TS027"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC061a(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'], "temperature", 8)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS023")
    def test_ts023(self):
        test_scenario = "TS023"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC060(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'], "temperature", 8)
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

    @pytest.mark.tags("TS042")
    def test_ts042(self):
        test_scenario = "TS042"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC101(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        TC102(self.driver, test_scenario)
        TC103(self.driver, test_scenario)
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

    @pytest.mark.tags("TS035")
    def test_ts035(self):
        print("Start of Exceution")
        test_scenario = "TS035"
        Functions().create_document(self.driver, self.module, test_scenario)
        #TC062(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        TC063(self.driver, test_scenario)
        TC065(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS036")
    def test_ts036(self):
        test_scenario = "TS036"
        Functions().create_document(self.driver, self.module, test_scenario)
        #TC066(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password']) #VALIDATED
        #TC070(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password']) #VALIDATED
        TC072(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS049")
    def test_ts049(self):
        test_scenario = "TS049"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC073(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS047")
    def test_ts047(self):
        test_scenario = "TS047"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC122(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS048")
    def test_ts048(self):
        test_scenario = "TS048"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC123(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS044")
    def test_ts044(self):
        test_scenario = "TS044"
        Functions().create_document(self.driver, self.module, test_scenario)
        #TC112(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password']) #VALIDATED
        TC114(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password']) #VALIDATED

        Functions().tag_status(self.module, test_scenario, "Passed")
    @pytest.mark.tags("TS040")
    def test_ts040(self):
        test_scenario = "TS040"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC085(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        TC086(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        TC087(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS045")
    def test_ts045(self):
        test_scenario = "TS045"
        Functions().create_document(self.driver, self.module, test_scenario)
        #TC116(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'], Outage['outage_internal_sin']) VALIDATED
        TC117(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'], Outage['outage_internal_sin']) #toBeContinue
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

    @pytest.mark.tags("TS038")
    def test_ts038(self):
        test_scenario = "TS038"
        Functions().create_document(self.driver, self.module, test_scenario)
        #TC076(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        TC077(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password'])
        #TC078(self.driver, test_scenario, Outage['cxe_email'], Outage['cxe_password']) #FOR TOMRROW

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
        TC146(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
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
        TC129(self.driver, test_scenario, Outage['outage_sin'])
        TC130(self.driver, test_scenario, Outage['outage_sin'], Outage['outage_email'], Outage['outage_password'])
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


    @pytest.mark.tags("TS063")
    def test_ts063(self):
        test_scenario = "TS063"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC147(self.driver, test_scenario)
        TC148(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS071")
    def test_ts071(self):
        test_scenario = "TS071"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC156(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
       # TC146(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS072")
    def test_ts072(self):
        test_scenario = "TS072"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC157(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS064")
    def test_ts064(self):
        test_scenario = "TS064"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC149(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS066")
    def test_ts066(self):
        test_scenario = "TS066"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC151(self.driver, test_scenario, Outage['reference_number'], Outage['lastname'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS067")
    def test_ts067(self):
        test_scenario = "TS067"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC152(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS068")
    def test_ts068(self):
        test_scenario = "TS068"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC153(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS069")
    def test_ts069(self):
        test_scenario = "TS069"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC154(self.driver, test_scenario, Outage['outage_email'], Outage['outage_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS070")
    def test_ts070(self):
        test_scenario = "TS070"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC155(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")



    @pytest.mark.tags("TS022")
    def test_ts072(self):
        test_scenario = "TS022"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC059(self.driver, test_scenario)
        Functions().tag_status(self.module, test_scenario, "Passed")
