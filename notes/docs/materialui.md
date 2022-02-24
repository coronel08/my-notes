# MaterialUI
- System 
    - [Grid](https://mui.com/system/grid/)
    - [Flexbox](https://mui.com/system/flexbox/)
    - [Palette](https://mui.com/system/palette/)
    - [Sizing](https://mui.com/system/sizing/)
    - [Spacing](https://mui.com/system/spacing/)
    - [Typography](https://mui.com/system/typography/)


- Aligning Items / Center Items
    - `margin-left:auto` `margin-right:auto`
```
<Stack direction="row" justifyContent="end">
    <Button variant="contained"> Item 1 </Button>
</Stack>

or

<Grid container alignContent="flex-end or justifyContent="flex-end"">
    <Button> Example </Button>
</Grid>
```
## Table of Contents

-   [Components](#components)
-   [Styling](#styling)
    -   [Styled](#styled)
        -   [useForwardProp](#forwardprop)
    -   [Reuseable Components](#reuseable-components)
-   [Hooks](#hooks)
    -   [ThemeProvider & createTheme](#themeprovider-&-createTheme)
    -   [useStyles & makeStyles](#makestyles-&-usestyles)
    -   [useMediaQuery & useTheme](#useMediaQuery-&-useTheme)

## Components

-   Layout
    -   Box - wrapper component can override the div/default `component` to something else like a span.
        -   Has access to all **system properties** [System Properties](https://mui.com/system/properties/)
    -   Container - fluid container with `maxwidth`
    -   Data Grid - tables
    -   Grid
        -   Types
            -   Containers - contains grid items
            -   Items - go inside grid container
        -   Styling
            -   Span - define span of columns using breakpoint and number`xs={1} - xs={12}/ xs={8} md={4}`. If span not defined uses auto-layout. Can set to `xs="auto"` to size based on content
                -   Columns - can change # of columns, defaults to 12 `columns=16`
            -   Spacing - spacing between grids `spacing={3}` can also do `rowSpacing` and `columnSpacing`
            -   Common
                -   direction - `row` `row-reverse` `column` `column-reverse`
                -   justifyContent - `flex-start` `center` `flex-end` `space-between` `space-around` `space-evenly`
                -   alignItems - `flex-start` `center` `flex-end` `stretch` `baseline`
    -   Stack - used to stack items horizontal or vertical. takes `spacing={2}` and `direction="row"`. can also add `divider`. responsive exmaple below
    ```
    <Stack
    direction={{ xs: 'column', sm: 'row' }}
    spacing={{ xs: 1, sm: 2, md: 4 }}
    >
    <Item>Item 1</Item>
    <Item>Item 2</Item>
    <Item>Item 3</Item>
    </Stack>
    ```
    -   Image List - uniform container size, ratio, and spacing.
-   Inputs
    -   Button
        -   can add icons with `startIcon`/`endIcon`
        -   IconButton - add icons
        -   ButtonGroup - group buttons together can do advanced features like `Vertical Group` or `Split Button`
        -   Fab(Floating Action Button) - circular button with icon in font of all content
    -   CheckBox - can wrap in `FormGroup` and `FormControlLabel` to give it a label
    -   TextField
        -   InputAdornment
    -   FormGroup
        -   FormControlLabel
-   Navigation
    -   AppBar - a nav bar
    -   Drawer - anchor left or right edge of screen
    -   Link - [Routing with Link](https://mui.com/guides/routing/)
    -   Menu
-   List
    -   ListItemButton / ListItem(old)
    -   ListItemIcon
    -   ListItemText
-   ToggleButton
    -   ToggleButton
-   Toolbar
-   Typography -
    -   can take `variant`/ typography stles and `component`/element type
-   Transitions/ TransitionGroup - collapse, fade, grow, slide

## Styling

**system properties** [System Properties](https://mui.com/system/properties/)

-   Can use 2 different styling systems:
    -   Styled-Components api -
    -   Material Ui System - one off styles / utility
-   Can use `sx={{}}` to pass styles into components
    -   Core Components - all core components take sx
    -   Box - used as a wrapper, renders a div
    -   Custom Components - can add sx prop to custom components by using `import { styled } from '@mui/material/styles'`

Example of box using Shorthands / Superset of CSS. Spacing and color shorthands

```
<Box
  sx={{
    boxShadow: 1, // theme.shadows[1]
    color: 'primary.main', // theme.palette.primary.main
    m: 1, // margin: theme.spacing(1)
    p: {xs: 1, // [theme.breakpoints.up('xs')]: { padding: theme.spacing(1) }},
    zIndex: 'tooltip', // theme.zIndex.tooltip
    ":hover": {boxShadow: 6,}, // psuedo selector
    '& .ChildSelector': {bgcolor: 'primary.main',}, // using nested selector
  }}
>
```

- Theme Aware Properties, can use shorthands like the ones above
    - Borders
    - Display
    - Grid
    - Palette
    - Positions
    - Shadows
    - Sizing
    - Spacing
    - Typography


### nested selectors
use an array in sx to partially override some styles. [Docs](https://mui.com/system/the-sx-prop/#array-values)
```
<Box
  sx={[
    {'&:hover': {
        color: 'red',
        backgroundColor: 'white',
      },
    },
    foo && {'&:hover': { backgroundColor: 'grey' },},
    bar && {'&:hover': { backgroundColor: 'yellow' },},
  ]}
/>
```

### Styled

can use `styled` from `@mui/material`. Example of using child selector with `&`

```
import Slider from "@mui/material/Slider"

const PrettySlider = styled(Slider)({
    color: "#3D424A",
    height: 22,
    width: 70%,
    "& .multiSlider-track": {
        border:"none",
        background:
        backgroundColor: "#0084FF"
    }
})
```

or take styling from theme

```
const ThemedDiv = styled("div")(({theme}) => ({
    color: theme.palette.primary.main,
    backgroundColor: theme.palette.teal.main,
    padding: theme.spacing(1),
    borderRadius: theme.shape.borderRadius
}))
```

#### forwardProp

can forward props using `shouldForwardProp` example

```
const Div = styled("div", {
    shouldForwardProp: (prop) => prop !== "primary",
})(({primary}) => ({
    backgroundColor: primary ? "palevioletred" : "white",
    color: primary ? "white" : "palevioletred",
}))
```

### Reuseable Components

Example of a Centered Card reuseable component. [](https://mui.com/system/advanced/)

```
import {Box} from "@mui/material"

export function CenteredCard({children}){
    return (
        <Box
            sx={{
                display:"flex",
                flexDirection:"column",
                alignItems:"center",
                minHeight: "100vh",
                justifyContent:"center"
            }}
        >
            <Box
                sx={{
                    boxShadow: "4px -4px 10px 1px rgba(106, 115, 123, 0.25)",
                    width:"30%"
                }}
                component="form"
                onSubmit={()=> console.log("test)}
            >
                <Box sx={{margin:"40px"}}
                >
                    {children}
                </Box>
            </Box>
        </Box>
    )
}
```

## Hooks

### themeprovider & createTheme

```
import { Box, ThemeProvider, createTheme } from '@mui/system';

const theme = createTheme({
    palette: {
        background:{paper: "#fff",},
        text:{
            primary:"#173A5E",
            secondary:"#46505A",
        },
    }
})

export default function Example(){
    return(
        <Box
            sx={{
                bgcolor: "background.paper"
                minWidth: 300;
            }}
        >
            <Box sx={{color:"text.secondary"}}> Secondary </Box>
            <Box sx={{color:"text.primary"}}> Primary</Box>
    )
}
```

### makestyles & usestyles

Can overwrite breakpoints using `makeStyles`

```
const useStyles = makeStyles(theme => ({
    root: {
        height: "100vh",
        backgroundColor: "blue",
        [theme.breakpoints.up("sm")]:{
            backgroundColor: "red",
        },
        [theme.breakpoints.up("md")]:{
            backgroundColor: "green",
        },
        [theme.breakpoints.up("lg")]:{
            backgroundColor: "orange",
        },
        [theme.breakpoints.up("xl")]:{
            backgroundColor: "cyan",
        },
    }
}))
```

`useStyle` hook will be called as `classes` usually

```
const App = () => {
    const classes = useStyles()
    return (
        <div>
            <Typography>
                The background will change color based on breakpoints
            </Typography>
        </div>
    )
}
```

### useMediaQuery & useTheme

`useMediaQuery` hook used for rendering conditionally, used with `useTheme` to return theme properties including breakpoints. [Source](https://gist.github.com/chadmuro/36b1ff7e182e9887bac81226fc9e9f46#file-app-js) and [article](https://levelup.gitconnected.com/using-breakpoints-and-media-queries-in-material-ui-47470d3c43d9)

```
import {useMediaQuery} from '@mui/material/useMediaQuery'
import { useTheme } from '@mui/material/styles';

const useTheme()
const showText = useMediaQuery(theme.breakpoints.up("sm"))
<!-- const showText = useMediaQuery("(min-width:600px)") -->
```
