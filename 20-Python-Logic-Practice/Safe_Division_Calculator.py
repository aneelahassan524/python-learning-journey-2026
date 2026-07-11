print("===Calculator===")
try:
    n1 = int(input("Enter a number 1:"))
    n2 = int(input("Enter a number 2:"))
    print(f"The Answer is:{n1/n2}")
except:
    if(n2==0):
       print("Zero Division Error")    
    



