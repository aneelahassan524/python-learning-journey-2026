class ShoppingCart:

    def __init__(self,Customer_name,Number_of_items):
        self.Customer_name = Customer_name
        self.Number_of_items = Number_of_items

    def __add__(self,other):
        return self.Number_of_items+other.Number_of_items
    
cart1 = ShoppingCart("Ahmed",20)
cart2 = ShoppingCart("Fatima",40)
print(f"Total Number Of Items:{cart1+cart2}")