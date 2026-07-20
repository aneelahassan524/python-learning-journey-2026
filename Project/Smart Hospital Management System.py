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
    def hosiptal_name(cls):
        print(f"Hospital Name:{cls.hosiptal_name}")

    def change_hospital_name(self,new_name): 
        self.hospital_name = new_name
        return self.hospital_name
    
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
    def __init__(self, name, age, gender,doctor_id,specialization):
        super().__init__(name, age, gender)  
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.__salary = 50000

    def work(self):
        print("Doctor is treating patients.")

    def diagnose(self):
        pass       

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
        print("Nurse is assisting patients.")

    def admit(self):
        pass

    def discharge(self):
        pass

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
        pass

class HospitalAssistant(Doctor,Nurse):
    def __init__(self, name, age, gender, doctor_id, specialization,shift):
        super().__init__(name, age, gender,doctor_id, specialization)  
        self.shift = shift

    def work(self):
        print("Hospital Assistant is handling emergency cases.")    



class CashPayment:
    def pay(self):
        pass
    def make_payment(payment_method):
        payment_method.pay()

class CardPayment:
    def pay(self):
        pass
    def make_payment(payment_method):
        payment_method.pay()
        
class OnlinePayment:
    def pay(self):
        pass
    def make_payment(payment_method):
        payment_method.pay()


