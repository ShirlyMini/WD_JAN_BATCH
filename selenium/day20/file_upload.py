from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.foundit.in/")

driver.maximize_window()
driver.find_element(By.XPATH,"//div[contains(text(),'Upload Resume')]").click()
sleep(7)
print(driver.find_element(By.XPATH,"//span[@class='action-cta']").is_enabled())# false
file_path = r'C:\Users\user\PycharmProjects\pythonProject_WD_eve_jan2024\selenium\day20\samplefile.pdf'
driver.find_element(By.ID,"file-upload").send_keys(file_path)
print(driver.find_element(By.XPATH,"//span[@class='action-cta']").is_enabled())# true

sleep(10)


