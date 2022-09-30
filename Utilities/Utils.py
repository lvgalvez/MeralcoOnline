import inspect
import logging

from selenium.webdriver import ActionChains

from Utilities.Config import *

class Utilities():
    def getlogger(self):
        # set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # create Logger
        logger = logging.getLogger(logger_name)
        # create console handler or file handler and set the log level
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(f'{root_dir.parent}' + "\\Logs\\automaton_" + stamp + ".log")
        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')
        # add formatter to file handler
        fh.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(fh)

        return logger

    def mouse_hover(self, driver, element, elementname):
        action = ActionChains(driver)
        if elementname == None:
            move = element(driver)
        else:
            move = element(driver, elementname)
        action.move_to_element(move).perform()

    def mouse_hover_click(self,driver,element,elementname):
        action = ActionChains(driver)
        if elementname == None:
            move = element(driver)
        else:
            move = element(driver, elementname)
        action.move_to_element(move).click(move).perform()


        # mouse hover on dresses
        #a = ActionChains(self.driver)
        #m = catalog.hover_category(self.driver, category_dresses[counter])
        #a.move_to_element(m).perform()

        # mouse hover and click evening dress
        #e = catalog.get_sub_cat(self.driver, category_evedress[counter])
        #a.move_to_element(e).click().perform()



