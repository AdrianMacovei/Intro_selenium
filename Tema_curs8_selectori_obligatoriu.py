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
browser.get("http://automationpractice.com/index.php")
browser.maximize_window()
sleep(2)

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

#CSS_SELECTOR by class
# search = browser.find_element(by=By.CSS_SELECTOR, value="a.login")
# search.click()

# elements = browser.find_elements(by=By.TAG_NAME, value="div")
# for e in elements:
#     print(elements)
# elements[5].click()