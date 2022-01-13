*** Settings ***
Library    OperatingSystem
Library    SeleniumLibrary
Library    ../src/RobotAxeLibrary/RobotAxeLibrary.py
# A python file to store variable informations to be used in the test, like a dictionary with config rules
Variables    VariableFile.py

# Suite Teardown    Close All Browsers
Test Teardown       Close All Browsers

*** Variables ***
# a array list of a11y rules to search in the page
@{specific_a11y}    area-alt    color-contrast
# a specific wcag rule to search in the page
@{specific_one_a11y}    area-alt
# a array list of a11y tags to search in the page
@{specific_tags_a11y}    wcag2a    wcag2aa
# a specific wcag tag to search in the page
@{specific_one_tag_a11y}    wcag2a
# a list of elements to be filter out by target information
@{ignore_targets}    .mb-32.m-0:nth-child(1) > .text-color-primary    .button-wide-mobile    .button.button-primary[href$="doar"]
# a list of elements to be filter out by html information
@{ignore_htmls}    <a href="/doar" class="button button-primary">DOAR</a>

*** Test Cases ***
Check for specifics tags

    Open Browser                https://retrospective-twitter.web.app/     chrome
    Wait Until Page Contains    Faça o login com a sua conta do twitter

    Check for accessibility issues    type_issues=tags    specific_issues=${specific_one_tag_a11y}

    Should Not Exceed Maximum Issues    1

Check for other rules

    Open Browser                https://retrospective-twitter.web.app/     chrome
    Wait Until Page Contains    Faça o login com a sua conta do twitter

    Check for accessibility issues    rules_config=${DICTIONARY}

    Should Not Exceed Maximum Issues    1

Default Check Pass

    Open Browser                https://retrospective-twitter.web.app/     chrome
    Wait Until Page Contains    Faça o login com a sua conta do twitter

    Check for accessibility issues

    Should Not Exceed Maximum Issues    4

Default Check Fail

    Open Browser                https://retrospective-twitter.web.app/     chrome
    Wait Until Page Contains    Faça o login com a sua conta do twitter

    Check for accessibility issues

    Should Not Exceed Maximum Issues    1

Ignore targets

    Open Browser                https://retrospective-twitter.web.app/     chrome
    Wait Until Page Contains    Faça o login com a sua conta do twitter

    Log                               ${ignore_targets}
    Check for accessibility issues    ignore_targets=${ignore_targets}

    Should Not Exceed Maximum Issues    2

Ignore htmls

    Open Browser                https://retrospective-twitter.web.app/     chrome
    Wait Until Page Contains    Faça o login com a sua conta do twitter

    Log                               ${ignore_htmls}
    Check for accessibility issues    ignore_htmls=${ignore_htmls}

    Should Not Exceed Maximum Issues    3

# To Be Implemented
#Check for specifics impact
#
#    Open Browser                https://retrospective-twitter.web.app/     chrome
#    Wait Until Page Contains    Faça o login com a sua conta do twitter
#
#    Check for accessibility issues    impact    serious
#
#    Should Not Exceed Maximum Issues    1