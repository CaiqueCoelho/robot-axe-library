*** Settings ***
Library  OperatingSystem
Library  SeleniumLibrary
Library    AxeLibrary.py
Variables    VariableFile.py

# Suite Teardown     Close All Browsers
Test Teardown    Close All Browsers

*** Variables ***
@{specific_a11y}    area-alt    color-contrast
@{specific_one_a11y}    area-alt
@{specific_tags_a11y}    wcag2a    wcag2aa
@{specific_one_tag_a11y}    wcag2a
@{ignore_targets}    .mb-32.m-0:nth-child(1) > .text-color-primary      .button-wide-mobile     .button.button-primary[href$="doar"]
@{ignore_htmls}    <a href="/doar" class="button button-primary">DOAR</a>

*** Test Cases ***

#Assertion Issues A11y
#    Open Browser  https://retrospective-twitter.web.app/  chrome
#    Wait Until Page Contains   Faça o login com a sua conta do twitter
#    
#    Check for accessibility issues   report_accessibility.json
#
#    Should Not Exceed Maximum Issues        1

#Assertion Violations A11y
#    Open Browser  https://retrospective-twitter.web.app/  chrome
#    Wait Until Page Contains   Faça o login com a sua conta do twitter
#    
#    Check for accessibility issues   report_accessibility.json
#
#    Should Not Exceed Maximum Violations    1

#Check for specifics errors

    #Open Browser  https://retrospective-twitter.web.app/  chrome
    #Wait Until Page Contains   Faça o login com a sua conta do twitter
    
    #Check for accessibility issues   rule    ${specific_a11y}   None   None     None    report_accessibility.json

    #Should Not Exceed Maximum Issues    1

#Check for specifics tags

    #Open Browser  https://retrospective-twitter.web.app/  chrome
    #Wait Until Page Contains   Faça o login com a sua conta do twitter
    
    #Check for accessibility issues   tags    ${specific_one_tag_a11y}   None    None      None    report_accessibility.json

    #Should Not Exceed Maximum Issues    1

#Check for other rules

    #Open Browser  https://retrospective-twitter.web.app/  chrome
    #Wait Until Page Contains   Faça o login com a sua conta do twitter
    
    #Check for accessibility issues   None    None   ${DICTIONARY}   None    None    report_accessibility.json

    #Should Not Exceed Maximum Issues    1

Default Check Pass

    Open Browser  https://retrospective-twitter.web.app/  chrome
    Wait Until Page Contains   Faça o login com a sua conta do twitter
    
    Check for accessibility issues   None    None   None   None     None    report_accessibility.json

    Should Not Exceed Maximum Issues    4

Default Check Fail

    Open Browser  https://retrospective-twitter.web.app/  chrome
    Wait Until Page Contains   Faça o login com a sua conta do twitter
    
    Check for accessibility issues   None    None   None   None     None    report_accessibility.json

    Should Not Exceed Maximum Issues    1

Ignore targets

    Open Browser  https://retrospective-twitter.web.app/  chrome
    Wait Until Page Contains   Faça o login com a sua conta do twitter
    
    Log     ${ignore_targets}
    Check for accessibility issues   None    None   None   ${ignore_targets}     None    report_accessibility.json

    Should Not Exceed Maximum Issues    2

Ignore htmls

    Open Browser  https://retrospective-twitter.web.app/  chrome
    Wait Until Page Contains   Faça o login com a sua conta do twitter
    
    Log     ${ignore_htmls}
    Check for accessibility issues   None    None   None   None     ${ignore_htmls}    report_accessibility.json

    Should Not Exceed Maximum Issues    3

#Check for specifics impact
#
#    Open Browser  https://retrospective-twitter.web.app/  chrome
#    Wait Until Page Contains   Faça o login com a sua conta do twitter
#    
#    Check for accessibility issues   impact    serious   report_accessibility.json
#
#    Should Not Exceed Maximum Issues    1