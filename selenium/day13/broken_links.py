from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.deadlinkcity.com/")
driver.implicitly_wait(10)
driver.maximize_window()

list_we_links=driver.find_elements(By.XPATH, "//a")

for we_link in list_we_links:
    url = we_link.get_attribute("href")
    # print(url)
    try:
        return_status = requests.get(url)
        print(return_status.status_code)
        if int(return_status.status_code)>299:
            print(f"{url} - invalid")
        else:
            print(f"{url} - valid")
    except Exception as msg:
        print(f"{url} - invalid {msg}")


###########################################333
# request
# get# post# put[edit]#delete
