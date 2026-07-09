student_count = 0
with open("student.txt", "r") as file:
    for line in file:
        if "Name:" in line:
            student_count += 1

print(f"Total Students: {student_count}")