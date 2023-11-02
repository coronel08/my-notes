# Swift

Swift is a type safe language that uses the following types similar to typescript

-   String
-   Int
-   Float
-   Double
-   Bool
-   Any

## Table of Contents

-   [Swift](#swift)
    -   [Basics](#basics)
    -   [Strings](#strings)
    -   [Data Types](#data-types)
    -   [Conditionals](#conditionals)

## Basics

-   define a constant with `let name:String = 'Test' `
-   define a variable with `var score:Int = 0`
-   optional chaning `?`
    -   optional value `var optionalString: String? = "Hello"` `let nickname: String? = nil`
-   nullish coalescing `highScore ?? 0`
-   do catch for error handling

## Strings

-   string interpolation
-   Use three double quotation marks (""") for strings that take up multiple lines

```
    print("\(newScore)! A new high score for \(name)! 🎉")
```

-   STRING FUNCTIONS
    -   count
    -   isEmpty
    -   capitalized
    -   uppercased
    -   lowercase
    -   hasPrefix
    -   hasSuffix

## Data Types

-   tuple - We cannot add or remove elements from a tuple in Swift but can use a nested dictionary to edit values of a tuple `var product = ("MacBook", 1099.99)`

    -   named tuple - `var company = (product: "Programiz App", version: 2.1)`

-   list - []

    -   type notations - `let emptyArray: [String] = []`
    -   append - add to list
    -   combine two lists
        ```
        var primeNumbers = [2, 3, 5]
        var evenNumbers = [4, 6, 8]
        // join two arrays
        primeNumbers.append(contentsOf: evenNumbers)
        ```
    -   insert - add to a certain point of a list `emptyArray.insert('test',1)`
    -   remove - `languages.remove(at: 1)`
    -   LIST METHODS
        -   count
        -   isEmpty
        -   removeFirst()
        -   removeLast()
        -   removeAll()
        -   sort()
        -   shuffle()
        -   forEach()
        -   contains()
        -   swapAt()
        -   reverse()
    -   access one item of a lists

    ```
    var fruits = ["strawberries", "limes", "tangerines"]
    fruits[1] = "grapes"
    ```

    -   loop thru an array

    ```
    for fruit in fruits {
    print(fruit)
    }
    ```

-   dictionary - empty dictionary [:]
    -   type notations - `let emptyDictionary: [String: Float] = [:]`
    -   countof items in dictionary `emptyDictionary.count`
    -   append to a dictionary - `emptyDictionary["item"] = "Added Item"`
    -   return all keys `var countryName  = Array(emptyDictionary.keys)`
    -   return all values `Array(emptyDictionary.values)`
    -   remove value `emptyDictionary.removeValue(forKey: 112)`
    -   OTHER DICTIONARY METHODS
        -   sorted() -
        -   shuffled() -
        -   contains() -
        -   randomElement()-
        -   firstIndex()

```
var occupations = [
    "Malcolm": "Captain",
    "Kaylee": "Mechanic",
 ]
occupations["Jayne"] = "Public Relations"
```

-   Iterate thru a dictionary

```
for (key,value) in emptyDictionary {
  print("\(key): \(value)")
}
```

## Conditionals

-   IF and ELSE statement

```

let scoreDecoration = if teamScore > 10 {
"🎉"
} else {
""
}

```

-   Switch Case

```

let vegetable = "red pepper"
switch vegetable {
case "celery":
print("Add some raisins and make ants on a log.")
case "cucumber", "watercress":
print("That would make a good tea sandwich.")
case let x where x.hasSuffix("pepper"):
print("Is it a spicy \(x)?")
default:
print("Everything tastes good in soup.")
}

```

## Loops

-   for Loop

```
let individualScores = [75, 43, 103, 87, 12]
for score in individualScores {
print(score)
}
```

-   while loop

```
var n = 2
while n < 100 {
    n *= 2
}
print(n)
```

## Functions

```
func greet(person: String, day: String) -> String {
    return "Hello \(person), today is \(day)."
}

greet(person: "Bob", day: "Tuesday")
```

A function can return a tuple for example

Async functions similar to javascript

```
func fetchUsername(from server: String) async -> String {
    let userID = await fetchUserID(from: server)
    if userID == 501 {
        return "John Appleseed"
    }
    return "Guest"
}
```

## Classes

```
class Shape {
    init(name: String) {
       self.name = name
    }

}
var shape = Shape(name:'test')

```

Use struct to create a structure. Structures support many of the same behaviors as classes, including methods and initializers. One of the most important differences between structures and classes is that structures are always copied when they’re passed around in your code, but classes are passed by reference.

```
struct Card {
    var rank: Rank
    var suit: Suit
    func simpleDescription() -> String {
        return "The \(rank.simpleDescription()) of \(suit.simpleDescription())"
    }
}
let threeOfSpades = Card(rank: .three, suit: .spades)
let threeOfSpadesDescription = threeOfSpades.simpleDescription()
```
