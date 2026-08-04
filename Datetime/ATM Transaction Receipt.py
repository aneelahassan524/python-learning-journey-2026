#You are developing software for an ATM machine.
#Whenever a customer withdraws money, the ATM prints a receipt with the transaction details.
from datetime import datetime

print("===========ATM RECEIPT===========")
transaction_id = input("Enter your Transaction ID:")
customer_name = input("Enter your Customer Name:")
withdraw_amount = int(input("Enter your amount to withdraw:"))

current = datetime.now()

print(f"Transaction ID: {transaction_id}")
print(f"Customer Name: {customer_name}")
print(f"Amount: Rs.{withdraw_amount}")

if withdraw_amount >= 10000:
    print("Premium Transaction")
else:
    print("Regular Transaction")

print(f"Transaction Date: {current.strftime('%d %B %Y')}")
print(f"Transaction Time: {current.strftime('%H:%M:%S')}")

print("Thank you for banking with us!\nHave a nice day.")