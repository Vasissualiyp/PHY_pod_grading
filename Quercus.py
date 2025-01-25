# By Vasilii Pustovoit with help of ChatGPT in 2023
# Libraries {{{
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
#}}}

# Get driver {{{
def get_driver(browser):
    # Launch the webdriver and navigate to the Quercus login page
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    if browser == 'Firefox':
        driver = webdriver.Firefox()
    return driver 
#}}}

# Log into quercus {{{
def login_to_quercus(driver, auth_info):
    # Read data from the input arrays {{{
    username = auth_info[0]
    password = auth_info[1]
    browser = auth_info[2]
    TFA= auth_info[3]
    #}}}
    # Log in with your account {{{
    # Enter the login information and submit the form
    driver.get("https://q.utoronto.ca")
    username_field = driver.find_element('name',"j_username")
    username_field.send_keys(username)
    password_field = driver.find_element('name',"j_password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    # Two Factor Authentification {{{
    if TFA=='Duo':
        # Wait for the page to load and navigate to the gradebook page
        time.sleep(2)
        iframe = driver.find_element('id','duo_iframe')
        driver.switch_to.frame(iframe)
        
        # locate and click the "Send Me a Push" button
        push_button = driver.find_element('xpath',"//button[contains(text(),'Send Me a Push')]")
        push_button.click()
    #}}}
    time.sleep(4)

    #}}}    
#}}}

# Function that imports the dataframe df to quercus {{{
def import_grades_to_quercus(driver, df, course_info):

    # Read data from the input arrays {{{
    webpg_course = course_info[0]
    assignment = course_info[1]
    out_path = course_info[2]
    #}}}

    
    time.sleep(5)
    print("Using Gradebook approach 2...")
    #GRADEBOOK APPROACH 2
    #Go to gradebook webpage
    webpg_gradebook = webpg_course + "/gradebook_upload/new"
    driver.get(webpg_gradebook)
    time.sleep(2)
    print("Now uploading grades...")
    upload_input = driver.find_element('id',"gradebook_upload_uploaded_data")
    upload_input.send_keys(out_path)
    
    #Click button to upload    
    upload_button = driver.find_element('xpath','//input[@type="submit" and @name="commit" and @value="Upload Data"]')
    upload_button.click()
    
    #Click button to save changes
    time.sleep(5)
    form_element = driver.find_element('css_selector','form')
    save_changes_button = driver.find_element('css_selector','#gradebook_grid_form > div.button-container > button')
    #save_changes_button.click()
    time.sleep(10)
    
    #Handle the pop-up alert window (failed) {{{
    #alert = Alert(driver)
    #alert.accept()
    #driver.switch_to.window(driver.window_handles[-1])
    #driver.find_element_by_tag_name("body").send_keys(Keys.ENTER)
    #}}}
    

    # Close the webdriver
    driver.quit()
#}}}

# This function gets a link from the element that contains a certain string {{{
def get_link_for_element_with_string(driver, url, search_string):
    driver.get(url)
    time.sleep(1)
    element = driver.find_element('xpath',f"//a[contains(text(), '{search_string}')]")
    link = element.get_attribute('href')
    print(link)
    return link
#}}}

def get_assignment_id(driver, url, search_string):
    print("Getting assignment id...")
    url = url + '/assignments'
    link = get_link_for_element_with_string(driver, url, search_string)
    ID = link.rsplit('/', 1)[-1]
    #ID = ID[1:]
    return ID

def get_students_group(driver, webpg_course, Student_group):
    time.sleep(1)
    # Go to the gradebook page
    webpg_gradebook = webpg_course + "/gradebook"
    driver.get(webpg_gradebook)
    time.sleep(2)

    x = driver.find_element('css selector', '#uOgDapYPnaO3')
    drop=Select(x)
    #drop.select_by_visible_text("Export Entire Gradebook")
    
    #element_to_click.click()
    time.sleep(2)
