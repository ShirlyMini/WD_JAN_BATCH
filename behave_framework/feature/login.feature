Feature: NopCommerce login
  Scenario: NopCommerce Verify homepage title
    Given Launch browser
    When  Launch Nopcommerce website
    Then Verify title of home page

  Scenario: NopCommerce Verify Login
    Given Launch browser
    When  Launch Nopcommerce website
    And Enter Username "admin@yourstore.com" and Password "admin"
    And Click Login button
    Then Verify Dashborad page
