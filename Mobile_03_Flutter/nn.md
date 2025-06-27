# Widget Catalogs
Base widgets support a range of common rendering options like input, layout, and text.

## Accessibility
Make your app accessible.

- ExcludeSemantics
A widget that drops all the semantics of its descendants. This can be used to hide subwidgets that would otherwise be reported but that would...

- MergeSemantics
A widget that merges the semantics of its descendants.

- Semantics
A widget that annotates the widget tree with a description of the meaning of the widgets. Used by accessibility tools, search engines, and other semantic...


## Animation and motion
Bring animations to your app.


- AlignTransition
Animated version of an Align that animates its Align.alignment property.


- AnimatedAlign
Animated transition that moves the child's position over a given duration whenever the given alignment changes.


- AnimatedBuilder
A general-purpose widget for building animations. AnimatedBuilder is useful for more complex widgets that wish to include animation as part of a larger build function....


- AnimatedContainer
A container that gradually changes its values over a period of time.


- AnimatedCrossFade
A widget that cross-fades between two given children and animates itself between their sizes.


- AnimatedDefaultTextStyle
Animated version of DefaultTextStyle which automatically transitions the default text style (the text style to apply to descendant Text widgets without explicit style) over a...


- AnimatedList
A scrolling container that animates items when they are inserted or removed.


- AnimatedListState
The state for a scrolling container that animates items when they are inserted or removed.


- AnimatedModalBarrier
A widget that prevents the user from interacting with widgets behind itself.


- AnimatedOpacity
Animated version of Opacity which automatically transitions the child's opacity over a given duration whenever the given opacity changes.


- AnimatedPhysicalModel
Animated version of PhysicalModel.


- AnimatedPositioned
Animated version of Positioned which automatically transitions the child's position over a given duration whenever the given position changes.


- AnimatedSize
Animated widget that automatically transitions its size over a given duration whenever the given child's size changes.


- AnimatedWidget
A widget that rebuilds when the given Listenable changes value.


- ImplicitlyAnimatedWidget
An abstract class for building widgets that animate changes to their properties.


- DecoratedBoxTransition
Animated version of a DecoratedBox that animates the different properties of its Decoration.


- DefaultTextStyleTransition
Animated version of a DefaultTextStyle that animates the different properties of its TextStyle.


- FadeTransition
Animates the opacity of a widget.


- Hero
A widget that marks its child as being a candidate for hero animations.


- MatrixTransition
Animates the Matrix4 of a transformed widget.


- PositionedTransition
Animated version of Positioned which takes a specific Animation to transition the child's position from a start position to and end position over the lifetime...


- RelativePositionedTransition
Animated version of Positioned which transitions the child's position based on the value of rect relative to a bounding box with the specified size.


- RotationTransition
Animates the rotation of a widget.


- ScaleTransition
Animates the scale of transformed widget.


- SizeTransition
Animates its own size and clips and aligns the child.


- SlideTransition
Animates the position of a widget relative to its normal position.


- SliverFadeTransition
Animates the opacity of a sliver widget.



## Assets, images, and icons
Manage assets, display images, and show icons.


AssetBundle
Asset bundles contain resources, such as images and strings, that can be used by an application. Access to these resources is asynchronous so that they...

Image/visualization of the Icon widget.
Icon
A Material Design icon.

Image
A widget that displays an image.


RawImage
A widget that displays a dart:ui.Image directly.




## Async
Widgets supporting async patterns in your Flutter apps.


FutureBuilder
Widget that builds itself based on the latest snapshot of interaction with a Future.


StreamBuilder
Widget that builds itself based on the latest snapshot of interaction with a Stream.


## Basics
Widgets to know before building your first Flutter app.

Image/visualization of the AppBar widget.
AppBar
Container that displays content and actions at the top of a screen.

Column
Layout a list of child widgets in the vertical direction.

Container
A convenience widget that combines common painting, positioning, and sizing widgets.

