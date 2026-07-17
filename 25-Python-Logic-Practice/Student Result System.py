#Problem
#A university wants to store student information and protect students' marks.

#Python Code:
class Student:

    def __init__(self,name,rollnumber):
         self.name = name
         self.rollnumber = rollnumber
         self.__marks = 80
    
    def set_marks(self,new_marks):
         if(new_marks>0 and new_marks<=100):
            self.__marks = new_marks
            return self.__marks
         else:
              print("Invalid marks")
              

    def get_marks(self):
         return self.__marks
    
    def calculate_grade(self):
         if(self.__marks>=90 and self.__marks<=100):
              return "Grade A"
         elif(self.__marks>=80 and self.__marks<=89):
              return "Grade B"
         elif(self.__marks>=70 and self.__marks<=79):
              return "Grade C"
         elif(self.__marks>=60 and self.__marks<=69):
              return "Grade D"
         else:
              return "Grade F"
         
    def display_result(self):
         print("Student Information:")   
         print(f"Student Name:{self.name}")
         print(f"Roll Number:{self.rollnumber}")
         print(f"Marks:{self.get_marks()}")
         print(f"Grade:{self.calculate_grade()}")

student1 = Student("Aneela Hassan",1001)  
student2 = Student("Sara Ali",1002)
student1.set_marks(90) 
student1.display_result()
student2.set_marks(70)
student2.display_result()



         


