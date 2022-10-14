from Utilities.Drivers.MO_Functions import *
from Utilities.Config import *
from Utilities.Functions import *
from Utilities.Utils import Utilities

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


def TC143(driver, ts_id):
    test_case = "TC143"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Adjust_Zoom_Level(driver, 8, 9)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Adjust_Zoom_Level(driver, 9, 8)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

def TC144(driver, ts_id, email, password):
    test_case = "TC144"

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
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Adjust_Zoom_Level(driver, 8, 9)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    Adjust_Zoom_Level(driver, 9, 8)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

def TC145(driver, ts_id):
    test_case = "TC143"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

