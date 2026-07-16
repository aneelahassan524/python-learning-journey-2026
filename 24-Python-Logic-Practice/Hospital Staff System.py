# Problem
# A hospital wants to store information about doctors.

# Human Thinking
# Create a parent class.
# Store common information.
# Create a child class.
# Inherit the parent.
# Add doctor's specialization.
# Display all information.
# Create two objects.


# Pseudocode
# START
# Create Person class.
# Create Doctor class.
# Inherit Person.
# Add specialization.
# Display information.
# Create two objects.
# END

#Python Code:
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Doctor(Person):

    def __init__(self,name,age,specialization):
         super().__init__(name, age)
         self.specialization = specialization

    def display(self):
        print(f"Information:")  
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Specialization: {self.specialization}")   

doctor = Doctor("Ahmed",40,"Dentist")
doctor.display()
person = Person("Bilal",45)
person.name