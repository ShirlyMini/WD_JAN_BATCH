from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.facebook.com/")

##################################################
# ID

# driver.find_element(By.ID, "email").send_keys("abc@gmail.com")
# driver.find_element(By.ID, "pass").send_keys("123456")

################################################
# tag
# print(driver.find_element(By.TAG_NAME, "h2").text)


##################################################
# name
# driver.find_element(By.NAME, "login").click()
# driver.find_element(By.TAG_NAME, "button").click()
# sleep(10)
#######################################
# linktext or partial link text# <a>

# driver.find_element(By.LINK_TEXT, "Forgotten password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten").click()

####################################################33
# classname

# _42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy

driver.find_element(By.CLASS_NAME, "_4jy2").click()
sleep(10)