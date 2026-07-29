def parking_tickets():
    for tickets in range(1,10000):
        yield tickets

tickets = parking_tickets()
print(next(tickets))
print(next(tickets))
print(next(tickets))
print(next(tickets))
print(next(tickets))
print(next(tickets))
print(next(tickets))
print(next(tickets))