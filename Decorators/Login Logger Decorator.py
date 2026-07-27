def login_logger(func):

    def  wrapper(*args,**kwargs):
       print("User login verified...") 
       result = func(*args,**kwargs)
       print("Activity Logged Successfully.")
       return result
    
    return  wrapper
    
@ login_logger    
def view_profile(username):
    print(f"Opening profile of {username}")

view_profile("Aneela")

