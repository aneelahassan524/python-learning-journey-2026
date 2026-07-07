# Problem:
# Write a program to rotate a list one position to the right.

# Human Thinking:
# First, I take a list of numbers.
# Then, I create a new empty list.
# I move the last element of the original list to the beginning of the new list.
# After that, I add all the remaining elements from the first element
# to the second-last element into the new list.
# I repeat this process until all the elements are added.
# Finally, I display the rotated list.

# Pseudocode:
# Start
# Take a list of numbers.
# Create a new empty list.
# Add the last element of the original list to the new list.
# For each element from the first index to the second-last index:
#     Add the current element to the new list.
# Display the new list.
#End

# Python Code:
numbers = [10, 20, 30, 40, 50]
new_list = []
new_list.append(numbers[len(numbers) - 1])
for number in range(len(numbers) - 1):
    new_list.append(numbers[number])
print(f"New List:{new_list}")