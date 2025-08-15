# polymorphism - many + form

# ways to achieve polymorphism

# method overloading - same method name with diff arguments / parameters
# method overriding - same method name with exact parameters can behave differently in child class
# operator overloading - same operator works differently

# method overloading possible in java

# Eg..,
"""
Java - method overloading

Invalid Example :
----------------
class Example {
    void display(String s) {
        System.out.println("First: " + s);
    }

    void display(String str) {
        System.out.println("Second: " + str);
    }
}

Error: Method display(String) is already defined in class Example.

👉 Reason: Both methods have the same name and same parameter type —
  Java can't distinguish between them, so it’s not valid overloading.

Valid Example:
---------------
class Example {
    void display(String s) {
        System.out.println("String: " + s);
    }

    void display(String s, int count) {
        System.out.println("String and int: " + s + ", " + count);
    }
}

python - method overloading

class Example:
    def display(self, s: str):
        print("First method:", s)

    def display(self, str_: str):  # This overwrites the first method
        print("Second method:", str_)

obj = Example()
obj.display("Hello")  # Output: "Second method: Hello"

Python does not care about parameter types — only the latest method definition is kept.


class Example:
    def display(self):
        print("No arguments")

    def display(self, a):
        print("With argument:", a)

obj = Example()
obj.display(5)  # Calls the second method: "With argument: 5"
obj.display()   # ❌ Error: missing 1 required positional argument

"""


# method overriding

# Case 1: Penguine class overrides fly() method
class Bird:
    def fly(self):
        print("Bird can fly")

class penguine(Bird):
    def fly(self):
        print("Bird can't fly")

b = penguine()
b.fly()

# Case 2: Penguine class simple inherits fly() method
class Bird:
    def fly(self):
        print("Bird can fly")

class penguine(Bird):
   pass

b = penguine()
b.fly()

# Case 3: Create an object of Bird class - fly() method called from Bird class

class Bird:
    def fly(self):
        print("Bird can fly")

class penguine(Bird):
    def fly(self):
        print("Bird can't fly")

b = Bird()
b.fly()

# operator overloading

class operatoroverloading:
    def __init__(self, num1, num2, str1, str2):
        self.sum_of_numbers = num1 + num2
        self.concating_string = str1 + str2

    def newmethod(self):
        print(self.sum_of_numbers)
        print(self.concating_string)

b = operatoroverloading(10, 20 , "Vijay", "Kumar")
b.newmethod()

class circle:
    def area(self):
        return 3.14 * 4 * 4

class square:
    def area(self):
        return 4 * 4

class traingle:
    def area(self):
        return 0.5 * 4 * 6

objects = [circle(), square(), traingle()]

for object in objects:
    print(object.area())

    
