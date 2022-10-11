from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest


class SignInTest(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.chrome.get("https://jules.app/sign-in")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_corect_page_name(self) -> None:
        self.assertEqual(self.chrome.title, "Jules", "Incorrect page title")

    def test_logo_displayed(self) -> None:
        self.assertTrue(self.chrome.find_element(by=By.XPATH, value="//img[@alt='Jules']").is_displayed(),
                        "Logo not displayed!")

    def test_login_empty_credentials(self) -> None:
        self.assertFalse(self.chrome.find_element
                         (by=By.XPATH, value="//button[@type='submit']").is_enabled(), "Login should not be enable")

    def test_wrong_email_message(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']").send_keys("dfsdfsdfds")
        self.assertTrue(self.chrome.find_element
                        (by=By.TAG_NAME, value="p").is_displayed(), "Please enter a valid email address! not displayed")

    def test_error_message_when_email_is_correct_foramt(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']")\
            .send_keys("myemail@gmail.com")
        try:
            self.chrome.find_element(by=By.TAG_NAME, value="p")
            exist = True
        except NoSuchElementException:
            exist = False
        self.assertFalse(exist, "Message is not displayed")

    def test_login_activation_correct_email_no_password(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']")\
            .send_keys("myemail@gmail.com")
        self.assertFalse(self.chrome.find_element
                         (by=By.XPATH, value="//button[@type='submit']").is_enabled(), "Login should not be enable")

    def test_login_activation_correct_credentials_format(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']").send_keys(
            "myemail@gmail.com")
        self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']").send_keys(
            "1234566789")
        self.assertTrue(self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").is_enabled(),
                        "Login should be enable")

    def test_message_after_delete_password(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']").send_keys(
            "myemail@gmail.com")
        self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']").send_keys(
            "1234566789")
        messsage_password = self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']")
        messsage_password.send_keys(Keys.CONTROL + "a")
        messsage_password.send_keys(Keys.DELETE)

        self.assertTrue(self.chrome.find_element(by=By.TAG_NAME, value="p").is_displayed(),
                        "Error message should appear")

    def test_eye_icon_not_activated_until_pressed(self) -> None:
        pwd = self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']")
        self.assertEqual(pwd.get_attribute("type"), "password", "This should ce type password not text when open "
                                                                "first time the page")

    def test_eye_icon_password(self) -> None:
        pwd = self.chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']")
        pwd.send_keys("sfsdf5345")
        self.chrome.find_element(by=By.CLASS_NAME, value="MuiSvgIcon-root").click()

        # when pres eye icon element password attribute type should change password -> text
        self.assertEqual(pwd.get_attribute("type"), "text", "This should be text after press eye icon!")

        # text -> password
        self.chrome.find_element(by=By.CLASS_NAME, value="MuiSvgIcon-root").click()
        self.assertEqual(pwd.get_attribute("type"), "password", "This should be password after "
                                                                "press two times eye icon!")

    def test_forgot_password_link(self) -> None:
        self.chrome.find_element(by=By.LINK_TEXT, value="Forgot password?").click()

        sleep(1)
        self.assertEqual(self.chrome.current_url, "https://jules.app/forgot-password", "Link send to wrong URL!")

    def test_signup_link(self) -> None:
        self.chrome.find_element(by=By.LINK_TEXT, value="Sign up.").click()

        sleep(1)
        self.assertEqual(self.chrome.current_url, "https://jules.app/sign-up", "Link send to wrong URL!")

    def test_appstore_img_link(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//img[@alt='Download on the App Store']").click()
        sleep(2)

        # this 2 line of code change the primary chrome windows to new open tab
        tabs = self.chrome.window_handles
        self.chrome.switch_to.window(tabs[1])

        self.assertEqual(self.chrome.current_url, "https://apps.apple.com/us/app/jules-mobile/id1443574567",
                         "Invalid link!")

    def test_google_play_link(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//img[@alt='Get it on Google Play']").click()
        sleep(2)

        # this 2 line of code change the primary chrome windows to new open tab
        tabs = self.chrome.window_handles
        self.chrome.switch_to.window(tabs[1])

        self.assertEqual(self.chrome.current_url, "https://play.google.com/store/apps/details?id=app.jules."
                                                  "mobile&pcampaignid=MKT-Other-global-all-co-"
                                                  "prtnr-py-PartBadge-Mar2515-1", "Invalid link!")

    def test_FAQ_link(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//span[normalize-space()='FAQ']").click()
        sleep(2)

        tabs = self.chrome.window_handles
        self.chrome.switch_to.window(tabs[1])

        self.assertEqual(self.chrome.current_url, "https://static.jules.app/faq.html", "Invalid link!")

    def test_termandconditions_link(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//span[normalize-space()='TERMS & CONDITIONS']").click()
        sleep(2)

        tabs = self.chrome.window_handles
        self.chrome.switch_to.window(tabs[1])

        self.assertEqual(self.chrome.current_url, "https://static.jules.app/terms_of_use.html", "Invalid link!")

    def test_privacy_policy_link(self) -> None:
        self.chrome.find_element(by=By.XPATH, value="//span[normalize-space()='PRIVACY POLICY']").click()
        sleep(2)

        tabs = self.chrome.window_handles
        self.chrome.switch_to.window(tabs[1])

        self.assertEqual(self.chrome.current_url, "https://static.jules.app/privacy_policy.html", "Invalid link!")
