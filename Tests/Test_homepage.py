import pytest

from PageObjects.Homepage import HomePage
from Testdata.HomePage_TestData import HomepageData
from Utilities.Baseclass import Baseclass

@pytest.mark.usefixtures("getdata")
class TestHomepage(Baseclass):

    def test_homepage(self,getdata):
        log = self.getlogger()
        homepageobj=HomePage(self.driver)
        homepageobj.formSubmission(getdata)
        log.info("Firstname is " +getdata["Firstname"])

    @pytest.fixture(params=HomepageData.TestHomePagedata)
    def getdata(self, request):
        return request.param






