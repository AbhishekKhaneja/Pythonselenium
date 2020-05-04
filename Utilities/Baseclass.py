import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:


    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 6)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectdropDown(self,xpath,visibleText):
        dropDown=Select(self.driver.find_element(*xpath))
        dropDown.select_by_visible_text(visibleText)
        #dropDown.select_by_index(0)


    def getlogger(self):
        loggerName= inspect.stack()[1][3] # here it is used to get logs from where the execution is being called not from the baseclass in thsi particular scenario
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.log') #defining in which file the logs has been reported
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s") # defining the format
        filehandler.setFormatter(formatter) #make a connection between findhandler and the formatter
        logger.addHandler(filehandler) #findhandler object # since logger is the object and filehandler knows about the log file details

        logger.setLevel(logging.DEBUG)
        #logger.debug("A debug statement is executed")
        #logger.info("Information Statement")
        #logger.warning("Something is in warning mode")
        #logger.error("A error has occured")
        #logger.critical("A critical issue is reported")
        return logger

