salary = int(input("Enter your salary:"))
loan = input("Do you have an existing loan? (yes/no): ").strip().lower()
score = int(input("Enter your score:"))
if(salary>=100000 and loan=="no" and score>=750):
    print("Low Risk")
elif(salary>=50000 and loan=="no" and score>=650):
    print("Medium Risk")   
else:
    print("High Risk")     
