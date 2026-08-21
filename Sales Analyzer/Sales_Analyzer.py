sales = []
number = int(input("Enter your number of sales:"))
for sale in range(1,number+1):
    sales_input = int(input("Enter a sale:"))
    sales.append(sales_input)
print(f"Sales: {sales}") 

print("====== Final sales report ======")
total_sales = 0
for sale in sales:
    total_sales = total_sales+sale
print(f"Total sales: {total_sales}")

max_sale = sales[0]
for sale in range(len(sales)):
    if sales[sale] > max_sale:
        max_sale = sales[sale]
print(f"Highest Sale: {max_sale}")


min_sale = sales[0]
for sale in range(len(sales)):
    if sales[sale] < min_sale:
        min_sale = sales[sale]
print(f"Lowest Sale: {min_sale}")


count = 0 
for sale in sales:
    if sale >= 1000:
        count = count+1
print(f"Sales greater than 1000: {count}")        

target = int(input("Enter your sale to target:"))
count = 0 
for sale in sales:
  if sale < target:
        continue
  count = count+1
  print("Sales: {sales}")
print(f"Number of sales meeting target: {count}")

check = int(input("Enter a particular sale to search:"))
if check in sales:
        print("Sale is present")
else:
        print("Sale is not Present")    

if total_sales >= 5000:
    print("Sales Performance: Excellent Sales")
elif total_sales >= 3000:
    print("Sales Performance: Good Sales")
else:
    print("Sales Performance: Needs Improvement") 


