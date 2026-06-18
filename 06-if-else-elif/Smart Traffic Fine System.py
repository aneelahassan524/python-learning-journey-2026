speed_limit = 60
actual_speed = int(input("Enter your vehicle speed:"))
overspeed = actual_speed-speed_limit
if(overspeed<8):
    print("Warning")
elif(overspeed<18):
    print("Minor Fine")    
elif(overspeed<35):
    print(" Major Fine")   
else:
    print("License Review")    