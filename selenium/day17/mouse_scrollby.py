from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

act_obj = ActionChains(driver)

flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
print(flag.location)
# act_obj.scroll_to_element(flag).perform()
# act_obj.scroll_by_amount(flag.location['x'], flag.location['y']).perform()
scroll_origin = ScrollOrigin.from_element(flag)
sleep(2)
act_obj.scroll_from_origin(scroll_origin, 0,1000).perform()
sleep(10)