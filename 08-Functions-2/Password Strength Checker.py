def password (password,length=10):
    if(len(password)<length):
        return "Weak"
    elif(len(password)>=length):
        return "Medium"
    else:
        return "Critical"
p = password("abc12345567")
print(f"The Password is:{p}")
    
