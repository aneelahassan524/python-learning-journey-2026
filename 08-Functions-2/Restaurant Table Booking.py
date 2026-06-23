def booking (total_guests,available_seats=2000):
    if(total_guests<=available_seats):
        return("Booking Confirmed")
    else:
        return("Not Enough Seats")
a = booking(1000) 
print(f"Total guests available:{a}")       

