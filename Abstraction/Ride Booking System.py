from abc import ABC, abstractmethod

class Ride(ABC):

    @abstractmethod
    def calculate_fare(self,distance):
        pass

class BikeRide(Ride):

    def calculate_fare(self,distance):
        print("Ride Type:Bike Ride")
        self.distance = distance
        print(f"Distance:{self.distance}km")
        fare = 25*distance
        print(f"Total Fare:{fare}\n")


class CarRide(Ride):
 
    def calculate_fare(self,distance):
        print("Ride Type:Car Ride")
        self.distance = distance
        print(f"Distance:{self.distance}km")
        fare= 60*distance
        print(f"Total Fare:{fare}\n")

class LuxuryRide(Ride):

    def calculate_fare(self,distance):
        print("Ride Type:Luxury Ride")
        self.distance = distance
        print(f"Distance:{self.distance}km")
        fare = 120*distance
        print(f"Total Fare:{fare}")

bike = BikeRide()
car = CarRide()
luxury = LuxuryRide()
bike.calculate_fare(8)
car.calculate_fare(15)
luxury.calculate_fare(20)
    