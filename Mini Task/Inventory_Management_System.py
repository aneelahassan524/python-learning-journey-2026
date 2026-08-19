products = {}

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Remove Product")
    print("6. Inventory Value")
    print("7. Low Stock Products")
    print("8. Exit")

    choice = input("Enter your choice:")

    
    if choice == "1":
      print("Add Product")

      product_name = input("Enter product name: ")
      price = float(input("Enter price: "))
      quantity = int(input("Enter quantity: "))

      products[product_name] = {
        "price": price,
        "quantity": quantity
      }

      print("Product added successfully.")
        
    elif choice == "2":
       print("View Products")

       for product, details in products.items():
           print(f"Product: {product}")
           print(f"Price: {details['price']}")
           print(f"Quantity: {details['quantity']}")
  

    elif choice == "3":

       print("Search Product")
       search = input("Enter your product to search:")

       if search in products:
           print("Product Found")
           print(products[search])    
       else:
           print("Product not found")    

    elif choice == "4":
      print("Update Quantity")
      product_name = input("Enter product name: ")
      if product_name in products:
         new_quantity = int(input("Enter new quantity: "))
         products[product_name]["quantity"] = new_quantity
         print("Quantity updated successfully.")
      else:
         print("Product not found.")


    elif choice == "5":
      print("Remove Product")
      product = input("Enter a product you want to remove: ")
      if product in products:
          products.pop(product)
          print(f"Products: {products}")
      else:
          print("Product not found.")

    elif choice == "6":
        total_value = 0
        for product in products:
          price = products[product]["price"]
          quantity = products[product]["quantity"]
          total_value = total_value + (price * quantity)
        print(f"Total Inventory Value: {total_value}")    

    elif choice == "7":
     print("\n===== STOCK STATUS =====")
     for product in products:
          quantity = products[product]["quantity"]
          if quantity < 5:
             print(f"{product}: Low Stock ({quantity} units)")
          else:
             print(f"{product}: Stock Available ({quantity} units)")

    elif choice == "8":
        print("Exit")
        break

    else:
        print("Invalid choice.")
