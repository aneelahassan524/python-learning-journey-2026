with open("student.txt","w") as file:
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    city = input("Enter your city:")
    file.write(f"Name:{name}") 
    file.write(f"\nAge:{age}")
    file.write(f"\nCity:{city}")
