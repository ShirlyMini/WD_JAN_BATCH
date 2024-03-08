*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource    ./Resources.robot
Variables    ./data.py


*** Test Cases ***
Login in to nopcommerce page-ddt
    Set Log Level    TRACE
    ${login_data_xml} =    Load Test Data xml    ./test_data_xml.xml
#    ${login_data_values} =    Get Dictionary Values    ${login_data_xml}
#    Log    ${login_data_xml['login_data']}    console=True
    ${login_data_values} =    Get Dictionary Values    ${login_data_xml['login_data']}
#    Log    ${login_data_values}    console=True
    FOR   ${data}    IN    @{login_data_values}
#        Log    ${data['user']}    console=True
#        Log    ${data['password']}    console=True
#        Log    ${data['expected']}    console=True
        Open Browser	${url}     Chrome
        Maximize Browser Window
        ${status}    Login using username and password with return    ${data['user']}    ${data['password']}
        Log    ${status}    console=True
        Run Keyword If    "${data['expected']}"=="Pass"    Title Should Be    Dashboard / nopCommerce administration
        ...    ELSE IF    "${data['expected']}"=="Fail"    Title Should Be    Your store. Login
        Close Browser
    END

