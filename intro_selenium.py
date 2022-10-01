from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://formy-project.herokuapp.com/form")
browser.maximize_window()
sleep(1)
# find element with id first name
first_name = browser.find_element(value="first-name")
print(first_name.tag_name)
print(first_name.text)
print(first_name.send_keys("Adrian"))

last_name = browser.find_element(by=By.ID, value="last-name")
last_name.send_keys("Macovei")

# formy_link = browser.find_element(by= By.LINK_TEXT, value="FORMY")
# formy_link.click()

component_link = browser.find_element(by=By.ID, value="nav-link dropdown-toggle")
component_link.click()

sleep(3)
