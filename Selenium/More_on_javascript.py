# importing necessary libraries for webdriver and automation
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

# installing firefox web driver for executing firefox browser
driver =  webdriver.Firefox(executable_path =GeckoDriverManager().install())

# navigating to facebook
# driver.get('https://www.facebook.com')


# retrieving the form locator
# form = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]")
# driver.execute_script("arguments[0].style.border = '2px solid green'" , form)

# navigating to amzon india
driver.get('https://www.amazon.in/')
print(driver.title)

# scrolling the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")