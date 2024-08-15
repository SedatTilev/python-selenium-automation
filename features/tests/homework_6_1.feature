Feature: Test scenario for target main page

  Scenario: User can search for a product
    Given Open target page
    When Search for coffee
    Then Verify search results shown for coffee
    Then Verify correct search results URL opens for coffee


#  Scenario: Verify benefit cells amount
#    Given Open circle page
#    Then Verify page has 10 benefit cells
#
#
#  Scenario: Verify customer can add a item to the cart
#    Given Open target page
#    When Search for coffe
#    And Add a product to the cart
#    Then Go to the cart and verify customer added a product

