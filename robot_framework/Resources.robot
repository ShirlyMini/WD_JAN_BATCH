*** Settings ***
Library    SeleniumLibrary

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