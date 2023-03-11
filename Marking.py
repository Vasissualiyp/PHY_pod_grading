# By Vasilii Pustovoit with help of ChatGPT

import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows




# START OF EDITABLE PARTS------------------------------------------------------------------------

file_in = r"Pods.xlsx"  # Filename with pod distributions

file_out = r"Marks.xlsx"  # Output file name

lastnamecolumn = 1  # ID of column with the last names of students
firstnamecolumn = 2  # ID of column with the first names of students
podnocolumn = 8  # ID of column with the pod numbers of students
latenesscolumn = 9  # ID of column with the lateness of students

removerows = 0  # How mnay rows to remove

max_pod = 9  # The maximum pod number (leave it as 9)

xlsx_colors = ["FFFFFF", "D3D3D3"]  # Colors for the excel output file
# END OF EDITABLE PARTS--------------------------------------------------------------------------


# Apply alternating coloring to the excel file of the dataframe


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


# Reading excel file
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


# Extracting info from excel file
# student list
students_last = df2[lastnamecolumn]
students_first = df2[firstnamecolumn]
students_pod = df2[podnocolumn]
if np.shape(df2)[0] >= latenesscolumn:
    lateness = students_pod
else:
    lateness = df2[latenesscolumn]
# print(students_pod)

# Marks
Excel_podno = df1[0]
Excel_podmarks = df1[1]
Excel_size = len(Excel_podmarks)
print(Excel_podmarks)


# GET THE MARKS FOR EACH POD
# Initialize the array with zeros and max_pod+1 elements
Pod_marks = [0] * (max_pod + 1)

# Get the marks for each pod
for i in range(0, Excel_size):
    # print(i)
    PodNo = int(Excel_podno[i])
    Pod_marks[PodNo] = Excel_podmarks[i]

# print(Pod_marks)


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
Names.append("Marks")


# Put data into the dataframe
df2[10] = marks
df = pd.DataFrame(df2)
df = df.T
df.columns = Names
df = df.drop(
    [
        "new_acorn-classlist.Person ID",
        "qclass_list.Practical",
        "qclass_list.Group",
        "qclass_list.Email Address",
        "qclass_list.UTORid",
        "Original Pod #",
    ],
    axis=1,
)
NewNames = ["Last", "First", "Pod#", "Late", "Mark"]
df.columns = NewNames

#Write to excel, apply coloring
write_to_excel_with_alternating_colors(df, xlsx_colors, file_out)








#QUERCUS IMPORTING

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def import_grades_to_quercus(df, username, password):
    # Launch the webdriver and navigate to the Quercus login page
    driver = webdriver.Chrome()
    driver.get("https://q.utoronto.ca")
    #time.sleep(3)
    
    # Enter the login information and submit the form
    username_field = driver.find_element('name',"j_username")
    username_field.send_keys(username)
    password_field = driver.find_element('name',"j_password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load and navigate to the gradebook page
    time.sleep(2)
    iframe = driver.find_element_by_id('duo_iframe')
    driver.switch_to.frame(iframe)
    
    # locate and click the "Send Me a Push" button
    push_button = driver.find_element_by_xpath("//button[contains(text(),'Send Me a Push')]")
    push_button.click()
    time.sleep(4)
    
    #GRADEBOOK APPROACH
    #Go to course webpage
    driver.get("https://q.utoronto.ca/courses/296927/gradebook")
    
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
    time.sleep(10)
    # Close the webdriver
    driver.quit()


"""
login =
pqssword =
import_grades_to_quercus(df, login, password)
"""
