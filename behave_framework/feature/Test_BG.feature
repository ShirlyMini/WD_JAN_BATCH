Feature: NopCommerce login Scenario Background
  Background: Login to nopcommerce website
    Given Launch browser
    When  Launch Nopcommerce website
    And Enter Username "admin@yourstore.com" and Password "admin"
    And Click Login button
    Then Verify Dashborad page

  Scenario: NopCommerce Verify customer page
    When Click Customer Menu
    Then Verify Customer Dashboard

  Scenario: NopCommerce Verify Online customer page
    When Click Online Customer Menu
    Then Verify Online Customer Dashboard