def student_report(**student):

    for key, value in student.items():
     print(f"{key}: {value}")

    if student["marks"]>=40:
         print(f"Student Result:Pass")
    else:
        print("Student Result:Fail")    
    if student["cgpa"]>=3.5:
        print(f"Highest CGPA:{student["cgpa"]}")  

student_report(
    name="Aneela",
    age=20,
    marks=87,
    cgpa=3.8
)


