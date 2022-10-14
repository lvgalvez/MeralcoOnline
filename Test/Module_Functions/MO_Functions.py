from Pages.Page_External_Outage import ExternalOutagePage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from Utilities.Functions import Functions
from Utilities.Utils import Utilities
import time

fc = Functions()
log = Utilities().getlogger()
home = HomePage()
login = LoginPage()
external_outage = ExternalOutagePage()

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
    fc.modal_click(driver, external_outage.get_weather_modal(driver))
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


def Verify_GPS_Prompt(driver):
    text = "Meralco would like to access your location to identify if your area is affected by an outage."
    fc.verify_text(external_outage.get_location_message(driver), text)


def Tick_Current_Address(driver):
    fc.click(external_outage.get_address_radio(driver))
    fc.click(external_outage.get_current_address_radio(driver))
