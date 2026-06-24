def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
s = sum(10)
print(f"Sum of Numbers is:{s}")