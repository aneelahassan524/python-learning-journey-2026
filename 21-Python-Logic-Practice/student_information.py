class student:
    school = "The City School"
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
student1 = student("Sara",20,80)        
student2 = student("Ahmed",21,85)
print(student1.name)
print(student1.school)
print(student2.age)
print(student2.school)
