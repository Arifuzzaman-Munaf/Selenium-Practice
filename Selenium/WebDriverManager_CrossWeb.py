# importing Necessary libraries for webdriver and automation
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


# installing Firefox driver manager for executing webdriver for further process
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(3)

# this is the page which will be automated for practice
driver.get('https://bux.bracu.ac.bd/login?next=%2F')

# showing the name of page
print(driver.title)

'''inputting the email and password for automating
# the webpage using firefox'''
