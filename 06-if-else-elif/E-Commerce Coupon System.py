value = int(input("Enter Cart Value:"))
code = int(input("Enter Coupon Code:"))
if(value>=5000 and code==20):
    discount = value*20/100
    total_bill = value-discount
    print(f"Total Bill with 20% discount:{total_bill}") 
elif(value>=3000 and code==10):
    discount = value*10/100
    total_bill = value-discount
    print(f"Total Bill with 10% discount:{total_bill}")
else:
    print("No discount")    

