from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_google(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('Go to cart')
def go_to_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(2)


@then('Verify cart is empty')
def verify_cart(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'
