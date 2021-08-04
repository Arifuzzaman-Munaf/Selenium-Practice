from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select


# installing Firefox driver manager for executing webdriver for further process
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(3)


# Visiting the webpage mentioned in the URL
driver.get("https://evaly.com.bd/")

# print the title of page
print(driver.title)

# Removing the pop-up advertising image for further access
driver.find_element(By.CSS_SELECTOR, 'button.absolute.top-0.right-0.p-2.text-black svg path').click()

time.sleep(1)

# clicking the menu for sign in
driver.find_element(By.CSS_SELECTOR, 'button.flex.items-center span.flex.w-full.items-center svg').click()

# Providing number and password to sign in
mobile = driver.find_element(By.XPATH, '//input[@title="Phone number should be 11 digit number"]')
password = driver.find_element(By.XPATH, '//input[@name = "password"]')
# sending mobile number and password through keys
mobile.send_keys('Use your registered number')
time.sleep(1)
password.send_keys('your password')


time.sleep(1)
# clicking the login button for authentication
login_button = driver.find_element(By.CSS_SELECTOR, 'form div.text-center button.Button__ButtonStyle-vbsn2i-0')
login_button.click()


time.sleep(1)

# clicking on speakers from categories
speakers = driver.find_element(By.XPATH, "//a[@href='/categories/speaker-2f615cf9a']")
speakers.click()

time.sleep(1)

# fetching all the brands' name situated in categories page
brands = driver.find_elements(By.CSS_SELECTOR, 'div.w-full.my-4 a div p')

# print the bands' name
print(f"total brands = {len(brands)} \nPrinting all the brands")
selected_brand = "MI"
for _, i in enumerate(brands):
    if i.text == selected_brand :
        selected_brand = driver.find_element(By.XPATH, "//a[@href ='/brands/xiaomi-004a023b8?category=speaker-2f615cf9a']")
    print(f"{_+1}. {i.text}")

# selecting a specific brand
selected_brand.click()


# initializing a dictionary to keep the track of product's links and prices
link_price ={}

# fetching the links and prices
links = driver.find_elements(By.CSS_SELECTOR, "div.container.m-auto a")
prices = driver.find_elements(By.CSS_SELECTOR, "div.container.m-auto a div.p-4.pt-0 p.Card___StyledP2-sc-1629dl9-1") + \
         driver.find_elements(By.CSS_SELECTOR, "div.container.m-auto a div.p-4.pt-0 p.Card___StyledP3-sc-1629dl9-2.bzqEqm")

# assigning values to the dictionary : key as links and values as prices
for i in range(len(links)):
    link_price[links[i].get_attribute('href')] = int((prices[i].text).replace("৳",""))

# sorting the items according to price
link_price = dict(sorted(link_price.items(), key=lambda item: item[1]))

time.sleep(1)

# travelling to the page where we get the pruduct with highest price
selected_link = list(link_price.keys())[-1]
driver.get(selected_link)

# printing the product name along with price
name = driver.find_element(By.CSS_SELECTOR,"h2.font-bold.text-gray-700")
price = f"৳ {link_price[selected_link]}"

print("\nThe product with highest price")
print(f"{name.text} ==> which will cost {price}")


time.sleep(1)

# navigating to career page
driver.get('https://evaly.com.bd/career')


# expanding all departments
departments = driver.find_elements(By.CSS_SELECTOR, "div.flex-1.my-8.mr-10 div.flex.items-center.justify-between.px-4.py-3.mb-4.bg-gray-200.cursor-pointer")

for i in departments:
    driver.execute_script("arguments[0].click();", i)


# checking all emails located in svg contains @evaly.com or not
emails = driver.find_elements(By.CSS_SELECTOR, "div.flex.flex-col-reverse.md\:flex-row a")

for i in emails :
    if not "@evaly.com" in i.get_attribute('href') :
        print("A email contains an email without having '@evaly.com' ")
        break
    print("This email is ok")


