import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#@pytest.mark.usefixtures("setup") if you check this fixture has scope at class level do it will work fine also
#insted of using this fixture here we will define this in the baseclass of utilities package and then inherit that class
from PageObjects.Homepage import HomePage
from PageObjects.checkoutpage import checkoutpage
from Utilities.Baseclass import Baseclass


class TestOne(Baseclass):

    def test_e2e(self):
        log = self.getlogger()
        homepageobj= HomePage(self.driver)
        checkoutpageobj=homepageobj.shopitems()
        log.info("Getting all the Products")

        Allproducts = checkoutpageobj.allproductss()
        i =-1
        for product in Allproducts:
            log.info(product.text)
            i = i+1
            if product.text == "Blackberry":
                checkoutpageobj.allbuttonss()[i].click()

        ConfirmPageobj=checkoutpageobj.CheckoutButton()
        ConfirmPageobj.checkbutton().click()
        log.info("Entering Country name as IND")
        ConfirmPageobj.Countrypopup().send_keys("ind")
        self.verifyLinkPresence("India")
        ConfirmPageobj.CountrySelection().click()
        ConfirmPageobj.Checkboxselection().click()

        assert ConfirmPageobj.checkBoxassertion().is_selected()
        ConfirmPageobj.purchaseButton().click()
        SuccessMessage=self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

        log.info(SuccessMessage)
        assert "Mesaage" in SuccessMessage

        self.driver.get_screenshot_as_file("Screen.PNG") #taking screenshot


