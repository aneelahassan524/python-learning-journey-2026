def sum(n):
    if(n==0):
        return 0
    return (n % 10) + sum(n // 10)
s = sum(123456)
print(f"Sum of Digits is:{s}")