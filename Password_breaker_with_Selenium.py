from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
'''● Test 12 - brute force password hacking
- Completează user tomsmith
- Găsește elementul //h4
- Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
potențială parolă.
- Folosește o structură iterativă prin care să introduci rând pe rând
parolele și să apeși pe login.
- La final testul trebuie să îmi printeze fie
‘Nu am reușit să găsesc parola’
‘Parola secretă este [parola]’'''


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
        list_words = h4_element_text.split(" ")  # 30 words
        for i in range(len(list_words)):
            self.chrome.refresh()
            self.chrome.implicitly_wait(5)
            self.chrome.find_element(by=By.ID, value="username").send_keys("tomsmith")
            self.chrome.find_element(by=By.ID, value="password").send_keys(f"{list_words[i]}")
            self.chrome.find_element(by=By.XPATH, value="//button[@type='submit']").click()
            if self.chrome.current_url == "https://the-internet.herokuapp.com/secure":
                print(f"\nParola secretă este [{list_words[i]}].")
                break
            elif i == len(list_words) - 1:
                print("\nNu am reușit să găsesc parola!")
