Feature: Test scenarios for target
  Scenario:Users can verify cart is empty
    Given Open target main page
    When Go to cart
    Then Verify cart is empty
