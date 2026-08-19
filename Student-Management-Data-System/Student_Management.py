students = {}

while True:
    print("======= Student Management System =======")
    print("1.Add student")
    print("2.View all students")
    print("3.Search student")
    print("4.Update student")
    print("5.Delete student")
    print("6.Show course information")
    print("7.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        print("Add student")
        roll_no = input("Enter roll no:")
        name = input("Enter student name:")
        age = int(input("Enter student age:"))
        grade = input("Enter student grade:")
        courses = input("Enter student courses:")
        courses = {course.strip() for course in courses.split(",")}

        students[roll_no] = {
            "name"    : name,
            "age"     : age,
            "grade"   : grade,
            "courses" : courses
        }

        print("Student added successfully.")

    elif choice == "2":
        print("View all students") 
        for student , details in students.items():
           print(f"Roll No     : {student}")
           print(f"Student Name: {details['name']}")
           print(f"Age         : {details['age']}")
           print(f"Grade       : {details['grade']}")
           print(f"Courses     : {details['courses']}")

    elif choice == "3":
        print("Search student")
        search = input("Enter a student to search:")
        if search in students:
            print("Student Found.")
            print(students[search])
        else:
            print("Student not Found.")    

    elif choice == "4":
        print("Update student")
        student_roll = input("Enter a rollno of student you want to update:")
        if student_roll in students:
            new_name = input("Enter a new name:")
            students[student]['name'] = new_name
            print("Student Updated Successfully.")

    elif choice == "5":
        print("Delete student")
        student = input("Enter a student you want to delete:")
        if student in students:
            students.pop(student)
            print("Student deleted Successfully.")
            print(f"Students: {students}")
        else:
            print("Student not Found.")   


    elif choice == "6":
       print("===== Course Information =====")
       for roll_no, details in students.items():
        print(f"Student: {details['name']}")
        print(f"Roll No: {roll_no}")
        print(f"Courses: {details['courses']}")

    elif choice == "7":
        print("Exit")    
        break

    else:
        print("Invalid Choice")


