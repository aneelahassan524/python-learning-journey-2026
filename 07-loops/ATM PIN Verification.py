correct_code= 1234
attempt = 1
while(attempt<4):
    code =int(input("Enter your PIN code:")) 
    attempt= attempt+1
    if(code==correct_code):
        print("Access Granted")
        break
    elif(correct_code!=code):
        print("Wrong Pin code,Try again")
    else:
        print("Card Blocked")    


