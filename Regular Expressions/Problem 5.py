import re

company_report = """
==========================
ABC SOFTWARE COMPANY
==========================

Employee Name : Ali Khan
Employee ID   : EMP-1001
Department    : Software Development
Email         : ali.khan@gmail.com
Phone         : 03001234567
Password      : Python@123
Salary        : 85000 PKR

-------------------------------------

Employee Name : Sara Ahmed
Employee ID   : EMP-1002
Department    : HR
Email         : sara_99@yahoo.com
Phone         : 03111234567
Password      : sara123
Salary        : 72000 PKR

-------------------------------------

Employee Name : Ahmed Raza
Employee ID   : EMP-1003
Department    : Finance
Email         : ahmed.dev@company.pk
Phone         : 03221234567
Password      : Finance#2026
Salary        : 91000 PKR

-------------------------------------

Employee Name : Bilal Hassan
Employee ID   : EMP-1004
Department    : Sales
Email         : bilal123@hotmail.com
Phone         : 03331234567
Password      : Bilal@2025
Salary        : 68000 PKR


Meeting Date : 25-06-2026
Meeting Time : 10:30 AM

Company Website
https://www.abcsoftware.com
""" 

invoice = """
Invoice No : INV-2026-101

Laptop ............. 85000 PKR
Mouse .............. 1200 PKR
Keyboard ........... 3500 PKR
Monitor ............ 42000 PKR
Headphones ......... 5600 PKR
USB Cable .......... 800 PKR
Printer ............ 18000 PKR
Webcam ............. 7500 PKR

"""


#Extract all email addresses.
emails = re.findall(r"[\w.]+@\w+\.\w+", company_report)
print(emails)

#Extract All Phone Numbers.
phone_numbers = re.findall(r"03\d+",company_report)
print(phone_numbers)

#Extract only the employee IDs.
employee_ids = re.findall(r"EMP-\d+", company_report)
print(employee_ids)

#Extract All Prices from an Invoice.
prices = re.findall(r"\d+", invoice)
print(prices)

#Password Validation.

passwords = [
    "Python123",
    "python@123",
    "PYTHON@123",
    "Python@123",
    "Pass1!",
    "Strong#Password9",
    "HelloWorld",
    "Admin@2026",
    "Bank$2025",
    "abcDEF123!"
]

for password in passwords:

    if (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password) and
        re.search(r"[@#$%&!]", password)
    ):
        print(f"{password} → Valid Password")

    else:
        print(f"{password} → Invalid Password")
