from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class InternalOutagePage:
    location_message = "//p[contains(text(), 'Meralco would like to access your location to identify if your area is affected by an outage.' )]"
    map_iframe = "//iframe[@id='externalMap']"
    disagree_button = "//button[@ng-click = 'embed.onGPSDisagree()']"
    agree_button = "//button[@ng-click = 'embed.onGPSAgree()']"
    zoom_in = "//div[@title= 'Zoom In']"
    zoom_out = "//div[@title= 'Zoom Out']"
    map_views = "//div[@title= 'Map Views']"
    weather_modal = "//i[@class= 'material-icons closeButton ng-scope']"
    outage_modal = "/html/body/div[2]/div[11]/div[1]/img"
    show_temperature = "//img[@ng-src = '/resources/images/icons/temperature.png']"
    show_rainfall = "//img[@ng-src = '/resources/images/icons/light-rain.png']"
    show_wind_speed = "//img[@src = '/resources/images/icons/wind-moderate.png']"
    show_clouds = "//img[@ng-src = '/resources/images/icons/partly-cloud.png']"
    close_map_type = "//img[@ng-click='layout.closeMapType()']"
    service_message_button = "//*[@id='alertModal']/div/div/div[2]/button"
    address_radio = "//md-radio-button[@ng-click=\"embed.onSelectSearchMode('location')\"]"
    current_address_radio = "//md-radio-button[@ng-click=\"embed.onSelectLocationMode('currentLocation')\"]"
    current_address = "//*[@id='currentLocationMenu']/span"
    outage_pin = "//*[@id='map-canvas']/div/div/div[2]/div[2]/div"
    yellow_banner = "//div[@class='notify-panel scroll-left']"
    report_outage = "//span[contains(text(), 'Report an Outage')]"
    refresh_button = "//*[@id='navbarContainer']/ul[1]/li/div[2]/div[1]/div[1]/button"
    unplanned_outage_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Unplanned Outage')]"
    planned_outage_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Planned Outage')]"
    restored_power_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service with restored power')]"
    service_unplanned_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service with unplanned outage')]"
    service_planned_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service with planned outage')]"
    not_affected_legend = "//*[@id='embedLegend']/div/div[2]/p[contains(text(), 'Service not affected by an outage')]"
    service_radio = "//md-radio-button[@ng-click=\"embed.onSelectSearchMode('sin')\"]"
    reports_radio = "//md-radio-button[@ng-click=\"embed.onSelectSearchMode('reports')\"]"
    other_address_radio = "//md-radio-button[@ng-click=\"embed.onSelectLocationMode('otherLocation')\"]"
    legend_expand = "//i[contains(text(), 'expand_more')]"
    show_default = "//img[@src = '/resources/images/maptypes/default.png']"
    show_satellite = "//img[@src = '/resources/images/maptypes/satellite.png']"
    show_terrain = "//img[@src = '/resources/images/maptypes/terrain.png']"
    tooltip_other_address = "//i[contains(text(),'info')]"
    outage_report = "//*[@id='externalSideNavMobile']/md-content/div[4]/p/a"
    address = "//*[@id='radio_1']/div[1]/div[1]"
    meralcoicon = "/html/body/div[2]/div[10]/div[4]/div/div[2]/div/img"
    businessoutage_modal = "//*[@id='alertModal']/div/div/i"
    menu = "/html/body/div[3]/div[2]/md-list-item/div/button"
    map_display = "//img[@src= '/resources/images/map-display-hover.png']"
    weather = "//*[@id='headingOne']/h4/input"
    internal_modal = "//*[@id='weatherModal']/div/div/div[2]/button"
    meralco_header = "//*[@id='mainAppBody']/div[1]/div/div[1]/img"
    center_map = "//*[@id='map-canvas']/div/div/div[2]/div[2]/div/div[3]/div[1]/div"
    admin = "//*[@id='accordion-menulistTEST']/button"
    legends = "//*[@id='accordion-menulistTEST']/div/div[6]/div[1]/button"
    search = "//*[@id='accordion-menulistTEST']/div/div[3]/div[1]/button"
    SIN = "//input[@placeholder = 'Enter Service ID No.']"
    faci = "//*[@id='searchBoxArea']/div/div[1]/div/button"
    faci_value = "//*[@id='searchBoxArea']/div/div[1]/div/button/span"
    clear = "//*[@id='searchBoxArea']/div/div[2]/md-autocomplete/md-autocomplete-wrap/button"
    outage_area = "//*[@id='accordion-menulistTEST']/div/div[1]/div[1]/button"
    sector = "//*[@id='outageinfo']/div/div[1]/div/div/button/i"
    sector_value = "//a[contains(text(), 'Plaridel Sector')]"
    area_level = "//*[@id='outageinfo']/div/div[2]/div/div/button/i"
    area_value = "//a[contains(text(), 'City/Municipality')]"
    political_boundary = "//*[@id='mapLayerDragHandler']/i"
    sector_office = "//*[@id='layer_category_2']/div/ul/li[1]/div[2]/input"
    sector_pin = "//*[@id='map-canvas']/div/div/div[2]/div[2]/div/div[3]/div[4]/img"
    election_center = "//*[@id='layer_category_2']/div/ul/li[2]/div[2]/input"
    election_pin = "//*[@id='map-canvas']/div/div/div[2]/div[2]/div/div[3]/div[5]/img"
    vital_custom = "//*[@id='layer_category_2']/div/ul/li[3]/div[2]/input"
    vital_pin = "//*[@id='map-canvas']/div/div/div[2]/div[2]/div/div[3]/div[7]/img"
    mapview_internal = "//*[@id='map-canvas-container']/div[9]"
    sattelite = "//*[@id='map-canvas-container']/div[10]/div[2]/div[2]/img"
    FAQ_header = "//li[@label='FAQ']"
    QRG_header = "//li[@label='QRG']"
    hamburger_menu = "//span[contains(text(), 'menu')]"
    outage_pins_filter = "//i[contains(text(), 'filter_list') and @id = 'ongoingFilterBtn']"
    scheduled_interruption = "//span[contains(text(), 'Scheduled Interruptions')]"
    incident_type = "//md-radio-button[@aria-label= 'incident_type']"
    date_restoration = "//md-radio-button[@aria-label= 'date_restore']"
    restoration_today = "//div/div[2]/div/div[2]/div/span[@class= 'flatpickr-day today']"
    affected_facility_type = "//md-radio-button[@value= 'facility_type']"
    outage_load_shedding = "//span[contains(text(), 'Planned Outage- Load Shedding')]"
    type_no_device = "//span[contains(text(), 'No Device')]"
    menu_affected_areas = "//div[4]/input[@data-ng-model = 'layerItemInner.show']"
    by_count = "//md-radio-button[@value = 'count']"
    by_percentage = "//md-radio-button[@value = 'percentage']"
    select_cluster = "//img[1][@src = '/resources/images/cluster/red1.png']"
    affected_areas = "//button[contains(text(), 'Affected Areas')]"
    get_directions = "//button[contains(text(), 'Get Directions')]"
    incident_status_history = "//button[contains(text(), 'Incident Status History')]"
    interruption_back = "//button[contains(text(), 'Back')]"
    calendar_show = "//i[contains(text(), 'calendar_view_day')]"
    alert_modal = "//*[@id='alertModal']/div/div/div[2]/button"
    concern_reported_chk = "//*/md-radio-group/li[1]/div/div[2]/input"
    concern_reported_filter = "//i[@data-target='#concernFilterCollapse']"
    concern_type = "//md-radio-button[@value='concern_type']"
    case_status = "//md-radio-button[@value='case_status']"
    reported_date = "//md-radio-button[@value='reported_date']"
    date_highlight = "//tr/td[@class=' dateHighlight'][1]"
    text_election_centers = "//div/div/span[contains(text(), 'Election Centers')]"
    text_vital_customers = "//div/div/span[contains(text(), 'Vital Customers')]"
    text_sector_office = "//div/div/span[contains(text(), 'Sector Office')]"
    main_affected_facility = "//div[last()]/div/b[@class='ng-binding']"




    def get_sattelite(self, driver):
        return WebMisc().clickable_element(driver, self.sattelite, "sattelite")
    def get_map_view_internal(self, driver):
        return WebMisc().clickable_element(driver, self.mapview_internal, "mapview_internal")
    def get_vital_pin(self, driver):
        return WebMisc().clickable_element(driver, self.vital_pin, "vital_pin")
    def get_vital_custom(self, driver):
        return WebMisc().clickable_element(driver, self.vital_custom, "vital_custom")
    def get_election_pin(self, driver):
        return WebMisc().clickable_element(driver, self.election_pin, "election_pin")
    def get_election_center(self, driver):
        return WebMisc().clickable_element(driver, self.election_center, "election_center")
    def get_sector_pin(self, driver):
        return WebMisc().clickable_element(driver, self.sector_pin, "sector_pin")
    def get_sector_office(self, driver):
        return WebMisc().clickable_element(driver, self.sector_office, "sector_office")
    def get_political_boundary(self, driver):
        return WebMisc().clickable_element(driver, self.political_boundary, "political_boundary")
    def get_area_value(self, driver):
        return WebMisc().clickable_element(driver, self.area_value, "area_value")
    def get_area_level(self, driver):
        return WebMisc().clickable_element(driver, self.area_level, "area_level")
    def get_sector_value(self, driver):
        return WebMisc().clickable_element(driver, self.sector_value, "sector_value")
    def get_sector(self, driver):
        return WebMisc().clickable_element(driver, self.sector, "sector")
    def get_outage_area(self, driver):
        return WebMisc().clickable_element(driver, self.outage_area, "outage_area")
    def get_clear(self, driver):
        return WebMisc().clickable_element(driver, self.clear, "clear")
    def get_facility_value(self, driver):
        return WebMisc().clickable_element(driver, self.faci_value, "faci_value")
    def get_facility(self, driver):
        return WebMisc().clickable_element(driver, self.faci, "faci")
    def get_SIN(self, driver):
        return WebMisc().wait_element(driver, self.SIN, "SIN")
    def get_search(self, driver):
        return WebMisc().clickable_element(driver, self.search, "search")
    def get_legends(self, driver):
        return WebMisc().clickable_element(driver, self.legends, "legends")
    def get_admin(self, driver):
        return WebMisc().clickable_element(driver, self.admin, "admin")
    def get_center_map(self, driver):
        return WebMisc().clickable_element(driver, self.center_map, "center_map")
    def get_meralco_header(self, driver):
        return WebMisc().clickable_element(driver, self.meralco_header, "meralco_header")

    def get_internal_modal(self, driver):
        return WebMisc().clickable_element(driver, self.internal_modal, "internal_modal")

    def get_weather_click(self, driver):
        return WebMisc().clickable_element(driver, self.weather, "weather")
    def get_map_display(self, driver):
        return WebMisc().clickable_element(driver, self.map_display, "map_display")
    def get_menu(self, driver):
        return WebMisc().clickable_element(driver, self.menu, "menu")
    def get_meralco_icon(self, driver):
        return WebMisc().wait_element(driver, self.meralcoicon, "meralcoicon")
    def get_address(self, driver):
        return WebMisc().wait_element(driver, self.address, "address")
    def get_outage_report(self, driver):
        return WebMisc().wait_element(driver, self.outage_report, "outage_report")
    def get_tooltip_other_address(self, driver):
        return WebMisc().wait_element(driver, self.tooltip_other_address, "tooltip_other_address")
    def get_outage_pin(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='externalMap']")))

    def get_switch_frame(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='map-canvas']/div/div/div[3]")))

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

    def get_outage_modal(self, driver):
        return WebMisc().clickable_element(driver, self.outage_modal, "outage_modal")

    def get_businessoutage_modal(self, driver):
        return WebMisc().clickable_element(driver, self.businessoutage_modal, "businessoutage_modal")
    def get_show_temperature(self, driver):
        return WebMisc().clickable_element(driver, self.show_temperature, "show_temperature")

    def get_show_rainfall(self, driver):
        return WebMisc().clickable_element(driver, self.show_rainfall, "show_rainfall")

    def get_show_wind_speed(self, driver):
        return WebMisc().clickable_element(driver, self.show_wind_speed, "show_wind_speed")

    def get_show_clouds(self, driver):
        return WebMisc().clickable_element(driver, self.show_clouds, "show_clouds")

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

    def get_current_address(self, driver):
        return WebMisc().clickable_element(driver, self.current_address, "current_address")

    def get_current_address_radio(self, driver):
        return WebMisc().clickable_element(driver, self.current_address_radio, "current_address_radio")

    def get_show_default(self, driver):
        return WebMisc().clickable_element(driver, self.show_default, "show_default")

    def get_show_satellite(self, driver):
        return WebMisc().clickable_element(driver, self.show_satellite, "show_satellite")

    def get_show_terrain(self, driver):
        return WebMisc().clickable_element(driver, self.show_terrain, "show_terrain")

    def get_yellow_banner(self, driver):
        return WebMisc().wait_element(driver, self.yellow_banner, "yellow_banner")

    def get_report_outage(self, driver):
        return WebMisc().clickable_element(driver, self.report_outage, "report_outage")

    def get_refresh_button(self, driver):
        return WebMisc().wait_element(driver, self.refresh_button, "refresh_button")

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

    def get_faq_header(self, driver):
        return WebMisc().clickable_element(driver, self.FAQ_header, "FAQ_header")

    def get_qrg_header(self, driver):
        return WebMisc().clickable_element(driver, self.QRG_header, "QRG_header")

    def get_hamburger_menu(self, driver):
        return WebMisc().clickable_element(driver, self.hamburger_menu, "hamburger_menu")

    def get_outage_pins_filter(self, driver):
        return WebMisc().clickable_element(driver, self.outage_pins_filter, "outage_pins_filter")

    def get_scheduled_interruption(self, driver):
        return WebMisc().clickable_element(driver, self.scheduled_interruption, "scheduled_interruption")

    def get_incident_type(self, driver):
        return WebMisc().clickable_element(driver, self.incident_type, "incident_type")

    def get_date_restoration(self, driver):
        return WebMisc().clickable_element(driver, self.date_restoration, "date_restoration")

    def get_affected_facility_type(self, driver):
        return WebMisc().clickable_element(driver, self.affected_facility_type, "affected_facility_type")

    def get_outage_load_shedding(self, driver):
        return WebMisc().clickable_element(driver, self.outage_load_shedding, "outage_load_shedding")

    def get_restoration_today(self, driver):
        return WebMisc().clickable_element(driver, self.restoration_today, "restoration_today")

    def get_type_no_device(self, driver):
        return WebMisc().clickable_element(driver, self.type_no_device, "type_no_device")

    def get_menu_affected_areas(self, driver):
        return WebMisc().clickable_element(driver, self.menu_affected_areas, "menu_affected_areas")

    def get_by_percentage(self, driver):
        return WebMisc().clickable_element(driver, self.by_percentage, "by_percentage")

    def get_by_count(self, driver):
        return WebMisc().clickable_element(driver, self.by_count, "by_count")

    def get_select_cluster(self, driver):
        return WebMisc().clickable_element(driver, self.select_cluster, "select_cluster")

    def get_affected_areas(self, driver):
        return WebMisc().clickable_element(driver, self.affected_areas, "affected_areas")

    def get_get_directions(self, driver):
        return WebMisc().clickable_element(driver, self.get_directions, "get_directions")

    def get_incident_status_history(self, driver):
        return WebMisc().clickable_element(driver, self.incident_status_history, "incident_status_history")

    def get_interruption_back(self, driver):
        return WebMisc().clickable_element(driver, self.interruption_back, "interruption_back")

    def get_calendar_show(self, driver):
        return WebMisc().clickable_element(driver, self.calendar_show, "calendar_show")

    def get_alert_modal(self, driver):
        return WebMisc().optional_clickable_element(driver, self.alert_modal, "alert_modal")

    def get_concern_reported_chk(self, driver):
        return WebMisc().optional_clickable_element(driver, self.concern_reported_chk, "concern_reported_chk")

    def get_concern_reported_filter(self, driver):
        return WebMisc().optional_clickable_element(driver, self.concern_reported_filter, "concern_reported_filter")

    def get_concern_type(self, driver):
        return WebMisc().optional_clickable_element(driver, self.concern_type, "concern_type")

    def get_case_status(self, driver):
        return WebMisc().optional_clickable_element(driver, self.case_status, "case_status")

    def get_reported_date(self, driver):
        return WebMisc().optional_clickable_element(driver, self.reported_date, "reported_date")

    def get_date_highlight(self, driver):
        return WebMisc().optional_clickable_element(driver, self.date_highlight, "date_highlight")

    def get_text_sector_office(self, driver):
        return WebMisc().optional_clickable_element(driver, self.text_sector_office, "text_sector_office")

    def get_text_vital_customers(self, driver):
        return WebMisc().optional_clickable_element(driver, self.text_vital_customers, "text_vital_customers")

    def get_text_election_centers(self, driver):
        return WebMisc().optional_clickable_element(driver, self.text_election_centers, "text_election_centers")

    def get_main_affected_facility(self, driver):
        return WebMisc().optional_clickable_element(driver, self.main_affected_facility, "main_affected_facility")
