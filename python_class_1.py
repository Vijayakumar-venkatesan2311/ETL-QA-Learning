# example of downcasting
height_float = 5.8
print("heigh is" , height_float)
height_int = int(height_float)
print("heigh is", height_int)

# example of upcasting
height_int = 5
print("heigh is" , height_int)
height_float = float(height_int)
print("heigh is", height_float)

# with self parameter
class Hello:
    def printHello(self, name):
        print("Hi Gud mrng", name)

greet = Hello()
greet.printHello("vijay") # need self parameter - create object (greet) and then call with method (printHello)
                          # Here object.method


# without self
class Hello:
    def printHello(name):
        print("Hi Gud mrng", name)

Hello.printHello("vijay") # without self it will work ( directly call with class.method)


# This is a Class (Blueprint)
class Hello:

    # This is a method (function inside the class)
    def greet(self, name):  # 'self' refers to the object, 'name' is a parameter
        print("Hi, Good Morning", name)


# This is an object (created from the class)
person = Hello()

# Calling the method with an argument
person.greet("Vijay")  # "Vijay" is the argument


#typecasting
# convert the datatype into a specific datatype

age = int(18)
print(age)
print(type(age))


# looping concept

#if - else
age =20
if age >= 18:
    print("eligible for vote")
else:
    print("not eligible")

# if - elif - else
percentage = 20
if percentage <35:
    print("Failed")
elif percentage >=35 and percentage <=70:
    print("Second class")
else:
    print("First class")


# for loop
for x in range(5):
    print(x)

# while loop
i=0
while i<5:
    print(i)
    i +=1
