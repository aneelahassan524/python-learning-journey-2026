def order_summary(**order):

    for key,value in order.items():
        print(f"{key} : {value}")

    subtotal = order["quantity"] * order["price"] 
    if("discount" in order):   
      subtotal =  subtotal-order["discount"]
      print(f"Subtotal after discount:{subtotal}")

    if("delivery" in order):  
      subtotal = subtotal+order["delivery"]
      print(f"Subtotal after delivery:{subtotal}")
       
    print(f"Final Bill:{subtotal}")

order_summary(
    customer="Aneela",
    item="Laptop Bag",
    quantity=2,
    price=1500,
    discount=300,
    delivery=250
)

