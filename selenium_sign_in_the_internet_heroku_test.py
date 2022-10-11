from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.chrome.get("https://the-internet.herokuapp.com")
        self.chrome.find_element(by=By.XPATH, value="//a[normalize-space()='Form Authentication']").click()
        self.chrome.maximize_window()
        self.chrome.fullscreen_window()
        self.chrome.implicitly_wait(10)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_url(self):  # TEST 1
        assert self.chrome.current_url == "https://the-internet.herokuapp.com/login", "Wrong URL"

    def test_page_title(self):  # TEST 2
        assert self.chrome.title == "The Internet", "Wrong page title!"
        self.assertEqual(self.chrome.title, "The Internet", "Wrong page title!")

    def test_page_h1(self):  # TEST 3
        self.assertEqual(self.chrome.find_element(by=By.XPATH, value="//h2").text, "Login Page",  "Wrong page text")

    def test_login_is_displayed(self):  # TEST 4
        self.assertTrue(self.chrome.find_element(by=By.XPATH, value="//i[@class='fa fa-2x fa-sign-in']").is_displayed(),
                        "Login not displayed!")

    def test_selenium_link(self):  # TEST 5
        selenium_link = self.chrome.find_element(by=By.LINK_TEXT, value="Elemental Selenium")
        selenium_link.click()
        sleep(1)
        # code to swich to another open tab
        tabs = self.chrome.window_handles
        self.chrome.switch_to.window(tabs[1])
        self.assertEqual(self.chrome.current_url, "http://elementalselenium.com/", "Wrong href selenium link!")

    def test_error_empty_credentials(self):  # TEST 6
        self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        self.assertTrue(self.chrome.find_element(by=By.ID, value="flash").is_displayed(), "Error not displayed")

    def test_error_invalid_username(self):  # TEST 7
        self.chrome.find_element(by=By.ID, value="username").send_keys("Adrian")
        self.chrome.find_element(by=By.ID, value="password").send_keys("123456789")
        self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        expected_message = "Your username is invalid!"

        self.assertTrue(expected_message in self.chrome.find_element(by=By.ID, value="flash").text,
                        "Invalid message error!")

    def test_quit_error_invalid_credentials(self):  # TEST 8
        # first try
        # self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        # sleep(1)
        # # error_message = self.chrome.find_element(by=By.XPATH, value="//div[@id='flash']")
        # self.chrome.find_element(by=By.CLASS_NAME, value="close").click()
        # sleep(2)
        # # I had some problem here because the web object disappeare when pres quit button so the selenium can't find it
        # # self.assertFalse(self.chrome.find_element(by=By.CLASS_NAME, value="close").is_enabled())
        # web_objects = self.chrome.find_elements(by=By.XPATH, value="//div[@id='flash']")
        # self.assertListEqual(web_objects, [])

        # second try
        self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        sleep(1)
        self.chrome.find_element(by=By.CLASS_NAME, value="close").click()
        sleep(2)
        # for more efficiency we can find his parent first after to search only there
        try:
            self.chrome.find_element(by=By.XPATH, value="//body/div[1]").find_element(by=By.XPATH,
                                                                                      value="//div[@id='flash']")
            exist = True
        except NoSuchElementException:
            exist = False
        self.assertFalse(exist, "Message should not be displayed!")

    def test_label_text(self):  # TEST 9
        label_list = self.chrome.find_elements(by=By.XPATH, value="//label")
        print("Test label text")
        self.assertEqual(label_list[0].text, "Username")
        self.assertEqual(label_list[1].text, "Password")

    def test_login_correct_credentials(self):  # TEST 10
        self.chrome.find_element(by=By.ID, value="username").send_keys("tomsmith")
        self.chrome.find_element(by=By.ID, value="password").send_keys("SuperSecretPassword!")
        self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        self.assertTrue("/secure" in self.chrome.current_url, "URL not secured!")

        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.ID, "flash")))

        login_successful = self.chrome.find_element(by=By.XPATH, value='//div[@id="flash"]')
        self.assertTrue(login_successful.is_displayed(), 'Login successful message not displayed!')

        self.assertTrue("secure area!" in login_successful.text, 'Login successful message not contains secure area!')

    def test_login_correct_credentials_and_log_out(self):  # TEST 11
        self.chrome.find_element(by=By.ID, value="username").send_keys("tomsmith")
        self.chrome.find_element(by=By.ID, value="password").send_keys("SuperSecretPassword!")

        self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        self.chrome.find_element(by=By.XPATH, value="//i[@class='icon-2x icon-signout']").click()

        self.assertEqual(self.chrome.current_url, "https://the-internet.herokuapp.com/login")


# TEST 12
class PasswordBreaker(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.chrome.get("https://the-internet.herokuapp.com")
        self.chrome.find_element(by=By.XPATH, value="//a[normalize-space()='Form Authentication']").click()
        self.chrome.maximize_window()
        self.chrome.fullscreen_window()
        self.chrome.implicitly_wait(10)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_list_breeker_password(self):
        self.chrome.find_element(by=By.ID, value="username").send_keys("tomsmith")
        h4_element = self.chrome.find_element(by=By.XPATH, value="//h4[@class='subheader']")
        h4_element_text = h4_element.text
        potential_passwords = h4_element_text.split(" ")  # 30 words
        for i in range(len(potential_passwords)):
            self.chrome.refresh()
            self.chrome.implicitly_wait(5)
            self.chrome.find_element(by=By.ID, value="username").send_keys("tomsmith")
            self.chrome.find_element(by=By.ID, value="password").send_keys(f"{potential_passwords[i]}")
            self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
            if self.chrome.current_url == "https://the-internet.herokuapp.com/secure":
                print(f"\nParola secretă este [{potential_passwords[i]}].")
                break
            elif i == len(potential_passwords) - 1:
                print("\nNu am reușit să găsesc parola!")