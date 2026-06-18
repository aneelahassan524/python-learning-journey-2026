amount = int(input("Enter order amount:"))
member = input("Are you a member?(yes/no)").strip().lower()
if(amount>5000 and member=="yes"):
    discount = amount*20/100
    total_bill = amount-discount
    print(f"Total Bill with 20% discount:{total_bill}")
elif(amount>3000 and member=="yes"):   
    discount = amount*10/100
    total_bill = amount-discount
    print(f"Total Bill with 10% discount:{total_bill}")
elif(amount>5000 and member=="no"):   
    discount = amount*5/100
    total_bill = amount-discount
    print(f"Total Bill with 5% discount:{total_bill}") 
else:
    print(f"Total Bill:{amount}")       
