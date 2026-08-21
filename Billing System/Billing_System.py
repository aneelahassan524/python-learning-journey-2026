#Take product prices
products = []
product = int(input("Enter number of product:"))
for price in range(1,product+1):
   prices = int(input("Enter a product price:"))
   products.append(prices)
print(f"Total Product Prices: {products}")

#Calculate the subtotal
def calculate_subtotal():
   total = 0
   for price in products:
     total = total+price
   return total

#Apply a discount
def calculate_discount(total,discount="20"):
     if total >= 2000:
        bill = total * discount / 100
        total_bill = total - bill
        return total_bill

#Calculate tax
def calculate_tax(total_bill,tax="5"):
     tax = total_bill * tax / 100
     return tax

#Calculate total
def calculate_total(total_bill,tax):
   final_bill = total_bill + tax
   return final_bill


subtotal = calculate_subtotal()
print(f"Subtotal is: {subtotal}")

discount = calculate_discount(subtotal,10)
print(f"Total Bill with discount: {discount}")

tax = calculate_tax(discount,5)
print(f"Total Bill with tax: {tax}")

total = calculate_total(discount,tax)
print(f"Final Bill: {total}")

