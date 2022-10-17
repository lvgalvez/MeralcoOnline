import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from Pages.Page_External_Outage import ExternalOutagePage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Test.Module_Functions.MO_Functions import *
from Utilities.Config import *
from Utilities.Functions import *
from Utilities.Utils import Utilities
from Test.Module_Functions import MO_Functions
fc = Functions()
log = Utilities().getlogger()
module = "Outage"


def TC061a(driver, ts_id, email, password, weather, zoom_level):
    test_case = "TC061"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    Navigate_Outage(driver)
    default_zoom = Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Weather_Information(driver, weather)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Adjust_Zoom_Level(driver, default_zoom, zoom_level)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


def TC061b(driver, ts_id, weather, zoom_level):
    test_case = "TC061"
    default_zoom = 9
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Weather_Information(driver, weather)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Adjust_Zoom_Level(driver, default_zoom, zoom_level)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


def TC124(driver, ts_id):
    test_case = "TC124"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC125(driver, ts_id):
    test_case = "TC125"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC126(driver, ts_id, email, password):
    test_case = "TC126"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Tick_Current_Address(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC127(driver, ts_id, email, password):
    test_case = "TC127"
    fc.new_tab(driver, meralco_online)

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Tick_Current_Address(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC128(driver, ts_id, email, password):
    test_case = "TC128"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Handle_GPS_Prompt(driver, "Disagree")
    Verify_Yellow_Banner(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    Verify_Yellow_Banner(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")


def TC129(driver, ts_id, email, password):
    test_case = "TC129"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(external_outage.get_report_outage(driver))
    time.sleep(10)
    print(len(driver.window_handlers))
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0, 0)
    actions.move_by_offset(100, 100).click().perform()

    driver.switch_to.alert.dismiss()

def TC131(driver, ts_id):
    test_case = "TC131"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Refresh_Button(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC132(driver, ts_id, email, password):
    test_case = "TC132"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Refresh_Button(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC133(driver, ts_id):
    test_case = "TC133"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Legends_Guest(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC134(driver, ts_id, email, password):
    test_case = "TC134"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Legends_User(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC135(driver, ts_id):
    test_case = "TC135"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Map_Type(driver, "Default")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC136(driver, ts_id):
    test_case = "TC136"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Map_Type(driver, "Satellite")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC137(driver, ts_id):
    test_case = "TC137"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Map_Type(driver, "Terrain")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC138(driver, ts_id, email, password):
    test_case = "TC138"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Map_Type(driver, "Default")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC139(driver, ts_id, email, password):
    test_case = "TC139"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Map_Type(driver, "Satellite")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC140(driver, ts_id, email, password):
    test_case = "TC140"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Map_Type(driver, "Terrain")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC141(driver, ts_id):
    test_case = "TC141"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Other_Address(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Click_Anywhere_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


def TC142(driver, ts_id, email, password):
    test_case = "TC142"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.verify(external_outage.get_address_radio(driver))
    fc.verify(external_outage.get_service_radio(driver))
    fc.verify(external_outage.get_reports_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.click(external_outage.get_address_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    Click_Anywhere_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.click(external_outage.get_current_address_radio(driver))
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

    fc.bookmark(module, ts_id, test_case, "Step 8")
    fc.click(external_outage.get_reports_radio(driver))
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")

    fc.bookmark(module, ts_id, test_case, "Step 9")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")


