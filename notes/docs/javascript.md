# Javascript Basics
number += 1
* increment ++
* decrement --


Use **let** or **const** over **var**. Case Styling/Naming Conventions:
* camelCasing for objects
* start booleans with is ex: const isTrue = true
<br><br>


Objects / Key value pairs, can mix and match objects and arrays
```
const fitBitData{
    steps : 2131
    day : "Thursday"
    workout : ['steps', 'stairs']
    weight : {
        start : 180,
        goal : 160
    }
}
```
<br>

Array / List can mix and match objects and arrays
```
let plants = [
    ['fruits', 'apple','lemon'],
    ['vegetable','lettuce','kale']
    {
        tree: apple
        size : large
    }
]
```
<br>

## Table of Contents
* [Javascript Basics](#javascript-basics)
    * [Math](#math)
    * [Logical Operators](#logical-operators)
        * [Conditionals](#conditionals)
        * [Switch](#switch)
        * [Ternary](#ternary)
    * [String Methods](#string-methods)
        * [Template Literals](#template-literals)
        * [Strip HTML strings](#Strip-HTML-strings)
    * [Array Methods](#array-methods)
        * [Splicing](#splicing)
        * [Slice](#slice)
        * [Sorting Arrays](#sorting-arrays)
            * [Highest or Lowest Array Value](#highest-or-lowest-array-value)
    * [Array Itteration](#array-itteration)
    * [Objects Key/Value Pairs](#objects-key-value)
        * [Iterate Objects](#iterate-objects)
    * [Loops](#loops)
        * [For Loop](#for-loop)
            * [For Of Loop](#for-of-loop)
        * [While Loop](#while-loop)
        * [Recursion vs Loop](#recursion-vs-loop)
    * [Closures and Nesting Functions](#closures-and-nesting-functions)
        * [private variable](#private-variable)
    * [Destructuring](#destructuring)
    * [Arrow Functions](#arrow-functions)
    * [Function](#function)
    * [Promises](#promises)
    * [API](#api)
        * [Requests](#requests)


---
## Math
* random ( gives random number between 0 - 1)
```
<!-- Up to 100, +1 to avoid zero's -->
Math.floor(Math.random() * 100) + 1
```
* round 
* abs (removes neg)
* floor (removes decimal)
* ceil (removes decimal and rounds up)
<br><br>

---
## Logical Operators
* && (and)
* || (or)
* ! (not)

<br><br>


### Conditionals 
[Conditionals w3](https://www.w3schools.com/js/js_if_else.asp). If, else if, else statements
```
<!-- By default the && runs before || but can change that with parenthesis
if ((age > 0 && age < 5) || age <= 100 && age >= 65){}
 -->
if (typeof(age) == "number"){
    if (age > 0 && age < 5 || age <= 100 && age >= 65){
        console.log("Free!!!")
    } else if (age >= 5 && age < 13){
        console.log("$10")
    } else if ( age >= 13 && age < 65 ){
        console.log("$20")
    } else {
        console.log("Invalid?")
    }
} else {
    console.log("not a number?")
}
```
Truthy Boolean(if exist/true)
```
let arg= 10

if (arg){
    console.log(arg)
}
```

### Switch
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
    case 3:
        day = "Other";
        break;
}
```

### Ternary 
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
## String Methods
[W3schools](https://www.w3schools.com/jsref/jsref_obj_string.asp)
* concat
* repeat
* replace
* replaceAll
* slice
* split
* trim


### Template Literals
Allow embedded expressions, **Use backticks not single quotes** 
```
`I counted ${3 + 4} sheep`
```
<br>


### Strip HTML strings
strip the html from an element
```
const stripHTMLTags = str => str.replace(/<[^>]*>/g, '')
<!-- Example -->
stripHTMLTags ('<a href="#"> Me and you </a>')
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
* Push (add to end)
* Pop (remove from end)
* Shift (remove from start)
* Unshift (add to start)
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
Using Splice to add new items to an array. Changes array <br>
Splice(start,del, items)
```
fruits.splice(1,0,"item1")
```

### Slice
Slice method slices out a piece of an array into a new array. Doesn't chage array <br> 
slice(start,stop)
<br> <br>


### Sorting Arrays
[W3 Sorting Arrays page](https://www.w3schools.com/js/js_array_sort.asp)
sort(): Sorts an array alphabetically 
reverse(): reverse sort
random use [Fisher Yates Method](https://www.w3schools.com/js/js_array_sort.asp)<br><br>


#### Highest or Lowest Array Value
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
## Objects Key-Value
Objects are key-value pairs similar to Dicts in python. Different from an array.
```
const fitBitData = {
    totalSteps : 234234
    totalMiles : 324.1
    workoutsThisWeek : '5 of 7'

}
```
**Can access objects in two ways.**
* dot method, allows for variables 
* array method
```
let birthYear = 2020

let years = {
    1999 : "Good"
    2020 : "Bad" 
}

years.1999  <!-- returns good  -->
years[birthYear]  <!-- returns bad -->
```
<br>

### Iterate Objects
 Object.entries() both keys and values //  Object.keys()   //  Object.values()
<br>

#### For in
Arrays use **in** instead of **of** to Loop over an array. Can also use Object.values to iterate.
```
testScores ={
    kim:89
    shawn:91
    marlon:72
}

for (let person in testScores){
    console.log('${person} scored ${testScores[person]}')
}
```
<br><br>

---
## Loops
* for loop
* while loop
* for ... of loop
* for ... in loop 

### For Loop
Loops can be nested helpfull for nested arrays. 

Ex:for loop starts at 1,stops at 10, adds 1 each time
```
for (let i=1; i <= 10; i++ ){
    console.log(i)
}
```
Looping over an array
```
const animals = ['lions', 'tigers', 'bears']

for (let i = 0; i < animals.length; i++){
    console.log(animals[i])
}
```
<br>

#### For Of Loop
Easier way to loop and iterate arrays
```
let items = ['book','car','can']
for (let item of items){
    console.log(item)
}
```
Refractor student nested for loop
```
for (let row of seatingChart){
    for (let student of row){
        console.log(student)
    }
}
```

<br><br>

### While Loop
```
let secret = 'password'
let guess = prompt("Enter the code")

while (guess !== secret ){
    guess = prompt(guess)
    console.log("Wrong password")
    if (guess === "stop" || guess === "exit"){
        break;
    }
} 
console.log("Correct")
```
<br>

#### Recursion vs Loop
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
<br><br>

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
## Promises
[Web Dev Simplified YT](https://www.youtube.com/watch?v=DHvZLI7Db8E)


[CodePumpkin](https://codepumpkin.com/callbacks-promises-javascript/) Callbacks vs promises
<br><br>

---
## API
Using Json Server [Git](https://github.com/typicode/json-server) to create an Api tutorial using json-server to read json DB, Apollo server to work with Express, and then GraphQL  [Codeburst](https://codeburst.io/how-to-implement-a-graphql-api-on-top-of-an-existing-rest-api-db8b343ddb5a)

### Requests
5 Ways to make Http request in node/javascript
[Logrocket](https://blog.logrocket.com/5-ways-to-make-http-requests-in-node-js/)
and [Twilio](https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html)
<br>

Can test out API's by running the command below 
```
node {{filename}}
```
* HTTPS module
* Axios
* Got
* Super Agent
* node-fetch