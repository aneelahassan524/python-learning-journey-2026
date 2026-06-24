def Fibonacci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)
f = Fibonacci(10)
print(f"Fibonacci Number is:{f}")