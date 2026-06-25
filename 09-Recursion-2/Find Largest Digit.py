def largest_digit(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return max(n%10,largest_digit(n//10))
l =largest_digit(98543)
print(f"Largest Digit:{l}")
