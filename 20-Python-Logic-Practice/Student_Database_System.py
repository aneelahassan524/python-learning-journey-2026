students = {
    "Ali": 85,
    "Sara": 92,
    "Aneela": 95,
    "Ahmed": 78
}
try:
    name = input("Enter student name:")
    number = int(input("Enter a number to divide:"))
    print(f"Student Marks:{students[name]}")
    marks = students[name]
    print(marks/number)
    
except KeyError:
    print("Student not found.")

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")    