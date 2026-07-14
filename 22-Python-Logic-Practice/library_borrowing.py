#Problem
# A company stores employee salaries.
# employees = {
#     "Ali": 45000,
#     "Sara": 60000,
#     "Ahmed": 38000,
#     "Aneela": 72000,
#     "Bilal": 51000
# }
#
# 1. Count how many employees earn more than 50000.
# 2. Count how many employees earn less than 40000.
# 3. Calculate the total salary of all employees.
# 4. Calculate the average salary.
# 5. Print all the results.


#Human Thinking
# Take the employees dictionary.
# Create variables for:
# - High salary count
# - Low salary count
# - Total salary
# Visit every employee.
# Get the employee's salary.
# Add the salary to the total
# If salary > 50000
# Increase high salary count.
# If salary < 40000
# Increase low salary count.
# After checking everyone,
# calculate average salary.
# Print all answers.


#Pseudocode
# START
# Take employees dictionary.
# high_salary = 0
# low_salary = 0
# total_salary = 0
# Visit every employee.
# Get salary.
# Add salary to total.
# IF salary > 50000
#     Increase high salary.
# IF salary < 40000
#     Increase low salary.
# After loop
# Calculate average.
# Print all results.
# END

#Python Code:
employees = {
    "Ali": 45000,
    "Sara": 60000,
    "Ahmed": 38000,
    "Aneela": 72000,
    "Bilal": 51000
 }
high_salary_count = 0
low_salary_count = 0
total_salary= 0
for salary in employees:
    salary = employees[salary]
    total_salary = total_salary+salary
    
    if(salary>50000):
        high_salary_count = high_salary_count+1
        
    if(salary<40000):
        low_salary_count = low_salary_count+1
        
average_salary = total_salary/len(employees)

print(f"Average Salary is:{average_salary}")
print(f"Total Salary:{total_salary}")
print(f"Total Employees whose salary more than 50000:{high_salary_count}")
print(f"Total Employees whose salary more than 40000:{low_salary_count}")