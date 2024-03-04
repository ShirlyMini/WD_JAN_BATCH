from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
##############################JS Alerts
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()

# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
#
# alt_ref = driver.switch_to.alert
# print(alt_ref.text)# get msg from alrt
# alt_ref.accept()

# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# alt_ref = driver.switch_to.alert
# print(alt_ref.text)# get msg from alrt
# # alt_ref.accept()
# alt_ref.dismiss()
#
# driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# alt_ref = driver.switch_to.alert
# print(alt_ref.text)# get msg from alrt
# alt_ref.send_keys("welcome")
# alt_ref.accept()
#
#
# print(driver.find_element(By.ID, "result").text)

##############################Authentication Popup

# driver.get("https://the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
# alt_ref = driver.switch_to.alert
# alt_ref.send_keys("admin")
# alt_ref.send_keys("admin")
# alt_ref.accept()

###url
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
#
# sleep(10)

###autoit(third party tool)
##################Intsalll pyautoit
# import autoit
#
# driver.get("https://the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
#
# autoit.win_wait_active("", 30)
# autoit.send("admin{TAB}admin{TAB}{ENTER}")
#
# sleep(10)


##############################Notification--Browser
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification")

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://whatmylocation.com/")
driver.maximize_window()

sleep(10)

