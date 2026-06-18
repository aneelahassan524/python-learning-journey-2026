status = input("Enter your subscription status:").strip().lower()
age = int(input("Enter your age:"))
if(age>=18 and status=="active"):
    print("Full Access")
elif(age<=18 and status!="active"):
    print("Kids Mode") 
else:
    print("Access Denied")       