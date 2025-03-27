# Quickstarts 

[PHY131, Winter 2025](./docs/phy131_winter2025.md)

# Overview
A small script that I developed as a TA. It helps me to grade the students in their respective pods.
I use this for PHY courses at the Unviersity of Toronto.
It does a very simple thing: Takes an excel spreadsheet with 2 sheets: Pods and Marks.

The first sheet contains assignment of students to their pods, as well as their attendance.
The second sheet contains the marks for the entire pod.

Alter formula inside of the code to suit your needs.
Formula for marks in the current code: `Student_mark = Pod_Mark + Attendance_Mark`.
`Attendance_mark` is max 2, 1 if student is late (a separate column in the excel spreadsheet)
`Pod_Mark` is the mark for the group of students, with max being 6.

The code then takes the marks of pods and students' attendance into consideration, and makes it into a nice ordered spreadsheet that is easy to put into quercus (grading website powered by canvas) (if you have the xlsx output file type).

## Configuration
Most of the edits that you should do are located in the `config.txt` file. There you can put in your quercus login credentials, edit the name of the assignment (`PRA_name` variable), change the browser (For now Chrome and Firefox supported), give the webpage of the course, choose which grading scheme to use.

When it comes to grading schemes, you will have to manually change them in the `Grading.py` file for now.

## Input and Output
The input to the code the Excel file `Pods.xlsx`. Inside of this spreadsheet, you have two sheets: one that contains the names of the students and all relevant information for inputting marks to Quercus, their pods, and the second sheet that contains the marks for each pod. The output of the code is a CSV file named "Marks.csv" that contains the final processed data. 

You can choose to export the marks into the xlsx file instead, without uploading them to Quercus.

## Running with nix

After you install nix into your environment, run:
```
nix develop --experimental-features 'nix-command flakes
```
in the directory of this code. 

## Libraries Used
The following libraries are used in the code:

* numpy
* os
* pandas
* openpyxl
* csv
* selenium
* getpass4 or getpass
* configparser

# Quercus marks upload
**The code only can upload the marks to Quercus if you set the output file type to csv**

In order to upload the marks to Quercus, first you have to give the webpage of your course's gradebook. Example is provided in the script.

## Login to Quercus
**For security reasons, I advise you not to put in your login/password as the variables. I cannot stop you from doing that, though**

If you set the login credentials to an empty string (as it is advised), you will be prompted to enter your login information when you run the code. After that, if you have Two Factor Authentication on your account enabled, you should get a Duo security login notification and approve it - that is the script logging into your Quercus account to input the marks. You should be fast because the code might continue to act without waiting for you, and then you should just try again.

After that the script works automatically and inputs all the marks on its own.

# Setup
1. git clone this repository
2. Get the students list of your section from quercus using the gradebook (This step will be automated in the future)
3. Following the Sample Pods.xlsx file example, put in only the necessary columns into your Pods.xlsx file (This also will be automated in the future)
4. Install all required libraries (see above)
5. Install your browser driver (it should work with the python selenium library, google how to do that)
6. Edit your webpage address in the `config.txt` file. Use `sample_config.txt` as baseline.
7. Change the name of the assignment (Should be identical to one on quercus!)
8. (Recommended to skip this step) set your login credentials for quercus in `config.txt`
9. (Optional) Create your grading scheme in `Grading.py` and set its name in `config.txt`. See the grading scheme 'Full' as an example.
10. Run `Marking.py` with python
11. If you have 2FA enabled, be ready to use it on your phone. You have to be fast to do that
12. Once the code runs, you should confirm that the uploaded marks are truthful.

**USE AT YOUR OWN RISK!**
