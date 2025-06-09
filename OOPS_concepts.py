# OOPS - Object Oriented Programming

# classes - class is a blueprint/design/model/plan for a object. defines a set of attributes(data) and
#           methods(functions) that the objects created from the class can use

# objects - an object is an instance/physical existence of a class

class Scaler:
    Course1 = "SQL"
    Course2 = "Python"

print(Scaler.Course1)
print(Scaler.Course2)

obj = Scaler()
print(obj.Course2)

class Pet:
    def __init__(self, name, pet_type, age):
        self.name = name
        self.pet_type = pet_type
        self.age = age
        self.adopted = False

    def adopt_pet(self):
        self.adopted = True

    def display_info(self):
        status = "Adopted" if self.adopted else "Available"
        print(f"{self.name} is a {self.age} year old {self.pet_type}. status: {status}")

pet1= Pet("Jimmy", "Dog", 3)
pet2 = Pet("Laborador", "Dog", 4)

pet1.display_info()
pet2.display_info()

pet1.adopt_pet()
pet1.display_info()



# 1. constructor vs normal method

class Student:
    def __init__(self, name):  # Constructor
        self.name = name       # runs when object is created

    def say_hello(self):       # Normal Method
        print(f"Hello, my name is {self.name}")

# Usage
s1 = Student("Alice")   # __init__ is called here automatically
s1.say_hello()          # You manually call this method


# 2. Function vs method

# Regular Function
def is_prime(num):          # Function (not inside any class)
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))  # ✅ Function call

# Method inside a Class
class Number:
    def __init__(self, value):
        self.value = value

    def is_even(self):      # Method (belongs to class)
        return self.value % 2 == 0

n = Number(8)
print(n.is_even())          # ✅ Method call on object

# All methods are functions, but not all functions are methods

#3. how code works

class Pet:
    def __init__(self, name):
        self.name = name
        self.adopted = False

    def adopt_pet(self):  # Changes the object's state
        self.adopted = True
        print(f"{self.name} is now adopted!")

    def show_status(self):
        print(f"{self.name} - Adopted: {self.adopted}")

p1 = Pet("Jimmy")
p1.show_status()     # Shows: Adopted: False
p1.adopt_pet()       # Call method to adopt
p1.show_status()     # Now: Adopted: True

# 4.
# A method with self → called using an object
# A method without self → called using the class

class Greeting:
    def say_hello(self):  # method WITH self
        print("Hello from the object!")

    def say_bye():        # method WITHOUT self
        print("Bye from the class!")

g = Greeting()

g.say_hello()    # ✅ This will work: passes object as self

g.say_bye()      # ❌ This will give error (missing 1 argument)
                 # TypeError: say_bye() takes 0 positional arguments but 1 was given

Greeting.say_bye()  # ✅ This works fine!

