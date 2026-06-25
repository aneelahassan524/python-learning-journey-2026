def power(base,exponent):
    if(exponent==0):
        return 1
    return base * power(base, exponent-1)
p = power(2,4)
print(f"Power is:{p}")