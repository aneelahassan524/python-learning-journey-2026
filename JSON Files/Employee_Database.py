#A company wants to store employee information.
import json

employee = {
    "id": 101,
    "name": "Aneela",
    "department": "Software Development",
    "salary": 75000
}

with open ("employee.json","w") as file:
    json.dump(employee,file,indent=5)

with open ("employee.json","r") as file:
    employee = json.load(file)

print(f"Employee Name: {employee['name']}")
print(f"Department: {employee['department']}")
print(f"Salary: {employee['salary']}")
print(type(employee))

if employee["salary"] >= 70000:
    print("Senior Employee")
else:
    print("Junior Employee")    