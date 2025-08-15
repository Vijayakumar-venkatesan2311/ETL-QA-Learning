# Encapsulation - idea of Encapsulation is to wrap up both data and methods into one single unit

# why encapsulation
# to protect the internal state of the object
# to control how data is accessed or modified

# access modifier - helps to protect the methods and data inside the class

# class - variables + methods

#

# basic

class Employee:
    def __init__(self, name, age):
        self.name = name
        self._department = "HR"
        self.__salary = 60000

emp = Employee("Vijay", 26)
print(emp.name)
print(emp._department)

# print(emp.__salary) AttributeError: 'Employee' object has no attribute '__salary'
print(emp._Employee__salary)
print(emp.__dict__)

# Modifier	             Use Case
# public	          Fields/methods meant to be accessed by other parts of code (UI, APIs, etc.)
# _protected	      Meant for internal use within class or subclasses (not for external access)
# __private	          Sensitive data (salary, credentials) that should never be touched directly


# real world - salary system example

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def salary_raise(self, percent):
        self.__salary  += self.__salary * percent/100 if percent > 0 else "None"

    def get_salary(self):
        return self.__salary

emp = Employee("Vijay", 90000)
emp.salary_raise(10)
print(emp.get_salary())


# Intermediate level

class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

    def get_salary(self):
        return self.__salary

emp = Employee()
emp.set_salary(10000)
print(emp.get_salary())

# the same code ( line 55 - 70) in more advanced way using property and setter

class Employee:
    def __init__(self):
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

emp = Employee()
emp.salary = 60000
print(emp.salary)


# advanced

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number  # Read-only

acc = BankAccount("ABC123")
acc.deposit(1000)
print(acc.get_balance())      # 1000
print(acc.account_number()) 
# acc.account_number = "XYZ"  # ❌ Error, read-only

# if you define a setter it will work ( check below code)

class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number

    @property
    def account_number(self):     # ✅ Getter
        return self.__account_number

    @account_number.setter
    def account_number(self, value):  # ✅ Setter
        if isinstance(value, str):
            self.__account_number = value
        else:
            raise ValueError("Account number must be a string")

acc = BankAccount("ABC123")
print(acc.account_number)  # ✅ OK
acc.account_number = "XYZ999"  # ✅ Now this works too