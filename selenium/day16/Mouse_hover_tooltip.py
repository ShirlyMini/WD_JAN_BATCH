from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demoqa.com/tool-tips")
driver.maximize_window()

act_obj = ActionChains(driver)

button_elem = driver.find_element(By.ID, 'toolTipButton')
act_obj.move_to_element(button_elem).perform()
sleep(2)
print(driver.find_element(By.XPATH, "//div[@id='buttonToolTip']/div[@class='tooltip-inner']").text)


text_elem = driver.find_element(By.ID, 'toolTipTextField')
act_obj.move_to_element(text_elem).perform()
sleep(2)
print(driver.find_element(By.XPATH, "//div[@id='textFieldToolTip']/div[@class='tooltip-inner']").text)
sleep(5)