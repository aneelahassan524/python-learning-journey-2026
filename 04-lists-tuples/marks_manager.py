subject1 = int(input("Enter marks of first subject:"))
subject2 = int(input("Enter marks of second subject:"))
subject3 = int(input("Enter marks of third subject:"))
marks = [subject1,subject2,subject3]
total_marks = 300
total = marks[0]+marks[1]+marks[2]
print(f"Total:{total}")
average = (total)/3
print(f"The average is:{average}")
percentage = (total/total_marks)*100
print(f"The percentage is:{percentage}")
