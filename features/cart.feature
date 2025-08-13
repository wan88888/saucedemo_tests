Feature: Shopping Cart Functionality

  Background:
    Given the user is logged in to SauceDemo

  Scenario: Add item to cart
    When the user adds an item to the cart
    Then the cart should contain 1 item
    And the cart icon should show the item count

  Scenario: View cart contents
    Given the user has added an item to the cart
    When the user goes to the cart page
    Then the cart should display the added item
    And the item details should be correct

  Scenario: Remove item from cart
    Given the user has added an item to the cart
    And the user is on the cart page
    When the user removes the item from cart
    Then the cart should be empty

  Scenario: Continue shopping from cart
    Given the user has added an item to the cart
    And the user is on the cart page
    When the user clicks continue shopping
    Then the user should be redirected to the inventory page