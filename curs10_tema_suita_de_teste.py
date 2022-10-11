import unittest
import HtmlTestRunner

from selenium_sign_in_the_internet_heroku_test import LoginTest
from selenium_automation_jules_app_sign_in import SignInTest


class TestSuite(unittest.TestCase):

    tests_to_run = unittest.TestSuite()
    tests_to_run.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest),
        unittest.defaultTestLoader.loadTestsFromTestCase(SignInTest),
    ])

    runner = HtmlTestRunner.HTMLTestRunner(report_title="Test Jules and Heroku", report_name="Sign-in raport")

    runner.run(tests_to_run)