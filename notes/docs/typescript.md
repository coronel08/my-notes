# Typescript

-   Types - used by compiler to analyze our code for errors.
    -   Primitive Types:
        -   any - avoids checking values
        -   string -
        -   number -
        -   boolean -
        -   Date -
        -   void - used to not return anything, null or undefined
        -   undefined -
        -   null
        -   symbol -
    -   Object Types:
        -   functions -
        -   arrays - represent a collection of records with some sort order
        -   tupples - Typescript Data Structure, array like structure represents one record, fixed length with specified types.
        -   enum - adds values to a list
        -   classes -
        -   objects -
-   Type Annotations - We tell Typescript what type of value a variable will refer to
-   Type Inference - Typescript tries to figure out what type of value a variable refers to
-   Type Assertion - use angle brackets or `as` to change a type.

## Table of Contents

-   [Basics](#basics)
-   [Syntax](#syntax)
    -   [Destructure](#destructure)

## Basics

-   Type Alias - types can be used with primitives and unions

```
type Style = string;
let font: Style;
```

-   Interfaces - Creates a new type describing the property names and value types of an object. Can't be used with primitives and unions, best used with Objects

```
interface Vehicle {
    name: string;
    year:number;
    broken: boolean;
    [key: string]: any      //add any additional property
}

const oldCivic = {
    name: 'civic',
    year: 1998,
    broken: true
}

const printVehicle = (vehicle: Vehicle): void => {
    console.log(vehicle.year)
}

printVehicle(oldCivic)
```

## Commands

-   tsc --init - creates tscondig.json file
    -   tsconfig.json
        -   has options like `target` JS version, or `outDir` and `rootDir`
        -   `"watch":true` - watches and compiles file on changes
        -   `"lib": ["dom","es2017"]` - allows to use native dom classes
-   tsc {{file}} - compiles file
-   npx create-react-app . --template typescript

## Syntax

-   Optional - make a type definition optional, add question mark

    ```
    interface NumbersInterface {
        id:number,
        name:string,
        age?:number
    }

    const numbers:NumbersInterface = {
        id:1,
        name:"John Doe"
    }
    ```

-   Type Annotations: Use when we declare a variable on one line then initialize it later, need a variable with a type that can't be inferred, and When a function returns the "any" type and we need to clarify the value.

    -   string `let apples: number =5`
    -   array `let colors: string[] = ["red", "green", "blue"]` or `let myNumbers: number[] = [1,2,3]`
        -   mixed array `const importantDates: (Date | string)[] = [new Date()]`
    -   tupples `const pepsi: [string, boolean, number] = ["brown", true, 40]`
        -   tupple array - `let employee: [number, string][]` and `employee = [[1,"Brad"], [2, "John"],]`
    -   Classes - A blueprint to create an object with some fields(values) and methods(functions)

    ```
    class Person{
        id:number
        name:string

        constructor(id:number, name:string){
            this.id = id
            this.name = name
        }

        callName(): void {
            console.log(`Hello from ${this.name}`)
        }
    }

    let john = new Person(1,"John Doe")
    ```

    -   object literal `let point: {x: number; y:number} = {x:10, y:20}` or do the following `type Point = {x:number, y:number}` and `let point:Point = {x:10, y:20}`
    -   function
        -   arrow function `const logNumber:(i:number) => void = (i:number) => {console.log(i)}` or `const add = (a:number, b:number): number => {return a + b}`
        -   function `function divide(a:number, b:number): number{ return a/b}`
        -   anonymous function `const multiply = function(a:number, b:number): number { return a + b}`
            -   No Type Inference on arguments in a function
    -   Union/OR `let numberAboveZero: boolean | number = false`;

-   Type Inference - Use all the other times, guesses the type

### Destructure

```
const todaysWeather = {
    date = new Date(),
    weather = "sunny"
}

<!-- In TypeScript -->
const logWeather = ({date, weather } : {date: Date; weather: string;}) : void => {
    console.log(date, weather)
}

<!-- In JS6 Syntax -->
const logWeather = ({date, weather}) => console.log(date, weather)
```

<br>
Another Example of destructuring

```
const profile = {
    name: "alex",
    age: 20,
    coords: {
        lat:0,
        lng:15,
    },

    setAge(age:number): void{
        this.age = age
    }

}

const {age, name}: {age:number; name:string} = profile
const {
coords: {lat, lng},
}: {coords:{lat:number; lng:number}} = profile
```
