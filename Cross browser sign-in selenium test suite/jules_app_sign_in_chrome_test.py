from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest


class SignInTestChrome(unittest.TestCase):
    ENTER_EMAIL_SELECTOR = (By.XPATH, "//input[@placeholder='Enter your email']")
    LOGIN_BUTTON_SELECTOR = (By.XPATH, "//button[@type='submit']")
    ENTER_PASSWORD_SELECTOR = (By.XPATH, "//input[@placeholder='Enter your password']")
    SIGN_IN_URL = "https://jules.app/sign-in"
    FORGOT_PWD_URL = "https://jules.app/forgot-password"
    SIGN_UP_URL = "https://jules.app/sign-up"
    JULES_APPSTORE_URL = "https://apps.apple.com/us/app/jules-mobile/id1443574567"
    JULES_GPLAY_URL = "https://play.google.com/store/apps/details?id=app.jules.mobile&pcampaignid=MKT-Other-global-all"\
                      "-co-prtnr-py-PartBadge-Mar2515-1"
    FAQ_URL = "https://static.jules.app/faq.html"
    TERMS_URL = "https://static.jules.app/terms_of_use.html"
    PRIVACY_POLICY_URL = "https://static.jules.app/privacy_policy.html"
    INVALID_LINK_MESSAGE = "Invalid link!"

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
        self.assertFalse(self.browser.find_element(*self.LOGIN_BUTTON_SELECTOR).is_enabled(),
                         "Login should not be enable")

    def test_wrong_email_message(self) -> None:
        self.browser.find_element(*self.ENTER_EMAIL_SELECTOR).send_keys("dfsdfsdfds")
        self.assertTrue(self.browser.find_element
                        (by=By.TAG_NAME, value="p").is_displayed(), "Please enter a valid email address! not displayed")

    def test_error_message_when_email_is_correct_foramt(self) -> None:
        self.browser.find_element(*self.ENTER_EMAIL_SELECTOR) \
            .send_keys("myemail@gmail.com")
        try:
            self.browser.find_element(by=By.TAG_NAME, value="p")
            exist = True
        except NoSuchElementException:
            exist = False
        self.assertFalse(exist, "Message is not displayed")

    def test_login_activation_correct_email_no_password(self) -> None:
        self.browser.find_element(*self.ENTER_EMAIL_SELECTOR) \
            .send_keys("myemail@gmail.com")
        self.assertFalse(self.browser.find_element(*self.LOGIN_BUTTON_SELECTOR).is_enabled(),
                         "Login should not be enable")

    def test_login_activation_correct_credentials_format(self) -> None:
        self.browser.find_element(*self.ENTER_EMAIL_SELECTOR).send_keys("myemail@gmail.com")
        self.browser.find_element(*self.ENTER_PASSWORD_SELECTOR).send_keys("1234566789")
        self.assertTrue(self.browser.find_element(*self.LOGIN_BUTTON_SELECTOR).is_enabled(),
                        "Login should be enable")

    def test_message_after_delete_password(self) -> None:
        self.browser.find_element(*self.ENTER_EMAIL_SELECTOR).send_keys(
            "myemail@gmail.com")
        self.browser.find_element(*self.ENTER_PASSWORD_SELECTOR).send_keys(
            "1234566789")

        messsage_password = self.browser.find_element(*self.ENTER_PASSWORD_SELECTOR)
        messsage_password.send_keys(Keys.CONTROL + "a")
        messsage_password.send_keys(Keys.DELETE)

        self.assertTrue(self.browser.find_element(by=By.TAG_NAME, value="p").is_displayed(),
                        "Error message should appear")

    def test_eye_icon_not_activated_until_pressed(self) -> None:
        pwd = self.browser.find_element(*self.ENTER_PASSWORD_SELECTOR)
        self.assertEqual(pwd.get_attribute("type"), "password", "This should be type password not text when open "
                                                                "first time the page")

    def test_eye_icon_password(self) -> None:
        pwd = self.browser.find_element(*self.ENTER_PASSWORD_SELECTOR)
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
        self.assertEqual(self.browser.current_url, self.FORGOT_PWD_URL, self.INVALID_LINK_MESSAGE)

    def test_signup_link(self) -> None:
        self.browser.find_element(by=By.LINK_TEXT, value="Sign up.").click()

        sleep(1)
        self.assertEqual(self.browser.current_url, self.SIGN_UP_URL, self.INVALID_LINK_MESSAGE)

    def test_appstore_img_link(self) -> None:
        sleep(2)
        apple_icon = self.browser.find_element(by=By.XPATH, value="//img[@alt='Download on the App Store']")
        apple_icon.click()

        # this 2 line of code change the primary chrome windows to new open tab
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])
        sleep(1)
        self.assertEqual(self.browser.current_url, self.JULES_APPSTORE_URL, self.INVALID_LINK_MESSAGE)

    def test_google_play_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//img[@alt='Get it on Google Play']").click()
        sleep(2)

        # this 2 line of code change the primary chrome windows to new open tab
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, self.JULES_GPLAY_URL, self.INVALID_LINK_MESSAGE)

    def test_FAQ_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//span[normalize-space()='FAQ']").click()
        sleep(2)

        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, self.FAQ_URL, self.INVALID_LINK_MESSAGE)

    def test_term_and_conditions_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//span[normalize-space()='TERMS & CONDITIONS']").click()
        sleep(2)

        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, self.TERMS_URL, self.INVALID_LINK_MESSAGE)

    def test_privacy_policy_link(self) -> None:
        self.browser.find_element(by=By.XPATH, value="//span[normalize-space()='PRIVACY POLICY']").click()
        sleep(2)

        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

        self.assertEqual(self.browser.current_url, self.PRIVACY_POLICY_URL, self.INVALID_LINK_MESSAGE)
