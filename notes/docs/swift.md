# Swift

Swift has 2 types of memory `Stack` and `Heap`. Only objects in the Heap are counted towards ARC. Device shares heap

Objects in the Stack: String, Bool, Int, most basic types. Struct, Enum
Objects in the Heap: Functions, Class, Actors. Objects in the heap are Reference Types, when we edit them the object is changed in place.

Swift is a type safe language that uses the following types similar to typescript

-   String
-   Int
-   Float
-   Double
-   Bool
-   Any
-   Generics can be done like this `let fruits3 = Array<String> = ["Apple", "Orange"]`

## Table of Contents

-   [Swift](#swift)
    -   [Basics](#basics)
    -   [Strings](#strings)
    -   [Data Types](#data-types)
        -   [Tuple](#tuple)
        -   [List](#list)
        -   [Dictionary](#dictionary)
        -   [Sets](#sets)
            -   [Combining Data Types](#combining-data-types)
    -   [Conditionals](#conditionals)
        -   [If Let](#if-let)
        -   [Switch Case](#switch-case)
        -   [Guard](#guard)
    -   [Loops](#loops)
        -   [Higher order Functions](#higher-order-functions)
    -   [Functions](#functions)
    -   [OOP](#OOP)
        -   [Classes](#classes)
        -   [Enum](#enum)
        -   [Struct](#struct)
    -   [Async](#async)

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

---

## Data Types

### Tuple

-   tuple - We cannot add or remove elements from a tuple in Swift but can use a nested dictionary to edit values of a tuple `var product = ("MacBook", 1099.99)`

    -   named tuple - `var company = (product: "Programiz App", version: 2.1)`

### List

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

    -   look into an item if it exists

    ```
    if fruitsArray.indices.contains(4){
        let item = fruitsArray[4]
    }
    ```

    -   reference an item in the list or loop in a map

    ```
    newList = list.map{$0.name}
    ```

### Dictionary

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

-   Dictionary with typings

```
struct PostModel {
    let id:String
    let title: String
    let likeCount: Int
}

// written as an array
var postArray: [PostModel] = [
    PostModel(id:"abc123", title:"Post 1", likeCount: 5),
    PostModel(id:"abc1234", title:"Post 2", likeCount: 15)
]

written as a dict
var postDict: [String: PostModel] = [
    "abc123" : PostModel(id:"abc123", title:"Post 1", likeCount: 5),
    "abc1234" :  PostModel(id:"abc1234", title:"Post 2", likeCount: 15)

]
```

### Sets

Unique values only in a set

```
var fruitsSet: Set<String> = ["Apple", "Orange", "Apple"]
```

#### Combining data types

```
struct ProductModel {
    let title: String
    let price: int
}

var myProduct: [ProductModel] = [
    ProductModel(title: "Product 1", price: 50),
    ProductModel(title: "Product 2", price: 150),
    ]

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

### If-Let

if there is a value, let newvalue equal that value

```
if let newValue = userIsPremium {
    // Here we have access to the non optional equal value.
} else {
  return false
}

// easier way to write and read this.
if let newValue = userIsPremium {
    return newValue
}
return false
```

can also do if let chaining

```
checkIfUserIsSetup(){
    if let isNew= userIsNew, letDidCompleteOnboarding = userDidCompleteOnboarding{
        return true
    },

    //can shorthand
    if let userIsNew, userDidCompleteOnboarding

    // same but with guard
    guard let userIsNew, userDidCompleteOnboarding else {
        return false
    }

}
```

### Switch Case

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

### Guard

Guard makes sure there is a value

```
guard let newValue = userIsPremium else {
    return false // failure is entering this closure
}
// here we have access to the non optional value
return newValue


can also write it as this below where we reusethe variable name
guard let userIsPremium else {
    return false
}
return userIsPremium
```

## Loops

Loops can be broken or ended using `break` or `continue` to skip

-   for Loop

```
let individualScores = [75, 43, 103, 87, 12]
for score in individualScores {
print(score)
}
```

-   for loop of range

```
for item in 0 .. <100{
    print (item)
}
```

-   for loop enumerated

```
for (index, lesson) in itemList.enumerated(){
    print("index: \(index) || lesson: \(lesson)")
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

### Higher Order Functions

-   filter

```
struct DatabaseUser {
    let name: String
    let isPremium: Bool
    let order: Int
}

var allUsers: [DatabaseUser] = [
    DatabaseUser(name: "Nick", isPremium: true, order:4)
    DatabaseUser(name: "Emily", isPremium: false, order:3)
]

allPremiumUsers: [DatabaseUser] = allUsers.filter{ user in
    if user.isPremium {
        return true
    }

    return false
}

// shorthand for above code
allPremiumUsers: [DatabaseUser] = allUsers.filter{ user in
    return user.isPremium
}

// shorthand for above code, using $0
allPremiumUsers: [DatabaseUser] = allUsers.filter({$0.isPremium})
```

-   map: map thru an array and return a new array

```
    var usernames: [String] = allUsers.map{user in
        return user.name
    }

    // shorthand way of doing it
    var usernames: [String] = allUsers.map({$0.name})

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

## OOP

### Classes

Class vs Struct: class is in heap, struct is in stack. Example is A classroom is a class and giving out 30 quizzes is a struct.

```
class Shape {
    let isPaid: Bool ?
    let dateCreated: Date

    init(name: String, dateCreated: Date = .now, isPaid: Bool?) {
       self.name = name
       self.dateCreated = dateCreated ?? .now
       self.isPaid = isPaid
    }

}
var shape = Shape(name:'test')

```

### Struct

Use struct to create a structure. Structures support many of the same behaviors as classes, including methods and initializers. One of the most important differences between structures and classes is that structures are always copied when they’re passed around in your code, but classes are passed by reference.

-   Structs have an implicit init, but can be added to change behavoir like a default value or adding values to self.

```
struct Card {
    var rank: Rank
    var suit: Suit
    private(set) var hasWon : Bool

    func simpleDescription() -> String {
        return "The \(rank.simpleDescription()) of \(suit.simpleDescription())"
    }

    // Lets swift know that we are mutating inside of stack so it is okay with mutating in place.
    mutating func markUserAsWon(){
        isPremium = true
    }

    mutating func updateHasWon(newValue:Bool){
        hasWon = newValue
    }

}
let threeOfSpades = Card(rank: .three, suit: .spades)
let threeOfSpadesDescription = threeOfSpades.simpleDescription()
threeOfSpades.markUserAsWon()
threeOfSpades.updateHasWon(newValue: true)
```

### Enum

similar to structs except we have all known use cases at runtime

```
struct CarModel {
    let brand: CardBrandOption
    let model: String
}

enum CardBrandOption{
    case ford
    case toyota
    case honda

    // Switch case version
    var title:String {
        switch self {
            case .ford:
                return "Ford"
            case .toyota:
                return "Toyota"
        }
    }

    // if else version
    var title: String {
        if self == .ford {
            return "Ford"
        } else if self === .toyota {
            return "Toyota"
        } else {
            return "Default value"
        }
    }
}
```

## Async

```
func getData(){
    downloadData { (returnedData) in
        text = returnedData
    }

    downloadData4 {[weak self] (returnedResult) in
        self?.text = returnedResult.data
    }
}

func downloadData(completionHandler: @escaping (_ data: String) -> Void){
    DispatchQueue.main.asyncAfter(deadline: .now() + 2.0){
        completionHandler "New Data!"
    }
}

// cleaned format below
struct DownloadResult{
    let data:String
}

func downloadData2(completionHandler: @escaping (DownloadResult) -> Void){
    DispatchQueue.main.asyncAfter(deadline: .now() + 2.0){
        let result = DownloadResult(data: "NewData!")
        completionHandler(result)
    }
}

```
