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
from Grading_Schemes import *
from Quercus import *
#}}}
# Import configuration {{{
config = configparser.ConfigParser()
config.read('config.txt')

# Get the values from the QUERCUS section
login = config.get('QUERCUS', 'login')
password = config.get('QUERCUS', 'password')
browser = config.get('QUERCUS', 'browser')
TFA = config.get('QUERCUS', 'TFA')
webpg_course = config.get('QUERCUS', 'webpg_course')

# Get the values from the FILES section
file_in = config.get('FILES', 'file_in')
xlsx_colors = config.get('FILES', 'xlsx_colors').split(',')
#}}}

# Get students list {{{
def get_students_list(driver, section, course_info):
    # Read data from the input arrays {{{
    webpg_course = course_info[0]
    section = course_info[1]
    #}}}

    #Go to gradebook webpage
    webpg_gradebook = webpg_course + "/gradebook"
    driver.get(webpg_gradebook)
    time.sleep(2)

#}}}

# Set up the Pods.xlsx table with students {{{

if login =='':
    login = input("Enter your login: ")
if password == '':
    password = getpass("Enter your password: ")
auth_info = [login, password, browser, TFA]

driver = get_driver(browser) # Open the browser window
login_to_quercus(driver, auth_info) # Log into quercus

course_info = [webpg_course, section]
get_students_list(driver, course_info) # Import grades to quercus
#}}}
