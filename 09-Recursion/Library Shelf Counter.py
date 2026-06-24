def shelves(n):
    if(n==21):
        return 0
    print(f"shelve{n}")
    shelves(n+1)
shelves(1)    
