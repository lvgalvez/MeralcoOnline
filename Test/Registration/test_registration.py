import pytest

from Test.Registration.test_cases import *
from Utilities.Data import *


@pytest.mark.usefixtures("setup")
class TestRegistration:
    module = "Registration"

    @pytest.mark.tags("TS002")
    def test_ts002(self):
        test_scenario = "TS002"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_1(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'], Registration['can_single_service'])
        TC004(self.driver, test_scenario, Registration['single_service_pay_email'], Registration['single_service_first_name'],
              Registration['single_service_last_name'], Registration['single_service_mobile_num'], Registration['can_single_service'],
              Registration['single_service_kwh'], Registration['single_service_bill_date'], Registration['single_service_pay_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS003")
    def test_ts003(self):
        test_scenario = "TS003"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_1(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['can_single_service'])
        TC005(self.driver, test_scenario, Registration['single_service_nonpay_email'], Registration['single_service_first_name_np'],
              Registration['single_service_last_name_np'], Registration['single_service_mobile_num_np'], Registration['can_single_service'],
              Registration['single_service_kwh'], Registration['single_service_bill_date'], Registration['single_service_pay_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS004")
    def test_ts004(self):
        test_scenario = "TS004"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_2(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['can_multiple_service'])
        TC016(self.driver, test_scenario, Registration['multiple_service_pay_email'],
              Registration['multiple_service_pay_first_name'],
              Registration['multiple_service_pay_last_name'], Registration['multiple_service_pay_mobile_num'],
              Registration['can_multiple_service'],
              Registration['multiple_service_kwh'], Registration['multiple_service_bill_date'],
              Registration['multiple_service_password'], Registration['multiple_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS005")
    def test_ts005(self):
        test_scenario = "TS005"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_2(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['can_multiple_service'])
        TC006(self.driver, test_scenario, Registration['multiple_service_email'], Registration['multiple_service_first_name'],
              Registration['multiple_service_last_name'], Registration['multiple_service_mobile_num'], Registration['can_multiple_service'],
              Registration['multiple_service_kwh'], Registration['multiple_service_bill_date'], Registration['multiple_service_password'], Registration['multiple_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS006")
    def test_ts006(self):
        test_scenario = "TS006"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_2(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['match_bills_can'])
        TC007(self.driver, test_scenario, Registration['match_bills_email'], Registration['match_bills_first_name'],
              Registration['match_bills_last_name'], Registration['match_bills_mobile_num'], Registration['match_bills_can'],
              Registration['match_bills_kwh'], Registration['match_bills_date'], Registration['match_bills_password'], Registration['match_bills_sin'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS012")
    def test_ts012(self):
        test_scenario = "TS012"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC012(self.driver, test_scenario, Registration['new_gmail'], Registration['new_gpass'])
        TC015(self.driver, test_scenario, Registration['gmail_enroll_mobile'], Registration['can_multiple_service'],
              Registration['multiple_service_kwh'], Registration['multiple_service_bill_date'], Registration['multiple_service'])
        TC010(self.driver, test_scenario, Registration['new_gmail'], Registration['new_gpass'], Registration['match_bills_can']
              , Registration['match_bills_sin'], Registration['match_bills_kwh'], Registration['match_bills_date'])
        TC011(self.driver, test_scenario, Registration['new_gmail'], Registration['new_gpass'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS015")
    def test_ts015(self):
        test_scenario = "TS015"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_1(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['can_no_bill'])
        TC024(self.driver, test_scenario, Registration['can_no_bill_pay_email'], Registration['can_no_bill_pay_first_name'], Registration['can_no_bill_pay_middle_name'],
              Registration['can_no_bill_pay_last_name'], Registration['can_no_bill_pay_mobile_num'], Registration['can_no_bill'],
              Registration['can_no_bill_sing_bill_deposit'], Registration['can_no_bill_sing_payment_date'], Registration['can_no_bill_pay_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS016")
    def test_ts016(self):
        test_scenario = "TS016"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_1(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['can_no_bill'])
        TC024(self.driver, test_scenario, Registration['can_no_bill_email'], Registration['can_no_bill_first_name'], Registration['can_no_bill_middle_name'],
              Registration['can_no_bill_last_name'], Registration['can_no_bill_mobile_num'], Registration['can_no_bill'],
              Registration['can_no_bill_sing_bill_deposit'], Registration['can_no_bill_sing_payment_date'], Registration['can_no_bill_password'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS017")
    def test_ts017(self):
        test_scenario = "TS017"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_1(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['can_no_bill_multiple'])
        TC025(self.driver, test_scenario, Registration['can_no_bill_pmultiple_email'], Registration['can_no_bill_pmultiple_first_name'], Registration['can_no_bill_pmultiple_middle_name'],
              Registration['can_no_bill_pmultiple_last_name'], Registration['can_no_bill_pmultiple_mobile_num'], Registration['can_no_bill_multiple'],
              Registration['can_no_bill_multiple_bill_deposit'], Registration['can_no_bill_multiple_payment_date'], Registration['can_no_bill_pmultiple_password'], Registration['can_no_bill_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS018")
    def test_ts018(self):
        test_scenario = "TS018"
        Functions().create_document(self.driver, self.module, test_scenario)
        Precondition_1(self.driver, test_scenario, Registration['cxe_email'], Registration['cxe_password'],
                       Registration['can_no_bill_multiple'])
        TC025(self.driver, test_scenario, Registration['can_no_bill_multiple_email'], Registration['can_no_bill_multiple_first_name'], Registration['can_no_bill_multiple_middle_name'],
              Registration['can_no_bill_multiple_last_name'], Registration['can_no_bill_multiple_mobile_num'], Registration['can_no_bill_multiple'],
              Registration['can_no_bill_multiple_bill_deposit'], Registration['can_no_bill_multiple_payment_date'], Registration['can_no_bill_multiple_password'], Registration['can_no_bill_service'])
        Functions().tag_status(self.module, test_scenario, "Passed")

    @pytest.mark.tags("TS024")
    def test_ts024(self):
        test_scenario = "TS024"
        Functions().create_document(self.driver, self.module, test_scenario)
        TC012(self.driver, test_scenario, Registration['new_gmail'], Registration['new_gpass'])
        TC031(self.driver, test_scenario, Registration['can_no_bill_pmultiple_gmobile_num'], Registration['can_no_bill_multiple'],
              Registration['can_no_bill_multiple_bill_deposit'], Registration['can_no_bill_multiple_payment_date'], Registration['can_no_bill_service'])
        TC026(self.driver, test_scenario, Registration['new_gmail'], Registration['new_gpass'], Registration['can_no_bill']
              , Registration['can_no_bill_sing_bill_deposit'], Registration['can_no_bill_sing_payment_date'])
        TC011(self.driver, test_scenario, Registration['new_gmail'], Registration['new_gpass'])
        Functions().tag_status(self.module, test_scenario, "Passed")