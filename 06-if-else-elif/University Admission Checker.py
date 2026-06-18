m1 = int(input("Enter your Math Marks:"))
m2 = int(input("Enter your English Marks:"))
score = int(input("Enter your Interview Scores:"))   
print("UNIVERSITY ADMISSION")
if(m1>=70 and m2>=60 and score>= 75):
    print("Eligible")
    print("Result:\n\tAdmission Approved")
if(m1<70):
    print("Math Marks Below Requirement")
if(m2<60):
    print("English Marks Below Requirement")
if(score<75):
    print("Interview Score Below Requirement")
    print("Result:\n\tAdmission Rejected")


