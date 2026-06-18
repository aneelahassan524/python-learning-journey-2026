commits = int(input("Enter total commits this month:"))
if(commits>=100):
    print("Open Source Warrior")
elif(commits>=50):
    print("Consistent Developer")    
elif(commits>=20):
    print("Growing Developer")    
else:
    print("Keep Coding")    