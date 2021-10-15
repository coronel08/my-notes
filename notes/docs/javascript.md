# Javascript Basics
Same as Javascript Dom Manipulation and Selectors Section
Replace Jquery with Javascript[tobiashlin](https://tobiasahlin.com/blog/move-from-jquery-to-vanilla-javascript/)<br>
[sitepoint](https://www.sitepoint.com/jquery-vs-raw-javascript-1-dom-forms/)

number += 1
* increment ++
* decrement --


Use **let** or **const** over **var**. Case Styling/Naming Conventions:
* let x=1, y=2
* camelCasing for objects and functions
* start booleans with is ex: const isTrue = true
* control flow [Exploringjs](https://exploringjs.com/impatient-js/ch_control-flow.html)
    * if, switch, while, do-while, for, for-of, for-await-of-loop, for-in
    * break, continue, else, return
<br><br>


Objects / Key value pairs, can mix and match objects and arrays {}
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
            * [Nullish Operator](#nullish-operator)
    * [Function](#function)
        * [Closures and Nesting Functions](#closures-and-nesting-functions)
            * [Private Variable](#private-variable)
        * [High Order Functions](#high-order-functions)
            * [Accept Functions as Arguments](#accept-functions-as-arguments)
            * [Return a Function](#return-a-function)
        * [Function Expression](#function-expression)
        * [Function Declaration](#function-delcaration)
        * [Function Methods](#function-methods)
            * [This](#this)
        * [Arrow Functions](#arrow-functions)
    * [String Methods](#string-methods)
        * [Template Literals](#template-literals)
        * [Strip HTML strings](#Strip-HTML-strings)
    * [Array Methods](#array-methods)
        * [Splicing](#splicing)
        * [Slice](#slice)
        * [Sorting Arrays](#sorting-arrays)
            * [Highest or Lowest Array Value](#highest-or-lowest-array-value)
        * [Array Itteration](#array-itteration-methods)
            * [forEach](#forEach)
    * [Objects Key/Value Pairs](#objects-key-value)
        * [Iterate Objects](#iterate-objects)
    * [Loops](#loops)
        * [For Loop](#for-loop)
            * [For Of Loop](#for-of-loop)
        * [While Loop](#while-loop)
        * [Recursion vs Loop](#recursion-vs-loop)
    * [Rest and Spread](#rest-spread)
    * [Destructuring](#destructuring)
* [DOM Selectors](#dom-selectors)
    * [Manipulate](#manipulate)
    * [Event Listener](#eventlistener)
    * [Form Event Listener](#form-event-listener)
* [Promises](#promises)
    * [Async](#async)
    * [API](#api)
        * [Axios](#axios)
        * [Requests](#requests)
* [OOP](#oop)
* [Export](#export)

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
if (typeof(age) !== "number"){
    console.log("not a number?")
} else {
    if (age > 0 && age < 5 || age <= 100 && age >= 65){
        console.log("Free!!!")
    } else if (age >= 5 && age < 13){
        console.log("$10")
    } else if ( age >= 13 && age < 65 ){
        console.log("$20")
    } else {
        console.log("Invalid?")
    }
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

#### Nullish Operator
[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator) Nullish Coalescing Operator and Optional Chaining

Set Default value 
```
function calculatePrice(price, tax){
    price = price
    taxes = taxes ?? .25
    console.log(price, tax)
}

calculatePrice(10)
```

Optional Changing
```
let test = {prop : "Hello"}

console.log(test?.prop)
console.log(test?.thing)
```
<br><br>

---
## Function
### Closures and Nesting Functions
[Closures Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
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
    let privateCounter=0
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
<br>


#### Private Variable 
```
function secretVariable(){
    let private = "secret variable"
    return function(){
        return private
    }
}
var getPrivateVariable = secretVariable()
console.log(getPrivateVariable())
```
<br><br>


### High Order Functions
Operate with other functions, they accept other functions as arguments or return a function
<br>


#### Accept functions as arguments
```
function rollTwice(func){
    func()
    func()
}

function diceRoll(){
    roll = Math.floor( Math.random() * 6) + 1
    console.log(roll)
}

callTwice(diceRoll)
```
<br>


#### Return a function
```
function makeBetweenFunc(min, max){
    return function(num){
        return num >= min && num <= max;
    }
}

let isChild = makeBetweenFunc(0,18)
let isAdult = makeBetweenFunc(18,65)
let isSenior = makeBetweenFunc(66,110)

console.log(isChild(10))
```
<br><br>


### Function Expression
Function Expression, need to be declared before call
```
const getRectArea = function(width, height){
    return width * height;
}

```
<br><br>


### Function Declaration
Function Declaration, can be called at any point
```
function getRectArea(width, height){
    return width * height
}
```
<br><br>


### Function Methods
Can add functions as properties on objects
```
const myFunc = {
    multiply : function(x,y){return x * y},
    divide : function(x,y){return x / y},
<!-- Shorthand for adding methods -->
    root(x){ return x*x}
}
```
<br>


#### This
Use the keyword this to access other properties on the same object. 

If inheritting this, it could refer to the window. **This keyword acts different in arrow functions**
<br><br>

### Arrow Functions
[Web Dev Simplified YT](https://www.youtube.com/watch?v=h33Srr5J9nY) Arrow function tutorial
```
<!-- One Liner -->
    const isEven = num => num % 2 === 0
<!-- Implicit Return (only works on returning 1 thing) -->
    const isEven = num => (
        num % 2 === 0
    )
<!-- Standard -->
    const isEven = (num) => {
        return num % 2 === 0 
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

#### Formatting String Output
[Like Python string formatting, can do Inline styling](https://riptutorial.com/javascript/example/14972/formatting-console-output)
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
Using spread parameter
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


### Array Itteration Methods
[Youtube vid](https://www.youtube.com/watch?v=R8rmfD9Y5-c) on filter, map, find, foreach <br>
[W3 Array itteration](https://www.w3schools.com/js/js_array_iteration.asp) <br>
[High Order fucntions / array iteration exampels](https://vegibit.com/higher-order-functions-in-javascript/) <br>
[reduce map and filter functions](https://codeburst.io/learn-understand-javascripts-reduce-function-b2b0406efbdc)


* map(): creates a new array for function mapped  
* filter(): creates a new array with items that pass filter
* forEach(): replaced with for of loop but can be usefull 
* reduce(): adds all values
* every(): checks if every item passes test/function
* some(): check if some items pass test/function
* indexOf(): returns index of item looking for
* lastIndexOf(): returns last occurence of item 
* find(): returns value of item that passes test/fucntion
* findIndex(): 


Reduce Example
```
// Reduce function example 
const numbers = [2,3,4,5]
const addNumbers = (prevResult, currentItem) => {
    console.log(prevResult, currentItem)
    return prevResult + currentItem
}
const initValue = 12
const total = numbers.reduce(addNumbers, initValue)
```

Exmaple showing filter and map used in one line
```
const movies = [
    {
        title: "Sharknado",
        score: 35,
        year: 2013
    },
    {
        title: "Amadeus",
        score: 90,
        year: 1984
    }
]
let goodMovies = movies.filter(m => m.score > 80).map(m => m.title)
```
<br><br>

#### forEach
```
const nums = [9,8,7,6,5,4,3,2,1]

nums.forEach(function (el){
    if (el % 2 === 0){
        console.log(el)
    }
})
```

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
<br>

### Try and Catch
Need both try and catch
[Try/Catch and Throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#exception_handling_statements)
```
try{
    hello.toUpperCase()
} catch (e){
    console.log("ERorr ! 1 !")
}
```
<br><br>
---

## Rest Spread
Using ES6, use [rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters), spread examples can be seen in destructuring example. 

Rest parameter can be used for passing an array into an object and apply array functions 
```
function sum(...nums){
    return nums.reduce((prev,current) => prev + current)
}

console.log(sum(12,34,2))
```
<br><br>

---
## Destructuring
[Web Dev Simplified YT](https://www.youtube.com/watch?v=NIq3qLaHCIs) **Array** and **Object** destructuring tutorial

### Array Destructuring
Example below skips b and then defines the rest using rest/spread operator. Based on position
```
const alphabet = ['a','b','c','d','e','f']
const [a,,c,...rest] = alphabet
console.log(a,c,rest)
``` 
A function that returns an array that gets deconstructed
```
function testFunction(num1,num2){
    return [a+b, a*b]
}
const [sum, multiply, division='No'] = testFunction(3,4)
```

### Object Destructuring
instead of being based on position it is based on the name of the key. Need to research on how to destructure into a function
```
const person1 = {
    name:"Frank",
    age: 32,
    address: {
        city: "Los Angeles",
        state: "Ca"
    }
}
<!-- name is renamed to name1 so we can reference it as name1 instead  of name -->
const {name: name1, address:{ city }, zip='1234'} = person1

function printUser{}
```

### Param Destructuring
put the object key in the functions parameters{}
```
const runner = {
    first:"Tom",
    age: 36,
    last:"Henderson",
}

function fullName({first,last}){
    return `${first} ${last}`
}

<!-- longhand version
function fullName(runner){
    const first, last = runner
    return `${first} ${last}`
}
 -->

fullName(runner)
```
<br><br>

---
# DOM Selectors
Can select using getElement or querySelector [W3 Query](https://www.w3schools.com/jsref/met_document_queryselector.asp)
* document.getElementById || document.querySelector('#')
* document.getElementsByTagName || document.querySelector('a[title='Test']') attribute selector to select inside a tag
* document.getElementsByClassName || document.querySelector('.')
* document.querySelectorAll() 
<br><br>

## Manipulate
Important ones [W3](https://www.w3schools.com/jsref/dom_obj_all.asp) list of objects, [MDN](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode) list of methods like append, children. Look at Colt Steeles ch24: World of Dom to review. Practiced Dom manipulation in Javascript/Pokemon-Dom
* classlist - 
    * classlist.add("newClass") to add class to an element
    * classlist.remove()
    * classlist.contains()
    * classlist.toggle()
* getAttribute 
* setAttribute - can also change attributes using document.querySelector('input').type = "text"
* appendChild - [W3](https://www.w3schools.com/jsref/met_node_appendchild.asp)
* append - [W3](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/append)
* prepend
* removeChild
* remove
* createElement - create div/li/p etc [w3](https://www.w3schools.com/jsref/met_document_createelement.asp)
* innerText - senitive to display hidden or none change text
* textContent - return everything text
* innerHTML - can retreive html and update html, html changes wont change on innerText
* value
* parentElement - 
* children - can also do childrenCount 
* nextSibling - 
* nextElementSibling - avoids whitespace
* previousSibling -
* previousElementSibling - avoids whitespace 
* style - doesnt contain styles from stylesheet, only inline. 
    * window.getComputedStyle(h1).fontSize - get current style of an element
    ```
    <h1>
        <span>R</span>
        <span>A</span>
        <span>I</span>
        <span>N</span>
        <span>B</span>
        <span>O</span>
        <span>W</span>
    </h1>

    const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    let rainbow = document.querySelector('span')
    for(let i in rainbow){
        rainbow[i].style.color = colors[i];
    }
    ```
<br>

## eventListener
Example can be seen in /javascript/rand-bg-color.html. Event Listeneres can be 
* click
* submit
* change - only works when you click out the input box
* input - works everytime the input box changes

```
hello = document.querySelector('#hello')

hello.addEventListener('click', () =>{
    console.log('hello')
})
```
<br>

### Form Event Listener
Check file Javascript/input-events.html to see a formw ith javascript and event listener.


Can also do nested events / event Bubbling. To stop nest or bubbling use e.stopPropagation()
<br><br>

---
# Promises
Check /Javascript/Promises folder to see examples on Promises, Async, and Axios.
<br><br>

[Web Dev Simplified YT](https://www.youtube.com/watch?v=DHvZLI7Db8E)
<br>
[CodePumpkin](https://codepumpkin.com/callbacks-promises-javascript/) Callbacks vs promises
<br><br>


## Async
Async is just a promise, using **async** and **await**. Always returns a promise
<br>
Await can only be used with functions that use Async. Await will pause the execution of the function, waiting for a promise to be resolved.
<br>

Can do error checking with **try** or **then** and **catch** in an async and await function.
<br><br>

## API
[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) HTTP API Methods like **GET, POST, DELETE, PATCH**

Use Javascript fetch to get API, old way was XMLHttpRequest
```
<!-- using then and catch -->
fetch('https://api.cryptonator.com/api/ticker/btc-usd')
    .then(res => {
        console.log("Response, waiting to parse...", res)
        return res.json()
    })
    .then(data => {
        console.log(data.ticker.price)
    })
    .catch(e => {
        console.log("Error", e)
    })

<!-- Refractored using async and await -->
const fetchBitcoinPrice = async() => {
    try{
        const res = await fetch('https://api.cryptonator.com/api/ticker/btc-usd')
        const data = await res.json()
        console.log(data.ticker.price)
    } catch (e) {
        console.log("Something is wrong", e)
    }
}
```
Using Json Server [Git](https://github.com/typicode/json-server) to create an Api tutorial using json-server to read json DB, Apollo server to work with Express, and then GraphQL  [Codeburst](https://codeburst.io/how-to-implement-a-graphql-api-on-top-of-an-existing-rest-api-db8b343ddb5a)
<br>

### Axios
A library fo making HTTP request

Import into html or **npm install axios**
```
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```
```
axios.get('https://api.cryptonator.com/api/ticker/btc-usd')
    .then(res => {
        console.log(res.data.ticker.price)
    })
    .catch(err => {
        console.log("Error !!",err)
    })

const fetchBitcoinPrice = async() => {
    try {
        const res = await axios.get('https://api.cryptonator.com/api/ticker/btc-usd')
        console.log(res.data.ticker.price)
    } catch (e) {
        console.log("Error !!",err)
    }
}
```
<br>

### Requests
5 Ways to make Http request in node/javascript
[Logrocket](https://blog.logrocket.com/5-ways-to-make-http-requests-in-node-js/)
and [Twilio](https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html)

[Fetching Data in React Dev.to](https://dev.to/jideabdqudus/fetching-data-in-react-quick-guide-4fba)

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
<br><br>

---
# OOP
[MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS) OOP Tutorial
[dev.to](https://dev.to/yumatsushima07/javascript-7-oop-fundamentals-you-will-need-4hk8) 7 OOP concepts


Object Prototypes -- Old and wrong way to add to a class
<br><br>
Factory Functions -- returns a new object without new, better to use **new** keyword and constructor function
```
function person(firstName, LastName, age){
    const person = {}
    person.firstName = firstName
    person.lastName = lastName
    person.age = age
}
```

## New and Constructor Functions
[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new) New Operator and Constructor Functions
```
<!-- This is the constructor function -->
function Car(make, model, year){
    this.make = make
    this.model = model
    this.year = year
}

<!-- Create in instance of the object with new -->
const car1 = new Car('Honda', 'Talon', 1993)
<!-- Add a property to an object instance -->
car1.color = 'black'
```
### Classes
Use a class and constructor instead of constructor functions. Can inherit from other classes using **extends** and **super** inside of the constructor to inherit objects.  
<br><br>

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) Classes 
```
class Color{
    constructor(r,g,b,name){
        this.r = r
        this.g = g
        this.b = b 
        this.name = name
    }

    <!-- Method of the object -->
    greet(){
        <!-- Destructuring the variables -->
        let {r,g,b, name} = this
        return `Hello from ${name}, ${r}, ${g}, ${b}}`
    }
}

const c1 = new Color(255,67,89, 'black')
```

# Export
Create an object and then export it 
```
const PI = 3.14
const square = x => x* x

const math = {
    pi: pi
    square: square
}

module.exports = math

//could also add directly by adding module.exports to every variable that is going to be exported
```
