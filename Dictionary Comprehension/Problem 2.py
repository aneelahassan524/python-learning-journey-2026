#Create a new dictionary where every product price includes 15% GST.

products = {
    "Laptop": 50000,
    "Mouse": 1200,
    "Keyboard": 3000
}

new_products = {
    name : price+(price*15/100)
    for name,price in products.items()
}
print(new_products)