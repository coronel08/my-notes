# React Notes
Notes on learning React.

Docker a react app[mherman blog](https://mherman.org/blog/dockerizing-a-react-app/)
<br><br>

---
## Table of Contents
* [React Notes](#react-notes)
    * [Using Class and State](#class-state)
    * [Switch vs Router](#switch-vs-router)
    * [Hashrouter vs Browserrouter](#hashrouter-vs-browserrouter)
    * [Navlink vs Link](#navlink-vs-link)
    * [Inline Styling React](Inline-Styling-React)
* [React and Django](#react-and-django)


## Class State
An example of using classes, inheritance, and state on [medium](https://medium.com/swlh/create-a-web-page-using-react-d5ad9d03fb1f)



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

## Inline Styling React
Styled components using inline example.
```
import styled from "styled-component"
const StyledMenu = styled.div`
    .menu {
        list-style:none;
        background-color: white;
    }
    .menu.active {
        background-color:black;
    }
`
```

---
## React and Django
React as frontend and Django as Backend [Blog Tutorial](https://wsvincent.com/django-rest-framework-react-tutorial/)

React(redux, axios) and Django and Docker [medium tutorial](https://medium.com/swlh/how-to-deploy-django-rest-framework-and-react-redux-application-with-docker-fa902a611abf). gave up on this project