class Employee:

    company = "Google"

    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary

Employee1 = Employee("Sara","IT",50000) 
Employee2 = Employee("Ahmed","Chemsitry",30000)
Employee3 = Employee("Bilal","Pakstudies",20000)

print(Employee1.name)
print(Employee2.department)
print(Employee3.salary)
print(Employee3.company)