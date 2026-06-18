balance = int(input("Enter your Account Balance:"))
amount = int(input("Enter your Withdrawal Amount:"))
if(amount>balance):
    print("Insufficient Funds")
elif(amount<=0):
    print(" Invalid Amount")
else:
    print("Transaction successful")    

    