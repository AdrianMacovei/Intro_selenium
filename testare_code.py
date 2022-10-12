from selenium import webdriver
from time import sleep

browser = webdriver.Opera(executable_path="C:\\Users\\Adrian\\PycharmProjects\\Intro_Selenium\\operadriver.exe")

browser.get('https://www.google.ro/')


browser.maximize_window()
sleep(1)
browser.quit()