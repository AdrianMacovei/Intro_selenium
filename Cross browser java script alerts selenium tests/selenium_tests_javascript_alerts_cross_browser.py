import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class EdgeTestCase(TestCase):
    BASE_URL = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_BUTTON_SELECTOR = (By.XPATH, "//ul/li[1]/button")
    CONFIRM_BUTTON_SELECTOR = (By.XPATH, "//ul/li[2]/button")
    PROMPT_BUTTON_SELECTOR = (By.XPATH, "//ul/li[3]/button")
    RESULT_SELECTOR = (By.ID, "result")

    def setUp(self) -> None:
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.browser = webdriver.Edge(service=service)
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_simple_alert(self):
        alert_button = self.browser.find_element(*self.ALERT_BUTTON_SELECTOR)
        alert_button.click()

        alert_window = self.browser.switch_to.alert
        alert_window.accept()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You successfully clicked an alert"

    def test_confirm_alert_accept(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.accept()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Ok"

    def test_confirm_alert_dismiss(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.dismiss()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Cancel"

    def test_prompt_alert_accept_empty(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.accept()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered:"

    def test_prompt_alert_accept_with_insert(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.send_keys("Salut!")
        prompt_window.accept()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: Salut!"

    def test_prompt_alert_dismiss_empty(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.dismiss()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: null"

    def test_prompt_alert_dismiss_with_insert(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.send_keys("Salut!")
        prompt_window.dismiss()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: null"


class FirefoxTestCase(EdgeTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()


class ChromeTestCase(EdgeTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()


if __name__ == "__main__":
    pass