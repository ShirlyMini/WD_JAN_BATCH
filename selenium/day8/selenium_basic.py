from time import sleep

from selenium import webdriver
#############CHROME
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)# browser launch
# driver = webdriver.Chrome()# browser launch
#############EDGE
# from selenium.webdriver.edge.service import Service
# service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)

#############FIREFOX
# from selenium.webdriver.firefox.service import Service
#
# service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# application
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.minimize_window()
driver.refresh()
driver.forward()
driver.back()
sleep(10)
