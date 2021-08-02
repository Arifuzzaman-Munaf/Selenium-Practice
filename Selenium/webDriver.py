from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox(executable_path = "F:\\Practice Codes\\geckodriver.exe")
driver.implicitly_wait(1)
driver.get("http://www.google.com")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys('Django')
options = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li div.wM6W7d span')

for i in options:
    print(i.text)
    if i.text == "django channels" :
        i.click()
        break

time.sleep(3)
driver.quit()