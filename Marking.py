# By Vasilii Pustovoit with help of ChatGPT in Q1 2023

#Libraries import {{{
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
#}}}

# START OF EDITABLE PARTS-------------------------------------------------------------

file_in = r"Pods.xlsx"  # Filename with pod distributions, marks

file_out = r"Marks.xlsx"  # Output file name

lastnamecolumn = 1  # ID of column with the last names of students
firstnamecolumn = 2  # ID of column with the first names of students
podnocolumn = 8  # ID of column with the pod numbers of students
latenesscolumn = 9  # ID of column with the lateness of students

removerows = 0  # How mnay rows to remove

max_pod = 9  # The maximum pod number (leave it as 9)

xlsx_colors = ["FFFFFF", "D3D3D3"]  # Colors for the excel output file. Will alternate row coloring between all of them
# END OF EDITABLE PARTS--------------------------------------------------------------


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

# Reading excel file and altering it {{{
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
#}}}

# Making itself {{{
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
#}}}

#Writing marks into the output excel file {{{
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
        "original Pod # ",
    ],
    axis=1,
)
NewNames = ["Last", "First", "Pod#", "Late", "Mark"]
df.columns = NewNames

#Write to excel, apply coloring
write_to_excel_with_alternating_colors(df, xlsx_colors, file_out)
#}}}



"""
#QUERCUS IMPORTING {{{

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def import_grades_to_quercus(df, username, password):
    # Launch the webdriver and navigate to the Quercus login page
    driver = webdriver.Chrome()
    driver.get("https://q.utoronto.ca")
    time.sleep(3)

    # Enter the login information and submit the form
    username_field = driver.find_element('name',"j_username")
    username_field.send_keys(username)
    password_field = driver.find_element('name',"j_password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load and navigate to the gradebook page
    time.sleep(5)
    driver.get("https://quercus.utoronto.ca/courses/12345/grades")

    # Iterate over the rows in the DataFrame and enter each grade into the appropriate field
    for i, row in df.iterrows():
        # Find the appropriate field using its name or id attribute
        assignment_name = 'PRA4 - Upload'
        grade = row['Marks']
        field = driver.find_element_by_css_selector(f"input[name='{assignment_name}']")
        field.clear()
        field.send_keys(str(grade))
        field.send_keys(Keys.RETURN)
        time.sleep(1)

    # Close the webdriver
    driver.quit()
#}}}
"""
