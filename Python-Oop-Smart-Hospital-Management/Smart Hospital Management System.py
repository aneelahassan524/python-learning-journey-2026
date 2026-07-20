#Project : "Smart Hospital Management System"


class Person:
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age
        self.gender = gender 
    

    def work(self):
        print("Person is handling patients.")  

    hospital_name = "City Care Hospital"

    @classmethod
    def show_hospital_name(cls):
        print(f"Hospital Name:{cls.hospital_name}")

    def change_hospital_name(self,new_name): 
        Person.hospital_name = new_name
        return Person.hospital_name
    
    @staticmethod
    def validate_age(age):
        if(age<=120):
            print("Valid Age")
        else:
            print("Invalid Age")    

    def display_info(self):
        print("Person Information:")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        print(f"Hospital Name:{self.hospital_name}")

class Doctor(Person):
    def __init__(self,name,age,gender,doctor_id,specialization):
        super().__init__(name, age, gender)  
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.__salary = 50000

    def work(self):
        print("Doctor is treating patients.")

    def diagnose(self):
      print("Doctor has diagnosed the patient.")

    def set_salary(self,salary):
     self.__salary = salary
     return self.__salary

    def get_salary(self):
        return self.__salary
    
    def book_appointment(self):
        if(self.doctor_id):
          print(f"Doctor ID:{self.doctor_id}") 
        if(self.specialization):  
          print(F"Specialization:{self.specialization}")


    
class Patient(Person):
    def __init__(self, name, age, gender,patient_id,disease):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.disease = disease
        self.__bill = 10000


    def work(self):
        print("Patient is receiving treatment.")

    def admit(self,status):
        self.status = status
        if(self.status=="Admitted"):
            print("Patient admitted successfully.")
        else:    
           print("Patient is not admitted.")

    def discharge(self,status):
        self.status = status
        if(self.status=="Discharged"):
            print("Patient discharged successfully.") 

    def set_bill(self,bill):
        self.__bill = bill
        return self.__bill
    
    def get_bill(self):
        return self.__bill

    
    def __add__(self,other_patient):
        return self.__bill+other_patient.__bill
    
class Nurse(Person):
    def __init__(self, name, age, gender,nurse_id,department):
         super().__init__(name, age, gender)  
         self.nurse_id = nurse_id
         self.department = department

    def assist_doctor(self):
       print("Nurse is assisting the doctor.")

class HospitalAssistant(Doctor):

    def __init__(self, name, age, gender,doctor_id, specialization,shift):

        Doctor.__init__(self,name,age,gender,doctor_id,specialization)
        self.shift = shift

    def work(self):
        print("Hospital Assistant is handling emergency cases.")

from abc import ABC,abstractmethod


class Payment(ABC):
    @ abstractmethod
    def pay(self,amount):
        pass

class cashPayment(Payment):  

    def pay(self,amount):
        self.amount = amount
        print("Processing Cash Payment.....")
        print(f"Amount Paid:{self.amount}")
        print("Payment Successfully")


class CardPayment(Payment):

    def pay(self,amount):
        self.amount = amount
        print("Processing Card Payment.....")
        print(f"Amount Paid:{self.amount}")
        print("Payment Successfully")
        
        
class OnlinePayment(Payment):

    def pay(self,amount):
        self.amount = amount
        print("Processing Online Payment.....")
        print(f"Amount Paid:{self.amount}")
        print("Payment Successfully")




person = Person("Ahmed Khan",45,"Male")
person.change_hospital_name("HealthFirst Hospital")
person.work()
person.validate_age(person.age)
person.display_info()

doctor1 = Doctor(
    name="Ahmed Khan",
    age=45,
    gender="Male",
    doctor_id="DOC101",
    specialization="Cardiologist"
)
doctor2 = Doctor(
    name="Bilal Ahmed",
    age=50,
    gender="Male",
    doctor_id="DOC103",
    specialization="Orthopedic Surgeon"
)
doctor1.work()
doctor1.diagnose()
doctor1.set_salary(200000)
print(f"Doctor Salary:{doctor1.get_salary()}")
doctor1.book_appointment()
doctor2.work()
doctor2.diagnose()
doctor2.set_salary(400000)
print(f"Doctor Salary:{doctor2.get_salary()}")
doctor2.book_appointment()

patient1 = Patient(
    name="Aneela Hassan",
    age=20,
    gender="Female",
    patient_id="PAT101",
    disease="Typhoid"
)
patient2 = Patient(
    name="Sara Ahmed",
    age=25,
    gender="Female",
    patient_id="PAT102",
    disease="Asthma"
)
patient1.work()
patient1.admit("Admitted")
patient1.discharge("Discharged")
patient1.set_bill(10000)
print(f"Patient Bill:{patient1.get_bill()}")
patient2.work()
patient2.admit("Admitted")
patient2.discharge("Discharged")
patient2.set_bill(20000)
print(f"Patient Bill:{patient2.get_bill()}")
print(f"Total Bill of Both Patients: Rs.{patient1 + patient2}")


nurse = Nurse(
    name="Sara Ali",
    age=28,
    gender="Female",
    nurse_id="NUR101",
    department="Emergency"
)
nurse.assist_doctor()

assistant =  HospitalAssistant(
    name="Bilal Ahmed",
    age=35,
    gender="Male",
    doctor_id="DOC105",
    specialization="Orthopedic Surgeon",
    shift="Morning"
)
assistant.work()

cash = cashPayment()
cash.pay(5000)
card = CardPayment()
card.pay(10000)
online = OnlinePayment()
online.pay(20000)
