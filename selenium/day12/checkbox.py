from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").clear()
driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").send_keys("admin@yourstore.com")

driver.find_element(By.XPATH, "//input[@type='password']").clear()
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin")

driver.find_element(By.XPATH, "//*[text()='Log in']").click()

print(driver.find_element(By.XPATH, "//img[@class='brand-image-xl logo-xl']").is_displayed())


#//tbody/tr/td[1]
#//ul[@role='menu']/li/a/p[contains(text(),'Customers')]

#//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Customers')]

driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Customers')]").click()
list_elem = driver.find_elements(By.XPATH, "//tbody/tr/td[1]/input")

for elem in list_elem:
    elem.click()
    print(elem.is_selected())


#hands-on
#https://www.facebook.com/signup
# //label[text()='Custom']/following-sibling::input