Image/visualization of the ElevatedButton widget.
ElevatedButton
A Material Design elevated button. A filled button whose material elevates when pressed.


FlutterLogo
The Flutter logo, in widget form. This widget respects the IconTheme.

Image/visualization of the Icon widget.
Icon
A Material Design icon.

Image
A widget that displays an image.


Placeholder
A widget that draws a box that represents where other widgets will one day be added.

Row
Layout a list of child widgets in the horizontal direction.

Image/visualization of the Scaffold widget.
Scaffold
Implements the basic Material Design visual layout structure. This class provides APIs for showing drawers, snack bars, and bottom sheets.

Abc
Text
A run of text with a single style.



## Input
Take user input in addition to input widgets in Material components and Cupertino.


Autocomplete
A widget for helping the user make a selection by entering some text and choosing from among a list of options.


Form
An optional container for grouping together multiple form field widgets (e.g. TextField widgets).


FormField
A single form field. This widget maintains the current state of the form field, so that updates and validation errors are visually reflected in the...


KeyboardListener
A widget that calls a callback whenever the user presses or releases a key on a keyboard.


## Interaction models
Respond to touch events and route users to different views.


Touch interactions
Placeholder Flutter logo in place of missing widget image or visualization.
AbsorbPointer
A widget that absorbs pointers during hit testing. When absorbing is true, this widget prevents its subtree from receiving pointer events by terminating hit testing...

Placeholder Flutter logo in place of missing widget image or visualization.
Dismissible
A widget that can be dismissed by dragging in the indicated direction. Dragging or flinging this widget in the DismissDirection causes the child to slide...

Placeholder Flutter logo in place of missing widget image or visualization.
DragTarget
A widget that receives data when a Draggable widget is dropped. When a draggable is dragged on top of a drag target, the drag target...

Placeholder Flutter logo in place of missing widget image or visualization.
Draggable
A widget that can be dragged from to a DragTarget. When a draggable widget recognizes the start of a drag gesture, it displays a feedback...

Placeholder Flutter logo in place of missing widget image or visualization.
DraggableScrollableSheet
A container for a Scrollable that responds to drag gestures by resizing the scrollable until a limit is reached, and then scrolling.

Placeholder Flutter logo in place of missing widget image or visualization.
GestureDetector
A widget that detects gestures. Attempts to recognize gestures that correspond to its non-null callbacks. If this widget has a child, it defers to that...

Placeholder Flutter logo in place of missing widget image or visualization.
IgnorePointer
A widget that is invisible during hit testing. When ignoring is true, this widget (and its subtree) is invisible to hit testing. It still consumes...

Placeholder Flutter logo in place of missing widget image or visualization.
InteractiveViewer
A widget that enables pan and zoom interactions with its child.

Placeholder Flutter logo in place of missing widget image or visualization.
LongPressDraggable
Makes its child draggable starting from long press.

Placeholder Flutter logo in place of missing widget image or visualization.
Scrollable
Scrollable implements the interaction model for a scrollable widget, including gesture recognition, but does not have an opinion about how the viewport, which actually displays...

Routing
Placeholder Flutter logo in place of missing widget image or visualization.
Hero
A widget that marks its child as being a candidate for hero animations.

Placeholder Flutter logo in place of missing widget image or visualization.
Navigator
A widget that manages a set of child widgets with a stack discipline. Many apps have a navigator near the top of their widget hierarchy...




## Layout
Arrange other widgets columns, rows, grids, and many other layouts.


Single-child layout widgets
Align
A widget that aligns its child within itself and optionally sizes itself based on the child's size.

AspectRatio
A widget that attempts to size the child to a specific aspect ratio.

Abc
Baseline
Container that positions its child according to the child's baseline.

Center
Alignment block that centers its child within itself.

ConstrainedBox
A widget that imposes additional constraints on its child.

