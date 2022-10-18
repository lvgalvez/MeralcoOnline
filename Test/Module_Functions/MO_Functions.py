from Pages.Page_External_Outage import ExternalOutagePage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from Pages.Page_Report_Outage import ReportOutagePage
from Utilities.Functions import Functions
from Utilities.Utils import Utilities
import time

fc = Functions()
log = Utilities().getlogger()
home = HomePage()
login = LoginPage()
external_outage = ExternalOutagePage()
report_outage = ReportOutagePage()

def Log_In_Meralco_Online(driver, email, password):

    fc.input_text(login.get_email(driver), email)
    fc.input_text(login.get_password(driver), password)
    fc.click(login.get_log_in(driver))
    fc.verify(home.get_hello_message(driver))


def Verify_Successful_Login(driver):
    fc.verify(home.get_hello_message(driver))


def Navigate_Outage(driver):
    fc.click(home.get_outage_incidents(driver))
    fc.modal_click(driver, home.get_report_outage(driver))
    external_outage.get_switch_frame(driver)


def Check_Service_Located(driver):
    time.sleep(5)
    if external_outage.get_service_message_button(driver) is not None:
        fc.modal_click(driver, external_outage.get_service_message_button(driver))
        return 9
    else:
        return 16

def Click_Outage_Map_Views(driver):
    fc.click(external_outage.get_map_views(driver))


def Select_Weather_Information(driver, weather):
    if weather == "temperature":
        fc.click(external_outage.get_show_temperature(driver))
    elif weather == "rainfall":
        fc.click(external_outage.get_show_rainfall(driver))
    elif weather == "wind_speed":
        fc.click(external_outage.get_show_wind_speed(driver))
    elif weather == "clouds":
        fc.click(external_outage.get_show_clouds(driver))
    elif weather == "default":
        fc.click(external_outage.get_show_default(driver))
    elif weather == "satellite":
        fc.click(external_outage.get_show_satellite(driver))
    elif weather == "terrain":
        fc.click(external_outage.get_show_terrain(driver))

    fc.modal_click(driver, external_outage.get_weather_modal(driver))
    time.sleep(15)
    fc.click(external_outage.get_close_map_type(driver))


def Select_Map_Type(driver, Type):
    if Type == "Default":
        fc.click(external_outage.get_show_default(driver))
    elif Type == "Satellite":
        fc.click(external_outage.get_show_satellite(driver))
    elif Type == "Terrain":
        fc.click(external_outage.get_show_terrain(driver))
    time.sleep(15)
    fc.click(external_outage.get_close_map_type(driver))


def Adjust_Zoom_Level(driver, default_zoom, zoom_level):
    zoom = default_zoom - zoom_level
    if zoom > 0:
        for x in range(zoom):
            fc.click(external_outage.get_zoom_out(driver))
    if zoom < 0:
        for x in range(abs(zoom)):
            fc.click(external_outage.get_zoom_in(driver))


def Handle_GPS_Prompt(driver, button):
    if button == "Agree":
        fc.click(external_outage.get_agree_button(driver))
    else:
        fc.click(external_outage.get_disagree_button(driver))

    time.sleep(4)


def Click_Report_Outage(driver):
    fc.click(external_outage.get_report_outage(driver))
    fc.accept_alert(driver)
    time.sleep(4)
    report_outage = ReportOutagePage()
    fc.verify(report_outage.get_report_outage_text(driver))


def Verify_GPS_Prompt(driver):
    text = "Meralco would like to access your location to identify if your area is affected by an outage."
    fc.verify_text(external_outage.get_location_message(driver), text)


def Tick_Current_Address(driver):
    fc.click(external_outage.get_address_radio(driver))
    fc.click(external_outage.get_current_address_radio(driver))


def Verify_Yellow_Banner(driver):
    fc.verify(external_outage.get_yellow_banner(driver))


def Click_Refresh_Button(driver):
    fc.click(external_outage.get_refresh_button(driver))
    time.sleep(9)


def Click_Legends_Guest(driver):
    fc.click(external_outage.get_legend_expand(driver))
    fc.verify_text(external_outage.get_unplanned_outage_legend(driver), "Unplanned Outage")
    fc.verify_text(external_outage.get_planned_outage_legend(driver), "Planned Outage")
    fc.scroll_element(driver, external_outage.get_planned_outage_legend(driver))


def Click_Legends_User(driver):
    fc.click(external_outage.get_legend_expand(driver))
    fc.verify_text(external_outage.get_restored_power_legend(driver), "Service with restored power")
    fc.verify_text(external_outage.get_service_unplanned_legend(driver), "Service with unplanned outage")
    fc.verify_text(external_outage.get_service_planned_legend(driver), "Service with planned outage")
    fc.verify_text(external_outage.get_not_affected_legend(driver), "Service not affected by an outage")
    fc.verify_text(external_outage.get_unplanned_outage_legend(driver), "Unplanned Outage")
    fc.verify_text(external_outage.get_planned_outage_legend(driver), "Planned Outage")
    fc.scroll_element(driver, external_outage.get_planned_outage_legend(driver))


def Click_Other_Address(driver):
    fc.click(external_outage.get_other_address_radio(driver))


def Click_Anywhere_Map(driver):
    fc.coordinates_click(driver, 200, 200)
    time.sleep(5)


def Click_Current_Location(driver):
    fc.click(external_outage.get_current_address(driver))


def Click_Outage_Pin(driver):
    fc.click(external_outage.get_outage_pin(driver))


def Required_Field_Population(driver, sin):
    fc.click(report_outage.get_no_power_radio(driver))
    fc.click(report_outage.get_service_id_radio(driver))
    fc.input_text(report_outage.get_service_id_number(driver), sin)


def Required_Field_Population_User(driver, sin):
    fc.click(report_outage.get_no_power_radio(driver))
    fc.click(report_outage.get_service_id_radio(driver))
    #fc.click(report_outage.get_service_id_dropdown(driver))
    fc.click(report_outage.get_service_select(driver))


def Tick_Location_Map(driver):
    fc.click(report_outage.get_location_map(driver))
    time.sleep(5)
    fc.click(report_outage.get_location_map(driver))
    fc.page_down(driver, 1)


def Tick_Location_Map_User(driver):
    time.sleep(5)
    fc.click(report_outage.get_location_map(driver))
    time.sleep(5)
    fc.page_down(driver, 1)
