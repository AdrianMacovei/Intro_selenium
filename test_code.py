from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome.get("https://the-internet.herokuapp.com")
chrome.find_element(by=By.XPATH, value="//a[normalize-space()='Form Authentication']").click()
chrome.maximize_window()
chrome.implicitly_wait(10)
