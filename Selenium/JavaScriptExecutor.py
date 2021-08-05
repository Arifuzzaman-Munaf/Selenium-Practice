
# importing necessary libraries for webdriver and automation
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

# installing firefox web driver for executing firefox browser
driver =  webdriver.Firefox(executable_path =GeckoDriverManager().install())


# navigating to amzon india
driver.get('https://www.amazon.in/')
print(driver.title)

# getting the link of mobiles tab from navigation menu
mobile = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[2]')

# executing to JavaScript console and navigating to mobile section
driver.execute_script("arguments[0].click()" , mobile)

time.sleep(2)

# refreshing the tab
driver.execute_script("history.go(0)")

time.sleep(1)

# creating an alert in page
# driver.execute_script("alert('Hello Guys')")


# printing all text in the page
all_text = driver.execute_script("return document.documentElement.innerText")
print(len(all_text))


# marking the Amazon-Pay tab using CSS property
amazon_pay = driver.find_element(By.CSS_SELECTOR, "#nav-xshop > a:nth-child(4)")
driver.execute_script("arguments[0].style.border = '3px solid red'", amazon_pay)