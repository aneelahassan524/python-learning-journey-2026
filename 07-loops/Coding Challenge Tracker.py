days= 0
total_hours = 0
while True:
    hours = int(input("Enter coding hours: "))
    if hours == 0:
        break
    total_hours = total_hours + hours
    days = days+ 1
average_hours = total_hours / days

print("\nCODING REPORT")
print(f"Total days:{days}")
print(f"Total Hours:{total_hours}")
print(f"Average Hours:{average_hours}")
