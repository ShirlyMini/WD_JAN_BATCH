#xpath
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")

# abs - /
# email_input_elem=driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input")
# email_input_elem.clear()
# email_input_elem.send_keys("admin@yourstore.com")
# password_input_elem=driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input")
# password_input_elem.clear()
# password_input_elem.send_keys("admin")
#
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# sleep(10)


# relative -//

#//tag[@attr="value"]
#//*[@attr="value"]

# //tag[text()="value"]
#//*[text()="value"]


driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").clear()
driver.find_element(By.XPATH, "//input[@data-val-email='Wrong email']").send_keys("admin@yourstore.com")

driver.find_element(By.XPATH, "//input[@type='password']").clear()
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin")

driver.find_element(By.XPATH, "//*[contains(text(), 'Remember me?')]").click()
# driver.find_element(By.XPATH, "//*[@type='submit']").click()
driver.find_element(By.XPATH, "//*[text()='Log in']").click()
sleep(10)
