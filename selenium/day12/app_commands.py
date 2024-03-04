from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)# lauch

driver.get("https://admin-demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)

