# ReactNative Notes
Starting a project `npx create-expo-app my-app`


## Table of contents

-   []()

## native components

components that build the basics of react native [react docs](#https://reactnative.dev/docs/components-and-apis)

- `Button` vs `Pressable` button cant be styled, custom buttons need to be built with pressable
-   `Image` and `ImageBackground`
-   `FlatList` list view, renders items lazily. `FlatList vs ScrollView` opt for flatlist for large data
-   `ScrollView` allows scrolling, renders all its children components at once
-   `View` is like a div
-   Text in IOS doesnt allow borders can wrap it in view with styling

### flexbox

use `flex:1` to take up all height in app.js main view.
`justifyContent`and`alignItems` for aligning items

### events

`Touchable` is the old way, use `Pressable`

text fields have `onChangeText`
buttons have `onPress`

when updating state we can do something like

```
const [courseGoals, setCourseGoals] = useState([])

setCourseGoals(prev => [...prev, newGoals])
```


### Styling
- elevation is like box shadow. Android only property. 
- shadow works for IOS we have shadowColor, shadowOffset, shadowOpacity, shadowRadius
- borderRadius 
- linearGradient comes from expo

### Navigation
Install react navigation
```
npm install @react-navigation/native
npx expo install react-native-screens react-native-safe-area-context
npm install @react-navigation/native-stack or npx install @react-navigation/native-stack
```

The stack navigator uses the first item as the initial screen. You can also set the default by setting the initialRouteName