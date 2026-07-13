class Car:
    wheels = 4

    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

car1 = Car("BMW","X5","Blue") 
car2 = Car("Honda","Civic","Black")   
car3 = Car("Toyota","Corolla","White") 
car4 = Car("Hyundai","Tucson","Grey")   

print(car1.brand)
print(car2.color)
print(car3.wheels)
print(car4.model)
