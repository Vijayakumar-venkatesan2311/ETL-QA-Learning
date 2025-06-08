# datatypes in python

# primitive - basic datatype eg. int, float, double, long, boolean

# mark = 20 -- int datatype
# name = 'Ajay' -- str datatype
student_name = "Mayank"
print(f"{student_name} and datatype is {type(student_name)}")

student_rollno = 23738
print(f"{student_rollno} and datatype is {type(student_rollno)}")

student_mark = 98.00
print(f"{student_mark} and datatype is {type(student_mark)}")

student_pass_status = True
print(f"{student_pass_status} and datatype is {type(student_pass_status)}")

# non primitive - derived from primitive datatype
# marks = [ 20, 'Ajay'] - eg non primitive

# strings - sequence of characters
#         - but in python char datatype is not supported
#         - char type is supported by string


""""
List -  ordered collection of items , mutable , store different types of data
     -  order in which elements are inserted is maintained (Insertion order is preserved)
     -  Mutable - once list is defined, we can change the elements in the list (add, remove)
     - denoted by [] bracket
     - Elements in the list can be accessed by using indexes, index always start with 0
     - it contain duplicate values
"""

list  = ["Vijay", "Raj", "Venkat", 2, 2.05, True]
print(list)
print(type(list))

# add element by using index
list[0] = "Raghav"
print(list)

# accessing elements by index
print(list[1])

# adding elements
list.append("Vikram rathore")
print(list)

""""
result = list.append("Vikram rathore")
print(list)      -- this will give none as output why because vikram rathore is added to the list.
                 --  But .append() does not give you back the new list — it gives back None.
"""

# removing elements
list.remove(list[5]) # or remove("Vikram rathore")
print(list)

# list slicing
print(list[1:4:2]) # list[start:stop:step]
print(list[1:4]) # it will return 1, 2, 3 index not 4
print(list[:3])
print(list[2:])
print(list[-2:])

# negative slicing
my_list = ['a','b','c','d', 'e', 'f', 'g'] # negative index starts with 1... [-7,-6,-5,-4,-3,-2,-1]
print(my_list[-2:])
print(my_list[:-2])
print(my_list[::-2])
print(my_list[-6:-2])

# print all the items from the list --way 1--
names = ["Rohit", "Rickelton", "Jacks", "Surya", "Tilak"]
for i in names:
    print(i)

print("-----------------")

# print all the items from the list --way 2--
length = len(names)
print(length)
for i in range(0, length, 1):  # range(start, stop, step)
    print(names[i])

print("-----------------")

# print first 2 items from the list
for i in range(0,2,1):
    print(names[i])

""""
tuple - ordered collection of items that cannot be changed
      - order in which elements are inserted is maintained (insertion order is preserved)
      - Immmutable - once list is defined we cannot change the elements in the tuple
      - denoted by () bracket
      - Elements in the list can be accessed by using indexes, index always start with 0
      - it contain duplicate values
      - tuple is faster than list because in tuple the elements are static
"""

team_csk = ('Ruturaj', 'Dhoni', 'Jadeja', 'Ashwin', 'Dhoni')
print(type(team_csk))

# fetch value using index
print(team_csk[4])
print(team_csk)

# try to add element using index
team_csk[0] = 'conway'
print(team_csk)

"""
set - unordered collection of unique items that can be changed (mutable)
    - Insertion order is not preserved the order in which insertion happen is not guaranteed
    - mutable - we can change the elements in the list
    - denoted by {} bracket
    - Elements in the list can not be accessed by index
    - cannot contain duplicate values
"""

team_rcb = {"virat", "salt", "david", "krunal"}
print(team_rcb)

roll_nums = {1,2,3,32,4,25,24,2,24,233,423,4,4,5,2,1,42,2,3,4}
print(len(roll_nums))
print(roll_nums)

roll_nums.add(2)
print(roll_nums)

""""
Dictionary - Mapping datatype - unordered collection of key value pairs
cardinality - (1:1, 1:m, m:1, m:m)
Dictionary is a key value pair
"""

employees = {1:"Rajan", 2:"Velu", 3:"Guna", 4:"Thambi", 5:"Anbu"}
print(len(employees))
print(employees)

employees[2] = "Vijay"
employees[6] = "Gill"
print(employees)

# removing a key value pair
del employees[2]
print(employees)

# checking if a key exists
print(3 in employees)

# Boolean
# Boolean type represents true or false. used to represent binary conditions like logical operations

x = True
y = False

print(x and y)
print(x or y)
print(not x)

# Boolean values in conditional statements
for x in [True, False, True]:
    if x:
        print("Even")
    else:
        print("odd")
