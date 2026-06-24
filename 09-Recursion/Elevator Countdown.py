def elevator(n):
    if(n==0):
        return

    print(f"Floor {n}")
    elevator(n-1)

elevator(10)