from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# driver.maximize_window()
#
# print(driver.execute_script("return window.pageXOffset;"))
# print(driver.execute_script("return window.pageYOffset;"))
#
# # scroll to bottom
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#
# print(driver.execute_script("return window.pageXOffset;"))
# print(driver.execute_script("return window.pageYOffset;"))
#
# # scroll to top
# driver.execute_script("window.scrollTo(0,0);")
#
# print(driver.execute_script("return window.pageXOffset;"))
# print(driver.execute_script("return window.pageYOffset;"))
#
# # scroll to element
#
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# print(flag)
# driver.execute_script("arguments[0].scrollIntoView();",flag)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

email_elem =driver.find_element(By.ID,'Email')
driver.execute_script("arguments[0].value='';",email_elem)
driver.execute_script("arguments[0].value='admin@yourstore.com';",email_elem)

pswd_elem = driver.find_element(By.ID,'Password')
driver.execute_script("arguments[0].value='';",pswd_elem)
driver.execute_script("arguments[0].value='admin';",pswd_elem)

submit_elem  =driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]")
driver.execute_script("arguments[0].click();",submit_elem)

sleep(10)
