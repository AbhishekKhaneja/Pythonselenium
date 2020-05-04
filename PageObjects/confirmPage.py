from selenium.webdriver.common.by import By


class ConfirmPage:

   def __init__(self, driver):
      self.driver = driver

   checkoutbutton =(By.CSS_SELECTOR,"button[class='btn btn-success']")
   countrypopup =(By.ID,"country")
   countryselection=(By.LINK_TEXT,"India")
   checkboxSelection=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
   purchasebutton=(By.XPATH,"//input[@class='btn btn-success btn-lg']")
   Checkbox=(By.XPATH,"//input[@id='checkbox2']")

   def checkbutton(self):
      return self.driver.find_element(*ConfirmPage.checkoutbutton)

   def Countrypopup(self):
      return self.driver.find_element(*ConfirmPage.countrypopup)

   def CountrySelection(self):
      return self.driver.find_element(*ConfirmPage.countryselection)

   def Checkboxselection(self):
      return self.driver.find_element(*ConfirmPage.checkboxSelection)

   def purchaseButton(self):
      return self.driver.find_element(*ConfirmPage.purchasebutton)

   def checkBoxassertion(self):
      return self.driver.find_element(*ConfirmPage.Checkbox)