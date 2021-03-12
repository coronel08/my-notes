# Python
Indexing [start:stop:step]
```
a = [1, 2, 3, 4, 5, 6, 7, 8]
a[1:8:2]
```
<br>

* Naming Conventions for python
    * functions: snake_case
    * classes: CamelCase
* Use **with** to open files instead of **try open and close**. With closes file automatically 


Added python venv using 
```
virtualenv venv
<!-- Activate venv on linux -->
source venv/bin/activate
<!-- Activate venv on windows -->
venv\Scripts\activate
```

## Helpful Links
[FreeCodeCamp](https://www.freecodecamp.org/news/the-python-handbook/) Python Handbook
[RealPython](https://realpython.com/python-data-structures/) Python Data Structures

---
## Table of Contents
* [Python](#python)
    * [Data Types](#data-types)
    * [String Methods](#string-methods)
    * [Built in Functions](#built-in-functions)
    * [Loops and Conditionals](#loops-and-conditionals)
        * [While Loop](#while-loop)
        * [For Loop](#for-loop)
    * [Functions](#functions)
        * [Lambda](#lambda-functions)
        * [Recursion](#recursion)
* [OOP](#oop)
    * [Classes](#classes)
    * [Decorators](#decorators)

---
## Data Types
Immutable: cant be changed after its created
Mutable:can be changed, List/Dict/Set
* list - [] push and pop remove the last item
    * insert()/append() - add
    * remove()/pop() - remove 
* tuple (immutable) - () example below
```
name,age,country,career = ('Diana',32,'Canada','CompSci')
```
* dict - {'key':'value'}
    * .keys()
    * .values()
    * .items()
* set - set() or {'element1','element2'}
    * sets are unordered, no duplicates, but elements must be immutable. A tuple can include a set but not a list or dict
<br><br>
---

## String Methods
String methods dont modify original string, return a new string. [W3](https://www.w3schools.com/python/python_ref_string.asp) Python String Methods list
* isalpha() - string is not empty and contains only characters
* isalnum() - string is not empty and contains only digits
* isdeicaml() - string is not empty and contains digits
* lower() - get lowercase
* islower() - check if string is lowercase
* casefold() - turn lowercase
* upper() - get uppercase
* isupper() - check if string is uppercase
* title() - capitalize only 1st letter of words
* startwith() 
* endswith()
* replace()
* split()
* strip()
* join()
* find() 
* count() - counts number of times the string appears
<br><br>
---

## Loops and Conditionals
Can interrupt loop with **break or continue or pass or return** <br>
Exception handling with **try and except and raise and else**<br>


Ternary Operator
<result_if_true> if <condition> else <result_if_false>
```
def is_adult(age):
    return True if age > 18 else false
```
* use **if, elif, else, finally** for control flow


### While Loops
```
items = ['a','b','c','d','e']
start = 0
while start < len(items):
    print(items[start])
    start += 1
```

### For Loops
for loop

for loop with index
```
items = ['a','b','c','d','e']
for index, item in enumerate(items):
    print(index,item)
```
<br><br>

---
## Functions
```
def change(value=1):
    print (value)
change(5)
```

### Built in Functions
[Python Docs](https://docs.python.org/3/library/functions.html) <br>
[W3](https://www.w3schools.com/python/python_ref_functions.asp)
* abs() - absolute value
* dir() - returns a list of objects properties and methods
* enumerate() - takes a collection(tuple?) and returns it as an enumerated object
* filter()
* float()
* input()
* int()
* iter()
* len()
* map()
* max()
* print()
* sorted()
* str()
* tuple()
* zip()
<br>

### Args and Kwargs

#### Lambda Functions
lambda <arguments> : <expression>
```
multiply = lambda a,b : a*b
print (multiply(3,2))
```
Another Example
```
numbers = [1, 2, 3, 4, 5]
numbers_power_2 = list(map(lambda n : n**2, numbers))
```

#### Recursion

<br><br>
---

# OOP


## Classes
```
class Dog:
    def __init__(self,property):
        self.property = property

    def method/function
```
* __str__ - resturns a string (more for end users)
* __repr__ - returns a printable string (more for devs)

### Decorators

### Wrappers