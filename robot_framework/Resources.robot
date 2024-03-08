*** Settings ***
Library    SeleniumLibrary
Library    ./xmlUtility.py
Library    ./xl_utility.py

*** Keywords ***
nopcommerce setup
    Set Log Level    TRACE
    Open Browser	${url}     Chrome
    Maximize Browser Window

nopcommerce teardown
    Close Browser

Login using username and password
    Input Text    id:Email    ${user}    clear=True
    Input Text    id:Password    ${pswd}   clear=True
    Click Element    xpath: //button[contains(text(),'Log in')]

Login using username and password with parameter
    [Arguments]    ${usr}    ${pass}
    Input Text    id:Email    ${usr}    clear=True
    Input Text    id:Password    ${pass}   clear=True
    Click Element    xpath: //button[contains(text(),'Log in')]

Login using username and password with return
    [Arguments]    ${usr}    ${pass}
    Input Text    id:Email    ${usr}    clear=True
    Input Text    id:Password    ${pass}   clear=True
    Click Element    xpath: //button[contains(text(),'Log in')]
    RETURN    True

Load Test Data xml
    [Arguments]    ${file}
    ${test_data} =    xmlUtility.load_test_data    ${file}
    RETURN    ${test_data}

Load Test Data Excel
    [Arguments]    ${file}    ${sheet}
    ${r} =    xl_utility.GetRow    ${file}    ${sheet}
    ${c} =    xl_utility.GetCol    ${file}    ${sheet}
    ${data} =    Create List
    FOR    ${i}    IN RANGE    2    ${r}+1
        ${temp_data} =    Create List
        FOR    ${j}    IN RANGE    1    ${c}+1
            ${var} =    xl_utility.ReadCell    ${file}    ${sheet}   ${i}    ${j}
            Append To List    ${temp_data}    ${var}
        END
#        Log    ${temp_data}    console=True
        Append To List    ${data}    ${temp_data}
    END
    Log    ${data}    console=True


    RETURN    ${data}

Load Test Data Excel from py
    [Arguments]    ${file}    ${sheet}
    ${data} =   xl_utility.load_data    ${file}    ${sheet}
    Log    ${data}    console=True
    RETURN    ${data}