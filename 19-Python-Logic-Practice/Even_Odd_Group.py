# Problem:
# Write a program to separate even and odd numbers into two different lists.

# Human Thinking:
# First, take a list of numbers.
# Create two empty lists:
# One to store even numbers.
# One to store odd numbers.
# Visit each number in the list one by one.
# If the number is divisible by 2:
# Add it to the even list.
# Otherwise:
# Add it to the odd list.
# Repeat the process until all numbers are checked.
# Finally, display both the even and odd lists.

# Pseudocode:
# Start
# Take a list of numbers.
# Create an empty even_list.
# Create an empty odd_list.
# For each number in the list:
# If the number is divisible by 2:
# Add the number to even_list.
# Else:
# Add the number to odd_list.
# Display even_list.
# Display odd_list.
# End

#Python Code:
numbers = [4, 7, 2, 9, 6, 1]
even_list = []
odd_list = []
for number in numbers:
    if(number%2==0):
        even_list.append(number)
    else:
        odd_list.append(number)
print(f"Even Numbers:{even_list}")     
print(f"Odd Numbers:{odd_list}")   