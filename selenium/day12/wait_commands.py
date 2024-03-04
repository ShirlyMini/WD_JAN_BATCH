# imp
# exp
# sleep- hard
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
# driver.implicitly_wait(10)
wait_obj = WebDriverWait(driver, 10, 3, ignored_exceptions=[NoSuchElementException, TimeoutException])

wait_obj.until(expected_conditions.presence_of_element_located((By.XPATH, '//li[contains(text(),"Round Trip")]')))
driver.find_element(By.XPATH, '//li[contains(text(),"Round Trip")]').click()
print(driver.find_element(By.XPATH, '//li[contains(text(),"Round Trip")]').is_selected())
driver.find_element(By.XPATH, '//li[contains(text(),"Multi City")]').click()
print(driver.find_element(By.XPATH, '//li[contains(text(),"Multi City")]').is_selected())
