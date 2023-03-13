# By Vasilii Pustovoit with help of ChatGPT
# Libraries {{{
import numpy as np
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
import csv
#}}}
# START OF EDITABLE PARTS------------------------------------------------------------------------

file_in = r"Pods.xlsx"  # Filename with pod distributions
file_out = r"Marks.csv"  # Output file name

# Name of the assignment. It requires the Quercus id of the assignment in order to work properly
# Retrieving this ID automatically will be implemented later
PRA_name = "PRA5 - Upload (1032967)" 

# Login credentials for Quercus.
# FOR SECURITY ADVISED TO KEEP EMPTY
login =''
password = ''
browser = 'Firefox' #Chrome or Firefox

max_pod = 9  # The maximum pod number (leave it as 9)

xlsx_colors = ["FFFFFF", "D3D3D3"]  # Colors for the excel output file

#lastnamecolumn = 1  # ID of column with the last names of students
#firstnamecolumn = 2  # ID of column with the first names of students
namecolumn = 0  # ID of column with the names of students
podnocolumn = 7  # ID of column with the pod numbers of students
latenesscolumn = 8  # ID of column with the lateness of students

removerows = 0  # How manay rows to remove

# END OF EDITABLE PARTS--------------------------------------------------------------------------

# Create dataframe with all the marks {{{

# Apply alternating coloring to the excel file of the dataframe {{{
def write_to_excel_with_alternating_colors(df, color_list, filename):
    # Create a new workbook
    wb = Workbook()

    # Select the active worksheet
    ws = wb.active

    # Write the DataFrame to the worksheet
    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    # Set alternating row colors
    for i, row in enumerate(ws.iter_rows(min_row=2)):
        fill = PatternFill(
            start_color=color_list[i % len(color_list)],
            end_color=color_list[i % len(color_list)],
            fill_type="solid",
        )
        for cell in row:
            cell.fill = fill

    # Save the workbook
    wb.save(filename)
#}}}

#Write the dataframe into the CSV file {{{
def write_to_csv(df, filename):
    # Open the output file
    with open(filename, "w", newline="", encoding="utf-8") as f:
        # Create a CSV writer object
        writer = csv.writer(f)

        # Write the DataFrame headers to the CSV file
        writer.writerow(df.columns)

        # Write the DataFrame rows to the CSV file
        for i, row in df.iterrows():
            writer.writerow(row)
#}}}

# Reading excel file {{{
# Students list
dated = pd.read_excel(file_in, sheet_name="Pods")
df2 = dated.values.tolist()
df2 = list(map(list, zip(*df2)))

# Pod marks
dated2 = pd.read_excel(file_in, sheet_name="Marks")
df1 = dated2.values.tolist()
df1 = list(map(list, zip(*df1)))

# Remove rows at the start
df2 = [row[removerows:] for row in df2]
#}}}

# Extracting info from excel file {{{
# student list
#students_last = df2[lastnamecolumn]
#students_first = df2[firstnamecolumn]
students_name = df2[namecolumn]
students_pod = df2[podnocolumn]
lateness = df2[latenesscolumn]
# print(students_pod)

# Marks
Excel_podno = df1[0]
Excel_podmarks = df1[1]
Excel_size = len(Excel_podmarks)
print(Excel_podmarks)
#}}}

# Get the marks for each pod {{{
# Initialize the array with zeros and max_pod+1 elements
Pod_marks = [0] * (max_pod + 1)

# Get the marks for each pod
for i in range(0, Excel_size):
    # print(i)
    PodNo = int(Excel_podno[i])
    Pod_marks[PodNo] = Excel_podmarks[i]

# print(Pod_marks)
#}}}

# Dataframe manipulation {{{
# Creating a column with marks
marks = np.zeros(np.size(students_pod))
df2.append(marks)


# Writing marks into the mark column
for i in range(0, np.size(marks)):
    PodNo = int(students_pod[i])
    PodMark = Pod_marks[PodNo]
    marks[i] = PodMark
    if lateness[i] == "Late":
        marks[i] = marks[i] + 1
    elif PodNo != 0:
        marks[i] = marks[i] + 2


# Names for the columns in final excel file
Names = list(dated.columns.values)
Names.append(PRA_name)


# Put data into the dataframe
df2[9] = marks
df = pd.DataFrame(df2)
df = df.T
df.columns = Names
df = df.drop(
    [
        "Original Pod #",
        "Pod #, 0 if absent",
        "Lateness"
    ],
    axis=1,
)
#NewNames = ["Last", "First", "Pod#", "Late", "Mark"]
#df.columns = NewNames
#}}}
#}}}

# Import Marks to Quercus {{{

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
def import_grades_to_quercus(df, username, password):

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

    #GRADEBOOK APPROACH 2
    #Go to course webpage
    driver.get("https://q.utoronto.ca/courses/296927/gradebook_upload/new")
    time.sleep(2)
    upload_input = driver.find_element('id',"gradebook_upload_uploaded_data")
    upload_input.send_keys(out_path)
    
    #Click button to upload    
    upload_button = driver.find_element_by_xpath('//input[@type="submit" and @name="commit" and @value="Upload Data"]')
    upload_button.click()
    
    #Click button to save changes
    time.sleep(5)
    form_element = driver.find_element_by_css_selector('form')
    save_changes_button = driver.find_element_by_css_selector('#gradebook_grid_form > div.button-container > button')
    save_changes_button.click()
    #time.sleep(4)
    
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
#}}}

# Write to file, apply coloring for excel
file_extension = os.path.splitext(file_out)[1]

# Excel output
if file_extension == 'xlsx':
    write_to_excel_with_alternating_colors(df, xlsx_colors, file_out)

# csv output + Quercus marks import
elif file_extension == 'csv':
    out_path = os.path.join(os.path.dirname(__file__), file_out).replace('\\', '/')
    write_to_csv(df, file_out)
    if login =='':
        login = input("Enter your login: ")
    if password == '':
        password = input("Enter your password: ")
    import_grades_to_quercus(df, login, password)
