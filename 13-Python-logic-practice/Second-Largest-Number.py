# Problem:
# Write a program to find the second largest number in a list.

# Human Thinking:
# First, I assume the first number is the largest.
# I also keep another variable to store the second largest number.
# I compare each number with the current largest number.
# If the current number is greater than the largest number,
# the old largest number becomes the second largest,
# and the current number becomes the new largest.
# If the current number is smaller than the largest number
# but greater than the second largest number,
# I update the second largest number.
# I repeat this process until all the numbers in the list are checked.
# Finally, I display the second largest number.

# Pseudocode:
# Start
# Take a list of numbers.
# Assume the first number is the largest.
# Assume the first number is also the second largest.
# For each number in the list:
#     If the current number is greater than the largest number:
#         Update the second largest number with the old largest number.
#         Update the largest number.
#     Else if the current number is greater than the second largest number
#     and smaller than the largest number:
#         Update the second largest number.
# Display the second largest number.
# End

# Python Code:
numbers = [12, 45, 7, 89, 23, 58]
max_number = numbers[0]
second_max = max_number
for number in range(6):
    if(numbers[number]>max_number):
        second_max = max_number
        max_number = numbers[number]
    else:
       if(numbers[number]>second_max and numbers[number]<max_number):
           second_max = numbers[number]    
           
print(f"Second Largest Number:{second_max}")
