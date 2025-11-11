Feature: Testing the Salt Lake City airport website
    As a traveler
    I want to browse the Salt Lake City airport website
    So that I can see what's available at the airport

Scenario: I want to make sure the front page slogan is correct
    Given I open the Salt Lake City airport website
    Then I expect that the main page has the correct slogan
Scenario: I want to make sure the promotional video on the home page is correct
    Given I open the Salt Lake City airport website
    Then I want to make sure the promotional video is correct
Scenario: I want to make sure the salt lake city airport logo is displayed
    Given I open the Salt Lake City airport website
    Then I want to make sure the airport logo is displayed
Scenario: I want to look at Auntie Anne's restaurant
    Given I open the Salt Lake City airport website
    Then I want to look at Auntie Anne's restaurant
Scenario: I want to navigate to accessibility using the header button
    Given I open the Salt Lake City airport website
    Then I want to navigate to the accessibility page using the header button
Scenario: I want to view the medical assistance page
    Given I open the Salt Lake City airport website
    Then I want to navigate to the accessibility page using the header button
    Then I want to navigate to the medical assistance page
Scenario: I want to view more information about the airport
    Given I open the Salt Lake City airport website
    Then I want to navigate to the about the airport page
Scenario: I want to translate the website into Arabic
    Given I open the Salt Lake City airport website
    Then I want to open the language menu
    Then I want to translate the website to Arabic
Scenario: I want to open the hamburger menu to see what resources are in there
    Given I open the Salt Lake City airport website
    Then I want to open the hamburger menu
Scenario: I want to access customer assistance from the hamburger menu
    Given I open the Salt Lake City airport website
    Then I want to open the hamburger menu
    Then I want to look at customer service
Scenario: I want to go back to the home page from auntie anne's restaurant
    Given I open the Salt Lake City airport website
    Then I want to look at Auntie Anne's restaurant
    Then I want to go back to the home page
Scenario: I want to open up the builtin keyword search
    Given I open the Salt Lake City airport website
    Then I want to open up the search bar
Scenario: I want to search for travelling tips using the builtin search
    Given I open the Salt Lake City airport website
    Then I want to open up the search bar
    Then I want to navigate to Travel Tips
Scenario: I want to look at the airlines that service the Salt Lake City Airport
    Given I open the Salt Lake City airport website
    Then I want to look at the airlines that service SLC
Scenario: I want to visit the website for the Salt Lake City government
    Given I open the Salt Lake City airport website
    Then I want to visit the Salt Lake City government website
