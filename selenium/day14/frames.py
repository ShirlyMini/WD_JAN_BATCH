from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

# driver.find_element(By.XPATH, "/html/frameset/frame[1]")

driver.switch_to.frame(driver.find_element(By.XPATH, "/html/frameset/frame[1]"))

driver.find_element(By.XPATH,"//form[@id='id1']/div/input").send_keys("Frame1")
print(driver.find_element(By.XPATH,"//form[@id='id1']/div").text)

driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "/html/frameset/frameset/frame[1]"))

driver.find_element(By.XPATH,"//form[@id='id2']/div/input").send_keys("Frame2")
print(driver.find_element(By.XPATH,"//form[@id='id2']/div").text)

sleep(10)