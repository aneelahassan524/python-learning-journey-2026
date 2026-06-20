total_student = 30
present_student = 0
for i in range(1,31):
    status = input(f"Student{i}(absent/present):").strip().lower()
    print(status)
    if(status=="absent"):
        continue
    present_student = present_student+1
    print("\nAttendance Report")
    print("Present Students:", present_student)
    print("Absent Students:", total_student - present_student)

