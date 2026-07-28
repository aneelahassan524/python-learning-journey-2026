#Arrange the prices from lowest to highest.

new_list = []
employees = [
    {"name": "Ali", "salary": 50000},
    {"name": "Sara", "salary": 80000},
    {"name": "Ahmed", "salary": 65000}
]
new_list = sorted(employees,key=lambda employee:employee["salary"])
print(list(new_list))