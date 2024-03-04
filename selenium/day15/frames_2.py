from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

driver.switch_to.frame(driver.find_element(By.XPATH, "/html/frameset/frameset/frame[2]"))
driver.find_element(By.XPATH, "//form[@id='id3']/div/input").send_keys("Frame3")
print(driver.find_element(By.XPATH, "//form[@id='id3']/div").text)

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
driver.find_element(By.XPATH, "//div[@id='i5']/div[3]").click()
# print(driver.find_element(By.XPATH, "//div[text()='Form Filling Demo Page']").is_displayed())

driver.switch_to.parent_frame()
driver.find_element(By.XPATH, "//form[@id='id3']/div/input").clear()
driver.find_element(By.XPATH, "//form[@id='id3']/div/input").send_keys("parent Frame3")
print(driver.find_element(By.XPATH, "//form[@id='id3']/div").text)

driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "/html/frameset/frameset/frame[3]"))
driver.find_element(By.XPATH, "//form[@id='id4']/div/input").send_keys("Frame4")
print(driver.find_element(By.XPATH, "//form[@id='id4']/div").text)
sleep(10)