import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=".\\drivers\\chromedriver.exe")
        Name = driver.capabilities['browserName']
        print(Name)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=".\\drivers\\geckodriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    global Name
    config._metadata['Project Name'] = 'pytest-web-report'
    config._metadata['Tester'] = 'Hien Pham'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
