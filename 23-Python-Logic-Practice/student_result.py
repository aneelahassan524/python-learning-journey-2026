# Program: Student Result System
class Student:
     
     school = "ABC School"

     def __init__(self,name,marks):
          self.name = name
          self.marks = marks

     def display_info(self):
               print(f"Name:{self.name}\nMarks:{self.marks}")

     @ classmethod
     def show_school(cls):
            print(f"School Name:{cls.school}")

     @ staticmethod
     def pass_marks(marks):
            if(marks<40):
                   print("Fail")
            else:
                   print("Pass")

student1 = Student("Ahmed",45)    
student2 = Student("Sara",90) 
student3 = Student("Bilal",35) 

student1.display_info()
student2.show_school()
student3.pass_marks(student3.marks)
       




