from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://books-pwakit.appspot.com/")
# driver.maximize_window()
# shadow1 = driver.find_element(By.CSS_SELECTOR, 'book-app').shadow_root
#
# shadow1.find_element(By.ID, "input").send_keys("books1")
#
# sleep(10)

driver.get("chrome://settings/downloads")
driver.maximize_window()
shadow1=driver.find_element(By.CSS_SELECTOR, 'settings-ui').shadow_root
shadow2 = shadow1.find_element(By.CSS_SELECTOR,'settings-main#main').shadow_root
shadow3=shadow2.find_element(By.CSS_SELECTOR,'settings-basic-page.cr-centered-card-container').shadow_root
shadow4=shadow3.find_element(By.CSS_SELECTOR,'settings-downloads-page').shadow_root
shadow5=shadow4.find_element(By.CSS_SELECTOR,'settings-toggle-button.hr').shadow_root
shadow6=shadow5.find_element(By.CSS_SELECTOR,'cr-toggle#control').shadow_root

shadow6.find_element(By.CSS_SELECTOR,'span#bar').click()

sleep(10)

