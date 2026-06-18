passport = input("Is your Passport Available(yes/no):").strip().lower()
ticket = input("Is your Ticket Available (yes/no):").strip().lower()
arrival = int(input("Enter your arrival before flight (minutes):"))
print("Passport =", passport)
print("Ticket =", ticket)
print("Arrival =", arrival)
if(passport!="yes"):
    print("Passport missing")
if(ticket!="yes"):  
    print("Ticket missing") 
if(arrival<30):
    print("Late arrival")  
if ( passport.lower() == "yes" and ticket.lower() == "yes"and arrival >= 30):
    print("Ready for Boarding")     






