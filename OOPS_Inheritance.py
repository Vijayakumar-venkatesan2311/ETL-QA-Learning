# Inheritance - that allows a class (child class) to inherit properties and methods from another class (parent class)

# why it is needed -
# Avoid code duplication
# support polymorphism - same method behaves differently depending on the object

class Animal:
    def speak(self):
        print("Dog speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()

# Intermediate example

class Animal:
    def speak(self):
        print("Dog is not speaking")

class New_Dog(Animal):
    def speak(self):
        print("Dog barks instead")

new_dog = New_Dog()
new_dog.speak() # output will be - Dog barks instead


# real project structure using inheritance

# Base class - Generic ETL job

class ETLJob:
    def extract(self):
        raise NotImplementedError("Extraction not happened")

    def transform(self):
        raise NotImplementedError("Transformation not happened")

    def load(self):
        raise NotImplementedError("Loading not happened")

    def run(self):
        self.extract()
        self.transform()
        self.load()

# preprocessing job

class ExtractToInputJob(ETLJob):
    def extract(self):
        print("Reading files from input-extract")

    def transform(self):
        print("Applying preprocessing rules (renaming, flattening, validation)")

    def load(self):
        print("Saving processed files to input")

# Bronze and silver job

class InputToBronze(ETLJob):
    def extract(self):
        print("Reading clean input files from input")

    def transform(self):
        print("No transformation needed for this step")

    def load(self):
        print("Loading the raw data to bronze layer")

class BronzeToSilver(ETLJob):
    def extract(self):
        print("Reading data from bronze layer")

    def transform(self):
        print("Cleaning nulls, joining lookup tables, deriving columns")

    def load(self):
        print("Writing transformed data to silver layer")

def run_job(a):
    a.run()

# It creates a list of 3 objects job1, job2, job3
jobs = [
    ExtractToInputJob(),
    InputToBronze(),
    BronzeToSilver()
]

# Run each job one by one
for job in jobs:
    print(f"\nRunning job: {job.__class__.__name__}")
    run_job(job)

# job.__class__.__name__ - “Give me the name of the class of this object.”

# How iteration happens
"""
step 1:
job = ExtractToInputJob()
print("Running job: ExtractToInputJob")
run_job(job)

step 2:
def run_job(job):
    job.run()

step 3:
class ExtractToInputJob(ETLJob):
    def run(self):   # comes from ETLJob
        self.extract()
        self.transform()
        self.load()
"""


# New Example:

class Vehicle:
# parameterized constructor
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} started")

    def stop_engine(self):
        print(f"{self.brand} {self.model} stopped")

class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        # we have added one more parameter fuel_type that is not available in vehicle class
        # so we have explicitly mentioned that in the line 143 but we dont want to redundant whatever available in
        # line 128, 129 so that's why we added line 143 instead of line 128, 129
        super().__init__(brand,model)
        self.fuel_type = fuel_type

    def honk(self):
        print(f"{self.model} {self.brand} is honking: beep beep")

    def start_engine(self):
        print(f"{self.brand} {self.model} started with {self.fuel_type}")

class ElecticCar(Vehicle):

    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.model} {self.brand} is charging")

# create an object of the Vehcile class ( Parent class )
vehicle = Vehicle("Toyota","Camry")
vehicle.start_engine()
vehicle.stop_engine()

# Create an object of the Car class ( child class ) and see we can use the existing methods from Parent ( Vehicle class )
car = Car("Honda","Honda civic","Petrol")
car.start_engine()
car.honk()

electricCar = ElecticCar("Tesla","ModelS",100)
electricCar.start_engine()
electricCar.charge()
