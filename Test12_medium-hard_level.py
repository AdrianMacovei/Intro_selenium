from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://the-internet.herokuapp.com/login")
browser.maximize_window()
# username input
browser.find_element(by=By.ID, value="username").send_keys("tomsmith ")


h4_element = browser.find_element(by=By.XPATH, value="//h4[@class='subheader']")
h4_element_text = h4_element.text

# for testin elif ""Nu am reușit să găsesc parola!"
# h4_element_text = "This is where you can log into the secure area. Enter tomsmith for the username and " \
#                   "for the password. If the information is wrong you should see error messages."

list_words = h4_element_text.split(" ")  # 30 words

for i in range(len(list_words)):
    browser.refresh()
    browser.implicitly_wait(5)
    browser.find_element(by=By.ID, value="username").send_keys("tomsmith")
    browser.find_element(by=By.ID, value="password").send_keys(f"{list_words[i]}")
    browser.find_element(by=By.XPATH, value="//button[@type='submit']").click()
    if browser.current_url == "https://the-internet.herokuapp.com/secure":
        print(f"Parola secretă este [{list_words[i]}].")
        break
    elif i == len(list_words) - 1:
        print("Nu am reușit să găsesc parola!")

