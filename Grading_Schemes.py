# By Vasilii Pustovoit with help of ChatGPT in 2023
import numpy as np
# Grading Schemes {{{
def set_grade(students_pod, Pod_marks, marks, lateness,GradingScheme):
    if GradingScheme == 'PHY1610 Practical': #{{{
        # Writing marks into the mark column
        for i in range(0, np.size(marks)):
            PodNo = int(students_pod[i])
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif PodNo != 0:
                marks[i] = marks[i] + 2
    #}}}
    if GradingScheme == 'Full': #{{{
        for i in range(0, np.size(marks)):
            PodNo = int(students_pod[i])
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif lateness[i] == "No Work":
                marks[i] = marks[i] + 2 - 6*0.25 
            elif PodNo != 0:
                marks[i] = marks[i] + 2
    #}}}
    if GradingScheme == 'Custom': #{{{
        for i in range(0, np.size(marks)):
            PodNo = int(students_pod[i])
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif lateness[i] == "No Work":
                marks[i] = marks[i] + 2 - 6*0.25 
            elif PodNo != 0:
                marks[i] = marks[i] + 2
    #}}}
    return marks
#}}}
