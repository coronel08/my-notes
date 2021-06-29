# React Notes
Notes on learning React. 


[15 React Libraries](https://dev.to/coursesity/react-libraries-to-use-in-2021-15-top-picks-37d7) to use 
Docker a react app[mherman blog](https://mherman.org/blog/dockerizing-a-react-app/)
[React Best Practices](https://betterprogramming.pub/21-best-practices-for-a-clean-react-project-df788a682fb)
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
            * [useFetch](#usefetch)
    * [API](#api)
    * [Switch vs Router](#switch-vs-router)
    * [Hashrouter vs Browserrouter](#hashrouter-vs-browserrouter)
    * [Navlink vs Link](#navlink-vs-link)
    * [Styling](#styling)
        * [Inline Styling React](#inline-styling-react)
    * [Redux](#redux)
    * [Tutorials](#tutorials)
        * [Navbar](#navbar)
        * [Flashcard](#flashcard)
        * [Reactstrap](#reactstrap)
* [Next](#next)


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
<br>

#### UseFetch
[Medium](https://medium.com/swlh/write-a-custom-reusable-hook-usefetch-1443d8d4e1e1) useFetch to write a custom reusable hook
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
<br><br>

---
## Redux
[Medium](https://medium.com/swlh/understanding-react-redux-and-react-redux-c52d46dd1a04) Understanding react Store -> View -> Actions -> Reduce -> Store



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

---

# Next


## Basics
Make sure to edit [metadata](https://nextjs.org/learn/basics/assets-metadata-css/metadata) in head section and create a [layout](https://nextjs.org/learn/basics/assets-metadata-css/metadata)


### CSS styling
Global styles are imported into the pages/_app.js, all other styles use css modules and must end with .module.css



### Img
Next has its own [Image tag](https://nextjs.org/docs/basic-features/image-optimization) will need to [configure host](https://nextjs.org/docs/messages/next-image-unconfigured-host) when setting it up. 


### Static vs Server Rendering
[Next.js Pages](https://nextjs.org/docs/basic-features/pages) and (data fetching)[https://nextjs.org/docs/basic-features/data-fetching]
* Static Rendering - The HTML is generated at build time and will be reused on each request.
    * getStaticProps - page content depends on external data. Can Data Fetch so that we can pre render with data
    * getStaticPaths - page path depends on external data
* Server Rendering - The HTML is generated on each request. Best for data pages that need data that is rendered on each request.
    * getServerSideProps - is run on every request, fetches the data and passes it to the page

### Router
* index routes - The router will automatically route files named index to the root of the directory.
* nested routes - nested folders and files in the pages will be generated in the same way
* dynamic routes - use bracket syntax to match named parameters []
#### Link
Next has its own Link tag format
```
<Link href="/about">
    <a>About Us</a>
</Link>
```
#### useRouter
[useRouter hook](https://nextjs.org/docs/api-reference/next/router#userouter), can use router.push for buttons and for passing data into url. Also looks into router.prefetch that would for example prefetch a page after login.

