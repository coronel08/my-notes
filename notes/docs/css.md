# CSS and HTML and Bootstrap
**HTML CSS Bootstrap Notes**

[Fireship Wavy Backgrounds tutorial](https://fireship.io/lessons/wavy-backgrounds/)


[Fonts in HTML and CSS](https://twitter.com/BHolmesDev/status/1565346414955073536?s=20&t=f9VKeBU0Gw7h6XF4d8dscQ)

Notes for CSS, made during vid-site1 project
Check [Readme for Video site](https://github.com/coronel08/website-vid-project) I made.

Id and Class names should use - ex: commet-form, do not camelcase or underscore
FontAwesome
```
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
```

Bootstrap
```
```

---
## Table of Contents
* [HTML](#html)
    * [Semantic Elements](#semantic-elements)
        * [Form Example](#form-example)
* [CSS](#css)
    * [Stylesheet](#stylesheet)
        * [CSS Properties](#css-properties)
            * [Custom property/variable](#custom-property-/-variable)
        * [Fonts](#fonts)
    * [Styling](#styling)
        * [Measurements](#measurements)
        * [Media Queries](#media-queries)
        * [Navbar](#navbar)
    * [Selectors](#selectors)
    * [Pseudo Classes](#pseudo-classes)
        * [Pseudo Elements](#pseudo-elements)
    * [Positions](#positions)
    * [Display](#display)
        * [Visiblity vs Display](#visiblity-vs-display)
    * [Transition](#transition)
    * [Transform](#transform)
    * [Background](#background)
    * [Flexbox](#flexbox)
        * [Example of Flex ](#example-of-flex)
    * [CSS grid](#css-grid)
    * [Box Sizing](#box-sizing)
        * [Photos](#photos)
* [Bootstrap](#bootstrap)
    * [Bootstrap Components](#bootstrap-components)
    * [Bootstrap Utilities](#bootstrap-utilities)
        * [Bootstrap Spacing](#bootstrap-spacing)
        * [Bootstrap Flex](#bootstrap-flex)
    * [Grid System](#grid-system)
        * [Container](#container)
        * [Row and Col](#row-and-col)
    * [Typography](#typography)
    * [Bootstrap Button](#bootstrap-button)
        * [Button Grouping](#button-grouping)
    * [Bootstrap Badge](#bootstrap-badge)
    * [Bootstrap Images](#bootstrap-images)
    * [Bootstrap Forms](#bootstrap-forms)
        * [Input Group](#input-group)
    * [Bootstrap Navbar](#bootstrap-navbar)
    * [Bootstrap Icon](#bootstrap-icon)
        * [FontAwesome Icon](#font-awesome-icon)
    * [Bootstrap Accordion Example](#bootstrap-accordion-example)
* [Tailwind](#tailwind)

---
## HTML
Can use [Emmet shortcuts](https://docs.emmet.io/cheat-sheet/) for html.<br>


[CSS Tricks](https://css-tricks.com/best-way-implement-wrapper-css/) Use Wrapper to wrap body and section 
* Wrapper vs Section 
* Body vs Div

[SVG Example building out card](https://codepen.io/darkwiiplayer/pen/rNzvjwZ?editors=1000) uses svg, defs to make shape. use to reuse shape. 

### Semantic Elements
Use more specified elements rather than Divs, not included the **tables element**

[MDN Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#forms)<br> also has table elements here
[Input types MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) such as radio, checkbox, date, email etc. As well as attributes like value, name, placeholder, required etc
Dropdown using [Select MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
```
<main> for major components that go on every page navbar header etc
<nav>
<header>
<aside> something like a navbar,  call out, or photo

<section> creates large sections
<article> used for like a blog post, have text here for SEO
<form action=""> google for form elements
    <input type="" placeholder=""> goes in form, usually use with <label>
<footer>
<summary>
<details>
```
<br>

#### Form Example
Use a form to search google results
```
<form action="https://www.google.com/search">
    <input type="text" name="q">
    <buton>Search Google</button>
</form>
```
<br>
Buttons inside form default "type="submit"" change to "type="button"" or something else to change behavior.
<br><br>

Form method defaults to **GET** method, not **POST**
<br><br>


### Example HTML 
Dropdown uses `datalist` and `options` to create a dropdown with suggestions
```
<label for="ice-cream-choice"> Choose a flavor</label>
<input list="ice-cream-flavors" id="ice-cream-choice" name="ice-cream-choice"/>

<datalist id="ice-cream-flavors">
    <option value="Chocolate">
    <option value="Coconut">
    <option value="Mint">
</datalist>
```

Usings `details` to create an accordion
```
<details>
    <summary> Frequently asked questions </summary>
    This is the faqs page details
</details>
<details>
    <summary> Privacy </summary>
    This is the privacy page details
</details>
```

Using `base` to create a base url for something like images
```
<head>
    <base href="https://test.com/" target="_blank">
</head>
<body>
    <a href="etc"> GO to img</a>
</body>
```

Use `loading="lazy"` for loading images once they enter iframe.


Use img on error to remove img
```
<img src="test.png" onerror="this.remove()" />
```

Look into `scroll-snap-align` and `scroll-snap-stop` and `scroll-snap-type`

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


[Web Dev Simplified YT](https://www.youtube.com/watch?v=X6tTBxEmZCE) tutorial on using CSS properties

* overflow
* text-shadow / border-shadow / box-shadow
* background-image on text

<br>

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

#### Fonts
https://fonts.google.com/
```
<link href="" rel="stylesheet">
```
<br><br>

---
### Styling
Common styling properties and usefull sites.<br>
[Text styling](https://www.w3schools.in/css3/text/)<br>
[Text decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration) shorthand for underline or color<br>
[Border styling MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/border)<br>


[Fireship YT](https://www.youtube.com/watch?v=rXuHGLzSmSE&t=6s) Switching between themes in css and some javascript

#### Measurements
Units of measurement for CSS em/rem/px/% etc[w3 schools](https://www.w3schools.com/cssref/css_units.asp) [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/length)

* em (parents size, changes if nested in a loop/list)
* rem (gets size from root of document)
* auto
* ch (character height, good for rows)
* fr (fraction, good for columns)
<br><br>

#### Media Queries
[MDN](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/) Media Queries

scoped custom properties with calc for hover effects
```
.card:hover { --hover: 1; }
.card__img {
  transform: scale(calc(1 + (var(--hover) * 0.5)))
    rotate(calc(var(--hover) * -5deg)); 
  transition: transform 0.2s;
}
```

Container Queries
https://twitter.com/shadeed9/status/1566807515299446786?s=20&t=f9VKeBU0Gw7h6XF4d8dscQ
https://twitter.com/shadeed9/status/1564682064204648455?s=20&t=f9VKeBU0Gw7h6XF4d8dscQ

<br><br>

#### Navbar 
[Fireship YT](https://www.youtube.com/watch?v=biOMz4puGt8&t=335s) Building an animated CSS Bar tutorial

[Sidebar HTML and CSS Example](https://dev.to/code_mystery/sidebar-menu-using-html-and-css-o49)<br>

<br><br>

---
### Selectors
Order of selectors specificity, the more specific css will override the lower ones.
* ID (Most specific) Ex: #heading-group
* Class Ex: .class-name
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
Select every 2nd text input, red border. Uses an [attribute selector MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to select all input elements with a type=text
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
Select an element with both classes
```
.test.purple{
    background-color:purple;
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

---
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

---
### Positions
Positions allows you to place things anywhere and is more flexible than the flex box or grid. Added test.html to show difference between relative and absolute. followed [FreecodeCamp](https://www.freecodecamp.org/news/css-position-property-explained/amp/)

[Position MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
[Position Property Values](https://www.w3schools.com/cssref/pr_class_position.asp)

* static
* USE RELATIVE for PARENT and ABSOLUTE for CHILD
* relative (can change top and sides from where it would be regularly, takes it out of document flow and can overlap) PARENT
* absolute (removed from flow, can get position from closest ancestor, if no ancestor then the initial containing block. Try by making parent relative.) CHILD
* fixed (always present)


<br><br>

---
### Display 
[w3 Display Property Values](https://www.w3schools.com/cssref/pr_class_display.asp)
[w3 Display Prop example](https://www.w3schools.com/css/css_display_visibility.asp) Show display on click and hide on click
[Flex align/center/justify etc](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)<br>
* none - deletes the item
* inline - like using span, height and width have no effect
* block - starts on a new line and takes up all width
* inline-block - can apply height and width

#### Visibility vs Display
Can use visibility instead of [display:none](https://www.w3schools.com/css/css_display_visibility.asp). display none deletes the item, visibility just hides it in place.
<br><br>

---
### Transition
[Transition MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) format for changing speed of transitions. Works well on hover or active. Look into timing functions for ease in animations etc   
{
    Transition: (property name) (duration) (timing function) (delay)
}
<br><br>

---
### Transform
[MDN transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) for rotate, scale, move/translate etc
<br><br>

---
### Background 
* [Background property](https://developer.mozilla.org/en-US/docs/Web/CSS/background) shorthand
    * background-color
    * background-image
    * [background-size](https://developer.mozilla.org/en-US/docs/Web/CSS/background-size)
    * background position
    * background-repeat

<br><br>

---
### Flexbox
[Web Dev Simplified YT](https://www.youtube.com/watch?v=fYq5PXgSsbE&t=170s) flexbox in 15 minutes


[MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) Flexbox concepts. and list of property references [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox)


* flex **shorthand** for flex-grow, flex-shrink, flex-basis. Based on Axis, works with wrap. 
    * flex-grow [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow) to make an item take up more space
    * flex-shrink [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink)
    * flex-basis [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis) sets the size of the content box
* flex-direction (can use column or row or reverse) 
* justify-content (spacing for content in div. relies on flex direction)
* align-items (centers vertical or horizontal, used to have all items start at the align)
* flex-wrap (wraps instead of shrinks content)
    * align-content should be used with wrap
<br>

#### Example of Flex 

The align-items centers vertical, justify content centers horizontal.
ALIGN-CONTENT should be used with WRAP in flex container.
```
    display: flex;
    align-items: center;
    justify-content: center;
```
<br><br>

---
### CSS grid
[Fireship YT](https://www.youtube.com/watch?v=uuOXPWCh-6o&t=3s) Introduction setting up css grid


[Fireship YT](https://www.youtube.com/watch?v=705XCEruZFs) Using grid like a bootstrap or flex tutorial


[FreeCodeCamp](https://www.freecodecamp.org/news/learn-css-grid-by-building-5-layouts/amp/) Excercises followed in HTML grid files. 


[MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) Grid Layout and CSS properties
* grid template **Shorthand** for grid-template-rows, grid-template-columns, grid-template-areas 
    * grid-template-column [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns)
        * repeat (positive-integer, auto-fill, auto-fit)
        * grid-column **Shorthand** for start and end(# / span #)
            * grid-column-start
            * grid-column-end
        * column-gap
    * grid-template-row [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows)
    * grid-template-areas [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Grid_Template_Areas)


Using fr unit / fraction and repeat, fr avoids the overspan problems of using a %
```
grid{
    display: grid;
    grid-template-columns: repeat(4,1fr);
    grid-column-gap: 10px;
}
```
Flashcard grid example
```
.card-grid {
  display: grid;
  align-items: center;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: .5rem;
}
```
<br><br>

---
### Box-Sizing
[MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) Use for sizing and layout elements.
* content-box default box behavior
* border-box includes padding in box width

---
### Photos 
[Lightbox Photo Gallery w3](https://www.w3schools.com/howto/howto_js_lightbox.asp)<br>

[Carousel Photo](https://dev.to/code_mystery/image-slider-using-html-css-and-javascript-5dfn)<br>

[Modal photo Gallery w3](https://www.w3schools.com/howto/howto_css_modal_images.asp)


[Object fit property to resize images or not](https://www.w3schools.com/csS/css3_object-fit.asp)
<br><br>


---
# Bootstrap
BOOTSTRAP Tutorial[Bootstrap site](https://getbootstrap.com/docs/4.5/getting-started/introduction/) Components tab for styling


[Bootstrap site](https://getbootstrap.com/docs/3.4/css/) Introduction 
* Media Queries 
* Grid Options
    * Nesting Columns Column Ordering

Added in [BootstrapCDN](https://fontawesome.com/v3.2.1/get-started/), imported into head
```
    <!-- Bootstrap CDN https://fontawesome.com/v3.2.1/get-started/ -->
    <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.no-icons.min.css" rel="stylesheet">
    <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">
```
<br>

## Bootstrap Components
[Bootstrap Site](https://getbootstrap.com/docs/4.5/components/) list of component names / classes. Popular ones below.
* Buttons
* Card
* Carousel
* Collapse
* Dropdown
* Forms
* Modal
* Navbar
* Progress
<br><br>

**Bootstrap Rows then Cols need to be in a container/container-fluid class**

### Bootstrap Utilities
[Bootstrap Site](https://getbootstrap.com/docs/4.1/layout/utilities-for-layout/) Easy way to do CSS styling using Bootstrap Classes instead
<br>


#### Bootstrap Spacing
[Bootstrap Site](https://getbootstrap.com/docs/4.0/utilities/spacing/) Spacing. Sizing goes from 0-5 or auto. 
* m = margin
* p = padding
    * t = top
    * b = bottom
    * l = left
    * r = right
    * x = both left and right
    * y = both top and bottom
    * blank = all 4 sides
<br>
In [Bootstrap5](https://stackoverflow.com/questions/18672452/left-align-and-right-align-within-div-in-bootstrap) For aligning within a flexbox div or row...

ml-auto is now ms-auto
mr-auto is now me-auto

##### Responsive margin and paddings
Change margin or padding based on screen size in bootstrap
```
mr-lg-5 #margin right on large screens
pr-lg-5 #padding right on large screens
```
<br>

#### Bootstrap Flex
[Bootstrap Site](https://getbootstrap.com/docs/4.0/utilities/flex/) alignment with breakpoints and other flex properties

[StackOverflow Bootstrap5 how to center](https://stackoverflow.com/questions/42388989/bootstrap-center-vertical-and-horizontal-alignment)
Might need to add d-flex or d-block to get these working. Can also center things by adding a col inside a row.
* justify-content-center : can change alignment of everything in flexbox
* align-items / align-self : for the y axis, move up and down
    * align-items : used on row
    * align-self : used on col
* text-center

<br><br>

#### Bootstrap Sizing
[Bootstrap Sizing](https://mdbootstrap.com/docs/standard/utilities/sizing/) for width, height, and also relative to the viewport.


--- 
### Grid System
[Bootstrap Site](https://getbootstrap.com/docs/4.0/layout/grid/) Grid tutorial, container grid made up of 12 columns. Defaults to include **gutter**

#### Container
[Container ](https://www.w3schools.com/bootstrap4/bootstrap_containers.asp) Usually goes Container -> row -> col
* container gives a responsive container use like divs
    * container-fluid wraps entire width
    * container-sm to container-xl responsive breakpoints based on screen size

#### Row and Col
* row
    * col (responsive equal width)
        * col-8 (example of 2/3 width)
        * col-md-auto (variable width content, based on width of content)
        * mix and match breakpoints in col to make responsive
```
<!-- Stack the columns on mobile by making one full-width and the other half-width -->
<div class="row">
  <div class="col-12 col-md-8">.col-12 .col-md-8</div>
  <div class="col-6 col-md-4">.col-6 .col-md-4</div>
</div>
```
<br><br>

---
### Typography
[Bootstrap Site](https://getbootstrap.com/docs/4.0/content/typography/) Shows typography class name options
* Headers like H1 can be replaced with **display-1** all the way to display 4
* lead make a paragraph stand out
* inline text
    * mark to highlight
    * del or s to strikethough
    * u for underline
    * small for subscript/ fine print
    * strong to bold
    * em as italicized
* text alignment and wrapping and transform [Bootstrap Site](https://getbootstrap.com/docs/4.0/utilities/text/)
    * text-center, text-justify, text-left
* blockquote for quotes
* footer for naming a source or quote
* list-style or list-unstyled
* list-inline with list-inline-item to have span of list items
<br><br>

---
### Bootstrap button 
[Bootstrap Site](https://getbootstrap.com/docs/4.0/components/buttons/) button section
* outline buttons (btn-outline-warning)
* sizes (btn-md)
* active
* disabled

Example of a bootstrap button
```
<button type="button" class="btn btn-warning"> Primary <button>
```
<br>

#### Button Grouping
[Bootstrap Site](https://getbootstrap.com/docs/4.1/components/button-group/) group buttons, may require javascript. make sure to use role="group".
<br><br>

---
### Bootstrap Badge
[Bootstrap Site](https://getbootstrap.com/docs/4.0/components/badge/) Also **badges** and **pills** 
<br><br>

---
### Bootstrap Images
[Bootstrap Site](https://getbootstrap.com/docs/4.0/content/images/)<br> 
Can also use srcset to make responsive images [css-tricks](https://css-tricks.com/responsive-images-youre-just-changing-resolutions-use-srcset/)
<br><br>

---
### Bootstrap Forms
[Bootstrap Site](https://getbootstrap.com/docs/4.0/components/forms/) Forms section and [custom forms](https://getbootstrap.com/docs/4.0/components/forms/#custom-forms)
* class="form-row" (form grid overrides default column gutters)
    * class="form-group" (adds structure to forms)
        * class="form control"
<br>

#### Input group
[Bootstrap Site](https://getbootstrap.com/docs/4.0/components/input-group/) input groups extend form controls
<br><br>

---
### Bootstrap Navbar
[Bootstrap Site](https://getbootstrap.com/docs/4.0/components/navbar/) Responsive Navbar that collapses
<br><br>

---
### Bootstrap Icon
[Bootstrap Site](https://icons.getbootstrap.com/) Can also use Icons in forms using **Input Group**
<br>

[Tutorial Example](https://www.tutorialandexample.com/bootstrap-icons/) Bootstrap Icon examples
<br><br>

#### FontAwesome Icon
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
[Css-Tricks](https://css-tricks.com/adding-shadows-to-svg-icons-with-css-and-svg-filters/) add shadow to font awesome icons.

<br>

Resources
* Font Awesome Sizing Icons [FontAwesome Site](https://fontawesome.com/v5.9.0/how-to-use/on-the-web/styling/sizing-icons)
<br><br>

---
### Bootstrap Accordion Example 
[Bootstrap Cards Equal Heights](https://mdbootstrap.com/docs/b4/jquery/plugins/equal-height-columns/)
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


# Tailwind
[Tailwind Infoworld](https://www.infoworld.com/article/3622288/tailwind-css-learn-the-joys-of-functional-responsive-css.amp.html) shows navbar, responsive layout


[Github.io Tailwind cheatsheet](https://umeshmk.github.io/Tailwindcss-cheatsheet/) && [Nerdcave](https://nerdcave.com/tailwind-cheat-sheet) Tailwind Cheat Sheet


[Tailwind Install Docs](https://tailwindcss.com/docs/installation)


[Tailwind Display](https://tailwindcss.com/docs/display)
[Tailwind Position](https://tailwindcss.com/docs/position)
[Hover, Active, Focus, Checked, First-Child, etc and other states](https://tailwindcss.com/docs/hover-focus-and-other-states)


Tailwind reuse a component throughout the app
```
const outlineBox = "border-2 rounded-lg border-slate-50"
<div className={outlineBox} />
```


Tailwind set up for full page
```
<div class="flex flex-col justify-between min-h-screen bg-blue-800">
    <nav class="h-20 w-full bg-blue-500">
    </nav>

    <section class="h-1/4 bg-blue-300">
    </section>

    <footer class="h-20 w-full bg-blue-500">
    </footer>
</div>

```


* Responsive breakpoints:
    * flex - base breakpoint < 640px
    * sm: - 640px
    * md: - 768px
    * lg: - 1024px
    * xl: - 1280px
    * 2xl: - 1536px
* Positions:
    * static - normal positionining
    * relative - parent, used as parent container
    * absolute - child, child container that gets positioned
        * inset - to control where item is [Inset](https://devmap.org/p/enhance-tailwindcss-projects.html)
    * fixed - for navbars always on top
    * sticky - once scrolled past it sticks to top
* Displays:
    * hidden - display-none
    * invisible - visiblity-none
    * block - like flex except items stack on top of each other
        * inline-block - width doesnt go all the way
    * flex - create a flex container(groups everything in one line) 
        * inline-flex - width doesnt go all the way
    * grid - create a grid container ```"grid gap-4 grid-cols-3"```
    * table - 
    * contents - to inherit parent container by using a phantom container
* Other Positioning:
    * [Tailwind Float](https://tailwindcss.com/docs/float) and [Tailwind Clear](https://tailwindcss.com/docs/clear)
    * [Tailwind Object-Fit](https://tailwindcss.com/docs/object-fit)
    * [Tailwind Object Position](https://tailwindcss.com/docs/object-position)



## Sizing and Spacing
Margin and Padding is the same as bootstrap but can go higher in numbers <br>
Can go from text-base to text-6xl 
<br>

Set margin, padding, height, width, space and max/min with either 
* auto - center
* Margin Padding and Spacing :
    * space-x-[ number ] - 
    * mx-auto / my-auto - to center item
    * ml-auto / mr-auto mt-auto / mb-auto - to align item to one side
* Width and Height:
    * w-24 or w-1/6 - to set width to a number or fractions
    * w-screen / h-screen - takes the entire width of viewport
    * w-full / h-full- full width
    * min
        * width - min-w-full / min-w-min / min-w-max
        * height - min-h-0 / min-h-full / min-h-screen
    * max 
        * width - max-w-0 or max-w-none / max-w-full / max-w-min / max-w-max / max-w-screen-[ xs|sm|md|lg|xl|2xl ] / max-w-[ xs|sm|md|lg|xl ] / max-w-{2-7}xl
        * height - max-h-24 / max-h-full / max-h-screen

## Tailwind Flex vs Grid

* Containers - set max screen size depending on screen, doesn't center or come with any padding
* Flex - Makes the area responsive to viewport, can combine flex-col and flex-row along with w-1/4 to make a responsive flexbox grid.
    * flex-row - default flex / horizontal
    * flex-col - flex up and down / vertical
    * flex-wrap / flex-no-wrap - to make the flex wrap or overflow
    * Control flex grow and shrink - 
        * flex-1 - shrink and grow evenly
        * flex-initial - shrink but dont grow 
        * flex-auto - shrink and grow (taking into account starting size)
        * flex-none - 
    * flex-grow-0 / flex-grow - use flex-grow to have an item grow
    * flex-shrink-0 / flex-shrink - use flex-shrink to have an item shrink

* Grid - 
    * grid-cols-[ 1-12 ] - to make grid
        * col-span-{ 1-12 / full / auto} - 
        * col-start-{ 1-12 / auto } -
        * col-end-{ 1-12 / auto } -
    * grid-rows [ 1-6] - to make row
        * row-span-{ 1-6 / full / auto} - 
        * row-start-{ 1-6 / auto } -
        * row-end-{ 1-6 / auto } -
    * grid-flow-row / grid-flow-col


|Flex           |       Grid            |   Both                | Notes
---             |        ---            |   ---                 |   ---
|               |                       |   gap-{size}          | Spacing between 
|               |                       | justify-center        | Align horizontally / left and right
|               | justify-items-center  |                       | Align horizontally / left and right
|               | justify-self-center   |                       | Align individual horizontally / left and right
|content-center | content-center        |                       | Controls how grids and *flex-wrap* align vertically /up and down
|               |                       | items-center          | Align vertically / up and down  
|               |                       | self-center           | Align individual vertically / up and down
|               |                       |place-content-center   | Align vertically and horizontally at the same time
|               |                       |place-items-center     | Align vertically and horizontally at the same time, items dont flex or grow
|               |                       |place-self-center      | Align individual vertically and horizontally at the same time 



#### Cards
Made responsive card design in tailwind
```
    <div class="grid grid-cols-1 sm:grid-cols2 md:grid-cols-3 justift-items-center gap-2">
        <div class="w-64 h-64 md:w-11/12 border border-solid border-blue-900 rounded bg-blue-200">
            <div class="w-full bg-blue-500 font-bold pl-2">Title 1</div>
            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit</div>
          </div>
        <div class="w-64 h-64 md:w-11/12 border border-solid border-blue-900 rounded bg-blue-200">
            <div class="w-full bg-blue-500 font-bold pl-2">Title 1</div>
            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit</div>
          </div>
          <div class="w-64 h-64 md:w-11/12 border border-solid border-blue-900 rounded bg-blue-200">
            <div class="w-full bg-blue-500 font-bold pl-2">Title 1</div>
            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit</div>
          </div>
    </div>
```

#### Tailwind React
[SmashMagazine](https://www.smashingmagazine.com/2020/02/tailwindcss-react-project/) uses tailwind post-css and autoprefixer
[Logrocket](https://blog.logrocket.com/theming-react-components-tailwind-css/) Creates a dark and light theme in react. Not too helpful



Can build reusable components in React [SmashingMag](https://www.smashingmagazine.com/2020/05/reusable-react-components-tailwind/) Used methods 1 and 2 succesfully.
[React Docs](https://reactjs.org/docs/components-and-props.html) on Components and Props 

[Dynamic Values Section](https://tailwindcss.com/docs/just-in-time-mode) to see how to change styles based on classname
