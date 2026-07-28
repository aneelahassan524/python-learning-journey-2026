#Create a new list containing only the students who passed (marks ≥= 40).

new_list = []

marks = [25, 70, 40, 35, 95, 80]
new_list = filter(lambda marks:marks>=40,marks)

print(list(new_list))