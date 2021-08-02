
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('http://www.youtube.com')