*** Settings ***
Library    SeleniumLibrary
Resource    ./Resources.robot
Variables    ./data.py

#*** Variables ***
#${url}    https://admin-demo.nopcommerce.com/
#${user}    admin@yourstore.com
#${pswd}    admin

*** Test Cases ***
Login in to nopcommerce page
    [setup]    nopcommerce setup
#    Set Log Level    TRACE
#    Open Browser	${url}     Chrome
#    Maximize Browser Window
#    Login using username and password
#    Login using username and password with parameter    ${user}    ${pswd}
    ${status}    Login using username and password with return    ${user}    ${pswd}
    Log    ${status}    console=True
    Title Should Be    Dashboard / nopCommerce administration
#    Close Browser
    [teardown]  nopcommerce teardown

Login in to nopcommerce page-ddt
    Set Log Level    TRACE
    FOR   ${data}    IN    @{login_data_py}
        Open Browser	${url}     Chrome
        Maximize Browser Window
        ${status}    Login using username and password with return    ${data[0]}    ${data[1]}
        Log    ${status}    console=True
        Run Keyword If    "${data[2]}"=="Pass"    Title Should Be    Dashboard / nopCommerce administration
        ...    ELSE IF    "${data[2]}"=="Fail"    Title Should Be    Your store. Login
        Close Browser
    END

