# Abstraction - hiding complex inner details and showing only the essential features to the user

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog:
    def make_sound(self):
        print("Woof!!!!")

class Cat:
    def make_sound(self):
        print("Meow!")

# dog = Animal()  # ❌ Error: Can't instantiate abstract class

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()


from abc import ABC,abstractmethod

class Vehicle(ABC):  # ABC is Abstract class which is needed to be inherited to make a class as abstract class
 def __init__(self,numberOftires):
     self.numberOftires = numberOftires
 @abstractmethod
 def start(self):
     pass
 def stop(self): # Concrete method
    print("Vehicle stops")

class Car(Vehicle):
 def __init__(self):
     super().__init__(2)
 def start(self):
    print("Car starts")

class Bike(Vehicle):
 def __init__(self):
     super().__init__(2)

 def start(self):
     print("Bike start")

# v = Vehicle(3) # can’t create object of an abstract class here so it won’t work
                # Create an object of concrete class Bike as Bike class has implemented the abstract method start()
b = Bike()
b.start() # Bike start
b.stop() # Vehicle stop