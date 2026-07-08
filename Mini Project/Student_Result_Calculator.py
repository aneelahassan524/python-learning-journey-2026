#Functions:
def percentage (marks,total_marks):
    return (marks/total_marks)*100
def grade (average):
    if(average<=100 and average>=90):
        return "Grade A"
    elif(average>=80 and average<90):
        return "Grade B"
    elif(average>=70 and average<80):
        return "Grade C"
    elif(average>=60 and average<70):
        return "Grade D"
    else:
        return "Grade F"
i = 0
while True:
    
    name = input("Enter your name:")
    m1 = int(input("Enter your marks of subject 1:"))
    m2 = int(input("Enter your marks of subject 2:"))
    m3 = int(input("Enter your marks of subject 3:"))
    m4 = int(input("Enter your marks of subject 4:"))
    m5 = int(input("Enter your marks of subject 5:"))
    print(f"Student Name:{name}")
    total_marks = 500
    print(f"Maximum Marks:{total_marks}")
    marks =m1+m2+m3+m4+m5
    print(f"Obtained Marks:{marks}")
    average = marks/5
    print(f"Average:{average}")
    p = percentage(marks,total_marks)
    print(f"Percentage:{p}")
    g = grade(average)
    print(f"Grade:{g}")

    result = input("Do you want to calculate another student's result(Yes/NO)").strip().lower()
    if(result=="yes"):
        i = i+1
    else:
     break
    