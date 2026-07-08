# Problem:
# Write a program to find the longest streak of even numbers in a list.

# Human Thinking:
# First, I take a list of numbers.
# Then, I create one variable to count the current streak of even numbers.
# I also create another variable to store the longest even streak found so far.
# I check each number in the list one by one.
# If the current number is even, I increase the current streak count.
# If the current number is odd, it means the current even streak has ended.
# Then, I compare the current streak with the longest streak.
# If the current streak is greater, I update the longest streak.
# After that, I reset the current streak to 0 because a new even streak will start when the next even number is found.
# I repeat this process until all the numbers are checked.
# Finally, I compare the last current streak with the longest streak because the list may end with an even streak.
# Then, I display the longest even streak.

# Pseudocode:
# Start
# Take a list of numbers.
# Set current_streak = 0.
# Set longest_streak = 0.
# For each number in the list:
#     If the number is even:
#         Increase current_streak by 1.
#     Else:
#         Compare current_streak with longest_streak.
#         If current_streak is greater:
#             Update longest_streak.
#         Reset current_streak to 0.
# After the loop, compare current_streak with longest_streak.
# Update longest_streak if needed.
# Display longest_streak.
# End

#Python Code:
numbers = [2, 4, 6, 1, 8, 10]
current_sequence = 0
longest_sequence = 0
for number in numbers:
    if(number%2==0):
        current_sequence = current_sequence+1
    else:
        if(current_sequence>longest_sequence):
               longest_sequence = current_sequence
        current_sequence = 0
if(current_sequence>longest_sequence):
     longest_sequence = current_sequence
print(f"Longest even streak:{longest_sequence}")        