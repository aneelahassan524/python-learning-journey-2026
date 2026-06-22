def calculation (hours_worked,hourly_rate,rate=0.05):
     bill = hours_worked * hourly_rate  
     tax_rate = bill*rate
     total_bill = bill - tax_rate
     return total_bill
a = calculation(8,500) 
print(f"Total Bill is:{a}")