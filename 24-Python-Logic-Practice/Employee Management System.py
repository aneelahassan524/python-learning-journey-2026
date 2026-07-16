# A software company wants to manage its employees.

#Human Thinking
# Every employee belongs to one company.
# Every developer is also an employee.
# The parent stores common information.
# The child stores programming language.
# Use inheritance to avoid duplicate code.
# Override display().
# Use super() to print employee details first.
# Then print programming language.
# The class method changes the company
# for every employee.
# The static method checks salary validity.
# Create two developers.
# Display before and after changing company.
# Check salary.

#Pseudocode
# START
# Create Employee class.
# Add class variable.
# Create constructor.
# Create display method.
# Create class method.
# Create static method.
# Create Developer class.
# Inherit Employee.
# Add programming language.
# Override display().
# Use super().
# Create two objects.
# Display both.
# Change company.
# Display again.
# Validate salaries.
# END

#Python Code:
class Employee:

    company_name = "Tech Solutions Pvt Ltd"

    def __init__(self,employee_name,employee_id,salary):
      self.employee_name = employee_name
      self.employee_id = employee_id
      self.salary = salary


    def display_employee(self):
       print(f"Company Name:{self.company_name}")
       print(f"Employee Name:{self.employee_name}")
       print(f"Employee ID:{self.employee_id}")
       print(f"Salary:{self.salary}")


    @ classmethod
    def change_company(cls,new_company):
       cls.company_name = new_company
       print(f"New Company Name:{cls.company_name}")

    @ staticmethod
    def is_valid_salary(salary):
       if(salary>=30000):
          print("Valid Salary") 
       else:
          print("Invalid Salary")

class Developer(Employee):
   
   def __init__(self,employee_name,employee_id,salary,programming_language):
      super().__init__(employee_name,employee_id,salary)
      self.programming_language = programming_language

   def display_employee(self):
       super().display_employee()
       print(f"Programming Language:{self.programming_language}")


developer1 = Developer("Ahmed Khan","EMP101",28000,"Java")
developer2 = Developer("Aneela Hassan","EMP102",55000,"Python")

developer1.change_company("OpenTech Solutions")
developer1.display_employee()
developer2.display_employee()
Employee.is_valid_salary(developer2.salary)


             

         