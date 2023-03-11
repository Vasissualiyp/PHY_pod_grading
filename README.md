# PHY_pod_grading
A small script that helps me to grade the students in their respective pods.

I use this for PHY courses at the Unviersity of Toronto.

It does a very simple thing: Takes an excel spreadsheet with 2 sheets: Pods and Marks.

The first sheet contains assignment of students to their pods, as well as their attendance.

The second sheet contains the marks for the entire pod.

Alter formula inside of the code to suit your needs

Formula for marks in the current code: Student_mark = Pod_Mark + Attendance_Mark

Attendance_mark is max 2, 1 if student is late (a separate column in the excel spreadsheet)

Pod_Mark is the mark for the group of students, with max being 6



The code then takes the marks of pods and students' attendance into consideration, and makes it into a nice ordered spreadsheet that is easy to put into quercus (grading website powered by canvas).

In the future, I am planning to automate uploading of marks to quercus so that everything is completely automatic.