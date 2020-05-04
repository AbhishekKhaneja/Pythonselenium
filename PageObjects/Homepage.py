import pytest
from selenium.webdriver.common.by import By

from PageObjects.checkoutpage import checkoutpage
from Testdata.HomePage_TestData import HomepageData
from Utilities.Baseclass import Baseclass


class HomePage(Baseclass):

    shop = (By.XPATH,"//a[@href='/angularpractice/shop']")
    name =(By.NAME,"name")
    email =(By.NAME,"email")
    checkbox =(By.XPATH,"//input[@id='exampleCheck1']")
    dropdown = (By.XPATH,"//select[@id='exampleFormControlSelect1']")
    submitbutton = (By.XPATH,"//input[@class='btn btn-success']")


    def __init__(self,driver):
        self.driver = driver

   # self.driver.find_element_by_xpath("//a[@href='/angularpractice/shop']").click()
    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = checkoutpage(self.driver)
        return checkoutPage


    def formSubmission(self, getdata):
        self.driver.find_element(*HomePage.name).send_keys(getdata["Firstname"])
        self.driver.find_element(*HomePage.email).send_keys(getdata["Email"])
        self.driver.find_element(*HomePage.checkbox).click()
        self.SelectdropDown(HomePage.dropdown, getdata["Gender"])
        self.driver.find_element(*HomePage.submitbutton).click()
        self.driver.refresh();

