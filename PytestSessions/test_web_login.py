# importing Necessary libraries for webdriver and automation
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


# installing Firefox driver manager for executing webdriver for further process
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def test_github():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(3)

    # this is the page which will be automated for practice
    driver.get('https://github.com/')

    assert driver.title == "GitHub: Where the world builds software · GitHub"
    driver.quit()


def test_facebook():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(3)

    # this is the page which will be automated for practice
    driver.get('https://www.facebook.com/')

    assert driver.title == "Facebook – log in or sign up"
    driver.quit()


def test_google():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(3)

    # this is the page which will be automated for practice
    driver.get('https://www.google.com')
    assert driver.title == "Google"
    driver.quit()


def test_instragram():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(3)

    # this is the page which will be automated for practice
    driver.get('https://www.instagram.com/')

    assert driver.title == "Instagram"
    driver.quit()