Container
A convenience widget that combines common painting, positioning, and sizing widgets.

Placeholder Flutter logo in place of missing widget image or visualization.
CustomSingleChildLayout
A widget that defers the layout of its single child to a delegate.

Placeholder Flutter logo in place of missing widget image or visualization.
Expanded
A widget that expands a child of a Row, Column, or Flex.

Placeholder Flutter logo in place of missing widget image or visualization.
FittedBox
Scales and positions its child within itself according to fit.

Placeholder Flutter logo in place of missing widget image or visualization.
FractionallySizedBox
A widget that sizes its child to a fraction of the total available space. For more details about the layout algorithm, see RenderFractionallySizedOverflowBox.

Placeholder Flutter logo in place of missing widget image or visualization.
IntrinsicHeight
A widget that sizes its child to the child's intrinsic height.

Placeholder Flutter logo in place of missing widget image or visualization.
IntrinsicWidth
A widget that sizes its child to the child's intrinsic width.

Placeholder Flutter logo in place of missing widget image or visualization.
LimitedBox
A box that limits its size only when it's unconstrained.

Placeholder Flutter logo in place of missing widget image or visualization.
Offstage
A widget that lays the child out as if it was in the tree, but without painting anything, without making the child available for hit...

Placeholder Flutter logo in place of missing widget image or visualization.
OverflowBox
A widget that imposes different constraints on its child than it gets from its parent, possibly allowing the child to overflow the parent.

Padding
A widget that insets its child by the given padding.

