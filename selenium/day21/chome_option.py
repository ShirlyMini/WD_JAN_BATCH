from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as ff_service
from selenium.webdriver.common.by import By
#https://peter.sh/experiments/chromium-command-line-switches/
###########################chrome
# chrome_ops = webdriver.ChromeOptions()
# # chrome_ops.add_argument("--headless")
# # chrome_ops.add_argument("--incognito")
# chrome_ops.add_argument("--start-maximized")
#
# chrome_ops.add_extension(r"E:\selenium\drivers\ljngjbnaijcbncmcnjfhigebomdlkcjo-6.1.12-Crx4Chrome.com.crx")
#
#
# service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj, options=chrome_ops)#open brow

###########################################firefox
firefox_ops = webdriver.FirefoxOptions()

# service_obj = ff_service(r"E:\selenium\drivers\geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj, options=firefox_ops)#open brow
driver = webdriver.Firefox()
driver.install_addon(r"E:\selenium\drivers\ljngjbnaijcbncmcnjfhigebomdlkcjo-6.1.12-Crx4Chrome.com.crx")
# driver.get("https://www.foundit.in/")
# # driver.maximize_window()
# sleep(7)
# driver.find_element(By.XPATH,"//div[contains(text(),'Upload Resume')]").click()
#
#
# file_path = r'C:\Users\user\PycharmProjects\pythonProject_WD_eve_jan2024\selenium\day20\samplefile.pdf'
# driver.find_element(By.ID,"file-upload").send_keys(file_path)
# print(driver.find_element(By.XPATH,"//input[@id='pop_upload']").is_enabled())# true
#
# sleep(10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()


driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

alt_ref = driver.switch_to.alert
print(alt_ref.text)# get msg from alrt
alt_ref.accept()