from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select

# installing Firefox driver manager for executing webdriver for further process
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(2)

# Visiting the webpage mentioned in the URL
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

# print the title of page
print(driver.title)

# getting the dropdown values
elements = driver.find_element(By.ID, 'Form_submitForm_Industry')


# selecting a specific option
select = Select(elements)

# showing all the options in Undustries
options = select.options
for i in options :
    print(i.text)


# select by text options
select.select_by_visible_text('Education')
time.sleep(1)

# select by index of options
select.select_by_index(3)

time.sleep(1)

# select by value attribute
select.select_by_value('Government-Local')

# confirming as we can select single option or multiple options
print(select.is_multiple)


time.sleep(1)
# deselecting all to clear the selection
# only works for multi select
# select.deselect_all()

# Showing all the process without SELECT
opt = driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Industry']/option")
for i in opt:
    if i.text == "Education" :
        i.click()
        break