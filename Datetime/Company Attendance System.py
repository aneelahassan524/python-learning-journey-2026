from datetime import datetime

current = datetime.now()

print("Employee: Aneela Hassan")
print(f"Login Date: {current.strftime('%d-%m-%Y')}")
print(f"Login Time: {current.strftime('%I:%M %p')}")
print(f"Month: {current.strftime('%B')}")
print(f"Year: {current.strftime('%Y')}")