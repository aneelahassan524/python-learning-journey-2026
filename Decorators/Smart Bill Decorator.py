def discount(func):

    def  bill(*args,**kwargs):
       print("Calculating Bill...") 
       result = func(*args,**kwargs)
       print("Thank You for Shopping!") 
       return result
    return  bill
    
@ discount  
def calculate_bill(quantity,price):
    total_bill = quantity*price
    print(f"Original Bill: {total_bill}")
   
    if(total_bill>5000):
        total_bill = total_bill*0.20
        print(f"Total Bill with Discount: {total_bill}")
    else:
         print("No Discount Available.")
           
calculate_bill(5,300)         
        



    
    