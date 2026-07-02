# Problem:
# Write a program to find the duplicate numbers in a list.

# Human Thinking:
# First, I take a list of numbers.
# I choose one number from the list.
# Then, I compare it with the remaining numbers one by one.
# If I find the same number again, I know it is a duplicate.
# I repeat this process for every number in the list.
# Finally, I display the duplicate numbers.

# Pseudocode:
# Start
# Take a list of numbers.
# For each number in the list:
#     Compare it with the remaining numbers in the list.
#     If both numbers are the same:
#         Display the duplicate number.
# End
#Python Code:
numbers = [2, 5, 3, 2, 8, 5, 9]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]==(numbers[j])):
            print(f"Duplicate Numbers:{numbers[i]}")
