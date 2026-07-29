data = [12, 18, 25, 30, 42]
it = iter(data)
while True:
    try:
        value = next(it)
        if(value%2==0):
          print(f"Processing even value:{value}")
        else:
             print(f"Skipping odd value:{value}")
             
    except StopIteration:
        print("Data stream ended.")  
        break   
