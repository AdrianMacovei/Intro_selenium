from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest


class SignInTestEdge(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Edge()
        self.browser.get("https://jules.app/sign-in")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_corect_page_name(self) -> None:
        self.assertEqual(self.browser.title, "Jules", "Incorrect page title")

    def test_logo_displayed(self) -> None:
        self.assertTrue(self.browser.find_element(by=By.XPATH, value="//img[@alt='Jules']").is_displayed(),
                        "Logo not displayed!")

    def test_login_empty_credentials(self) -> None:
        self.assertFalse(self.browser.find_element
                         (by=By.XPATH, value="//button[@type='submit']").is_enabled(), "Login should not be enable")

    def test_wrong_email_message(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']").send_keys("dfsdfsdfds")
        self.assertTrue(self.browser.find_element
                        (by=By.TAG_NAME, value="p").is_displayed(), "Please enter a valid email address! not displayed")

    def test_error_message_when_email_is_correct_foramt(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']")\
            .send_keys("myemail@gmail.com")
        try:
            self.browser.find_element(by=By.TAG_NAME, value="p")
            exist = True
        except NoSuchElementException:
            exist = False
        self.assertFalse(exist, "Message is not displayed")

    def test_login_activation_correct_email_no_password(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']")\
            .send_keys("myemail@gmail.com")
        self.assertFalse(self.browser.find_element
                         (by=By.XPATH, value="//button[@type='submit']").is_enabled(), "Login should not be enable")

    def test_login_activation_correct_credentials_format(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']").send_keys(
            "myemail@gmail.com")
        self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']").send_keys(
            "1234566789")
        self.assertTrue(self.browser.find_element(by=By.XPATH, value="//button[@type='submit']").is_enabled(),
                        "Login should be enable")

    def test_message_after_delete_password(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']").send_keys(
            "myemail@gmail.com")
        self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']").send_keys(
            "1234566789")
        messsage_password = self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']")
        messsage_password.send_keys(Keys.CONTROL + "a")
        messsage_password.send_keys(Keys.DELETE)

        self.assertTrue(self.browser.find_element(by=By.TAG_NAME, value="p").is_displayed(),
                        "Error message should appear")

    def test_eye_icon_not_activated_until_pressed(self) -> None:
        pwd = self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']")
        self.assertEqual(pwd.get_attribute("type"), "password", "This should ce type password not text when open "
                                                                "first time the page")

    def test_eye_icon_password(self) -> None:
        pwd = self.browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']")
        pwd.send_keys("sfsdf5345")
        self.browser.find_element(by=By.CLASS_NAME, value="MuiSvgIcon-root").click()

        # when pres eye icon element password attribute type should change password -> text
        self.assertEqual(pwd.get_attribute("type"), "text", "This should be text after press eye icon!")

        # text -> password
        self.browser.find_element(by=By.CLASS_NAME, value="MuiSvgIcon-root").click()
        self.assertEqual(pwd.get_attribute("type"), "password", "This should be password after "
                                                                "press two times eye icon!")

    def test_forgot_password_link(self) -> None:
        self.browser.find_element(by=By.LINK_TEXT, value="Forgot password?").click()

        sleep(1)
        self.assertEqual(self.browser.current_url, "https://jules.app/forgot-password", "Link send to wrong URL!")

    def test_signup_link(self) -> None:
        self.browser.find_element(by=By.LINK_TEXT, value="Sign up.").click()

        sleep(1)
        self.assertEqual(self.browser.current_url, "https://jules.app/sign-up", "Link send to wrong URL!")

    def test_appstore_img_link(self) -> None:
        sleep(2)
        apple_icon = self.browser.find_element(by=By.XPATH, value="//img[@alt='Download on the App Store']")
        apple_icon.click()

        # this 2 line of code change the primary chrome windows to new open tab
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])
        sleep(1)
        self.assertEqual(self.browser.current_url, "https://apps.apple.com/us/app/jules-mobile/id1443574567",
                         "Invalid link!")

    def test_google_play_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//img[@alt='Get it on Google Play']").click()
        sleep(2)

        # this 2 line of code change the primary chrome windows to new open tab
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, "https://play.google.com/store/apps/details?id=app.jules."
                                                   "mobile&pcampaignid=MKT-Other-global-all-co-"
                                                   "prtnr-py-PartBadge-Mar2515-1", "Invalid link!")

    def test_FAQ_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//span[normalize-space()='FAQ']").click()
        sleep(2)

        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, "https://static.jules.app/faq.html", "Invalid link!")

    def test_term_and_conditions_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//span[normalize-space()='TERMS & CONDITIONS']").click()
        sleep(2)

        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, "https://static.jules.app/terms_of_use.html", "Invalid link!")

    def test_privacy_policy_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//span[normalize-space()='PRIVACY POLICY']").click()
        sleep(2)

        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, "https://static.jules.app/privacy_policy.html", "Invalid link!")
