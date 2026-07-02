# Problem:
# Write a program to find all pairs of numbers whose sum is 10.

# Human Thinking:
# First, I take a list of numbers.
# I choose one number from the list.
# Then, I compare it with the remaining numbers one by one.
# I add the current number and the compared number.
# If the sum of both numbers is equal to 10, I display both numbers.
# I repeat this process until all the numbers in the list are checked.
# Finally, I display all pairs whose sum is 10.

# Pseudocode:
# Start
# Take a list of numbers.
# For each number in the list:
#     Compare it with the remaining numbers in the list.
#     If the sum of both numbers is equal to 10:
#         Display both numbers.
# End
#Python Code:
numbers = [2, 8, 5, 5, 7, 3, 1, 9]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==10):
            print(f"List of Pairs:{numbers[i]}+{numbers[j]}={numbers[i]+numbers[j]}")

