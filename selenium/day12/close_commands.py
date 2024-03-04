from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)# lauch
#########################is_enabled()###############33
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Explore Community']").click()
driver.find_element(By.XPATH, "//span[text()='Explore Community']").click()
driver.find_element(By.XPATH, "//span[text()='Explore Community']").click()
sleep(3)
# driver.close()
# driver.quit()
sleep(10)