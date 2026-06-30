# Problem:
# Write a program to find the largest number in a list.

# Human Thinking:
# First, I assume the first number in the list is the largest.
# Then I compare it with the next number.
# If the current number is greater than the current largest number,
# I update the largest number.
# I repeat this process until all the numbers in the list are checked.
# At the end, the largest number is the answer.

#Pseudocode
#Start
#Take a list of numbers.
#Assume the first number is the largest.
#For each remaining number in the list:
#Compare the current number with the current largest number.
#If the current number is greater:
#Update the largest number.
#Display the largest number.
#End

#Python Code:
numbers = [12,45,7,89,23,58]
max_number = numbers[0]
for number in range(6):
    if(numbers[number]>max_number):
        max_number = numbers[number]
print(f"The largest number is:{max_number}")
