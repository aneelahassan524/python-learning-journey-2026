#Create a new dictionary where Every employee name is uppercases and Salary remains the same.

employees = {
    "ali": 50000,
    "sara": 65000,
    "ahmed": 70000
}
updated = {
    name.upper(): pay
    for name,pay in employees.items()
}
print(updated)