name = "aneela hassan" 
code = "aneela@123"
attempt = 1
while(attempt<4):
    username = input("Enter your username:").strip().lower()
    password = input("Enter a password:").strip()
    attempt = attempt+1
    if(name==username and code==password):
        print("Access Granted")
        break
    elif(name!=username or code!=password):
      print("wrong attempt,Try again") 
    else:
       print("Try again after few seconds")
       
     


