# By Vasilii Pustovoit with help of ChatGPT in 2023
# Libraries {{{
import numpy as np
import os
import pandas as pd
import configparser
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
import csv
try:
    from getpass4 import getpass
except ImportError:
    from getpass import getpass
#}}}
# Modules {{{
from Grading_Schemes import set_grade
from Quercus import get_driver, login_to_quercus, import_grades_to_quercus, get_link_for_element_with_string, get_assignment_id, get_students_group
from Marking import define_dataframes, grading, write_to_excel_with_alternating_colors, write_to_csv

#}}}
# Import configuration {{{
config = configparser.ConfigParser()
config.read('config.txt')

# Get the values from the PRA section
PRA_name = config.get('PRA', 'PRA_name')
Student_Group = config.get('PRA', 'Student_group')

# Get the values from the QUERCUS section
login = config.get('QUERCUS', 'login')
password = config.get('QUERCUS', 'password')
browser = config.get('QUERCUS', 'browser')
TFA = config.get('QUERCUS', 'TFA')
webpg_course = config.get('QUERCUS', 'webpg_course')

# Get the values from the FILES section
file_in = config.get('FILES', 'file_in')
file_out = config.get('FILES', 'file_out')
xlsx_colors = config.get('FILES', 'xlsx_colors').split(',')

# Get the values from the GRADING section
GradingScheme = config.get('GRADING', 'GradingScheme')
#}}}

# DEBUGGING {{{
removerows = 0  # How manay rows to remove
max_pod = 9  # The maximum pod number (leave it as 9)
#}}}

# Functions definitions {{{

#}}}

#Main function


# Output the dataframe into the file {{{
# Get the extension of the file
file_extension = os.path.splitext(file_out)[1]
file_extension = file_extension[1:]

# Login {{{
if login =='':
    login = input("Enter your login: ")
if password == '':
    password = getpass("Enter your password: ")
auth_info = [login, password, browser, TFA]
#}}}

driver = get_driver(browser) # Open the browser window
login_to_quercus(driver, auth_info) # Log into quercus
get_students_group(driver, webpg_course, Student_Group) # Get the Student group 

# Change the name of the assignment to correctly input it later
#out_path = os.path.join(os.path.dirname(__file__), file_out).replace('\\', '/')

#course_info = [webpg_course, PRA_name, out_path]

#write_to_csv(df, file_out) # Create the file with marks to export it later
#import_grades_to_quercus(driver, df, course_info) # Import grades to quercus
#}}}

