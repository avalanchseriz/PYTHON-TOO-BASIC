# abstract class = a class which contains one or more abstract methods.
# abstract method = a method which has a decleration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):
   
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("you drive the car")
        
    def stop(self):
        print("car stopped")

class Bike(Vehicle):
    
    def go(self):
        print("you ride the bike")

    def stop(self):
        print("bike stopped")

#vehicle = Vehicle()
car = Car()
bike = Bike()

#vehicle.go()
car.go()
bike.go()

car.stop()
bike.stop()

