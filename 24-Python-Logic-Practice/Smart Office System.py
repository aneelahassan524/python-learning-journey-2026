# Problem
# A company wants to build a Smart Office System.

#Human Thinking
# There are two parent classes.
# One parent stores computer information.
# Another parent stores printer information.
# SmartOffice combines both.
# Since SmartOffice has both devices,
# it should inherit from both classes.
# Store office name separately.
# Create one object.
# Display all information.
# Call all methods.

# Pseudocode
# START
# Create Computer class.
# Store computer name.
# Create Printer class.
# Store printer name.
# Create SmartOffice class.
# Inherit Computer and Printer.
# Store office name.
# Create display method.
# Create one object.
# Display information.
# Call all methods.
# END

#Python Code:
class Computer:

    def __init__(self,computer_name):
        self.computer_name = computer_name

    def start_computer(self):
        print("Computer Started")    

class Printer:

    def __init__(self,printer_name):
        self.printer_name = printer_name

    def print_document(self):
        print("Printing Document...")   

class  SmartOffice(Computer,Printer):
     
     def __init__(self,computer_name,printer_name,office_name):
         Computer.__init__(self,computer_name)
         Printer.__init__(self,printer_name)
         self.office_name = office_name

     def office_status(self):
         print("Smart Office is Ready")  

     def display(self):
         print(f"Computer Name:{self.computer_name}")
         print(f"Printer Name:{self.printer_name}")
         print(f"Office Name:{self.office_name}")

office1 = SmartOffice("Lenovo ThinkCentre M70","Canon PIXMA G3010","Islamabad Regional Office") 

office1.start_computer()
office1.print_document()
office1.office_status()
office1.display()