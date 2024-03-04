from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#//table/tbody/tr/td/a[contains(text(),'Signpost India')]/parent::td/following-sibling::td
service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
# to fetch row
# row_data = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[1]/td")
# row_data = driver.find_elements(By.XPATH,"//table/tbody/tr/td/a[contains(text(),'Signpost India')]/parent::td/following-sibling::td")
# for i in row_data:
#     print(i.text)

# to fetch col
# col_data = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr/td[1]")# company
# for i in col_data:
#     print(i.text)

#to fetch all row and col

elm_list = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr")

for i in range(1,len(elm_list)+1):# rows
    data_elem = driver.find_elements(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{i}]/td")
    print(data_elem[1].text)
    if data_elem[1].text == 'B':
        for i in data_elem:
            print(i.text,end="\t")
    print("\n")


