#####################################################3
# CSS(fast)

# id
# #value of id (or) tagname#valueofid
# class
# .value of class (or)tagname.valueofclass
# atrr
# [attr=value] or tagname[attr=value]


from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.CSS_SELECTOR,"input#Email").clear()
driver.find_element(By.CSS_SELECTOR,"#Email").send_keys("admin@yourstore.com")
driver.find_element(By.CSS_SELECTOR,"input.password").clear()
driver.find_element(By.CSS_SELECTOR,".password").send_keys("admin")

driver.find_element(By.CSS_SELECTOR,"#RememberMe").click()

driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()



