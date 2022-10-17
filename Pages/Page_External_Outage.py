from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ExternalOutagePage:
    location_message = "//p[contains(text(), 'Meralco would like to access your location to identify if your area is affected by an outage.' )]"
    map_iframe = "//iframe[@id='externalMap']"
    disagree_button = "//button[@ng-click = 'embed.onGPSDisagree()']"
    agree_button = "//button[@ng-click = 'embed.onGPSAgree()']"
    zoom_in = "//div[@title= 'Zoom In']"
    zoom_out = "//div[@title= 'Zoom Out']"
    map_views = "//div[@title= 'Map Views']"
    weather_modal = "//i[@class= 'material-icons closeButton ng-scope']"
    show_temperature = "//img[@ng-src = '/resources/images/icons/temperature.png']"
    show_rainfall = "//img[@ng-src = '/resources/images/icons/light-rain.png']"
    show_wind_speed = "//img[@src = '/resources/images/icons/wind-moderate.png']"
    show_clouds = "//img[@ng-src = '/resources/images/icons/partly-cloud.png']"
    show_default = "//img[@src = '/resources/images/maptypes/default.png']"
    show_satellite = "//img[@src = '/resources/images/maptypes/satellite.png']"
    show_terrain = "//img[@src = '/resources/images/maptypes/terrain.png']"
    close_map_type = "//img[@ng-click='layout.closeMapType()']"
    service_message_button = "//*[@id='alertModal']/div/div/div[2]/button"
    address_radio = "//md-radio-button[@ng-click=\"embed.onSelectSearchMode('location')\"]"
    service_radio = "//md-radio-button[@ng-click=\"embed.onSelectSearchMode('sin')\"]"
    reports_radio = "//md-radio-button[@ng-click=\"embed.onSelectSearchMode('reports')\"]"
    other_address_radio = "//md-radio-button[@ng-click=\"embed.onSelectLocationMode('otherLocation')\"]"
    current_address_radio = "//md-radio-button[@ng-click=\"embed.onSelectLocationMode('currentLocation')\"]"
    yellow_banner = "//div[@class='notify-panel scroll-left']"
    report_outage = "//span[contains(text(), 'Report an Outage')]"
    refresh_button = "//i[contains(text(), 'refresh')]"
    legend_expand = "//i[contains(text(), 'expand_more')]"
    unplanned_outage_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Unplanned Outage')]"
    planned_outage_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Planned Outage')]"
    restored_power_legend ="//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service with restored power')]"
    service_unplanned_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service with unplanned outage')]"
    service_planned_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service with planned outage')]"
    not_affected_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service not affected by an outage')]"

    def get_switch_frame(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='externalMap']")))

    def get_location_message(self, driver):
        return WebMisc().wait_element(driver, self.location_message, "location_message")

    def get_disagree_button(self, driver):
        return WebMisc().clickable_element(driver, self.disagree_button, "disagree_button")

    def get_agree_button(self, driver):
        return WebMisc().clickable_element(driver, self.agree_button, "agree_button")

    def get_map_views(self, driver):
        return WebMisc().clickable_element(driver, self.map_views, "map_views")

    def get_weather_modal(self, driver):
        return WebMisc().clickable_element(driver, self.weather_modal, "weather_modal")

    def get_show_temperature(self, driver):
        return WebMisc().clickable_element(driver, self.show_temperature, "show_temperature")

    def get_show_rainfall(self, driver):
        return WebMisc().clickable_element(driver, self.show_rainfall, "show_rainfall")

    def get_show_wind_speed(self, driver):
        return WebMisc().clickable_element(driver, self.show_wind_speed, "show_wind_speed")

    def get_show_clouds(self, driver):
        return WebMisc().clickable_element(driver, self.show_clouds, "show_clouds")

    def get_show_default(self, driver):
        return WebMisc().clickable_element(driver, self.show_default, "show_default")

    def get_show_satellite(self, driver):
        return WebMisc().clickable_element(driver, self.show_satellite, "show_satellite")

    def get_show_terrain(self, driver):
        return WebMisc().clickable_element(driver, self.show_terrain, "show_terrain")

    def get_zoom_in(self, driver):
        return WebMisc().clickable_element(driver, self.zoom_in, "zoom_in")

    def get_zoom_out(self, driver):
        return WebMisc().clickable_element(driver, self.zoom_out, "zoom_out")

    def get_close_map_type(self, driver):
        return WebMisc().clickable_element(driver, self.close_map_type, "close_map_type")

    def get_service_message_button(self, driver):
        return WebMisc().clickable_element(driver, self.service_message_button, "service_message_button")

    def get_address_radio(self, driver):
        return WebMisc().clickable_element(driver, self.address_radio, "address_radio")

    def get_service_radio(self, driver):
        return WebMisc().clickable_element(driver, self.service_radio, "service_radio")

    def get_reports_radio(self, driver):
        return WebMisc().clickable_element(driver, self.reports_radio, "reports_radio")

    def get_other_address_radio(self, driver):
        return WebMisc().clickable_element(driver, self.other_address_radio, "other_address_radio")

    def get_current_address_radio(self, driver):
        return WebMisc().clickable_element(driver, self.current_address_radio, "current_address_radio")

    def get_yellow_banner(self, driver):
        return WebMisc().wait_element(driver, self.yellow_banner, "yellow_banner")

    def get_report_outage(self, driver):
        return WebMisc().clickable_element(driver, self.report_outage, "report_outage")

    def get_refresh_button(self, driver):
        return WebMisc().clickable_element(driver, self.refresh_button, "refresh_button")

    def get_legend_expand(self, driver):
        return WebMisc().clickable_element(driver, self.legend_expand, "legend_expand")

    def get_unplanned_outage_legend(self, driver):
        return WebMisc().clickable_element(driver, self.unplanned_outage_legend, "unplanned_outage_legend")

    def get_planned_outage_legend(self, driver):
        return WebMisc().clickable_element(driver, self.planned_outage_legend, "planned_outage_legend")

    def get_restored_power_legend(self, driver):
        return WebMisc().clickable_element(driver, self.restored_power_legend, "restored_power_legend")

    def get_service_unplanned_legend(self, driver):
        return WebMisc().clickable_element(driver, self.service_unplanned_legend, "service_unplanned_legend")

    def get_service_planned_legend(self, driver):
        return WebMisc().clickable_element(driver, self.service_planned_legend, "service_planned_legend")

    def get_not_affected_legend(self, driver):
        return WebMisc().clickable_element(driver, self.not_affected_legend, "not_affected_legend")
