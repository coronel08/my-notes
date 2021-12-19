# Python
Can run a script -interactive by using -i flag

```
python -i <script>
```

Use pathlib instead of os.path [Towards DataScience](https://towardsdatascience.com/why-you-should-start-using-pathlib-as-an-alternative-to-the-os-module-d9eccd994745)


Indexing [start:stop:step]
```
a = [1, 2, 3, 4, 5, 6, 7, 8]
a[1:8:2]
```
<br>

* Naming Conventions for python
    * functions: snake_case, constants uppercase SNAKE_CASE
    * classes: CamelCase
    * module names/file names : keep name short and lowercase, avoid special symbols
    * Parameters = variable names in def statement, arguments = values passed into a function


Added python venv using, can use [configParser](https://pythonhowtoprogram.com/how-to-use-configparser-for-configuration-files-in-python-3/) or python-dotenv for secret/variavles
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
    * [Conditionals](#conditionals)
        * [Ternary Operators](#ternary-operator)
            * [If](#if)
            * [In](#in)
    * [Loops](#loops)
        * [While Loop](#while-loop)
        * [For Loop](#for-loop)
    * [Iterate](#iterate)
        * [List Comprehension](#list-comprehension)
        * [Dict Comprehension](#dict-comprehension)
    * [Functions](#functions)
        * [Built in Functions](#built-in-functions)
        * [Lambda](#lambda-functions)
        * [Recursion](#recursion)
        * [Generators](#generators)
* [OOP](#oop)
    * [Classes](#classes)
    * [Decorators](#decorators)
        * [Built in Decorators](#built-in-decorators)
    * [Wrappers](#wrappers)
* [Destructuring](#destructuring)

---
## Data Types
Immutable: cant be changed after its created <br>
Mutable:can be changed, List/Dict/Set <br>
Sets and Dictionaries are hash tables, they also drop duplicate entries. Dictionaries can not have two identicial keys<br>

* list - [] push and pop remove the last item
    * insert()/append() - add
    * remove()/pop() - remove 
* tuple (immutable) - () example below
    * namedtuple - also an option 
```
name,age,country,career = ('Diana',32,'Canada','CompSci')
```
* dict - {'key':'value'} dictionary methods below, can also do OrderedDict for a doubley linked list [thispointer dict multiple values](https://thispointer.com/python-dictionary-with-multiple-values-per-key/)
    * .get() - returns the value of a key
    * .keys()
    * .items()
    * .values()
    * .clear() - removes all keys
    * .update() - updates key value
    * .setdefault() - returns key value, if none sets it to default value and returns that
* set - set() or {'element1','element2'}
    * sets are unordered, no duplicates, but elements must be immutable. A tuple can include a set but not a list or dict
    * Python has set methods as well [tutorialsteacher.com](https://www.tutorialsteacher.com/python/set-methods)
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
[Mathspp Blog](https://mathspp.com/blog/pydonts/chaining-comparison-operators) chaining conditionals <br>

* use **if, elif, else, finally** for control flow
* use **with** to open files instead of **try open and close**. With closes file automatically, helpful for threading
* use **is** to compare instead of ==
* can **short-circuit** a conditional, prove a conditional wrong or right with **and** / **or** / **all**/ **any**
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

a, b = 10, 20
min = a if a < b else b
```

### If
We can check if an item exists 
```
if test:
    print(test, 'does exist')

<!-- checking in a dict -->
d = {'hello' : 'world' }
<!-- This prints world since hello exist -->
print(d.get('hello', 'default_value'))
<!-- This prints out default value since the key doesnt exist -->
print(d.get('howdy', 'default_value'))
```
### In
```
name_list = ["Fidel","Karina"]
number_list = [323,714]
text = "Mom text to someone out"

for index, value in enumerate(name_list):
    if value in text:
        print(f"{index}:{value} in text, return number {number_list[index]}")
    else:
        pass
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
```
words = ["Hey", "there"]

# pythonic way
for word in words:
    print(f"{word} has {len(word)} letters in it")

# bad way
for i in range(len(words)):
    print(f"{words[i]} has {len(words[i])} letters in it")
```

for loop with index
```
items = ['a','b','c','d','e']
for index, item in enumerate(items):
    print(index,item)
```
<br><br>

---


## Iterate
Using Enumerate to add index to item iteration. Can also use zip before enumerate to combine multiple lists
```
list1 = ['a', 'b', 'c', 'd', 'e']
for index, item in enumerate(list1):
    print(index,item)
```
Using zip
```
list_a = [1, 2, 3, 4]
list_b = [10, 20, 30, 40]
list_c = ["a","b","c","d"]

# zip a list into a tuple, could also enumerate a zip into a dict
test = list(zip(list_a,list_b, list_c))

# List comprehension
list_sum = [a + b for a, b in zip(list_a, list_b)]
# for loop to zip into a list
list_sum = []
for a, b in zip(list_a, list_b):
  list_sum.append(a + b)
print(list_sum) # [11, 22, 33, 44]
```
For list of unequal lengths zip_longest and zip_shortest
```
from itertools import zip_longest, zip_shortest
short = [1, 2]
long = [10, 20, 30, 40]
zip_short = [a + b for a, b in zip(short, long)]
print(zip_short) # [11, 22]
zip_long = [a + b for a, b in zip_longest(short, long, fillvalue=0)]
print(zip_long) # [11, 22, 30, 40]
```


### List Comprehension
List Comprehensions, can also do if-else in a condition
```
a = [3,4,5]
b = [i for i in a if i >4 ]
<!-- Can chain if, else statements in a list comprehension -->
c = [x ** 2 for x in range(7) if x%2 == 0 and x%6 == 0]
<!-- another example -->
L = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ]
resL = [ x.replace('_', ' ') for x in L ]


<!-- Nested Loop list comprehension, great for making coordinates -->
num1 = [1,2,3]
num2 = [4,5,6]
nums = [(x,y) for x in num1 for y in num2]
print(nums)

<!-- Multiple if conditions in list comprehension, print if divisbile by 2 and 5 -->
nums = [x for x in range(21) if x%2==0 if x%5==0]
```
### Dict Comprehension
```
my_basket = {'apple': 2, 'banana': 3, 'starfruit': 1}
double_my_basket = {k:v*2 for (k, v) in my_basket.items()}
print(double_my_basket) # {'apple': 4, 'banana': 6, 'starfruit': 2}
```


### Generator Expression
Generators are used to create iterators, use yield, next, and return for returning a result. Takes less memory than a regular function.
[geeksforgeeks example](https://www.geeksforgeeks.org/generator-expressions/)
```
test_generator = (num ** 2 for num in range(10))
for num in test_generator:
    print(num)
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
* abs() - absolute value, positive numbers only
* dir() - returns a list of objects properties and methods
* enumerate() - takes a collection(tuple?) and returns it as an enumerated object
* filter()
* float()
* input()
* int()
* iter()
* join()
* len()
* map()
* min() - accepts key function
* max() - accepts key function
* print()
* sorted() - accepts key function
* str()
* sum()
* tuple()
* zip()

```
# key passes a function to the elements

l1=['blue','green','red','orange']
print(max(l1, key=len))
```

### Lambda Functions
lambda <arguments> : <expression> <br>

```
multiply = lambda a,b : a*b
print (multiply(3,2))
```
Another Example can also be written as list comprehensions
```
numbers = [1, 2, 3, 4, 5]
numbers_power_2 = list(map(lambda n : n**2, numbers))
numbers_filter = list(filter(lambda n: n > 3, numbers))

L = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ]
resl = list(map((lambda x: x.replace('_', ' ')),L))

```

### Recursion
A function that calls itself is a recursive function
```
def factorial(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n, '*', end =' ')
        return n * factorial(n - 1)
```

### Generators
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
for x in squares:
    print(x)

<!-- or pass a generator function to another fucntion  -->
sum(x*x for x in range(5))
```
<br><br>

---
# OOP
* Attributes = variables, usually name following a .
* Methods = functions
* Property = 
* Objects = Classes instances
* Instantiate = test = class()

Private variable example using bank account (Beyond the Basic Stuff , Al S)[https://inventwithpython.com/beyond/chapter15.html]


## 4 Pillars of OOP
* Inheritance - inherits methods and property from another class, Parent and Children classes.
* Polymorphism - a parent object that gives structure to a child object, can use Method Overriding to overwrite parent methods. Method Overloading not available in python
* Encapsulation - setter and getter / private functions
```
# attributes can't be changed or accessed by self.wall_material
class House:
    def set_wall_material(self, wall_material):
        self.wall_material = wall_material
    
    def get_wall_material(self):
        print(self.wall_material)
```
* Abstraction - 

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

### Decorators and Wrappers
Can use a decorator to nest a function within another function. [tutorialsteacher.com](https://www.tutorialsteacher.com/python/decorators)
```
def myDecorator(function): # decorator function
    def innerFunction():
        function()
        print('Inner function')
    return innerFunction # return a wrapper function

@myDecorator
def greet():
    print('Hello from greet function')

greet()


""" Without using decorator called like below
def greet():
    print("Hello from greet function")
greet = myDecorator(greet)
"""
```

#### Built in Decorators
* @property can use on any method/ function in the class to declare the method as a property
    * @propertyName.setter
    * @propertyName.deleter 
* @classmethod
    * has to be called by Classname.MethodName() or object.MethodName()
    * can acccess class attributes but not the instance attributes
    * can be used to declare a factory method that returns objects of a class
* @staticmethod - used when you want to access the class method without Instantiation
    * has to be called by Classname.MethodName() or object.MethodName()
    * cant have cls or self parameter
    * cant access class attributes or instance attributes
* @abstractmethod 
    * used to create an abstract method, empty in base class and used only for defining structure, this decorator forces the subclasses to implement method
    * from abc import ABC, abstractmethod
    * [Abstract Base Class](https://towardsdatascience.com/abstract-base-classes-in-python-fundamentals-for-data-scientists-3c164803224b)




### High Order Functions
Functions that can accept other fucntions as an argument are called High Order Functions
```
def whisper(name):
    return name.lower()

def shout(name):
    return name.upper()

def greeting(func):
    return func("Test String")

print(greeting(whisper))
print(greeting(shout))
```
<br><br>


---

# Destructuring 
[Mathspp blog](https://mathspp.com/blog/pydonts/structural-pattern-matching-tutorial)
```
string = 'This is a test string.'
_, this, *rest = string.split(' ')
<!-- prints is -->
```
