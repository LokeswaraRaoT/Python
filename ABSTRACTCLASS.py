#abstract classes
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"
    
    def details(self):
        return f"I am drive AUDI car"
    
    
car_int = Car()
print(car_int.details())