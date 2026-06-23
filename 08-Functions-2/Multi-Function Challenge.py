total_marks = 300
def marks (subject_1,subject_2,subject_3):
    obtained_marks = subject_1+subject_2+subject_3
    return obtained_marks
m = marks(80,70,90)
print(f"Total Marks is:{m}")
def percentage (obtained_marks):
    percentage = obtained_marks/total_marks*100
    return percentage
p = percentage(m)
print(f"Percentage is:{p}")
def grade (percentage):
    if(percentage>=90):
        return "A Grade"
    elif(percentage>=75):
        return "B Grade"
    else:
        return "C Grade"
g = grade(p)    
print(f"Grade is:{g}")
