from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException



chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome.get("https://jules.app/sign-in")
chrome.maximize_window()
chrome.implicitly_wait(10)

chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']").send_keys("myemail@gmail.com")
chrome.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']").send_keys("123445678")
print(chrome.find_element(by=By.XPATH, value="//button[@type='submit']").is_enabled())