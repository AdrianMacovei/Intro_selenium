from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get("https://formy-project.herokuapp.com/form")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_login_with_correct_email(self):
        pass


