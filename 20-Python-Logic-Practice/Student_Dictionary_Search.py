students = {
    "Ali": 85,
    "Sara": 92,
    "Aneela": 95,
    "Ahmed": 78
}
try:

    name = input("Enter student name:")
    print(f"Student Name:{students[name]}")

except ValueError:

    print("Student not found")
