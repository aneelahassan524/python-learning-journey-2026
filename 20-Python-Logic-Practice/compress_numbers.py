numbers = [1, 1, 1, 2, 2, 5, 5, 5, 5, 8]

count = 1
for i in range(len(numbers) - 1):
    if(numbers[i] == numbers[i + 1]):
        count += 1
    else:
        print((numbers[i], count))
        count = 1
print((numbers[-1], count))