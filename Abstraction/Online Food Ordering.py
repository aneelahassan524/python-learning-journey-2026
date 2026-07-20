#Problem
#A food delivery company wants to build an online ordering system.

from abc import ABC, abstractmethod

class company:

    @abstractmethod
    def prepare_food(self):
        pass

class Pizza_Restaurant:

    def prepare_food(self):
        print("Pizza Restaurant: Preparing Cheese Pizza...")

class Burger_Restaurant:

    def prepare_food(self):
        print("Burger Restaurant: Preparing Chicken Burger...")

class Biryani_Restaurant:

    def prepare_food(self):
        print("Biryani Restaurant: Preparing Chicken Biryani...")

    
pizza = Pizza_Restaurant()
burger = Burger_Restaurant()
biryani = Biryani_Restaurant()
pizza.prepare_food()
burger.prepare_food()
biryani.prepare_food()