import pytest
from selenium import webdriver

#setting up command line options to invoke different browser
#command used-->>pytest --browser_name firefox
#use this link to read more:  https://docs.pytest.org/en/latest/example/simple.html
driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":

        driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\abhkhane\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "ie":
        driver = webdriver.Ie(executable_path="C:\\Users\\abhkhane\\Downloads\\IEDriverServer_x64_3.6.0\\IEDriverServer.exe")
        driver.get("https://rahulshettyacademy.com/")
        #driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)




