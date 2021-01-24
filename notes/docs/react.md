# React Notes
Notes on learning React.<br><br>

## Table of Contents
*[React Notes](#react-notes)
    * [Using Class and State](#class-state)
    * [Switch vs Router](#Switch-vs-Router)
    * [Hashrouter vs Browserrouter](#Hashrouter-vs-Browserrouter)
    * [Navlink vs Link](#Navlink-vs-Link)
    * [Inline Styling React](Inline-Styling-React)



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