def token():
    yield 1001
    yield 1002
    yield 1003
    yield 1004
gen = token()
while True:
    try:
        print(next(gen))

    except StopIteration:
        print("No more tokens available.")    
        break

