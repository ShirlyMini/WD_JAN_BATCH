from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from xl_utility import *
from CustomLogger import *

log=logger()
service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()
log.info("Application launched successfully...")

path = r'.\simple_interest.xlsx'
sheet = "Sheet2"

row_no = GetRow(path,sheet)
for r in range(2,row_no+1):
    IT_drop_dwn_obj = Select(driver.find_element(By.ID, "a"))
    IT_drop_dwn_obj.select_by_visible_text(ReadCell(path,sheet,r,5))
    log.info(f"Selected Intrest type {ReadCell(path, sheet, r, 5)}")
    # pricipal
    driver.find_element(By.ID, "c").clear()
    driver.find_element(By.ID, "c").send_keys(ReadCell(path,sheet,r,1))
    log.info(f"set Principal {ReadCell(path, sheet, r, 1)}")
    # rate
    driver.find_element(By.ID, "d").clear()
    driver.find_element(By.ID, "d").send_keys(ReadCell(path,sheet,r,2))
    log.info(f"set Rate {ReadCell(path, sheet, r, 2)}")

    PU_drop_dwn_obj = Select(driver.find_element(By.ID, "f"))
    PU_drop_dwn_obj.select_by_visible_text(ReadCell(path,sheet,r,4))
    log.info(f"Select Period Unit {ReadCell(path, sheet, r, 4)}")
    #period option
    driver.find_element(By.ID, "e").clear()
    driver.find_element(By.ID, "e").send_keys(ReadCell(path,sheet,r,3))
    log.info(f"Set Period option {ReadCell(path, sheet, r, 5)}")

    # total value
    value = driver.find_element(By.XPATH,"//div[@class='output']/label[text()='Total Value']/following-sibling::span").text
    value_from_page = float(value.replace("₹ ", "").replace(",",""))
    WriteCell(path,sheet,r,8, value_from_page)
    value_from_xl = ReadCell(path, sheet, r, 6)
    print(f"Page:{value_from_page}:xl{value_from_xl}")
    log.info(f"Page:{value_from_page}:xl{value_from_xl}")

    #validation
    # assert value_from_page==value_from_xl
    if value_from_page==value_from_xl and ReadCell(path, sheet, r, 7)=="Pass":
        WriteCell(path, sheet, r, 9, "PASS")
        FillGreen(path, sheet, r, 9)
        log.info(f"Validated Total value = PASS")
        assert True
    elif value_from_page!=value_from_xl and ReadCell(path, sheet, r, 7)=="Fail":
        WriteCell(path, sheet, r, 9, "PASS")
        FillGreen(path, sheet, r, 9)
        log.info(f"Validated Total value = PASS")
        assert True
    else:
        driver.save_screenshot("./ss.png")
        WriteCell(path, sheet, r, 9, "FAIL")
        FillRed(path, sheet, r, 9)
        log.error(f"Validated Total value = FAIL")
        assert False

