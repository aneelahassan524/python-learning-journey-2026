class mobile:

    operating_system = "Android"

    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

mobile1 = mobile("Samsung","GalaxyS25",285000)
mobile2 = mobile("Apple","iPhone17",365000)
mobile3 = mobile("Xiaomi","RedmiNote13Pro",95000)
mobile4 = mobile("Oppo","Reno13",145000)
mobile5 = mobile("Vivo","V40",165000)

print(mobile1.brand)
print(mobile2.price)
print(mobile3.model)
print(mobile4.operating_system)
print(mobile5.model)
