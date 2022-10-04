from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

""" Site used for this homework: http://automationpractice.com/index.php"""

"""Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)"""

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# First site: http://automationpractice.com/index.php
# browser.get("http://automationpractice.com/index.php")
# browser.maximize_window()
# sleep(2)

# search_bar = browser.find_element(by = By.ID, value="search_query_top")
# search_bar.click()
# search_bar.send_keys("dress")
# search_icon = browser.find_element(by = By.NAME, value="submit_search")
# search_icon.click()

# selenium_link = browser.find_element(by = By.PARTIAL_LINK_TEXT, value="Selenium")
# selenium_link.click()

# selenium_link = browser.find_element(by = By.LINK_TEXT, value="Selenium Framework")
# selenium_link.click()

# logging button
# login_button = browser.find_element(by = By.CLASS_NAME, value="login")
# login_button.click()

# bestsellerbutton
# bestseller_button = browser.find_element(by = By.CLASS_NAME, value="blockbestsellers")
# bestseller_button.click()

# prev_button = browser.find_element(by = By.CLASS_NAME, value="bx-prev")
# prev_button.click()

# CSS_SELECTOR
# logo = browser.find_element(by = By.CSS_SELECTOR, value= "img.logo.img-responsive")
# logo.click()

# CSS_SELECTOR
# sign_in = browser.find_element(by = By.CSS_SELECTOR, value= "div.header_user_info")
# sign_in.click()

# CSS_SELECTOR-ID
# newsletter = browser.find_element(by=By.CSS_SELECTOR, value="input#newsletter-input")
# newsletter.click()
# newsletter.send_keys("Adrian")

# newsletter = browser.find_element(by=By.CSS_SELECTOR, value="input[type = 'text']")
# newsletter.click()
# newsletter.send_keys("Adrian")

# RelativeXPath
# newsletter= browser.find_element(by = By.XPATH, value="//input[@id='newsletter-input']")
# newsletter.click()
# newsletter.send_keys("Adrian")

# XPath
# browser.set_window_size(700, 800)
# add_to_cart = browser.find_element(by=By.XPATH, value="//ul[@id='homefeatured']//li[@class='ajax_block_product col-xs-12"
#                                                       " col-sm-4 col-md-3 last-item-of-mobile-line']//span[contains"
#                                                       "(text(),'Add to cart')]")
# add_to_cart.click()


# Hover Mouse Action + index XPATH
# hover_mouse = ActionChains(browser)
# find_picture = browser.find_element(by=By.XPATH, value="(//img[@title='Faded Short Sleeve T-shirts'])[1]")
# hover_mouse.move_to_element(find_picture).perform()
# add_to_cart = browser.find_element(by=By.XPATH, value="(//span[contains(text(),'Add to cart')])[1]")
# add_to_cart.click()

# CSS_SELECTOR by class
# search = browser.find_element(by=By.CSS_SELECTOR, value="a.login")
# search.click()

# elements = browser.find_elements(by=By.TAG_NAME, value="div")
# for e in elements:
#     print(elements)
# elements[5].click()


# Second site pracitce: https://jules.app/sign-in
browser.get("https://jules.app/sign-in")
browser.maximize_window()
sleep(2)


# EMAIL INPUT
# email_input = browser.find_element(by=By.CLASS_NAME, value="MuiInputBase-input")
# email_input.click()
# email_input.send_keys("adrianmacovei17@gmail.com")

# email_input = browser.find_element(by=By.TAG_NAME, value="input")
# email_input.click()
# email_input.send_keys("adrianmacovei17@gmail.com")

# CSS_SELECTOR by class name
# email_input = browser.find_element(by=By.CSS_SELECTOR, value="input.MuiInputBase-input")
# email_input.click()
# email_input.send_keys("adrianmacovei17@gmail.com")

# relative XPATH
# email_input = browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your email']")
# email_input.click()
# email_input.send_keys("adrianmacovei17@gmail.com")

# index XPATH
# email_input = browser.find_element(by=By.XPATH, value="(//input[@placeholder='Enter your email'])[1]")
# email_input.click()
# email_input.send_keys("adrianmacovei17@gmail.com")

# PASSWORD INPUT
# pwd_input = browser.find_element(by=By.CLASS_NAME, value="MuiFilledInput-inputAdornedEnd")
# pwd_input.click()
# pwd_input.send_keys("bleah")

# CSS_SELECTOR by class name
# pwd_input = browser.find_element(by=By.CSS_SELECTOR, value="input.MuiFilledInput-inputAdornedEnd")
# pwd_input.click()
# pwd_input.send_keys("bleah")

# relative XPATH
# pwd_input = browser.find_element(by=By.XPATH, value="//input[@placeholder='Enter your password']")
# pwd_input.click()
# pwd_input.send_keys("ceva")

# index XPATH
# pwd_input = browser.find_element(by=By.XPATH, value="(//input[@placeholder='Enter your password'])[1]")
# pwd_input.click()
# pwd_input.send_keys("ceva")

# # see pwd button test

# by TAG_NAME
# eye_icon = browser.find_element(by=By.TAG_NAME, value="svg")

# by CLASS_NAME
# eye_icon = browser.find_element(by=By.CLASS_NAME, value="MuiSvgIcon-root")

# by CSS_SELECTOR class
# eye_icon = browser.find_element(by=By.CSS_SELECTOR, value="svg.MuiSvgIcon-root")

# by CSS_SELECTOR attribute
# eye_icon = browser.find_element(by=By.CSS_SELECTOR, value="svg[focusable='false'")

# by XPATH
# eye_icon = browser.find_element(by=By.XPATH, value="//div[@class='MuiInputAdornment-root MuiInputAdornment-filled "
#                                                    "MuiInputAdornment-positionEnd']//*[name()='svg']")
# eye_icon.click()

# forgot password
# forgot_pwd = browser.find_element(by=By.LINK_TEXT, value="Forgot password?")
# forgot_pwd = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Forgot pass")
# forgot_pwd.click()

# Absolute XPATH
# back_to_login = browser.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]")
# sleep(3)
# back_to_login.click()

# google_play = browser.find_element(by=By.CSS_SELECTOR, value="img[alt='Get it on Google Play']")
# google_play.click()
# app_store = browser.find_element(by=By.CSS_SELECTOR, value="img[alt='Download on the App Store']")
# app_store.click()

# find elem by tags - use index 2 because we have 3 img tags (0, 1, 2)
# app_store = browser.find_elements(by=By.TAG_NAME, value="img")[2]
# app_store.click()

def input_credentials(placeholder, input_value):
    input = browser.find_element(by=By.XPATH, value=f"//input[@placeholder='Enter your {placeholder}']")
    input.click()
    input.send_keys(input_value)


input_credentials("email", "adrianmacove")
input_credentials("password", "123456789")
login = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[2]/form/div/div[3]")

assert login.click(), "Wrong credentials!"

sleep(4)
