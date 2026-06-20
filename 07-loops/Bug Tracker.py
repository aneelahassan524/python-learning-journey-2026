bugs = 1
for i in range(1,bugs+1):
    total_bugs = int(input("How many number of bugs fixed today:"))
    print(f"Total Bugs:{total_bugs}")
    if(total_bugs>12):
        print("Critical level problem in program")
    elif(total_bugs>10):
        print("High level problem in program")
    elif(total_bugs>5):
        print("Medium level problem in program")  
    else:
        print("Low level problem in program")          
