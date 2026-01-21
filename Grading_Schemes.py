# By Vasilii Pustovoit with help of ChatGPT in 2023
import numpy as np
def set_grade(students_pod, Pod_marks, marks, lateness, GradingScheme):
    for i in range(0, np.size(marks)):
        PodNo = int(students_pod[i])
        if GradingScheme == 'PHY131_Practical_W2025':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif PodNo != 0:
                marks[i] = marks[i] + 2
        elif GradingScheme == 'PHY131_Practical_W2026':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            #if lateness[i] != 0:
            #    marks[i] = marks[i]
            #elif PodNo != 0:
            #    marks[i] = marks[i]
        elif GradingScheme == 'Grades_Column':
            PodMark = Pod_marks[PodNo] * 0
            marks[i] = PodMark + lateness[i]
        elif GradingScheme == 'Full':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif lateness[i] == "No Work":
                marks[i] = marks[i] + 2 - 6*0.25 
            elif PodNo != 0:
                marks[i] = marks[i] + 2
        elif GradingScheme == 'Custom':
            PodMark = Pod_marks[PodNo]
            marks[i] = PodMark
            if lateness[i] == "Late":
                marks[i] = marks[i] + 1
            elif lateness[i] == "No Work":
                marks[i] = marks[i] + 2 - 6*0.25 
            elif PodNo != 0:
                marks[i] = marks[i] + 2
        else: 
            raise ValueError(f"Grading scheme {GradingScheme} not defined.")
    return marks

def set_grade_individual_scheme(students_pod, Pod_marks, Pod_marks_extra, marks, marks_extra, lateness, GradingScheme):
    print(f"Pod_marks: {Pod_marks}")
    print(f"Pod_marks_extra: {Pod_marks_extra}")
    individual = np.zeros_like(marks)
    for i in range(0, np.size(students_pod)):
        PodNo = int(students_pod[i])
        print(f"PodNo for student {i}: {PodNo}")
        if GradingScheme == 'PHY131_Practical_W2025':
            PodMark = Pod_marks[PodNo]
            PodMark_extra = Pod_marks_extra[PodNo]
            marks[i] = PodMark
            marks_extra[i] = PodMark_extra
            if PodNo != 0:
                individual[i] = 1
            print(f"Mark for student {i}: {PodMark}")
            print(f"Extra Mark for student {i}: {PodMark_extra}")
        elif GradingScheme == 'PHY131_Practical_W2026':
            PodMark = Pod_marks[PodNo]
            PodMark_extra = Pod_marks_extra[PodNo]
            marks[i] = PodMark
            marks_extra[i] = PodMark_extra
            if PodNo != 0:
                individual[i] = 1
            print(f"Mark for student {i}: {PodMark}")
            print(f"Extra Mark for student {i}: {PodMark_extra}")
        else: 
            print(f"Grading scheme {GradingScheme} not defined.")
            raise ValueError(f"Grading scheme {GradingScheme} not defined.")
    return [ marks, marks_extra, individual, lateness ]
