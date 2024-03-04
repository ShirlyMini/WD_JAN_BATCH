from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

act_obj = ActionChains(driver)
elem1=driver.find_element(By.XPATH, "//span[text()='Courses']")
act_obj.move_to_element(elem1).perform()

elem2=driver.find_element(By.XPATH, "//span[text()='For Working Professionals']")
act_obj.move_to_element(elem2).perform()

elem3=driver.find_element(By.XPATH, "//a[text()='Data Science Training Program']")
act_obj.move_to_element(elem3).click().perform()
print(driver.title)

sleep(10)