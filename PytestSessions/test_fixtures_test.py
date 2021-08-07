# importing Necessary libraries for webdriver and automation
from selenium.webdriver.common.by import By
import time , pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains

# Declaring a global driver variable
driver = None

# decorator to set all the driver and termination
@pytest.fixture(scope='module')
def setup():
    global driver
    print("__________________________setup________________________")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    # yield helps to execute the test cases
    # the commands after "yield" keyword executes after all the test methods terminates
    yield
    driver.quit()


def test_google_title(setup):
    assert driver.title == "Google"


def test_google_url(setup):
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
