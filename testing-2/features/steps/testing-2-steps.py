from behave import Given, When, Then
from selenium.webdriver import *
from selenium.webdriver.common.by import By

@Given("I open the Salt Lake City airport website")
def step_open_page(context):
    context.behave_driver.get("https://slcairport.com/")
@Then("I expect that the main page has the correct slogan")
def step_check_for_slogan(context):
    slogan_element = context.behave_driver.find_element(By.CSS_SELECTOR, ".homepage .inner-middle h1")
    assert slogan_element.text == "EXPERIENCE THE NEW SLC"
@Then("I expect that there is at least one picture there")
def step_check_for_picture(context):
    images = context.behave_driver.find_elements(By.CSS_SELECTOR, "img") 
    assert images != []

@Then("I want to look at Auntie Anne's restaurant")
def step_go_to_restauraunt(context):
    dining_element = context.behave_driver.find_element(By.CSS_SELECTOR, ".quick-buttons > .quick-button:nth-child(3)")
    dining_element.click()
    auntie_anne_link = context.behave_driver.find_element(By.LINK_TEXT, "Auntie Anne's")
    context.behave_driver.execute_script("arguments[0].click()", auntie_anne_link)
    assert context.behave_driver.current_url == "https://slcairport.com/dining-and-shopping/dining/auntie-annes"

@Then("I want to navigate to the about the airport page")
def step_navigate_to_about_airport(context):
    context.behave_driver.click_element(".quick-buttons > .quick-button:nth-child(6)")
    assert context.behave_driver.current_url == "https://slcairport.com/about-the-airport/"

@Then("I want to open the language menu")
def open_language_menu(context):
    context.behave_driver.click_element("a.VIpgJd-ZVi9od-xl07Ob-lTBxed")
    language_element = context.behave_driver.find_element(By.CSS_SELECTOR, "iframe.VIpgJd-ZVi9od-xl07Ob-OEVmcd")
    #context.behave_driver.pause(500)
    assert language_element.is_displayed() == True
    #context.behave_driver.pause(500)

@Then("I want to translate the website to arabic")
def step_translate_to_arabic(context):
    context.behave_driver.pause(1000)
    iframe = context.behave_driver.find_element(By.CSS_SELECTOR, "iframe.VIpgJd-ZVi9od-xl07Ob-OEVmcd")
    context.behave_driver.switch_to.frame(iframe)
    context.behave_driver.click_element("tbody > tr td:nth-child(1) a:nth-child(2)")
    context.behave_driver.switch_to.default_content()
    context.behave_driver.pause(5000)
    exit_frame = context.behave_driver.find_element(By.CSS_SELECTOR, "div.skiptranslate > iframe")
    context.behave_driver.switch_to.frame(exit_frame)
    context.behave_driver.click_element("a.VIpgJd-ZVi9od-TvD9Pc-hSRGPd")

    context.behave_driver.switch_to.default_content()

@Then("I want to open the hamburger menu")
def step_open_hamburger_menu(context):
    context.behave_driver.click_element("#menu-toggle")
    nav_element = context.behave_driver.find_element(By.CSS_SELECTOR, "#main-nav")
    context.behave_driver.pause(100)

    assert nav_element.is_displayed() == True

@Then("I want to look at customer service")
def step_go_to_customer_service(context):
    context.behave_driver.click_link_text("Customer Assistance")

    assert context.behave_driver.current_url == "https://slcairport.com/customer-assistance/"

@Then("I want to go back to the home page")
def step_go_back_to_home(context):
    context.behave_driver.click_element("img.logo-responsive")
    assert context.behave_driver.current_url == "https://slcairport.com/"

@Then("I want to open up the search bar")
def step_open_search_bar(context):
    context.behave_driver.click_element("button.icon-search")
    search_input = context.behave_driver.find_element(By.CSS_SELECTOR, "input#SearchForm_Keywords")
    context.behave_driver.pause(100)

    assert search_input.is_displayed() == True

@Then("I want to navigate to Travel Tips")
def step_go_to_travel_tips(context):
    search_input = context.behave_driver.find_element(By.CSS_SELECTOR, "input#SearchForm_Keywords")

    assert search_input.is_displayed() == True

    search_input.send_keys("tips")

    context.behave_driver.click_element("input#Form_SearchForm_action_SearchFormSubmit")
    context.behave_driver.pause(500)
    link_element = context.behave_driver.find_element(By.LINK_TEXT, "Travel Tips")
    context.behave_driver.execute_script("arguments[0].click()", link_element)

    assert context.behave_driver.current_url == "https://slcairport.com/customer-assistance/security-and-baggage/"

@Then("I want to look at the airlines that service SLC")
def step_look_at_airlines(context):
    context.behave_driver.click_element(".quick-buttons > .quick-button:nth-child(1)")

    assert context.behave_driver.current_url == "https://slcairport.com/airlines-flights/"

@Then("I want to visit the Salt Lake City government website")
def step_visit_salt_lake_government(context):
    context.behave_driver.click_element("#slcgov-site-button")

    assert context.behave_driver.current_url == "https://www.slc.gov/?ref=slcairport.com"
@Then("I want to make sure the promotional video is correct")
def step_check_promotional_video(context):
    video_element = context.behave_driver.find_element(By.CSS_SELECTOR, ".background-video-wrapper > iframe")
    assert video_element.get_attribute("src") == "https://player.vimeo.com/video/1020761903?h=81521909d5&api=1&background=1&autoplay=1&loop=1&autopause=0&muted=1"

@Then("I want to make sure the airport logo is displayed")
def step_check_airport_logo(context):
    logo_element = context.behave_driver.find_element(By.CSS_SELECTOR, "img.logo-responsive")

    assert logo_element.get_attribute("src") == "https://slcairport.com/dist/img/slc-intl-airport-logo.png"

@Then("I want to navigate to the accessibility page using the header button")
def step_navigate_to_accessibility(context):
    context.behave_driver.click_element(".header-access > a")
    assert context.behave_driver.current_url == "https://slcairport.com/customer-assistance/accessibility/"

@Then("I want to navigate to the medical assistance page")
def step_navigate_to_medical_assistance(context):
    #for whatever reason the link is not visible at smaller sizes so the console needs to send the click
    link_element = context.behave_driver.find_element(By.CSS_SELECTOR, "#collapseSidebarNav > ul > li:nth-child(2) > a")
    context.behave_driver.execute_script("arguments[0].click()", link_element)
    #context.behave_driver.click_element("#collapseSidebarNav > ul > li:nth-child(2) > a")

    assert context.behave_driver.current_url == "https://slcairport.com/customer-assistance/medical-assistance/"