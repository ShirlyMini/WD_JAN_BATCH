from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given(u'Launch browser')
def step_impl(context):
    context.driver=webdriver.Chrome(service=Service(r"E:\selenium\drivers\chromedriver.exe"))
    context.wait_obj = WebDriverWait(context.driver, 10)

@when(u'Launch Nopcommerce website')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")

@then(u'Verify title of home page')
def step_impl(context):
    assert context.driver.title=="Your store. Login"

@when(u'Enter Username "{user}" and Password "{pswd}"')
def step_impl(context, user, pswd):
    context.driver.find_element(By.ID, "Email").clear()
    context.driver.find_element(By.ID, "Email").send_keys(user)
    context.driver.find_element(By.ID, "Password").clear()
    context.driver.find_element(By.ID, "Password").send_keys(pswd)


@when(u'Click Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then(u'Verify Dashborad page')
def step_impl(context):
    context.wait_obj.until(expected_conditions.presence_of_element_located((By.XPATH, "//ul[@class='navbar-nav ml-auto pl-2']/li[2]/a")))
    assert context.driver.find_element(By.XPATH, "//ul[@class='navbar-nav ml-auto pl-2']/li[2]/a").text == "John Smith"

@then(u'Verify Dashborad page with status "{status}"')
def step_impl(context, status):
    try:
        context.wait_obj.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//ul[@class='navbar-nav ml-auto pl-2']/li[2]/a")))
        assert context.driver.find_element(By.XPATH, "//ul[@class='navbar-nav ml-auto pl-2']/li[2]/a").text == "John Smith" and status=="True"
    except:
        assert status=="False"

@when(u'Click Customer Menu')
def step_impl(context):
    sleep(2)
    context.driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Customers')]").click()


@when(u'Click Online Customer Menu')
def step_impl(context):
    sleep(2)
    context.driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Online customers')]").click()

@Then(u'Verify Customer Dashboard')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1[@class='float-left']").text=="Customers"

@Then(u'Verify Online Customer Dashboard')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1[@class='float-left']").text=="Online customers"