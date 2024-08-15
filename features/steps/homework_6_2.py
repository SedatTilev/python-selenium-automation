from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Go to cart')
def go_to_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(2)


@then('Verify cart is empty')
def verify_cart(context):
    context.app.cart_result_page.verify_cart_result()

