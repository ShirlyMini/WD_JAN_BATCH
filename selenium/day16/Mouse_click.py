from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

act_obj = ActionChains(driver)
######right click
# act_obj.context_click(driver.find_element(By.XPATH, "//span[text()='right click me']")).perform()
# act_obj.move_to_element(driver.find_element(By.XPATH, "//ul[@class='context-menu-list context-menu-root']/li[2]/span")).click().perform()
# sleep(2)
# alt_obj = driver.switch_to.alert
# print(alt_obj.text)
# alt_obj.accept()
# sleep(5)
##########double click

act_obj.double_click(driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")).perform()
sleep(2)
alt_obj = driver.switch_to.alert
print(alt_obj.text)
alt_obj.accept()
sleep(5)