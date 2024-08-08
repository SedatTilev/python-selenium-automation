from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target page')
def open_google(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('search for {product}')
def search_product(context, product):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(3)


@then('Verify search worked for {product}')
def verify_search(context, product):
    search_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert product in search_result, f'Expected product {product} not in {search_result}'



@given('Open circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('Verify page has 10 benefit cells')
def verify_circle(context):
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, "[href='/icons/ArrowRight.svg#ArrowRight']")
    assert len(benefit_cells) == 10, f'Expected 10 benefit cells, got {len(benefit_cells)}'


@when('Add a product to the cart')
def add_product(context):
    context.driver.execute_script("window.scrollBy(0, 600);")
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor13478923").click()
    sleep(5)
    context.driver.find_element(By.XPATH, "//div[@class='h-margin-b-x2']//button[@id='addToCartButtonOrTextIdFor13478923']").click()
    sleep(2)
    context.driver.back()
    sleep(3)


@then('Go to the cart and verify customer added a product')
def verify_added_product(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(2)
    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".h-margin-b-tight.h-text-grayDark").text
    expected_text = 'subtotal'
    assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

