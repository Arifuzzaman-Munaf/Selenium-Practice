# importing Necessary libraries for webdriver and automation
from selenium.webdriver.common.by import By
import time , pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains

# Declaring a global driver variable
driver = None


def setup(module):
    global driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")


def teardown_module(module):
    global driver
    driver.quit()


def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == "http://www.google.com"
