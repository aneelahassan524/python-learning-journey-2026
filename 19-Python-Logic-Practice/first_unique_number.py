# Problem:
# Write a program to find the first unique number in a list.

# Human Thinking:

# First, take a list of numbers.
# Visit the first number in the list.
# Compare it with all the other numbers.
# Count how many times the current number appears.
# If it appears only once:
# Display the number.
# Stop the program.
# Otherwise:
# Move to the next number.
# If no unique number is found:
# Display "No unique number found."

# Pseudocode:
# Start
# Take a list of numbers.
# For each number in the list:
# Set count = 0.
# Compare the current number with every number in the list.
# If both numbers are the same:
# Increase count by 1.
# If count == 1:
# Display the current number.
# Stop.
# If no unique number is found:
# Display "No unique number found."
# End

#Python Code:
numbers = [4, 2, 4, 6, 2, 8, 8]
found = False
for i in numbers:
    count = 0
    for j in numbers:
        if i == j:
            count = count + 1
    if count == 1:
        print(f"First Unique Number: {i}")
        found = True
        break

if not found:
    print("No unique number found.")

