#Take the details of product
customer_name = input("Enter your name:")
product_name = input("Enter a product name:")
price = float(input("Enter a price of product:"))
quantity = int(input("Enter a quantity:"))
discount_percentage = float(input("Enter your discount percentage:"))

#Calculate the final bill
subtotal = price * quantity
discount_amount  = subtotal * discount_percentage /100

#Print all the details
print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Discount Percentage: {discount_percentage}")

if discount_percentage < 0:
     print("Invalid Input")
elif discount_percentage >= 20:
    final_total = subtotal-discount_amount-100
    print(f"Final Bill: {final_total}")
else:
    final_total = subtotal - discount_amount
    print(f"Final Bill: {final_total}")