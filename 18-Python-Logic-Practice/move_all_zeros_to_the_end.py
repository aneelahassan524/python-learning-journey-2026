# Problem:
# Write a program to move all zeros to the end of a list.

# Human Thinking:

# First, take a list of numbers.
# Then, create an empty list to store all non-zero numbers.
# Create a variable to count the total number of zeros.
# Visit each number in the list one by one.
# If the current number is not zero:
# Add it to the new list.
# Otherwise:
# Increase the zero counter by 1.
# After checking all the numbers:
# Add the counted zeros to the end of the new list.
# Finally, display the updated list.

# Pseudocode:
# Start
# Take a list of numbers.
# Create an empty list called new_list.
# Set zero_count = 0.
# For each number in the list:
# If the number is not 0:
# Add the number to new_list.
# Else:
# Increase zero_count by 1.
# While zero_count > 0:
# Add 0 to the end of new_list.
# Decrease zero_count by 1.
# Display new_list.
# End

#Python Code:
numbers = [0, 5, 0, 3, 8, 0, 2]
new_list = []
zero_count = 0
for number in numbers:
    if(number!=0):
        new_list.append(number)
    else:
        zero_count = zero_count+1
while(zero_count>0):
            new_list.append(0)
            zero_count = zero_count-1
print(f"New List:{new_list}")

