Reportcard={}
name = input("Enter your name:")
m1 = int(input("Enter your python marks:"))
m2 = int(input("Enter your c++ marks:")) 
m3 = int(input("Enter your java marks:")) 
Reportcard ={
    "Name":name,
    "Python marks":m1,
    "C++ marks":m2,
    "Java marks":m3
}
print(f"Report card:{Reportcard}")
total_marks = 300
total = m1+m2+m3
print(f"Total:{total}")
average = total/3
print(f"The average of marks is:{average}")
percentage = (total/total_marks)*100
print(f"The percentage of marks is:{percentage}")