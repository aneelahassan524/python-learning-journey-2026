# Problem:
# Write a program to find the first repeated number in a list.

# Human Thinking:
# First, I take a list of numbers.
# Then, I compare each number with the remaining numbers.
# If I find the same number again, I display it and stop checking.
# Otherwise, I continue checking the next number.
# If no repeated number is found, I display a message.

# Pseudocode:
# Start
# Take a list of numbers.
# Set is_found = False.
# For each number:
#     Compare it with the remaining numbers.
#     If a repeated number is found:
#         Display it.
#         Set is_found = True.
#         Stop both loops.
# If no repeated number is found:
#     Display "No repeated number found."
# End

# Python Code:
numbers = [5, 8, 2, 7, 8, 10, 2]
is_found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(f"First repeated number is: {numbers[i]}")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print("No repeated number found.")