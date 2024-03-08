*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource    ./Resources.robot
Variables    ./data.py


*** Test Cases ***
Login in to nopcommerce page-ddt
    Set Log Level    TRACE
#    ${login_data_xl}=    Load Test Data Excel    ./LoginData.xlsx    Sheet1
    ${login_data_xl}=    Load Test Data Excel from py    ./LoginData.xlsx    Sheet1
    FOR   ${data}    IN    @{login_data_xl}
        Open Browser	${url}     Chrome
        Maximize Browser Window
        ${status}    Login using username and password with return    ${data[0]}    ${data[1]}
        Log    ${status}    console=True
        Run Keyword If    "${data[2]}"=="Pass"    Title Should Be    Dashboard / nopCommerce administration
        ...    ELSE IF    "${data[2]}"=="Fail"    Title Should Be    Your store. Login
        Close Browser
    END

