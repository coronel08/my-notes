# CSS
**HTML CSS Bootstrap Notes**

Notes for CSS, made during vid-site1 project
Check [Readme for Video site](https://github.com/coronel08/website-vid-project) I made.
Javascript to handle toggle is at bottom of index.html of vid-site1 project

Javascript if else practice using Javascipt Query Selector, Classlist.conatins, and GetElementByClassname. See Javascript section of file for if/else selecting javascript examples. 


[BOOTSTRAP Tutorial SITE](https://getbootstrap.com/docs/4.5/getting-started/introduction/) Components tab for styling


---
## Table of Contents
* [HTML](#html)
    * [Semantic Elements](#semantic-elements)
    * [Button](#button)
* [CSS](#css)
    * [Stylesheet](#stylesheet)
        * [CSS Properties](#css-properties)
            * [Custom property/variable](#custom-property-/-variable)
    * [Styling](#styling)
        * [Measurements](#measurements)
    * [Selectors](#selectors)
    * [Pseudo Classes](#pseudo-classes)
        * [Pseudo Elements](#pseudo-elements)
    * [Positions](#positions)
    * [Display](#display)
        * [Visiblity vs Display](#visiblity-vs-display)
    * [Transition](#transition)
    * [Transform](#transform)
    * [Example of Flex ](#example-of-flex)
* [Lightbox Photos](#lightbox-photos)
* [Bootstrap](#bootstrap)
    * [Bootstrap button ](#bootstrap-button)
    * [FontAwesome Icon](#fontawesome-icon)
    * [Bootstrap Accordion Example](#bootstrap-accordion-example)

---
## HTML
Can use [Emmet shortcuts](https://docs.emmet.io/cheat-sheet/) for html


### Semantic Elements
Use more specified elements rather than Divs, not included the ** tables element **

[MDN Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#forms)<br> also has table elements here
[Input types MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) such as radio, checkbox, date, email etc. As well as attributes like value, name, placeholder, required etc
Dropdown using [Select MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
```
<main> for major components that go on every page navbar header etc
<nav>
<header>
<aside> something like a navbar,  call out, or photo

<section> creates large sections
<article> used for like a blog post
<form action=""> google for form elements
    <input type="" placeholder=""> goes in form, usually use with <label>
<footer>
<summary>
<details>
```
<br><br>

#### Form Example
Use a form to search google results
```
<form action="https://www.google.com/search">
    <input type="text" name="q">
    <buton>Search Google</button>
</form>
```
<br>

#### Button 
Buttons inside form default "type="submit"" change to "type="button"" or something else to change behavior
<br><br>

---
## CSS
### Stylesheet
Can add 

* CSS inline (not preffered), 
* Style element (add style div in head of document), 
* Add stylesheet (by using code below)
```
<link rel="stylesheet" href="__.css"> 
```
<br>

#### CSS Properties
Properties are used for styling ex: font weight, color, padding [CSS common properties MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference)

[Extended CSS properties list MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)<br>


##### Custom Property / Variable
Can also create custom properties/variables. Example shows adding a custom property for the color blue
```
:root {
    --overlay-color: #03a9f4;
}

<!-- Gets called in Div like this -->
    color: var(--overlay-color)
```
<br>


### Styling
Common styling properties and usefull sites.<br>
[Text styling](https://www.w3schools.in/css3/text/)<br>
[Text decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration) shorthand for underline or color<br>
[Styling Color Names](https://htmlcolorcodes.com/color-names/)<br>
[Color Pallete Ideas ](https://coolors.co/palettes/trending)<br>
[Border styling MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/border)<br>

#### Measurements
[Units of measurement for CSS em/rem/px/% etc](https://www.w3schools.com/cssref/css_units.asp)

* em (parents size, changes if nested in a loop/list)
* rem (gets size from root of document)
* auto
<br><br>

### Selectors
Order of selectors specificity, the more specific css will override the lower ones.
* ID (Most specific)
* Class
* Element


Universal Selector, select everything
```
* {
    color:pink;
}
```
Select all elements like h1, h2 or nav
```
h1,h2 {
    color:purple;
}
```
Select every 2nd text input, red border. Uses an [attribute selector MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to sellect all input elements with a type=text
```
input[type="text]:nth-of-type(2n){
    border:2px solid:red;
}
```
Select a class
```
.test{
    background-color:blue;
}
```
Select an ID/Label
```
#test{
    background-color:black;
}
```
Descendant selector, select an anchor tag in a .class
```
.class a{
    color:white;
}
```
Adjacent Selector, example selects every button that comes after a button on the same level
```
h2 + button {
    font-size:40px
}
```
Direct Child Selector, example selects only the anchors within the footer element
```
footer > a {
    color:purple;
}

or footer.class{
    color:purple;
}
```
Example targeting the "a" item inside of text, inside of showcase when active.
```
.showcase:active .text a{
    background-color: black;
}
```
<br><br>

### Pseudo Classes 
Example of using active psuedo class
```
.toggle.active=looking for active on the toggle  
.toggle .active=looking for active inside of toggle 
```

Section7 vid 76, goes into selecting nth of element. [Full MDN list](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

* :active
* :checked
* :first
* :first-child
* :hover
* :not()
* :nth-child()
* :nth-of-type() 
Example highlight a button inside a post class on hover
```
.post button:hover{
    background:color: red;
}
```

Nth of example
```
.post:nth-of-type(2n){
    color:black;
}
```
<br>

#### Pseudo Elements
Keyword added to a selector
* ::after
* ::before
* ::first-letter
* ::first-line
* ::selection
<br><br>


### Positions
[Position MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
[Position Property Values](https://www.w3schools.com/cssref/pr_class_position.asp)

* static
* relative (can change top and sides from where it would be regularly)
* absolute (removed from flow, can get position from closest ancestor, if no ancestor then the initial containing block. Try by making parent relative )
* fixed (always present)
<br><br><br>

### Display 
[w3 Display Property Values](https://www.w3schools.com/cssref/pr_class_display.asp)
[w3 Display Prop example](https://www.w3schools.com/css/css_display_visibility.asp) Show display on click and hide on click
[Flex align/center/justify etc](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)<br>


#### Visibility vs Display
Can use visibility instead of [display:none](https://www.w3schools.com/css/css_display_visibility.asp). display none deletes the item, visibility just hides it in place.
<br><br>

### Transition
[Transition MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) format for changing speed of transitions. Works well on hover or active. Look into timing functions for ease in animations etc   
{
    Transition: (property name) (duration) (timing function) (delay)
}
<br><br>

### Transform
[MDN transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) for rotate, scale, move/translate etc
<br><br>

### Example of Flex 
The align-items centers vertical, justify content centers horizontal.
ALIGN-CONTENT should be used with WRAP in flex container.
```
    display: flex;
    align-items: center;
    justify-content: center;
```
<br><br>



---
## Lightbox Photos
[Lightbox Photo Gallery w3](https://www.w3schools.com/howto/howto_js_lightbox.asp)

[Modal photo Gallery w3](https://www.w3schools.com/howto/howto_css_modal_images.asp)
<br><br>

---
## Bootstrap
Added in [BootstrapCDN](https://fontawesome.com/v3.2.1/get-started/), imported into head
```
    <!-- Bootstrap CDN https://fontawesome.com/v3.2.1/get-started/ -->
    <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.no-icons.min.css" rel="stylesheet">
    <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">
```
### Bootstrap button 
Example of a bootstrap button
```
<button type="button" class="btn btn-warning"> Primary <button>
```
<br>

### FontAwesome Icon
Import Icon in [Bootstrap tutorial](https://fontawesome.com/v3.2.1/examples/)
```
<i class="icon-facebook">Facebook</i> 
```
CSS for adding Font Awesome Icon, Icon tag inside of toggle. Showing how to select icon and change it between states
```
/* Active state of toggle below, background turns blue on click */
.toggle:active {
    background-color: blue;
}

/* Add Font Awesome Icon  */
.toggle i:before {
    font-family: FontAwesome; 
    content: "\f0d7";
    position: absolute;
    left: 5px;
    bottom: -5px;
}

/* Change Font Awesome Icon on active state */
.toggle.active i:before {
    font-family: FontAwesome; 
    content: "\f0d8";
    position: absolute;
    left: 5px;
    bottom: 3px;
}
```
<br>


### Bootstrap Accordion Example 
[Bootstrap Accordion Docs](https://getbootstrap.com/docs/4.5/components/collapse/)


Can use **href** or **data-target** to target the collapsable item ID. 

Button needs data-toggle="collapse"
```
<p>
    <a class="btn btn-primary" data-toggle="collapse" href="#collapseExample">
        Link with href
    </a>
    <button class="btn btn-primary" data-toggle="collapse" href="#collapse1">
        Button with data-target
    </button>
    <button class="btn btn-primary" data-toggle="collapse" data-target=".collapse" >
        Toggle both buttons
    </button>
</p>
```

[Bootstrap Accordion Example](https://mdbootstrap.com/snippets/jquery/mdbootstrap/888142#html-tab-view) shows/ expands card on click. Optionally Can add Id's for styling 
```
<div class="accordion">

    <!-- Card 1 -->
    <div class="card">
        <div class="card-header">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block" data-toggle="collapse" data-target="#clps1">
                    Collapse Group 1
                </button>
            </h2>
        </div>

        <div class="collapse show" id="clps1">
            <div class="card-body">
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
            </div>
        </div>
    </div>

    <!-- Card 2 -->
    <div class="card">
        <div class="card-header">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block" data-toggle="collapse" href="#clps2">
                    Collapsible Group 2
                </button>
            </h2>
        </div>

        <div class="collapse show" id="clps2">
            <div class="card-body">
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
            </div>
        </div>
    </div>

</div>
```
