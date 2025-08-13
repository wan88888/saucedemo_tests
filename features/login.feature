Feature: Login to SauceDemo

  Scenario: Successful login
    Given the user is on the SauceDemo login page
    When they enter valid credentials
    Then they should be redirected to the inventory page