SizedBox
A box with a specified size. If given a child, this widget forces its child to have a specific width and/or height (assuming values are...

Placeholder Flutter logo in place of missing widget image or visualization.
SizedOverflowBox
A widget that is a specific size but passes its original constraints through to its child, which will probably overflow.

Transform
A widget that applies a transformation before painting its child.

Multi-child layout widgets
Column
Layout a list of child widgets in the vertical direction.

Placeholder Flutter logo in place of missing widget image or visualization.
CustomMultiChildLayout
A widget that uses a delegate to size and position multiple children.

Rendered image or visualization of the CarouselView widget.
CarouselView
A Material carousel widget that presents a scrollable list of items, each of which can dynamically change size based on the chosen layout.

Placeholder Flutter logo in place of missing widget image or visualization.
Flow
A widget that implements the flow layout algorithm.

Rendered image or visualization of the GridView widget.
GridView
A grid list consists of a repeated pattern of cells arrayed in a vertical and horizontal layout. The GridView widget implements this component.

Placeholder Flutter logo in place of missing widget image or visualization.
IndexedStack
A Stack that shows a single child from a list of children.

Placeholder Flutter logo in place of missing widget image or visualization.
LayoutBuilder
Builds a widget tree that can depend on the parent widget's size.

Placeholder Flutter logo in place of missing widget image or visualization.
ListBody
A widget that arranges its children sequentially along a given axis, forcing them to the dimension of the parent in the other axis.

Rendered image or visualization of the ListView widget.
ListView
A scrollable, linear list of widgets. ListView is the most commonly used scrolling widget. It displays its children one after another in the scroll direction....

Row
Layout a list of child widgets in the horizontal direction.

Stack
This class is useful if you want to overlap several children in a simple way, for example having some text and an image, overlaid with...

Placeholder Flutter logo in place of missing widget image or visualization.
Table
Displays child widgets in rows and columns.

Placeholder Flutter logo in place of missing widget image or visualization.
Wrap
A widget that displays its children in multiple horizontal or vertical runs.

Sliver widgets
Rendered image or visualization of the CupertinoSliverNavigationBar widget.
CupertinoSliverNavigationBar
A navigation bar with iOS-11-style large titles using slivers.

Placeholder Flutter logo in place of missing widget image or visualization.
CupertinoSliverRefreshControl
A sliver widget implementing the iOS-style pull to refresh content control.

Placeholder Flutter logo in place of missing widget image or visualization.
CustomScrollView
A ScrollView that creates custom scroll effects using slivers.

Rendered image or visualization of the SliverAppBar widget.
SliverAppBar
A material design app bar that integrates with a CustomScrollView.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverChildBuilderDelegate
A delegate that supplies children for slivers using a builder callback.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverChildListDelegate
A delegate that supplies children for slivers using an explicit list.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverFixedExtentList
A sliver that places multiple box children with the same main axis extent in a linear array.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverGrid
A sliver that places multiple box children in a two dimensional arrangement.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverList
A sliver that places multiple box children in a linear array along the main axis.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverPadding
A sliver that applies padding on each side of another sliver.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverPersistentHeader
A sliver whose size varies when the sliver is scrolled to the edge of the viewport opposite the sliver's GrowthDirection.

Placeholder Flutter logo in place of missing widget image or visualization.
SliverToBoxAdapter
A sliver that contains a single box widget.



## Painting and effects
These widgets apply visual effects to the children without changing their layout, size, or position.

- BackdropFilter
A widget that applies a filter to the existing painted content and then paints a child. This effect is relatively expensive, especially if the filter...

- ClipOval
A widget that clips its child using an oval.


- ClipPath
A widget that clips its child using a path.

- ClipRect
A widget that clips its child using a rectangle.

- CustomPaint
A widget that provides a canvas on which to draw during the paint phase.

- DecoratedBox
A widget that paints a Decoration either before or after its child paints.


- FractionalTranslation
A widget that applies a translation expressed as a fraction of the box's size before painting its child.

- Opacity
A widget that makes its child partially transparent.


- RotatedBox
A widget that rotates its child by a integral number of quarter turns.

- Transform
A widget that applies a transformation before painting its child.


## Scrolling
Scroll multiple widgets as children of the parent.

- CarouselView
A Material carousel widget that presents a scrollable list of items, each of which can dynamically change size based on the chosen layout.


- CustomScrollView
A ScrollView that creates custom scroll effects using slivers.


- DraggableScrollableSheet
A container for a Scrollable that responds to drag gestures by resizing the scrollable until a limit is reached, and then scrolling.

- GridView
A grid list consists of a repeated pattern of cells arrayed in a vertical and horizontal layout. The GridView widget implements this component.

- ListView
A scrollable, linear list of widgets. ListView is the most commonly used scrolling widget. It displays its children one after another in the scroll direction....


- NestedScrollView
A scrolling view inside of which can be nested other scrolling views, with their scroll positions being intrinsically linked.


- NotificationListener
A widget that listens for Notifications bubbling up the tree.


- PageView
A scrollable list that works page by page.


- RefreshIndicator
A Material Design pull-to-refresh wrapper for scrollables.


- ReorderableListView
A list whose items the user can interactively reorder by dragging.


- ScrollConfiguration
Controls how Scrollable widgets behave in a subtree.


- Scrollable
Scrollable implements the interaction model for a scrollable widget, including gesture recognition, but does not have an opinion about how the viewport, which actually displays...


- Scrollbar
A Material Design scrollbar. A scrollbar indicates which portion of a Scrollable widget is actually visible.


- SingleChildScrollView
A box in which a single widget can be scrolled. This widget is useful when you have a single box that will normally be entirely...



## Styling
Manage the theme of your app, make your app responsive to screen sizes, or add padding.

- MediaQuery
Establishes a subtree in which media queries resolve to the given data.

- Padding
A widget that insets its child by the given padding.


- Theme
Applies a theme to descendant widgets. A theme describes the colors and typographic choices of an application.







## Text
Display and style text.

- DefaultTextStyle
The text style to apply to descendant Text widgets without explicit style.


- RichText
The RichText widget displays text that uses multiple different styles. The text to display is described using a tree of TextSpan objects, each of which...

- Text
A run of text with a single style.




이렇게 나와있어

