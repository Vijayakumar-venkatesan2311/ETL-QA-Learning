# List

new_list = [10,20,30,40,50]

print(new_list[-1])
print(new_list[-2])
print(new_list[2])
print(new_list[1:3])

# set
set_1 = {10,20,30,40,50,60,60,50}

# for ele in set_1:
#     print(ele)

my_new_list = list(set_1)
print(my_new_list[0])
print(my_new_list)

# Dictionary
""""
stores key value pair 
unordered, mutable - add or remove key value pairs in the dictionary where key must be unique and immutable
"""

my_dic = {1:"Rohit", 2:"Rickelton", 3:"Jacks", 4:"Surya", 5:"Tilak"}

print(my_dic)

# accessing values using get method
print(my_dic.get(1))

# accesing values using key
print(my_dic[2])

# adding or modifying elements
my_dic[6] = "Hardik"
print(my_dic)

my_dic[3] = "David"
print(my_dic)

# removing elements
del my_dic[3]
print(my_dic)

my_dic.pop(4) # specify which element we need to remove
print(my_dic)

my_dic.popitem()  # remove last element
print(my_dic)

# iterating over keys
for key in my_dic:
    print(key)

# iterating over values
for values in my_dic.values():
    print(values)

# iterating over key value pairs
for key, values in my_dic.items():
    print(key, values)

# accessing key and value
print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())

# list
# how to print a list
"""
using index - list[0], list[1], list[2]
using slicing - list[0:3:1]
using loop - for i in range(0,3,1)
"""

# how to access last 3 elements
list = [1,2,3,4,5,6,7,8,9]

#way 1
for i in range(-1,-4,-1):
    print(list[i])

# way 2
len_list = len(list)
last_index = len_list -1

for i in range(last_index,last_index-3,-1):  # (8, 5, -1)
    print(list[i])

# way 3
while last_index >= len(list)-3 :
    print(list[last_index])
    last_index -=1

# Write a function that doesn’t return but print the max number from the list

"""
first create one variable and store the first element 
check the first number with all the numbers if any number is greater than first number store in that variable
"""
def getmax(list2):
   max = list2[0]
   for i in list2:
       if i > max:
           max = i
   print(max)
   return max     # find the max value from the list and retrun the max number and add 100 to it and print that

s = getmax([1,23,13,42,53,11,24])
print(s+100)

# Program that returns a list of all prime numbers without using function
# find prime from 1 - 20
"""
1. the number divided by 1 and itself is prime 
2. 2/1 2/2, 3/1 3/2 3/3 , 4/1 4/2 4/3 4/4, 
"""
primes = []
for i in range(1,21):
    count = 0
    for j in range(1, i+1):  # (1,5) i=4
        if i % j ==0:
          count = count +1
    if count ==2:
        primes.append(i)

print(primes)

#  Q 1:  From a given list, how to count the number of occurrences of each element in the list.

d_list = [1,3,4,5,2,1,4,2,1,4,2,1,5,2,6,3,2,4,6,3,4,2]
"""
1. we need to check one value with all the values in the list 
"""
dic = {}

for i in d_list:
    if i in dic:
        dic[i] = dic[i] +1
    else:
        dic[i] = 1

print(dic)

# or

from collections import Counter

dic = Counter(d_list)
print(dic)

# or

dic1 = {}

for i in d_list:
    dic1[i] = dic.get(i,0) + 1

print(dic)

# get method

new_dic = {1: "vijay", 2:"Raj"}
print(new_dic.get(1, 0)) # key available so return vijay
print(new_dic.get(3, 0)) # key not available so return our default value 0
print(new_dic.get(3)) # key not available and also we didn't mention default value as well so return none

# How to Acess the last 3 element from the 3rd last to last element

# way 1
list_new = [1, "a", 3, 4, 1, 2, 3, 4, 5, "a", "b"]

for i in range(-3,0,1):
    print(list_new[i])

"""
rule of slicing (range function works differently) 
check start and stop first if it is negative first convert that into positive ( using len(list) )
positive step -  start < stop
negative step -  start > stop 
"""

"""
rules for range function
positive step -  start < stop
negative step -  start > stop 
special case:
start == stop, range() always gives empty list
"""

# way 2
len_list = len(list_new)
last_index_1 = len_list - 1   # 10

for i in range(last_index_1-2, last_index_1+1, 1): #(8, 11, 1)
    print(list_new[i])

# checking if the list is having duplicates
a = [1, 3, 2, 4, 6, "a", "b"]

set_element = set(a)

if len(a) == len(set_element):
    print("there are no duplicates in the list")
else:
    print("duplicates found")

# way 2

def check_duplicate_in_the_list(a):
    new_set = set()
    for ele in a:
        if ele in new_set:
            return True
        new_set.add(ele)
    return False


if check_duplicate_in_the_list(a):
    print("duplicate")
else:
    print("no duplicate")

# set

set_item = {1,2,3,4,1,2,5}

for ele in set_item:
    if ele == 4:
        print("present")




