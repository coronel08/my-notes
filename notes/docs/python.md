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
    * [Conditionals](#conditionals)
        * [Ternary Operators](#ternary-operators)
    * [Loops](#loops)
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
Immutable: cant be changed after its created <br>
Mutable:can be changed, List/Dict/Set <br>
Sets and Dictionaries are hash tables, they also drop duplicate entries. Dictionaries can not have two identicial keys<br>

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

## Conditionals
Exception handling with **try and except and raise and else**<br>

* use **if, elif, else, finally** for control flow
* use **with** to open files instead of **try open and close**. With closes file automatically, helpful for threading
```
with open("file.txt", "w") as output:
    output.write(
        "testing writing function"
    )
```

### Ternary Operator
<result_if_true> if <condition> else <result_if_false>
```
def is_adult(age):
    return True if age > 18 else false
```

### If
We can check if an item exists 
```
if test:
    print(test, 'does exist')
d = {'hello' : 'world' }
print(d.get('hello', 'default_value'))
<!-- This prints world since hello exist -->
print(d.get('howdy', 'default_value'))
<!-- This prints out default value since the key doesnt exist -->
```


---

## Loops
Can interrupt loop with **break or continue or pass or return** <br>


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
def func(positional, keyword=value, *args, **kwargs):
* positional are mandatory and have no defualt values
* keyword are optional and have default values
* args
* kwargs keyword arguments for passing a dictionary

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

#### Comprehensions
List Comprehensions, can also do if-else in a condition
```
a = [3,4,5]
b = [i for i in a if i >4 ]


<!-- Nested Loop list comprehension, great for making coordinates -->
num1 = [1,2,3]
num2 = [4,5,6]
nums = [(x,y) for x in num1 for y in nums2]
print(nums)

<!-- Multiple if conditions in list comprehension, print if divisbile by 2 and 5 -->
nums = [x for x in range(21) if x%2==0 if x%5==0]
```

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
numbers_filter = list(filter(lambda n: n > 3, numbers))
```

#### Recursion
A function thaat calls itself is a recursive function
```
def facotiral(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n, '*', end =' ')
        return n * factorial(n - 1)
```

#### Generators
Generators use parenthesis, need to use yield instead of return, and next(functionName) to call functionName. <br>
Can be used when dealing with complex function, large data, or state
```
def get_sequence(x):
    for i in range(x):
        yield i

seq = get_sequence(5)
next(seq)

<!-- Generator Expression -->
squares = (x*x for x in range(5))
print(next(square))

<!-- or pass a generator function to another fucntion  -->
sum(x*x for x in range(5))
```

<br><br>
---

# OOP
* Attributes = variables
* Methods = functions
* Property = 
* Objects = Classes instances
* Instantiate = test = class()

## Classes
```
class Dog:
    count = 0 # class attribute

    def __init__(self,property, age):
        self.property = property # instance attribute
        self.__age = age # private variable because dunder __
        Dog.count += 1 # alters the class attribute whenever a class is instantiated

    def test(self): # a class method/function
        pass
    
    @property #delcare property age
    def age(self):
        return self.__age

    @age.setter # setter for property age
    def age(self, value):
        self.__age = value

    @age.deleter # deleter for property age
    def age(self, value):
        print('...Deleting')
        del self.__age

    @classmethod
    def toStringClass(cls):
        print('Dog Class attribute ', cls.property)
    
    @staticmethod
    def toStringStatic(): 
        print('Static method of dog')
```
* __str__ - resturns a string (more for end users)
* __repr__ - returns a printable string (more for devs)

### Decorators
Can use a decorator to nest a function within another function. [tutorialsteacher.com](https://www.tutorialsteacher.com/python/decorators)
```
def myDecorator(function) # decorator function
    def innerFunction():
        function()
        print('Inner function')
    return innerFunction # return a wrapper function

@myDecorator
def greet():
    print('Hello from greet function')

greet()
```

#### Built in Decorators
* @property can use on any method/ function in the class to declare the method as a property
    * @propertyName.setter
    * @propertyName.deleter 
* @classmethod
    * has to be called by Classname.MethodName() or object.MethodName()
    * can acccess class attributes but not the instance attributes
    * can be used to declare a factory method that returns objects of a class
* @staticmethod 
    * has to be called by Classname.MethodName() or object.MethodName()
    * cant have cls or self parameter
    * cant access class attributes or instance attributes

### Wrappers

# Destructuring 
```
string = 'This is a test string.'
_, is, *rest = string.split(' ')
<!-- prints is -->
```
