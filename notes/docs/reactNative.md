# ReactNative Notes

## Table of contents

-   []()

## native components

components that build the basics of react native [react docs](#https://reactnative.dev/docs/components-and-apis)

-   `Image` and `ImageBackground`
-   `FlatList` list view, renders items lazily. `FlatList vs ScrollView` opt for flatlist for large data
-   `ScrollView` allows scrolling, renders all its children components at once
-   `View` is like a div
-   Text in IOS doesnt allow borders can wrap it in view with styling

### flexbox

use `flex:1` to take up all height in app.js main view.
`justifyContent`and`alignItems` for aligning items

### events

text fields have `onChangeText`
buttons have `onPress`

when updating state we can do something like

```
const [courseGoals, setCourseGoals] = useState([])

setCourseGoals(prev => [...prev, newGoals])
```
