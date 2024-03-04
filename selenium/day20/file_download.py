from time import sleep
import os

import autoit
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
loc = os.getcwd()
print(loc)
###########################chrome
# chrome_ops = webdriver.ChromeOptions()
# preferences = {"download.default_directory":loc}
# chrome_ops.add_experimental_option("prefs", preferences)
#
# service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj, options=chrome_ops)#open brow

###########################edge
# edge_ops = webdriver.EdgeOptions()
# preferences = {"download.default_directory":loc}
# edge_ops.add_experimental_option("prefs", preferences)
#
# service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj, options=edge_ops)#open brow

###################################ff

firefox_ops = webdriver.FirefoxOptions()

firefox_ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")#/msword,/txt,/pdf
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
firefox_ops.set_preference("bowser.download.manager.showWhenStarting",False)
firefox_ops.set_preference("browser.download.folderList",2)#0-desktop,1-downloadfolder,2-desiredloc
firefox_ops.set_preference("browser.download.dir",loc)# only the folder list is 2
# firefox_ops.set_preference("extention")
service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj, options=firefox_ops)#open brow
driver = webdriver.Firefox()#open brow

driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
sleep(5)
driver.find_element(By.XPATH,"//button[@id='download']").click()
sleep(2)
# autoit.win_wait_active("", 30)
autoit.send(loc+r"\test_file_name.pdf")
sleep(2)
autoit.send("{Enter}")
sleep(10)
driver.quit()

