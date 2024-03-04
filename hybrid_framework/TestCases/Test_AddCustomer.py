import random
import string
from time import sleep
from hybrid_framework.PageObject.LoginPageObj import Login
from hybrid_framework.PageObject.AddCustomerPageObj import AddCustomer
from hybrid_framework.Utility.CustomLogger import custom_log
from hybrid_framework.Utility.ReadIni import ReadProperty

class Test_Add_Customer_Functionality:
    log=custom_log()
    def test_verify_add_new(self, setup):
        driver = setup
        self.log.info("Launching browser")
        login_obj = Login(driver)
        login_obj.SetEmail(ReadProperty.GetUser())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        self.log.info("Successfully login to the Dashbord...")
        ac_obj = AddCustomer(driver)
        ac_obj.NavigatetoAddCustomer()
        ac_obj.SetCustomerEmail("".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])+"@gmail.com")
        ac_obj.SetCustomerPassword("123456")
        ac_obj.SetCustomerFirstName("sam")
        ac_obj.SetCustomerLastName("pooja")
        ac_obj.SetCustomerGender("Male")
        ac_obj.SetCustomerDOB("3/2/2024")
        ac_obj.SetCustomerCompany("xyz company")
        ac_obj.SetCustomerTax("yes")
        ac_obj.SetCustomerNewsletter("Your store name")
        ac_obj.SetCustomerRole("Guests")
        ac_obj.SetCustomerVendor("Vendor 1")
        ac_obj.SetCustomerActive("yes")
        ac_obj.SetAdminContent()
        ac_obj.ClickSave()

        status = ac_obj.Verify_Alert()
        if status == True:
            login_obj.ClickLogOut()
            self.log.info("TC::test_verify_add_new=PASSED")
            assert True
        else:
            self.log.error("TC::test_verify_add_new=FAILED")
            driver.save_screenshot(r".\ScreenShot\test_verify_add_new.png")
            assert False