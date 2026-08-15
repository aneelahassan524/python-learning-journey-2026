employee_name = input("Enter your name:")
monthly_salary = int(input("Enter your monthly salary:"))
housing_expense = int(input("Enter your House Expense:"))
food_expense = int(input("Enter your Food Expense:"))
transport_expense = int(input("Enter your Transport Expenses:"))
other_expense = int(input("Enter your Other Expenses:"))

total_expenses = housing_expense+food_expense+transport_expense+other_expense 
remaining_salary = monthly_salary - total_expenses
yearly_salary = monthly_salary * 12
yearly_expenses = total_expenses *12

print(f"Employee Name: {employee_name}")
print(f"Monthly Salary: {monthly_salary}")
print(f"Housing: {housing_expense}")
print(f"Food: {food_expense}")
print(f"Transport: {transport_expense}")
print(f"Other: {other_expense}\n") 
print(f"Total Expenses: {total_expenses}")
print(f"Remaining Salary: {remaining_salary}")
print(f"Yearly Salary: {yearly_salary}")
print(f"Yearly Expenses: {yearly_expenses}")
