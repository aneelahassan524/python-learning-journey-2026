class student:

    university = "ABC University"

    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = student("Sara",20) 
student2 = student("Bilal",24) 
student3 = student("Ahmed",21)

student2.university = "XYZ University"

print(student1.name)
print(student1.university)
print(student2.age)
print(student2.university)
