from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://demoqa.com/auto-complete")
# driver.maximize_window()
#
# act_obj = ActionChains(driver)
# elem1=driver.find_element(By.XPATH,"//div[@id='autoCompleteMultiple']/div/div/div[1]")
# elem1=driver.find_element(By.XPATH,"//input[@id='autoCompleteMultipleInput']")
# elem1.send_keys("a")
# sleep(3)
# suggestions_list = driver.find_elements(By.XPATH,"//div[@class='auto-complete__menu css-26l3qy-menu']/div/div")
# for suggestion in suggestions_list:
#     if suggestion.text == "Aqua":
#         act_obj.scroll_to_element(suggestion).perform()
#         suggestion.click()
# elem1.send_keys(Keys.ENTER)
# elem1.send_keys("b")
# elem1.send_keys(Keys.ENTER)

#######################################without autosuggestion locator
# driver.get("https://jqueryui.com/autocomplete/")
# driver.maximize_window()
#
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
# driver.find_element(By.ID,'tags').send_keys("a")
# sleep(2)
# # while True:
# for _ in range(20):
#
#     driver.find_element(By.ID,'tags').send_keys(Keys.ARROW_DOWN)
#     if driver.find_element(By.ID,'tags').get_attribute("value") == "Java":
#         driver.find_element(By.ID,'tags').send_keys(Keys.ENTER)
#         break

#################################33multiple keys
driver.get("https://money.rediff.com/feedback")
driver.maximize_window()
act_obj = ActionChains(driver)
driver.find_element(By.NAME, 'username').send_keys("abc@gmail.com")
# ctrl +a and ctrl+c

# act_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# act_obj.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act_obj.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()
act_obj.send_keys(Keys.TAB).perform()
#ctrl+V
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

act_obj.send_keys(Keys.TAB).perform()
#ctrl+V
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

act_obj.send_keys(Keys.TAB).perform()
#ctrl+V
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


sleep(10)