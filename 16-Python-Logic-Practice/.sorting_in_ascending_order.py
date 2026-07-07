# Problem:
# Write a program to check whether a list is sorted in ascending order.

# Human Thinking:
# First, I take a list of numbers.
# Then, I compare each number with the next number in the list.
# If the current number is less than or equal to the next number,
# I continue checking the remaining numbers.
# If I find a current number that is greater than the next number,
# I know the list is not sorted.
# I repeat this process until all the required numbers are checked.
# Finally, if no wrong order is found, I display that the list is sorted.
# Otherwise, I display that the list is not sorted.

# Pseudocode:
# Start
# Take a list of numbers.
# Assume the list is sorted.
# For each number except the last one:
#     Compare the current number with the next number.
#     If the current number is greater than the next number:
#         The list is not sorted.
#         Stop checking.
# If no wrong order is found:
#     Display "The list is sorted."
# Else:
#     Display "The list is not sorted."
# End

#Python Code:
numbers = [2, 8, 5, 10, 15]
is_sorted = True
for i in range(4):
     if(numbers[i]>numbers[i+1]):    
       is_sorted = False
       break
if(is_sorted):
        print(f"The list is sorted")  
else:
      print(f"The list is not sorted")        
        


               
        