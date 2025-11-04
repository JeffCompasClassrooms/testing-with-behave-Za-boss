Feature: Testing with builtin behave commands
  As a [ROLE]
  I want to [GOAL]
  So that I [REASON]

  Scenario: I want to navigate to wikimedia
    Given I open the url "https://www.wikipedia.org/"
    When I move to element ".frb-header-minimize-icon svg"
    When I click on the element ".frb-header-minimize-icon svg"
    When I pause for 100ms 
    When I move to element ".frb-conversation-close"
    When I click on the element ".frb-conversation-close"
    When I click on the element ".other-project-link"
    Then I expect that the url is "https://commons.wikimedia.org/wiki/Main_Page"

  Scenario: I want to look up the article for ISBN
    Given I open the url "https://www.wikipedia.org/"
    When I add "ISBN" to the inputfield "#searchInput"
    When I press "enter"
    Then I expect that the url is "https://en.wikipedia.org/wiki/ISBN"

  Scenario: I want to look for the Henry Draper Catalogue
    Given I open the url "https://www.wikipedia.org/"
    When I add "HD" to the inputfield "#searchInput"
    When I press "enter"
    When I click on the link "Henry Draper Catalogue"
    Then I expect that the url is "https://en.wikipedia.org/wiki/Henry_Draper_Catalogue"

  Scenario: I want to navigate to an autocompleted article quickly
    Given I open the url "https://www.wikipedia.org/"
    When I move to element "#searchInput"
    When I add "ISB" to the inputfield "#searchInput"
    When I pause for 500ms
    When I press "ARROW_DOWN"
    When I pause for 500ms
    When I press "ARROW_DOWN"
    When I press "enter"
    Then I expect that the url is "https://en.wikipedia.org/wiki/ISBN"

  Scenario: I want to navigate to the wikipedia main page
    Given I open the url "https://www.wikipedia.org/"
    When I click on the element "#js-link-box-en"
    Then I expect that the url is "https://en.wikipedia.org/wiki/Main_Page"

  Scenario: I want to make sure the language list is hidden by default
    Given I open the url "https://www.wikipedia.org/"
    Then I expect that element "#js-lang-lists" is not visible

  Scenario: I want to make sure the language list pops up when I click on the relevant element
    Given I open the url "https://www.wikipedia.org/"
    Then I expect that element "#js-lang-lists" is not visible
    When I pause for 500ms
    When I click on the element ".lang-list-button-wrapper"
    When I pause for 500ms
    Then I expect that element "#js-lang-lists" is visible
    When I pause for 1500ms

  Scenario: I want to view wikipedia's creative commons license
    Given I open the url "https://www.wikipedia.org/"
    When I scroll to element ".jsl10n a"
    When I click on the link "Creative Commons Attribution-ShareAlike License" 
    Then I expect that the url is "https://creativecommons.org/licenses/by-sa/4.0/"

  Scenario: I want to navigate the article for vega from the henry draper catalogue article
    Given I open the url "https://en.wikipedia.org/wiki/Henry_Draper_Catalogue"
    When I click on the link "Vega"
    Then I expect that the url is "https://en.wikipedia.org/wiki/Vega"

  Scenario: I want to navigate to the russian wikipedia article for Roblox
    Given I open the url "https://www.wikipedia.org/"
    When I select the option with the text "Русский" for element "#searchLanguage"
    When I add "Roblox" to the inputfield "#searchInput"
    When I press "enter"
    When I pause for 500ms
    Then I expect that the url is "https://ru.wikipedia.org/wiki/Roblox"
    Given I open the url "https://www.wikipedia.org/"
    When I select the option with the text "English" for element "#searchLanguage"