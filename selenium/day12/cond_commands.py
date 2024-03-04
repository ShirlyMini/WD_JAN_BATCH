from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)# lauch
#########################is_enabled()###############33
# driver.get("https://www.linkedin.com/learning-login/")
#
# status = driver.find_element(By.ID, "auth-id-button").is_enabled()#false
# if status==False:
#     driver.find_element(By.ID, "auth-id-input").send_keys("abc@gmail.com")
#     if driver.find_element(By.ID, "auth-id-button").is_enabled():
#         print("button is enabled")
# sleep(10)

#########################is_displayed###############
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").clear()
# driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").send_keys("admin@yourstore.com")
#
# driver.find_element(By.XPATH, "//input[@type='password']").clear()
# driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin")
#
# driver.find_element(By.XPATH, "//*[text()='Log in']").click()
#
# print(driver.find_element(By.XPATH, "//img[@class='brand-image-xl logo-xl']").is_displayed())
# sleep(10)

##########################is_selected()###################
# works only for inputtag

# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
#
# print(driver.find_element(By.ID, "RememberMe").is_selected())# false
# driver.find_element(By.ID, "RememberMe").click()
# print(driver.find_element(By.ID, "RememberMe").is_selected())# true

############################################################33
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
sleep(10)
driver.find_element(By.XPATH, '//li[contains(text(),"Round Trip")]').click()
print(driver.find_element(By.XPATH, '//li[contains(text(),"Round Trip")]').is_selected())
sleep(10)