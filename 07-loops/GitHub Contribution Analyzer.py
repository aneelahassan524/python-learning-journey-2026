days = int(input("How many days did you code this month:"))
total_commits = 0
for i in range(1,days+1):
    commits = int(input("Enter your day commits:"))
    total_commits = total_commits+commits
    print(f"Total Commits:{total_commits}")
average_commits = total_commits/days  
print(f"Average Commits:{average_commits}") 
if(average_commits>=20):
    print("Highly Active Developer")
elif(average_commits>=10):
    print("Moderately Active Developer")   
else:
    print("Inactive Developer")    

