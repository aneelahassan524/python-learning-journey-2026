# Problem:
# Write a program to remove all negative numbers from a list.

# Human Thinking:
# First, I take a list that contains positive and negative numbers.
# Then, I create a new empty list.
# I check each number in the original list.
# If the number is greater than or equal to 0, I add it to the new list.
# If the number is negative, I do not add it.
# I repeat this process until all the numbers are checked.
# Finally, I display the new list without the negative numbers.

# Pseudocode:
# Start
# Take a list of numbers.
# Create an empty list.
# For each number in the list:
#     If the number is greater than or equal to 0:
#         Add the number to the new list.
# Display the new list.
# End
#Python Code:
numbers = [4, -2, 7, -5, 0, 9, -1]
new_list = []
for number in range(len(numbers)):
    if(numbers[number]>=0):
        new_list.append(numbers[number])
print(f"New List:{new_list}")        
