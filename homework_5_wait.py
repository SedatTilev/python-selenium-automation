from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 15)

driver.get("https://target.com")
SIGN_IN_BUTTON = (By.XPATH, "//a[@data-test='@web/AccountLink']")
SIGN_IN_BUTTON_2 = (By.XPATH, "//a[@data-test='accountNav-signIn']")
SIGN_IN_PAGE_TEXT = (By.CSS_SELECTOR, ".sc-fe064f5c-0")
driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()
driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON_2)).click()
expected_text = 'Sign into your Target account'
actual_text = driver.wait.until(EC.presence_of_element_located(SIGN_IN_PAGE_TEXT)).text
assert actual_text == expected_text , "actual text does not match"



