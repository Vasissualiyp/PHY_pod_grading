# By Vasilii Pustovoit with help of ChatGPT in 2023
import numpy as np
def set_grade(students_pod, Pod_marks, marks, lateness, GradingScheme):
    for i in range(0, np.size(marks)):
        PodNo = int(students_pod[i])
        if GradingScheme == 'PHY1610_Practical':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif PodNo != 0:
                marks[i] = marks[i] + 2
        if GradingScheme == 'PHY131_Practical_W2025':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif PodNo != 0:
                marks[i] = marks[i] + 2
        if GradingScheme == 'Grades_Column':
            PodMark = Pod_marks[PodNo] * 0
            marks[i] = PodMark + lateness[i]
        if GradingScheme == 'Full':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif lateness[i] == "No Work":
                marks[i] = marks[i] + 2 - 6*0.25 
            elif PodNo != 0:
                marks[i] = marks[i] + 2
        if GradingScheme == 'Custom':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif lateness[i] == "No Work":
                marks[i] = marks[i] + 2 - 6*0.25 
            elif PodNo != 0:
                marks[i] = marks[i] + 2
    return marks
