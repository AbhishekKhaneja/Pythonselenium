from selenium.webdriver.common.by import By

from PageObjects.confirmPage import ConfirmPage


class checkoutpage():
    allproducts = (By.CSS_SELECTOR, ".card-title a")
    allbuttons = (By.XPATH, "//div[@class='card-footer']/button")
    checkoutButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def __init__(self,driver):
        self.driver = driver

    def allproductss(self):
        return self.driver.find_elements(*checkoutpage.allproducts)
    def allbuttonss(self):
        return self.driver.find_elements(*checkoutpage.allbuttons)
    def CheckoutButton(self):
        self.driver.find_element(*checkoutpage.checkoutButton).click()
        confirmPage=ConfirmPage(self.driver)
        return confirmPage





