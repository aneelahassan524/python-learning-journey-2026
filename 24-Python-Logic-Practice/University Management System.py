# Problem
# A university wants to manage graduate students.

#Human Thinking
# Start with the Person class.
# Store common information (name and age).
# Student is also a Person.
# It should inherit Person.
# Add roll number.
# GraduateStudent is also a Student.
# It should inherit Student.
# Add thesis topic.
# Use super() to avoid rewriting code.
# Create one display() method that prints all information.
# Create two graduate student objects.
# Display both students.

#Pseudocode
# START
# Create Person class.
# Create Student class.
# Inherit Person.
# Use super().
# Create GraduateStudent class.
# Inherit Student.
# Use super().
# Create display() method.
# Create two objects.
# Display information.
# END

#Python Code:
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age 

class Student(Person):

    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno = rollno


class GraduateStudent(Student):

    def __init__(self,name,age,rollno,thesis_topic):
        super().__init__(name,age,rollno)
        self.thesis_topic =  thesis_topic

    def display(self):
        print("Information:")          
        print(f"Name:{self.name}")   
        print(f"Age:{self.age}")   
        print(f"Roll Number:{self.rollno}")
        print(f"Thesis Topic:{self.thesis_topic}")

student1 = GraduateStudent("Aneela",25,11220,"Photosynthesis")                                  
student1.display()
