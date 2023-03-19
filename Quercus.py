# By Vasilii Pustovoit with help of ChatGPT in 2023
# Libraries {{{
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
#}}}

# Function that imports the dataframe df to quercus {{{
def import_grades_to_quercus(df, username, password, webpg_course, assignment):

    # Log in with your account {{{
    # Launch the webdriver and navigate to the Quercus login page
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    if browser == 'Firefox':
        driver = webdriver.Firefox()
    driver.get("https://q.utoronto.ca")
    
    # Enter the login information and submit the form
    username_field = driver.find_element('name',"j_username")
    username_field.send_keys(username)
    password_field = driver.find_element('name',"j_password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    # Two Factor Authentification {{{
    if TFA=='Duo':
        # Wait for the page to load and navigate to the gradebook page
        time.sleep(2)
        iframe = driver.find_element_by_id('duo_iframe')
        driver.switch_to.frame(iframe)
        
        # locate and click the "Send Me a Push" button
        push_button = driver.find_element_by_xpath("//button[contains(text(),'Send Me a Push')]")
        push_button.click()
        time.sleep(4)
    #}}}

    #}}}    
    
    # Get the assignment id {{{
    course_id = get_assignment_id(driver, webpg_course, assignment)   
    print(course_id)
    #}}}
    
    ##GRADEBOOK APPROACH 2
    ##Go to gradebook webpage
    #webpg_gradebook = webpg_course + "/gradebook_upload/new"
    #driver.get("https://q.utoronto.ca/courses/296927/gradebook_upload/new")
    #time.sleep(2)
    #upload_input = driver.find_element('id',"gradebook_upload_uploaded_data")
    #upload_input.send_keys(out_path)
    #
    ##Click button to upload    
    #upload_button = driver.find_element_by_xpath('//input[@type="submit" and @name="commit" and @value="Upload Data"]')
    #upload_button.click()
    #
    ##Click button to save changes
    #time.sleep(5)
    #form_element = driver.find_element_by_css_selector('form')
    #save_changes_button = driver.find_element_by_css_selector('#gradebook_grid_form > div.button-container > button')
    #save_changes_button.click()
    ##time.sleep(4)
    
    #Handle the pop-up alert window (failed) {{{
    #alert = Alert(driver)
    #alert.accept()
    #driver.switch_to.window(driver.window_handles[-1])
    #driver.find_element_by_tag_name("body").send_keys(Keys.ENTER)
    #}}}
    
    #Approaches that failed {{{
    #GRADEBOOK APPROACH 1
    """
    time.sleep(2)
    # Find the search bar element and enter text
    search_bar = driver.find_element_by_id("assignments-filter")
    search_bar.click()
    search_bar.send_keys("PRA5 - Upload")
    
    # Press the enter key to submit the search
    search_bar.send_keys(Keys.ENTER)
    
    time.sleep(2)    
    element = driver.find_element_by_id("assignments-filter")
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(2)
    # send the down arrow key to simulate opening the dropdown
    driver.send_keys(Keys.ARROW_DOWN)
    """
    
    """
    #SPEEDGRADER APPROACH
    #Go to course webpage
    driver.get("https://q.utoronto.ca/courses/296927/modules")
    
    #Go to the practical speed grader page
    link = driver.find_element_by_link_text('PRA5 - Upload')
    link.click()
    link = driver.find_element_by_css_selector("a.icon-speed-grader")
    link.click()
    
    time.sleep(5)
    with open('pagesource.txt', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    f.close()
    
    
    
    
    # find the input box element
    #input_box = wait.until(EC.presence_of_element_located((By.ID, "grading-box-extended")))
    input_box = driver.find_element_by_class_name('criterion_points')
    input_box.send_keys("8")
    
    # find the button element
    button = driver.find_element_by_css_selector("i.icon-arrow-right.next")
    action = ActionChains(driver)
    action.move_to_element(button).click().perform()
    
    print(driver.page_source)
    
    """
    #}}}

    # Close the webdriver
    driver.quit()
#}}}

# This function gets a link from the element that contains a certain string {{{
def get_link_for_element_with_string(driver, url, search_string):
    driver.get(url)
    element = driver.find_element_by_xpath(f"//a[contains(text(), '{search_string}')]")
    link = element.get_attribute('href')
    return link
#}}}

def get_assignment_id(driver, url, search_string):
    link = get_link_for_element_with_string(driver, url, search_string)
    ID = link.rsplit('/', 1)[-1]
    ID = ID[1:]
    return ID
