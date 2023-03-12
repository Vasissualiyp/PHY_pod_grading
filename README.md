# Overview
A small script that I developed as a TA. It helps me to grade the students in their respective pods.

I use this for PHY courses at the Unviersity of Toronto.

It does a very simple thing: Takes an excel spreadsheet with 2 sheets: Pods and Marks.

The first sheet contains assignment of students to their pods, as well as their attendance.

The second sheet contains the marks for the entire pod.

Alter formula inside of the code to suit your needs.

Formula for marks in the current code: Student_mark = Pod_Mark + Attendance_Mark.

Attendance_mark is max 2, 1 if student is late (a separate column in the excel spreadsheet)

Pod_Mark is the mark for the group of students, with max being 6.

The code then takes the marks of pods and students' attendance into consideration, and makes it into a nice ordered spreadsheet that is easy to put into quercus (grading website powered by canvas).

In the future, I am planning to automate uploading of marks to quercus so that everything is completely automatic. For now, you still have to put in the course webpage


# Input and Output
The input to the code the Excel file "Pods.xlsx". Inside of this spreadsheet, you have two sheets: one that contains the names of the students and all relevant information for inputting marks to Quercus, their pods, and the second sheet that contains the marks for each pod. The output of the code is a CSV file named "Marks.csv" that contains the final processed data. 

You can choose to export the marks into the xlsx file instead, without uploading them to Quercus.

# Quercus marks upload
In order to upload the marks to Quercus, first you have to give the webpage of your course's gradebook. Example is provided in the script.

For now, you also have to give the ID of the assignment. It is a little bit tricky to do, but the process goes like this:
1. On the "modules" webpage of your course, find the assignment of interest that you want to mark. For me it was "PRA5 - Upload"
2. Right click on the link that would redirect you to the assignment.
3. Find the "inspect" option
4. Somewhere in the pop-up window there should be a highlighted html code that describes this element on the webpage. Find the part that states its ID.
5. Put the updated name into the script. For me, that was "PRA5 - Upload (123456)"

# Libraries Used
The following libraries are used in the code:

* numpy
* os
* pandas
* openpyxl
* csv
* selenium
