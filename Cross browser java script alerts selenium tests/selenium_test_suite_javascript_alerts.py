import unittest
import HtmlTestRunner
from selenium_tests_javascript_alerts_cross_browser import EdgeTestCase, ChromeTestCase, FirefoxTestCase


class TestSuite(unittest.TestCase):

    def test_suite_javascript_alerts(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(EdgeTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(FirefoxTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(ChromeTestCase),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(report_title="Test JavaScript Alerts on Chrome, Edge and Firefox",
                                               report_name="Test report", combine_reports=True)

        runner.run(tests_to_run)
