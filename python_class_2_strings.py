# strings
"""
- strings are characters of symbols. arrays of bytes representing unicode characters
- computer only understands bytes. unicode = universal character encoding standards
- strings in python are surrounded by single or double quotes
- python doesn't have char datatype
- each characters can be accessed by using indexes, index always starts with 0
"""

# A = 65
# convert character to equivalent unicode
print(ord('A'))

# converts unicode to equivalent character
print(chr(65))

address = "Bangalore"
size = len(address)
print(address[size - 1])
print(address[0])

print(address.upper())

# --way1-- print the characters in the string
for char in address:
    print(char)

# --way2-- print the characters in the string
for char in range(4):
    print(address[char])

# string slicing - to extract substring from the strings

# syntax substring = s[start:stop:step]

#specify only start index
s = "Hello World"
print(s[2])

# positive index - Hello World -> 0 1 2 3 4 5 6 7 8 9 10
# negative index - Hello World -> -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# omitting indices
print(s[:8])
print(s[::3])
print(s[-9::-2]) # lH   right ----> Left
print(s[-9::2]) # loWrd  Left ----> right
print(s[9:-1]) #l        Left ----> right

# split function
# it is used to divide a list of substrings based on a specified delimiter

a = "vijay.venkat99@gmail.com"
print(a.split("@"))
print(a.split("."))

i = a.split('9')
print(i, type(i))