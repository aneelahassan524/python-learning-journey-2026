def check (employee_id,length=5,first_digit="1"):
    employee_id = str(employee_id)
    if(len(employee_id)==length and employee_id[0]=="1"):
        return True
    else:
        return False
a=check(1234) 
print(a)   