def Temperature (temperature):
    if(temperature<30):
       return "Normal Temperature"
    elif(temperature>35 and temperature<45):
        return "Warning" 
    else:
        return "Critical Temperature"
t = Temperature(50)    
print(t)                  

    