from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://admin-demo.nopcommerce.com/")
# driver.implicitly_wait(10)
# driver.maximize_window()
#
#
# #######################Login
# driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").clear()
# driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").send_keys("admin@yourstore.com")
#
# driver.find_element(By.XPATH, "//input[@type='password']").clear()
# driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin")
#
# driver.find_element(By.XPATH, "//*[text()='Log in']").click()
#
# print(driver.find_element(By.XPATH, "//img[@class='brand-image-xl logo-xl']").is_displayed())
# ########################
#
# driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Promotions')]").click()
# list_options = driver.find_elements(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Promotions')]/ancestor::li/ul/li")
#
# for option in list_options:
#     if option.text == "Discounts":
#         option.click()
#         break
# print(driver.find_element(By.XPATH, "//h1[contains(text(), 'Discounts')]").is_displayed())



# Select
#from selenium.webdriver.support.select import Select

driver.get("https://www.facebook.com/signup")
driver.implicitly_wait(10)
driver.maximize_window()

# driver.find_element(By.NAME, "birthday_day")#---webelem
drp_down_day = Select(driver.find_element(By.NAME, "birthday_day"))
drp_down_day.select_by_visible_text("15")

drp_down_month = Select(driver.find_element(By.NAME, "birthday_month"))
drp_down_month.select_by_value("10")

drp_down_year = Select(driver.find_element(By.NAME, "birthday_year"))
drp_down_year.select_by_index(0)# 0 to n-1
sleep(1)
drp_down_year.select_by_index(1)# 0 to n-1
sleep(1)
drp_down_year.select_by_index(5)# 0 to n-1
sleep(1)
drp_down_year.select_by_index(10)# 0 to n-1

sleep(10)