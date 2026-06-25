def digits(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return 1+digits(n//10)
d = digits(986754)
print(f"Count Digits:{d}")