import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword, library
from axe_selenium_python import Axe
from selenium import webdriver
from robot.api import logger
from robot.utils.asserts import fail
from .version import VERSION

@library
class RobotAxeLibrary:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        self.axe = None
        self.result = None
        self.violations = None
        self.count_violations = None
        self.count_issues = None
        self.ignore_htmls = None
        self.ignore_targets = None

    def helloA11y(self):
        print("Hello from A11y")

    @keyword
    def check_for_accessibility_issues(self, type_issues=None, specific_issues=None, rules_config=None, ignore_targets=None, ignore_htmls=None, report_file='report_accessibility.json'):
        """
        Executes accessibility tests in the current page and write the issues into the file pass in report_file variable. Return report, results and self.result
        With this keyword you can pass the type of issues, rules and wcag levels you want to search, also you can filter out specific elements from the page

        |  = Attribute =    |  = Description =  |
        |  type_issues      |  Pass the type of issues you want to check for, for example: tags or rule |
        |  specific_issues  |  Pass the specific issues you want to check, for example: for tags use wcag2a, wcag2aa, for rules use area-alt, color-contrast |
        |  rules_config     |  Pass the rules to check or to not check, using a dict with the rules follow by the key enabled, for example like: {"rules": {"color-contrast": { "enabled": 0 }, "heading-order": { "enabled": 1 }}} |
        |  ignore_targets   |  Pass the elements you dont want to check, using the target information |
        |  ignore_htmls     |  Pass the elements you dont want to check, using the html information |
        |  report_file      |  File to store accessibility issues result for example: report_accessibility.json  |
        """
        
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        webdriver = seleniumlib.driver

        if ignore_htmls == None:
            ignore_htmls = []
        else:
            logger.info('Ignoring elements html: {}'.format(ignore_htmls))

        if ignore_targets == None:
            ignore_targets = []
        else:
            logger.info('Ignoring elements target: {}'.format(ignore_targets))

        self.ignore_htmls = ignore_htmls
        self.ignore_targets = ignore_targets

        self.axe = Axe(webdriver)
        self.axe.inject()

        if(type_issues != None and specific_issues != None):
            logger.info('Searching for accesibility issues with options: {}'.format(specific_issues))
            self.result = self.axe.run(
                options={
                    "runOnly": {
                        "type": type_issues,
                        "values": specific_issues
                    }
                }
            )
        elif(rules_config != None):
            self.result = self.axe.run(
                options= rules_config
            )
        else:
            self.result = self.axe.run()

        self.axe.write_results(self.result, report_file)
        report = self.axe.report(self.result["violations"])

        results = {"violations":self.result["violations"], "count_violations":len(self.result["violations"])}
        self.violations = self.result["violations"]
        self.count_violations = len(self.result["violations"])

        self.count_issues = 0
        for violation in self.violations:
            for node in violation['nodes']:
                if node['html'] not in ignore_htmls and node['target'][0] not in ignore_targets:
                    self.count_issues += 1

        return report, results, self.result


    @keyword
    def get_json_accessibility_result(self):
        """
        Return accessibility test self.result in Json format. Need to be used after `Check for accessibility issues` keyword    
        """
        result = json.dumps(self.result, indent = 3)
        logger.info(result)
        return result

    @keyword
    def should_not_exceed_maximum_violations(self, maxAcceptableViolations):
        """
        Return an error if count_violations > maxAcceptableViolations
        """

        logger.info('You have {} violations'.format(self.count_violations))
        self.log_accessibility_result()
        if(self.count_violations > int(maxAcceptableViolations)):
            return fail("You have {} violations and you just accept {}".format(self.count_violations, maxAcceptableViolations))

    @keyword
    def should_not_exceed_maximum_issues(self, maxAcceptableIssues):
        """
        Return an error if count_issues > maxAcceptableIssues
        """

        logger.info('You have {} issues'.format(self.count_issues))
        self.log_accessibility_result()
        if(self.count_issues > int(maxAcceptableIssues)):
            return fail("You have {} issues and you just accept {}".format(self.count_issues, maxAcceptableIssues))
        
    
    @keyword
    def log_accessibility_result(self):
        """
        Inserts accessibility result into the `log.html` file. Need to be used after `Check for accessibility issues` keyword
        """

        for violation in self.violations:
            nodes_violation = 0
            for node in violation['nodes']:
                if node['html'] not in self.ignore_htmls and node['target'][0] not in self.ignore_targets:
                    nodes_violation = True

            if nodes_violation:
                style = """
                    <style>
                        #demo table, #demo th, #demo td{
                            border: 1px dotted black;
                            border-collapse: collapse;
                            table-layout: auto;
                        }
                    </style>
                """


                table_issues = """
                 <table id="demo" style="width:100%%">
                    <tr>
                        <th style="width:10%%">Violation id</th>
                        <th style="width:50%%">Violation</th>
                        <th style="width:5%%">How to fix</th>
                        <th style="width:7%%">Impact</th>
                        <th>Tags</th>
                    </tr>
                    <tr>
                        <td style="text-align:center">%s</td>
                        <td>%s</td>
                        <td style="text-align:center"><a href="%s">Link</a></td>
                        <td style="text-align:center">%s</td>
                        <td style="text-align:center">%s</td>
                    </tr>
                </table>
                """%(str(violation['id']), str(violation['description']), str(violation['helpUrl']), str(violation['impact']), str(violation['tags']))

                html_text = style + table_issues

                logger.info(html_text, html=True)

        for violation in self.violations:
            for node in violation['nodes']:
                if node['html'] not in self.ignore_htmls and node['target'][0] not in self.ignore_targets:
                    style = """
                        <style>
                            #demo table, #demo th, #demo td{
                                border: 1px dotted black;
                                border-collapse: collapse;
                                table-layout: auto;
                            }
                        </style>
                    """


                    table_issues = """
                    <table id="demo" style="width:100%%">
                        <tr>
                            <th style="width:10%%">Violation id</th>
                            <th>Issue</th>
                            <th style="width:20%%">html</th>
                            <th style="width:20%%">target</th>
                        </tr>
                        <tr>
                            <td style="text-align:center">%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                        </tr>
                    </table>
                    """%(violation['id'], node['any'][0]['message'], node['html'].replace('<', '&lt;').replace('>', '&gt;'), node['target'][0])

                    new_html = style + table_issues

                    logger.info(new_html, html=True)