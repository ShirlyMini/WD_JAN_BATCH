Feature: NopCommerce login Data Driven approach
#  Scenario Outline: NopCommerce Verify Login
  Scenario Template: NopCommerce Verify Login
    Given Launch browser
    When  Launch Nopcommerce website
    And Enter Username "<username>" and Password "<password>"
    And Click Login button
    Then Verify Dashborad page with status "<expected>"

    Examples:
      |  username           | password  | expected  |
      | admin@yourstore.com | admin     | True      |
      | admin               | admin     | False     |
      | xyz@gmail.com       | abcdef    | False     |
      | admin@your.com      | admin     | False      |