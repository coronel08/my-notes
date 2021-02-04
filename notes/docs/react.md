# React Notes
Notes on learning React. 

Docker a react app[mherman blog](https://mherman.org/blog/dockerizing-a-react-app/)
<br><br>

---
## Table of Contents
* [React Notes](#react-notes)
    * [Class](#class)
        * [Class Lifecycle Methods](#class-lifecycle-methods)
        * [Async and Await](#async-await)
    * [Functions](#functions)
        * [hooks](#hooks)
            * [useState](#usestate)
            * [useEffect](#useeffect)
    * [API](#api)
    * [Switch vs Router](#switch-vs-router)
    * [Hashrouter vs Browserrouter](#hashrouter-vs-browserrouter)
    * [Navlink vs Link](#navlink-vs-link)
    * [Styling](#styling)
        * [Inline Styling React](#inline-styling-react)
    * [Tutorials](#tutorials)
        * [Navbar](#navbar)
        * [Flashcard](#flashcard)
        * [Reactstrap](#reactstrap)


---
## Class
An example of using classes, inheritance, and state on [medium](https://medium.com/swlh/create-a-web-page-using-react-d5ad9d03fb1f)
<br><br>

### Class Lifecycle Methods
Lifecycle methods docs [react](https://reactjs.org/docs/react-component.html#commonly-used-lifecycle-methods)

* constructor() 
    * used for initializing local state by assigning an object to this.state. 
    * used for binding an event handler method to an isntance
    ```
        constructor(props) {
        super(props);
        // Don't call this.setState() here!
        this.state = { counter: 0 };
        this.handleClick = this.handleClick.bind(this);
        }
    ```
* getDerivedStateFromProps()
    * invoked right before calling the render method, used for when state depends on changes in props over time
* render()
    * the only method required in a class component
* componentDidMount()
<br><br>

### Async Await
A synthatic sugar over Javascript Promises, helpful when fetching from an API. You can use try/catch for proper error handling [valntinog blog](https://www.valentinog.com/blog/await-react/)
<br><br>

---
## Functions
Building a clock component using classes then refractoring to functions [dev.to](https://dev.to/danielleye/react-class-component-vs-function-component-with-hooks-13dg) able to use Hooks. 
<br><br>

### Hooks
[Fireship YT](https://www.youtube.com/watch?v=TNhaISOUy6Q) Hook tutorials and building your own Hook from scratch. 
<br><br>

#### UseState
Instead of setting state with this.state in a constructor we can import useState.

[Web Dev Simplified YT](https://www.youtube.com/watch?v=O6P86uwfdR0)
<br><br>

#### UseEffect
We can pass in a function in useEffect to update on change. Also allows to pass in an array as the second argument.


[Web Dev Simplified YT](https://www.youtube.com/watch?v=0ZJgIjIuY7U&t=309s)


useEffect replacing componentDidMount [stackoverflow](https://stackoverflow.com/questions/53945763/componentdidmount-equivalent-on-a-react-function-hooks-component)


[Webdev blog](https://thewebdev.info/2020/05/05/react-hooks-equivalent-of-componentdidmount/) on using useEffect
<br><br>

---
## API
Can test api with api placeholders [jsonplaceholder](https://jsonplaceholder.typicode.com/users)


---
## Switch vs Router
[Router vs Switch explained](https://medium.com/@jenniferdobak/react-router-vs-switch-components-2af3a9fc72e)
[Router and Switch example](https://reactrouter.com/web/api/Switch)
A switch is helpfull with **nested routes**, will only render the first matched.<br><br>


## Hashrouter vs Browserrouter
**Hash Router**: for small applications that dont need backend. Has # in url 
**Browser Router**: recommended when we have backend or static web page host <br><br>


## Navlink vs Link
Example of React Navlink and Route. Navlink is used to specify which element is active in a Navigation Bar with CSS
```
<li><NavLink to="/about">About</NavLink></li>
<Route path="/about" component={About}/>

<!-- CSS -->
.active {
  background-color: #0099FF;
}
```
<br><br>

---
## Styling


### Inline Styling React
Styled components are inline and can be used to define styles and reusable components. [Styled-Components Site](https://styled-components.com/docs/basics) Getting Started styling components


[Styled-Components Site](https://styled-components.com/docs/faqs#can-i-nest-rules) Faqs show to Nest Rules, CSS Frameworks, Override Styles, Attrs
<br>

---
## Tutorials
An extensive tutorial on building a react Todo List from scratch. [vegibit site](https://vegibit.com/create-a-react-element-from-scratch/)


[Brian Design YT](https://www.youtube.com/watch?v=3nLTB_E6XAM) building a React site 2hr tutorial. Have not gone through it

[Dev.to](https://dev.to/rafavls/creating-a-weather-app-with-reactjs-part-2-5gi3) Creating a weather app with React, Openweather API, Google Geocode API

### Navbar
[Fireship YT](https://www.youtube.com/watch?v=IF6k0uZuypA) Recreating Facebook Navbar using React, CSS, and HTML

[Brian Design YT](https://www.youtube.com/watch?v=CXa0f4-dWi4) creating a slide out navbar.
<br><br>

### Flashcard
[Web Dev Simplified YT](https://www.youtube.com/watch?v=hEtZ040fsD8&t=2096s) building a flashcard app, using an API for data.
<br><br>

### Reactstrap
A bootstrap for React
<br><br>