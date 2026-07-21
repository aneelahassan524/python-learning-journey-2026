def student_marks(*marks):

    total_subjects = len(marks)
    total_marks = 0

    for mark in marks:
        total_marks = total_marks+mark

    average = total_marks/total_subjects

    print(f"Total Subjects: {total_subjects}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average}")
    print(f"Highest Marks: {max(marks)}")
    print(f"Lowest Marks: {min(marks)}")

    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")


student_marks(78, 90, 85, 67, 95)