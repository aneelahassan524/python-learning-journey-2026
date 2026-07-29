orders = [101, 102, 103]

it = iter(orders)

while True:
    try:
        order = next(it)
        print(order)
        
    except StopIteration:
        print("No more orders available.")
        break