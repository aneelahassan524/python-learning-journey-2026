# Problem:
# Write a program to count the positive numbers in a list.

# Human Thinking:
# First, I take a list of numbers.
# Then, I create a count variable and set it to 0.
# I check each number in the list.
# If the number is greater than 0, I increase the count.
# I repeat this process until all the numbers in the list are checked.
# Finally, I display the total count of positive numbers.

# Pseudocode:
# Start
# Take a list of numbers.
# Set count = 0.
# For each number in the list:
#     If the number is greater than 0:
#         Increase count by 1.
# Display the total count.
# End

# Python Code:
numbers = [4, -2, 0, 7, -5, 9, -1]
count = 0
for number in numbers:
    if number>0:
        count = count+1
print(f"Total Positive Numbers in a List:{count}")   
     