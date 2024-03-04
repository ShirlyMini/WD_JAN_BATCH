from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
t1 = datetime.datetime.now()
# t1 = datetime.datetime(2025, 6,22,6,2,40)
##year month date time min sec millisec
date_1 = t1.strftime("%m/%d/%Y")


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()

# driver.find_element(By.ID, 'datepicker2').send_keys(date_1)
# sleep(3)
# driver.find_element(By.XPATH, "//a[text()='Close']").click()
#################datepicker disabled
driver.find_element(By.ID, 'datepicker1').click()
sleep(3)
# prev_elem = driver.find_element(By.XPATH, "//a[@title='Prev']")
# next_elem = driver.find_element(By.XPATH, "//a[@title='Next']")
#year_elem=driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']/span[2]")
# month_elem=driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']/span[1]")
yy=int(t1.strftime("%Y"))#2025
mm=t1.strftime("%B")#"October"
dd=t1.strftime("%d").strip("0")
# year
while True:
    year_from_page = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']/span[2]").text
    # print(year_from_page)
    if int(year_from_page) != yy and int(year_from_page) > yy:
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()
    elif int(year_from_page) != yy and int(year_from_page) < yy:
        driver.find_element(By.XPATH, "//a[@title='Next']").click()
    elif int(year_from_page) == yy:
        break

# month
calender={"January":1, "February":2,"March":3, "April":4,"May":5, "June":6,"July":7, "August":8,
          "September":9, "October":10, "November":11, "December":12}
for _ in range(12):
    month_from_ui = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span[1]").text
    print(month_from_ui)
    if calender[month_from_ui]!=calender[mm] and calender[month_from_ui] > calender[mm]:
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()
    elif calender[month_from_ui]!=calender[mm] and calender[month_from_ui] < calender[mm]:
        driver.find_element(By.XPATH, "//a[@title='Next']").click()
    elif calender[month_from_ui]==calender[mm]:
        break

driver.find_element(By.XPATH,f"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a[text()={dd}]").click()



print(driver.find_element(By.ID, 'datepicker1').get_attribute("value"))
if date_1 == driver.find_element(By.ID, 'datepicker1').get_attribute("value"):
    print("validated....")

sleep(10)