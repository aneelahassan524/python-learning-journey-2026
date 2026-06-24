def factorial(n):
    if(n==0 or n==1):
        return 1
    print(f"{n}")
    return n*factorial(n-1)
a=factorial(8)  
print(f"Factorial:{a}")           
