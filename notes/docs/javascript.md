# Javascript Notes
* increment = ++
* decrement = --
<br><br>

---
## Table of Contents
* [Javascript Notes](#javascript-notes)
    * [Closures and Nesting Functions](#closures-and-nesting-functions)
        * [private variable](#private-variable)
    * [Recursion vs Loop](#recursion-vs-loop)
    * [Array Methods](#array-methods)
        * [splicing](#splicing)
        * [slice](#slice)
    * [Sorting Arrays](#sorting-arrays)
    * [Array Itteration](#Array-Itteration)
    * [Strip HTML strings](#Strip-HTML-strings)
    * [Destructuring](#Destructuring)
    * [Conditionals vs Switch vs Ternary](#Conditionals-vs-Switch-vs-Ternary)
    * [Arrow Functions](#arrow-functions)
    * [Function](#function)
    * [Promises](#promises)

---
## Closures and Nesting Functions
[Closures Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
```
function makeAdder(a){
    return function(b){
        return a + b
    }
}
var add5 = makeAdder(5)
var add20 = makeAdder(20)
add5(8)
add20(8)
```
another example
```
function init(){
    var private = 'Mozilla'
    function displayName(){
        return private
    }
    return displayName()
}
myInit = init()
myInit()
```
** best Example ** can also be redone to use arrow functions
```
var counter = function(){
    var privateCounter=0
    function changeCount(value){
        privateCounter += value
    }

    return{
        increment:function(){
            changeCount(1)
        },
        decrement:function(){
            changeCount(-1)
        },
        value:function(){
            return privateCounter
        }
    }
}
counter1=counter()
counter2=counter()
counter1.increment()
counter1.value()
counter2.value()
```
### private variable 
```
function secretVariable(){
    var private = "secret variable"
    return function(){
        return private
    }
}
var getPrivateVariable = secretVariable()
console.log(getPrivateVariable())
```
<br><br>

---
## Recursion vs Loop
For Loop below / Iteration
```
function countdown(number){
    for (let i=number; i > 0; i--) {
        console.log(i)
    }
}
```
Recursion below, a recursive function calls itself
```
function countdown(number){
    if(number === 0){
        return
    }

    console.log(number)
    countdown(number - 1)
}
```
<br><br>

---
## Array methods
* [array method chart](https://www.w3schools.com/jsref/jsref_obj_array.asp)
* [array method examples](https://www.w3schools.com/js/js_array_methods.asp)

[Web Dev Simplified YT](https://www.youtube.com/watch?v=R8rmfD9Y5-c) 8 Javascript array tutorials. 

<br><br>

### Add or Delete an item in an array

Can add or delete to an array using **pop/push** for last items. **Shift/unshift** for begining of array. 

Can also add to back of an array by using **Length**
```
fruits[fruits.length] = "Pineapple"
```
Using ES6, use [rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
```
fruits = ["start", ...fruits]
```
<br>

Change value of an item by using array index. changes apple to Kiwi
```
var fruits = ['Apple','Orange']
fruits[0] = 'Kiwi'
```
<br>

### Splicing
Using Splice to add new items to an array. <br>
Splice(start,del, items)
```
fruits.splice(1,0,"item1")
```

### Slice
Slice method slices out a piece of an array into a new array. <br> 
slice(start,stop)
<br> <br>

---
## Sorting Arrays
[W3 Sorting Arrays page](https://www.w3schools.com/js/js_array_sort.asp)
sort(): Sorts an array alphabetically 
reverse(): reverse sort
random use [Fisher Yates Method](https://www.w3schools.com/js/js_array_sort.asp)<br><br>

### Highest or Lowest Array Value
**Sorting Ascending**
Now points[0] will return lowest value
points[points.length - 1] will return highest value
```
var points = [40,100,1,5,25,10]
points.sort(function(a,b){return a - b})
```
**Sorting Descending**
```
points.sort((a,b) => b - a)
```
#### Can also use Math.max() or Math.min()
<br><br>

---
## Array Itteration
[Youtube vid](https://www.youtube.com/watch?v=R8rmfD9Y5-c) on filter, map, find, foreach
[W3 Array itteration](https://www.w3schools.com/js/js_array_iteration.asp)
[High Order fucntions / array iteration exampels](https://vegibit.com/higher-order-functions-in-javascript/)
* forEach(): need to learn, check link above
* map()
* filter(): creates a new array with items that pass filter
* reduce(): adds all values
* every(): checks if every item passes test/function
* some(): check if some items pass test/function
* indexOf(): returns index of item looking for
* lastIndexOf(): returns last occurence of item 
* find(): returns value of item that passes test/fucntion
* findIndex(): 
<br><br>

---
## Strip HTML strings
strip the html from an element
```
const stripHTMLTags = str => str.replace(/<[^>]*>/g, '')
<!-- Example -->
stripHTMLTags ('<a href="#"> Me and you </a>')
```
<br><br>

---
## Destructuring
[Web Dev Simplified YT](https://www.youtube.com/watch?v=NIq3qLaHCIs) Array and Object destructuring tutorial

Example below skips b and then defines the rest using rest/spread operator. Based on position
```
const alphabet = ['a','b','c','d','e','f']
const [a,,c,...rest] = alphabet
console.log(a,c,rest)
``` 
A function that returns an array thaat gets deconstructed
```
function testFunction(num1,num2){
    return [a+b, a*b]
}
const [sum, multiply, division='No'] = testFunction(3,4)
```
OBJECT DESTRUCTURING, instead of being based on position it is based on the name of the key. Need to research on how to destructure into a function
```
const person1 = {
    name:"Frank",
    age: 32,
    address: {
        city: "Los Angeles",
        state: "Ca"
    }
}

const {name, address:{ city }} = person1

function printUser{}
```
<br><br>

---
## Arrow Functions
[Web Dev Simplified YT](https://www.youtube.com/watch?v=h33Srr5J9nY) Arrow function tutorial
<br><br>

---
## Conditionals vs Switch vs Ternary
[Conditionals w3](https://www.w3schools.com/js/js_if_else.asp). If, Else statements
```
if (time < 10){
    greeting="Good morning"
} else if (time < 20){
    greeting = "Good day"
} else {
    greeting = "Good evening"
}
```

[Switch w3](https://www.w3schools.com/js/js_switch.asp). 

The getDay operator returns a number for the Day. The Switch conditional gives a name to the number.
```
switch (new Date().getDay()){
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
}
```

[Ternary Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)
```
var age = 26
var beverage = (age >= 21) ? "Beer":"Juice"
```
<br><br>

---
## Function
Function Expression, need to be declared before call
```
const getRectArea = function(width, height){
    return width * height;
}

```
Function Declaration, can be called at any point
```
function getRectArea(width, height){
    return width * height
}
```
<br><br>

---
## Promises
[Web Dev Simplified YT](https://www.youtube.com/watch?v=DHvZLI7Db8E)


[CodePumpkin](https://codepumpkin.com/callbacks-promises-javascript/) Callbacks vs promises