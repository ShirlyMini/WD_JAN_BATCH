#//a[contains(text(),'Andrew Yule & Co')]/parent::td/parent::tr/parent::tbody/parent::table
#//a[contains(text(),'Andrew Yule & Co')]/ancestor-or-self::table/descendant-or-self::a[contains(text(),'Andrew Yule & Co')]

#find_element

from time import sleep

from selenium import webdriver
#############CHROME
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://money.rediff.com/gainers")
# driver.maximize_window()

# find elem
# locator matching single elem
# print(driver.find_element(By.XPATH, "//a[contains(text(),'Urja Global')]").text)
# locator matching multiple elem
# print(driver.find_element(By.XPATH, "//a[contains(text(),'Urja Global')]/parent::td/following-sibling::td").text)

# invalid locator
# print(driver.find_element(By.XPATH, "//a[contains(text(),'Urja ksmxl;ascmdsma')]").text)#NoSuchElementException: Message: no such element:

# find elems
# locator matching single elem
# list_elem = driver.find_elements(By.XPATH, "//a[contains(text(),'Urja Global')]")
# print(list_elem)
# for e in list_elem:
#     print(e.text)

# locator matching multiple elem

# list_elem = driver.find_elements(By.XPATH, "//a[contains(text(),'Urja Global')]/parent::td/following-sibling::td")
# for e in list_elem:
#     print(e.text)

# invalid locator
# print(driver.find_elements(By.XPATH, "//a[contains(text(),'Urja ksmxl;ascmdsma')]"))#[]

#########################################################################3
# driver.get("https://admin-demo.nopcommerce.com/login")
# driver.maximize_window()
#
# print(driver.find_element(By.ID, "Email").get_attribute("aria-describedby"))
# print(driver.find_element(By.ID, "Email").get_attribute("id"))
# print(driver.find_element(By.ID, "Email").text)# return empty
# print(driver.find_element(By.ID, "Email").get_attribute("value"))

driver.get("https://money.rediff.com/feedback")
driver.find_element(By.NAME, "username").send_keys("feedback name")
print(driver.find_element(By.NAME, "username").text)
print(driver.find_element(By.NAME, "username").get_attribute("value"))