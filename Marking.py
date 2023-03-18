# By Vasilii Pustovoit with help of ChatGPT in 2023
# START OF EDITABLE PARTS------------------------------------------------------------------------

file_in = r"Pods.xlsx"  # Filename with pod distributions
file_out = r"Marks.csv"  # Output file name

# Name of the assignment. It requires the Quercus id of the assignment in order to work properly
# Retrieving this ID automatically will be implemented later
PRA_name = "PRA5 - Upload (1032967)" 

# Login credentials for Quercus.
# FOR SECURITY ADVISED TO KEEP EMPTY
login ='a'
password = 'b'
browser = 'Firefox' #Chrome or Firefox
webpg_course = "https://q.utoronto.ca/courses/296927"

GradingScheme = 'Full' # Set what grading scheme you want to use 
# Change it in the module "Grading_Schemes.py" 
# Possible schemes: PHY1610 Practical, Full, Custom

max_pod = 9  # The maximum pod number (leave it as 9)

xlsx_colors = ["FFFFFF", "D3D3D3"]  # Colors for the excel output file

# END OF EDITABLE PARTS--------------------------------------------------------------------------

# Libraries {{{
import numpy as np
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
import csv
from getpass4 import getpass
#}}}
# Modules {{{
import Grading_Schemes
from Grading_Schemes import set_grade
import Quercus
#}}}
# DEBUGGING {{{
removerows = 0  # How manay rows to remove
#}}}

# Functions definitions {{{

# Reading excel file {{{
def define_dataframes(file_in):

    # Students list
    dated = pd.read_excel(file_in, sheet_name="Pods")
    df_students = dated.values.tolist()
    df_students = list(map(list, zip(*df_students)))

    # Pod marks
    dated2 = pd.read_excel(file_in, sheet_name="Marks")
    df_marks = dated2.values.tolist()
    df_marks = list(map(list, zip(*df_marks)))

    # Remove rows at the start
    df_students = [row[removerows:] for row in df_students]

    # Names for the columns in final excel file
    Names = list(dated.columns.values)
    Names.append(PRA_name)

    return df_students, df_marks, Names
#}}}

# Grading routine{{{
def grading(df_students, df_marks, Names, GradingScheme): 

    # Extracting info from excel file {{{
    # Student List
    #students_last = df_students[lastnamecolumn]
    #students_first = df_students[firstnamecolumn]
    namecolumn = Names.index('Student')
    students_name = df_students[namecolumn]
    podnocolumn = Names.index('Pod #, 0 if absent')
    students_pod = df_students[podnocolumn]
    latenesscolumn = Names.index('Lateness') lateness = df_students[latenesscolumn]
    # print(students_pod)

    # Marks
    Excel_podno = df_marks[0]
    Excel_podmarks = df_marks[1]
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
    # }}}
    
    # Editing the column with marks {{{
    # Creating a column with marks
    marks = np.zeros(np.size(students_pod))
    df_students.append(marks)

    # Do the grading according to the scheme
    set_grade(students_pod, Pod_marks, marks, lateness,GradingScheme)

    #}}}

    # Put data into the dataframe {{{
    df_students[9] = marks
    df = pd.DataFrame(df_students)
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
    return df

#}}}

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

#}}}

#Main function

# Create dataframe with all the marks {{{

# Import data from excel file into the dataframes
df_students, df_marks, Names = define_dataframes(file_in)
print(Names)

#grading
df = grading(df_students, df_marks, Names, GradingScheme)

#}}}

# Output the dataframe into the file {{{
# Get the extension of the file
file_extension = os.path.splitext(file_out)[1]
file_extension = file_extension[1:]

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
        password = getpass("Enter your password: ")
    #import_grades_to_quercus(df, login, password, webpg_course)
#}}}

