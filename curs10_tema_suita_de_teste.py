import unittest
import HtmlTestRunner
from jules_app_sign_in_chrome_test import SignInTestChrome
from jules_app_sign_in_firefox_test import SignInTestGecko
from jules_app_sign_in_microsft_edge_test import SignInTestEdge


class TestSuite(unittest.TestCase):

    def test_suite_jules_app_sign_in(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SignInTestChrome),
            unittest.defaultTestLoader.loadTestsFromTestCase(SignInTestGecko),
            unittest.defaultTestLoader.loadTestsFromTestCase(SignInTestEdge),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(report_title="Test Jules App on Chrome, Edge and Firefox",
                                               report_name="Sign-in report", combine_reports=True)

        runner.run(tests_to_run)
