# python - high level, intepreted language (line by line execution)
# java - compiled language (reads entire code once and execute after that)

# python execution flow

# hello.py --> python interpreter --> bytecode (.pyc) [hello310.pyc] -- (python virtual machine) --> output

# java execution flow

# hello.java --> java compiler (javac) --> bytecode(.class) [hello.class] -- (java virtual machine) --> output

"""
programming paradigm
1. procedural way 2. object oriented way

python supports both procedural + object oriented ways
java supports only object oriented way

key differences

python                                                  java
1. Indentation                                   semicolon, paranthesis
2. platform specific                             highly portable run on any platform
3. faster (lesser lines of code)                 slower (lots of code)
4. slower not portable                           faster portable
we can't use .pyc on every platform              run .class file at any platform

"""

# single line comment

"""
Multi line comment 
"""

""" 
python is dynamically typed language , it means the datatype is pre defined like other programming 
languages, the data type is determined by python based on value it stores
"""

"""
package - contain __init__.py file
directory - no __init__.py file

In a package (i.e., a folder with __init__.py), Python knows it can import from that folder.
In a directory (no __init__.py), Python doesn't treat it as something it can import from directly.

✅ A Python file inside a package can be imported.
❌ A Python file inside a directory can’t be imported (unless it's in the same folder or the path is manually added).

"""

print("Hello world")

name = 'Vijayakumar'
age = 23

print(f"the age for this employee name {name} is {age}")

"""
ls - list all files in the directory
python -m compileall hello.py - (compile .py file into .pyc file) it will generate a .pyc file inside the __pycache__ directory
python -m py_compile hello.py - function is same as above one but it will compile only one file at a time 
python python_basics.py - it will produce the output 
python -m dis my_script.py - Disassembles Python bytecode into a human-readable format.
"""

""""
camelcase -  myFirstName
pascalcase - MyFirstName
snakecase - my_first_name
"""

"""
Typecasting -  conversion of datatype from one to another 

Upcasting - converting lower datatype to higher datatype eg.. int to float 

downcasting - converting from higher to lower datatype eg.. float to int 
            - potentially losing data

"""
