from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.myntra.com/tops")
driver.maximize_window()

print(driver.window_handles)
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[1]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[2]").click()
driver.find_element(By.XPATH, "//ul[@class='results-base']/li[3]").click()
print(driver.window_handles)#[parent, child]

print(driver.title)
for handle in driver.window_handles[1:]:
    driver.switch_to.window(handle)
    print(driver.title)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)