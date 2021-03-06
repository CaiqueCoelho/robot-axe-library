# Robot Axe Library
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/CaiqueCoelho/robot-axe-library/blob/master/LICENSE)

This project is a RobotFramework Library wrapper for axe-selenium-python package. In this project we abstracted the entire library setup for use in robotframework and also implemented the entire interface for communicating with the AXE library allowing to define specific filters to look for accessibility issues in addition to allowing the necessary assertions on the test side, for your your test passes or fails depending on the configuration you want, allowing a maximum number of issues, excluding elements you don't want to analyze, and allowing you to define specific accessibility rules, levels, tags and impact.

## How to install

```bash
pip install robot-axelibrary==0.1.8
```

## How to use
 ```
*** Settings ***
Library     SeleniumLibrary
Library     RobotAxeLibrary

*** Test Cases ***
Default Check Pass

    Open Browser                        https://retrospective-twitter.web.app/  chrome
    Wait Until Page Contains            Faça o login com a sua conta do twitter
    Check for accessibility issues
    Should Not Exceed Maximum Issues    2
 ```

 ## Keywords Documentation
 [Click Here](https://caiquecoelho.github.io/robot-axe-library/documentation/AxeLibrary.html)

 ## Glossary
- Violation: A violation is a type of accessibility problem, for example a color-contrast problem or a missing aria-label
- Issue: An issue is the occurrence of a violation in one element or more, for example we can get 2 issues from the type color-contrast and 1 from aria-label
 ## Feature Request

If you have any feature request just open an issue describing your request or feel free with your feature! Any pull pull request are welcome!

## Found an issue?

Register the issue [here](https://github.com/CaiqueCoelho/robot-axe-library/issues) and wait for us to solve it as soon as possible.
In addition, any contribution is welcome, so feel free to make a pull request if you want to solve any problem :happy:

## License

[MIT](https://github.com/CaiqueCoelho/robot-axe-library/blob/master/LICENSE)

#### Project Inspiration
[robotframework-axelibrary](https://github.com/adiralashiva8/robotframework-axelibrary) by [@adiralashiva8](https://github.com/adiralashiva8)

