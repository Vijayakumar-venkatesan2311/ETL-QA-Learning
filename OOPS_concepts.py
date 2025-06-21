# OOPS - Object Oriented Programming

# classes - class is a blueprint/design/model/plan for a object. defines a set of attributes(data) and
#           methods(functions) that the objects created from the class can use

# objects - an object is an instance/physical existence of a class

class Scaler:
    Course1 = "SQL"
    Course2 = "Python"

print(Scaler.Course1) # call directly using class name
print(Scaler.Course2)

obj = Scaler()   # create object for the class
print(obj.Course2)  # call the variables with the object created

class Pet:
    def __init__(self, name, pet_type, age): # built in function or method - constructor method
        self.name = name
        self.pet_type = pet_type
        self.age = age
        self.adopted = False

    def adopt_pet(self):
        self.adopted = True

    def display_info(self):
        print(f"DEBUG: adopted = {self.adopted}")
        status = "Adopted" if self.adopted else "Available"
        print(f"{self.name} is a {self.age} year old {self.pet_type}. status: {status}")

pet1= Pet("Jimmy", "Dog", 3) # create object and with the class name will pass values for the constructor method and during
                             # object creation the constructor will start executing
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
        return "No, it's not a prime number"
    for i in range(2, num):
        if num % i == 0:
            return f"No, {num} is divisible by {i}, so it's not prime"
    return f"Yes, {num} is a prime number"

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

class goa:
    name="Rajesh"
    drink=""
    def party(self):
        print("Let's party......")
    def beach(self):
        print("Enjoying the beach")

ramesh = goa()
suresh = goa()

ramesh.name = "ramesh"
suresh.name = "suresh"

ramesh.drink = "Yes"
suresh.drink = "No"

print(ramesh.name)
print(ramesh.drink)
print(suresh.name)
print(suresh.drink)

ramesh.party()
ramesh.beach()

# way 1
class laptop:
    def __init__(self): # python inbuilt function - constructor
        self.price=0
        self.ram=""
        self.processor=""

    def display(self):
        print("display")

hp = laptop() # create the object and without calling the function(__init__) explicitly like below, it will print
hp.display() # create the object and then we need to call the function explicitly then only it will print (ans: display)

hp.price=50000
hp.ram = "8gb"
hp.processor="i5"
print(hp.price)

# way 2
class HP_laptop:
    def __init__(self, price, ram, processor): # python inbuilt function - constructor
        self.price= price
        self.ram= ram
        self.processor=processor

    def display(self):
        print(f"HP laptop for {self.ram} ram and {self.processor} processor price is {self.price}")
        print("display")

hp = HP_laptop(80000, "12gb", "i7")
hp.display()


class student:
    def __init__(self):
        self.name="Vijay"
        self.register="53453"

    def display(self):
        print(f"Register no for student {self.name} is {self.register}")

s1 = student()
s1.display() # in background it will be act as s1.display(s1) it go to line 186 def display(s1) s1.name is vijay and s1.register = 53453