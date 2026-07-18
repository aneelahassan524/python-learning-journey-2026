class Delivery:

    def deliver(self):
        print("Delivering order...")

class BikeDelivery(Delivery):

    def deliver(self):
        print("Bike Delivery: Your order is on the way.")

class CarDelivery(Delivery):

     def deliver(self):
        print("Car Delivery: Your order is on the way.")

class DroneDelivery(Delivery):

     def deliver(self):
        print("Drone Delivery: Your order is on the way.")
      
bike = BikeDelivery()
car = CarDelivery()
drone = DroneDelivery()
bike.deliver()
car.deliver()
drone.deliver()