# Flutter 개요 - 위젯

  
Flutter를 시작하려면, Flutter 앱이 작성되는 **Dart** 언어와 Flutter UI의 구성 요소인 **위젯**에 대한 기본적인 이해가 필요합니다. 

이 페이지에서는 이 두 가지를 간략히 소개하며, 시리즈를 따라가며 더 깊이 배우게 됩니다. 

본문 곳곳에 참고 자료가 있으니 필요할 때 확인하세요. 단, 시작하기 위해 이 모든 것을 전문가처럼 알 필요는 없습니다.


<br><br>

---



## **위젯이란?**

  
Flutter에서는 흔히 “모든 것이 위젯이다”라는 말을 듣게 됩니다.

**위젯은 Flutter 앱 UI의 기본 구성 블록**이며, **UI의 일부분을 불변(immutable)하게 선언**한 것입니다. 텍스트나 버튼과 같은 시각적인 요소뿐 아니라, 패딩, 정렬 등 레이아웃 효과도 위젯으로 표현됩니다.

  

위젯은 Composition 기반의 계층 구조를 가집니다. 각 위젯은 부모 위젯 안에 중첩되며, 부모로부터 context를 받을 수 있습니다. 이 구조는 루트 위젯까지 이어지며, 다음은 간단한 예시입니다:


```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp( // 루트 위젯
      home: Scaffold(
        appBar: AppBar(
          title: const Text('My Home Page'),
        ),
        body: Center(
          child: Builder(
            builder: (context) {
              return Column(
                children: [
                  const Text('Hello, World!'),
                  const SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      print('Click!');
                    },
                    child: const Text('A button'),
                  ),
                ],
              );
            },
          ),
        ),
      ),
    );
  }
}
```

<br>

위 코드에서 생성된 모든 클래스는 위젯입니다:

MaterialApp, Scaffold, AppBar, Text, Center, Builder, Column, SizedBox, ElevatedButton



<br><br>

---

## Widget composition
> 위젯합성


Flutter는 **작고 단일 목적의 위젯을 조합해** 강력한 효과를 내는 **합성 방식의 UI 설계**를 강조합니다.

예를 들어, Padding, Alignment, Row, Column, Grid 같은 레이아웃 위젯(`layout widgets`)은 **자체적으로 시각 요소를 가지지 않으며**, 다른 위젯의 배치를 제어하는 목적만 가집니다.

  
또한 Container는 여러 레이아웃, 페인팅, 위치 지정, 크기 조절 위젯들을 합쳐서 구성된 **다목적 위젯**입니다.

시각 요소를 가진 위젯에는 Text, ElevatedButton, Icon, Image 등이 있습니다.


위 예제를 실행하면, “Hello, World!” 텍스트와 버튼이 수직 방향으로 화면 가운데에 표시됩니다.

이 위치는 Center 위젯이 가운데 정렬을, Column 위젯이 수직 배치를 담당해서 가능한 구조입니다.!



![|700](https://i.imgur.com/k7uqhd8.png)

<br><br>

## Building widgets
> 위젯빌드하기

Flutter에서 UI를 만들려면, **위젯 객체의 build 메서드를 오버라이드**해야 합니다.
모든 위젯은 build()를 가지고, 이 메서드는 **다른 위젯을 반환해야** 합니다.

예를 들어, 텍스트에 패딩을 추가하려면 아래와 같이 작성합니다:

```dart
class PaddedText extends StatelessWidget {
  const PaddedText({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: const Text('Hello, World!'),
    );
  }
}
```

<br>

이 build() 메서드는 위젯이 생성되거나, 이 위젯이 의존하는 상태가 변경될 때 호출됩니다.

프레임마다 호출될 수도 있으므로, **부수 효과(side effects)** 없이 **위젯만 반환**해야 합니다.

렌더링에 대한 더 깊은 설명은 [Flutter 아키텍처 개요](https://docs.flutter.dev/resources/architectural-overview)에서 확인할 수 있습니다.

<br><br>

## Widget state
> 위젯의상태

Flutter는 두 가지 주요 위젯 클래스를 제공합니다:

- StatelessWidget : 상태가 없는 UI
- StatefulWidget : 동적 상태를 가지는 UI

예를 들어, 단순한 텍스트나 아이콘은 상태가 바뀌지 않으므로 StatelessWidget으로 만듭니다.
반면, 버튼을 눌렀을 때 카운터가 증가하는 UI처럼 **상태가 변하는** 경우엔 StatefulWidget을 사용합니다.

예시
```dart
class CounterWidget extends StatefulWidget {
  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Text('$_counter');
  }
}
```

setState()를 호출해야 UI를 업데이트하도록 프레임워크에 알릴 수 있습니다.

**중요 포인트**: 위젯과 상태를 분리하면, 부모 위젯은 자식 위젯의 상태 유지에 신경 쓸 필요 없이, 새 인스턴스를 생성해도 Flutter가 기존 상태를 알아서 재사용합니다.

<br><br>

---

### 알아두면 좋은 주요 위젯

Flutter SDK에는 매우 다양한 위젯이 내장되어 있습니다.
그중, UI를 구성할 때 꼭 알아야 할 기본 위젯들은 다음과 같습니다:

- Container
- Text
- Scaffold
- AppBar
- Row, Column
- ElevatedButton
- Image
- Icon


Flutter Docs - Widget Catalog에 따르면,
활용에 따라 12가지로 나누고 있습니다.
[Flutter Docs - Widget Catalog](https://docs.flutter.dev/ui/widgets/basics)

<br>

| 카테고리 | 설명 |
|----------|------|
| Basics | 가장 기초적인 위젯 구성 요소들 (Text, Button 등) |
| Layout | 레이아웃 구성용 위젯 (Row, Column, Stack 등) |
| Text | 텍스트 표시 및 스타일링 관련 위젯 |
| Input | 사용자 입력을 위한 위젯 (TextField, Form 등) |
| Assets, Images, and Icons | 이미지, 아이콘, 에셋 관련 구성 요소 |
| Scrolling | 스크롤 가능한 콘텐츠를 구성하는 위젯 |
| Interaction Models | 제스처 및 터치 반응 처리 위젯 |
| Styling | 테마, 반응형 구성, 패딩 등 스타일링 위젯 |
| Painting and Effects | 시각적 효과 및 그리기 관련 위젯 |
| Animation and Motion | 애니메이션 효과와 트랜지션 처리 |
| Async | 비동기 상태를 다루기 위한 위젯 (Future, Stream 등) |
| Accessibility | 앱의 접근성을 향상시키는 도구 제공 |

<br>

다양한 카테고리를 학습해야하지만 
그중 Basics에 해당하는 위젯들을 먼저 시작하면 됩니다.

- Widget Catalog
    - Basics
        - AppBar
        - Column
        - Container
        - Elevated Button
        - FlutterLogo
        - Icon
        - Image
        - Placeholder
        - Row





아래는 Widget Catalogs에서 볼 수 있는 세부 카테고리입니다.


# Accessibility widgets
Make your app accessible.

### ExcludeSemantics
A widget that drops all the semantics of its descendants. This can be used to hide subwidgets that would otherwise be reported but that would...


### MergeSemantics
A widget that merges the semantics of its descendants.


### Semantics
A widget that annotates the widget tree with a description of the meaning of the widgets. Used by accessibility tools, search engines, and other semantic...

---

# Animation and motion widgets
Bring animations to your app.


### AlignTransition
Animated version of an Align that animates its Align.alignment property.
- Align 위젯의 alignment 속성을 애니메이션으로 처리한 버전입니다.



### AnimatedAlign
Animated transition that moves the child's position over a given duration whenever the given alignment changes.
- alignment가 바뀔 때 자식 위젯의 위치를 일정 시간 동안 애니메이션으로 이동시킵니다.

### AnimatedBuilder
A general-purpose widget for building animations. AnimatedBuilder is useful for more complex widgets that wish to include animation as part of a larger build function....
- 애니메이션 로직을 일반 위젯에 통합할 때 유용한 범용 애니메이션 위젯입니다.

### AnimatedContainer
A container that gradually changes its values over a period of time.
- Container의 속성(크기, 색상 등)을 일정 시간에 걸쳐 부드럽게 변경합니다

### AnimatedCrossFade
A widget that cross-fades between two given children and animates itself between their sizes.
- 두 자식 위젯 간에 크기와 함께 크로스 페이드 애니메이션을 수행합니다.

### AnimatedDefaultTextStyle
Animated version of DefaultTextStyle which automatically transitions the default text style (the text style to apply to descendant Text widgets without explicit style) over a...
- 자식 텍스트에 적용되는 기본 텍스트 스타일을 애니메이션으로 전환하는 위젯입니다.


### AnimatedList
A scrolling container that animates items when they are inserted or removed.
- 아이템이 추가되거나 제거될 때 애니메이션 효과를 적용하는 스크롤 리스트입니다.

### AnimatedListState
The state for a scrolling container that animates items when they are inserted or removed.


### AnimatedModalBarrier
A widget that prevents the user from interacting with widgets behind itself.
- AnimatedList의 상태를 관리하며, 삽입/삭제 애니메이션을 제어합니다

### AnimatedOpacity
Animated version of Opacity which automatically transitions the child's opacity over a given duration whenever the given opacity changes.
- 자식 위젯의 불투명도를 시간에 따라 점진적으로 변화시킵니다.

### AnimatedPhysicalModel
Animated version of PhysicalModel.
- 그림자, 모서리, 색상 등의 속성을 애니메이션으로 전환할 수 있는 PhysicalModel입니다

### AnimatedPositioned
Animated version of Positioned which automatically transitions the child's position over a given duration whenever the given position changes.
- 위치 속성이 변경될 때 부드럽게 애니메이션으로 전환합니다.

### AnimatedSize
Animated widget that automatically transitions its size over a given duration whenever the given child's size changes.
- 자식 위젯의 크기 변화에 따라 사이즈를 애니메이션으로 전환합니다

### AnimatedWidget
A widget that rebuilds when the given Listenable changes value.
- Listenable이 변경될 때마다 위젯을 다시 빌드하는 애니메이션 위젯입니다

### ImplicitlyAnimatedWidget
An abstract class for building widgets that animate changes to their properties.
- 속성 변화에 따라 애니메이션을 적용할 수 있도록 지원하는 추상 클래스입니다.

### DecoratedBoxTransition
Animated version of a DecoratedBox that animates the different properties of its Decoration.
- Decoration 속성(배경, 테두리 등)을 애니메이션으로 전환합니다

### DefaultTextStyleTransition
Animated version of a DefaultTextStyle that animates the different properties of its TextStyle.
- 텍스트 스타일의 변화(폰트, 색상 등)를 애니메이션으로 적용합니다

### FadeTransition
Animates the opacity of a widget.
- 위젯의 투명도를 애니메이션으로 조절합니다.

### Hero
A widget that marks its child as being a candidate for hero animations.
- 화면 전환 시 자식 위젯을 애니메이션으로 이동시키는 Hero 전환 대상입니다

### MatrixTransition
Animates the Matrix4 of a transformed widget.
- 변형 행렬(Matrix4)을 통해 위젯에 복합적인 애니메이션을 적용합니다

### PositionedTransition
Animated version of Positioned which takes a specific Animation to transition the child's position from a start position to and end position over the lifetime...
- Animation 객체를 기반으로 자식 위젯의 위치를 애니메이션으로 전환합니다

### RelativePositionedTransition
Animated version of Positioned which transitions the child's position based on the value of rect relative to a bounding box with the specified size.
- 바운딩 박스를 기준으로 자식 위치를 애니메이션으로 변경합니다

### RotationTransition
Animates the rotation of a widget.
- 위젯을 회전시키는 애니메이션 효과를 적용합니다.

### ScaleTransition
Animates the scale of transformed widget.
- 위젯의 크기를 확장하거나 축소하는 애니메이션을 적용합니다

### SizeTransition
Animates its own size and clips and aligns the child.
- 자신의 크기를 애니메이션으로 조절하며 자식 위젯도 클립 및 정렬합니다

### SlideTransition
Animates the position of a widget relative to its normal position.
- 자식 위젯의 위치를 기준 위치로부터 상대적으로 이동시키는 애니메이션입니다.


### SliverFadeTransition
Animates the opacity of a sliver widget.ㅁ
- sliver 위젯의 불투명도를 애니메이션으로 처리합니다.

---

# Assets, images, and icon widgets


### AssetBundle
Asset bundles contain resources, such as images and strings, that can be used by an application. Access to these resources is asynchronous so that they...

### Icon
A Material Design icon.

### Image
A widget that displays an image.


### RawImage
A widget that displays a dart:ui.Image directly.

# Async widgets

### FutureBuilder
Widget that builds itself based on the latest snapshot of interaction with a Future.


### StreamBuilder
Widget that builds itself based on the latest snapshot of interaction with a Stream.



# Basic widgets

### AppBar
Container that displays content and actions at the top of a screen.
- 화면 상단에 콘텐츠와 액션을 표시하는 컨테이너입니다.

### Column
Layout a list of child widgets in the vertical direction.
- 자식 위젯을 세로 방향으로 배치하는 레이아웃입니다

### Container
A convenience widget that combines common painting, positioning, and sizing widgets.
- 페인팅, 위치 지정, 크기 조절 기능이 결합된 다용도 위젯입니다.

### ElevatedButton
A Material Design elevated button. A filled button whose material elevates when pressed.
- 누르면 입체감이 생기는 머티리얼 스타일의 버튼입니다

### FlutterLogo
The Flutter logo, in widget form. This widget respects the IconTheme.
- Flutter 로고를 아이콘 형태로 표시하는 위젯입니다


### Icon
A Material Design icon.
- 머티리얼 디자인 아이콘을 표시하는 위젯입니다.

### Image
A widget that displays an image.
- 이미지를 표시하는 위젯입니다.

### Placeholder
A widget that draws a box that represents where other widgets will one day be added.
- 다른 위젯이 나중에 배치될 자리를 표시하는 박스 형태의 위젯입니다

### Row
Layout a list of child widgets in the horizontal direction.
- 자식 위젯을 가로 방향으로 배치하는 레이아웃입니다

### Scaffold
Implements the basic Material Design visual layout structure. This class provides APIs for showing drawers, snack bars, and bottom sheets.
- 앱의 기본적인 머티리얼 레이아웃 구조를 제공하며, 드로어, 스낵바, 바텀시트 등의 API를 포함합니다

### Text
A run of text with a single style.
- 하나의 스타일로 구성된 텍스트를 출력하는 위젯입니다

# Input widgets
Take user input in addition to input widgets in Material components and Cupertino.


### Autocomplete
A widget for helping the user make a selection by entering some text and choosing from among a list of options.


### Form
An optional container for grouping together multiple form field widgets (e.g. TextField widgets).


### FormField
A single form field. This widget maintains the current state of the form field, so that updates and validation errors are visually reflected in the...


### KeyboardListener
A widget that calls a callback whenever the user presses or releases a key on a keyboard.

---

# Interaction model widgets
Respond to touch events and route users to different views.

## Touch interactions
### AbsorbPointer
A widget that absorbs pointers during hit testing. When absorbing is true, this widget prevents its subtree from receiving pointer events by terminating hit testing...

### Dismissible
A widget that can be dismissed by dragging in the indicated direction. Dragging or flinging this widget in the DismissDirection causes the child to slide...

### DragTarget
A widget that receives data when a Draggable widget is dropped. When a draggable is dragged on top of a drag target, the drag target...

### Draggable
A widget that can be dragged from to a DragTarget. When a draggable widget recognizes the start of a drag gesture, it displays a feedback...

### DraggableScrollableSheet
A container for a Scrollable that responds to drag gestures by resizing the scrollable until a limit is reached, and then scrolling.

### GestureDetector
A widget that detects gestures. Attempts to recognize gestures that correspond to its non-null callbacks. If this widget has a child, it defers to that...

### IgnorePointer
A widget that is invisible during hit testing. When ignoring is true, this widget (and its subtree) is invisible to hit testing. It still consumes...

### InteractiveViewer
A widget that enables pan and zoom interactions with its child.

### LongPressDraggable
Makes its child draggable starting from long press.

### Scrollable
Scrollable implements the interaction model for a scrollable widget, including gesture recognition, but does not have an opinion about how the viewport, which actually displays...

## Routing
### Hero
A widget that marks its child as being a candidate for hero animations.

### Navigator
A widget that manages a set of child widgets with a stack discipline. Many apps have a navigator near the top of their widget hierarchy...


---

# Layout widgets
Arrange other widgets columns, rows, grids, and many other layouts.
- 여러 위젯을 세로(Column), 가로(Row), 그리드(Grid) 등 다양한 형태로 배치하는 레이아웃 위젯입니다.

## Single-child layout widgets
### Align
A widget that aligns its child within itself and optionally sizes itself based on the child's size.

### AspectRatio
A widget that attempts to size the child to a specific aspect ratio.

### Baseline
Container that positions its child according to the child's baseline.

### Center
Alignment block that centers its child within itself.
- 자식 위젯을 자신의 영역 내에서 가운데 정렬하는 위젯입니다.

### ConstrainedBox
A widget that imposes additional constraints on its child.

### Container
A convenience widget that combines common painting, positioning, and sizing widgets.


### CustomSingleChildLayout
A widget that defers the layout of its single child to a delegate.

### Expanded
A widget that expands a child of a Row, Column, or Flex.

### FittedBox
Scales and positions its child within itself according to fit.

### FractionallySizedBox
A widget that sizes its child to a fraction of the total available space. For more details about the layout algorithm, see RenderFractionallySizedOverflowBox.

### IntrinsicHeight
A widget that sizes its child to the child's intrinsic height.

### IntrinsicWidth
A widget that sizes its child to the child's intrinsic width.

### LimitedBox
A box that limits its size only when it's unconstrained.

### Offstage
A widget that lays the child out as if it was in the tree, but without painting anything, without making the child available for hit...

### OverflowBox
A widget that imposes different constraints on its child than it gets from its parent, possibly allowing the child to overflow the parent.

### Padding
A widget that insets its child by the given padding.

### SizedBox
A box with a specified size. If given a child, this widget forces its child to have a specific width and/or height (assuming values are...

### SizedOverflowBox
A widget that is a specific size but passes its original constraints through to its child, which will probably overflow.

### Transform
A widget that applies a transformation before painting its child.

## Multi-child layout widgets
### Column
Layout a list of child widgets in the vertical direction.
- 자식 위젯을 세로 방향(위→아래) 으로 배치하는 다자식 레이아웃 위젯입니다.

### CustomMultiChildLayout
A widget that uses a delegate to size and position multiple children.

### CarouselView
A Material carousel widget that presents a scrollable list of items, each of which can dynamically change size based on the chosen layout.

### Flow
A widget that implements the flow layout algorithm.

### GridView
A grid list consists of a repeated pattern of cells arrayed in a vertical and horizontal layout. The GridView widget implements this component.

### IndexedStack
A Stack that shows a single child from a list of children.

### LayoutBuilder
Builds a widget tree that can depend on the parent widget's size.

### ListBody
A widget that arranges its children sequentially along a given axis, forcing them to the dimension of the parent in the other axis.

### ListView
A scrollable, linear list of widgets. ListView is the most commonly used scrolling widget. It displays its children one after another in the scroll direction....

### Row
Layout a list of child widgets in the horizontal direction.

### Stack
This class is useful if you want to overlap several children in a simple way, for example having some text and an image, overlaid with...

### Table
Displays child widgets in rows and columns.

### Wrap
A widget that displays its children in multiple horizontal or vertical runs.

## Sliver widgets
### CupertinoSliverNavigationBar
A navigation bar with iOS-11-style large titles using slivers.

### CupertinoSliverRefreshControl
A sliver widget implementing the iOS-style pull to refresh content control.

### CustomScrollView
A ScrollView that creates custom scroll effects using slivers.

### SliverAppBar
A material design app bar that integrates with a CustomScrollView.

### SliverChildBuilderDelegate
A delegate that supplies children for slivers using a builder callback.

### SliverChildListDelegate
A delegate that supplies children for slivers using an explicit list.

### SliverFixedExtentList
A sliver that places multiple box children with the same main axis extent in a linear array.

### SliverGrid
A sliver that places multiple box children in a two dimensional arrangement.

### SliverList
A sliver that places multiple box children in a linear array along the main axis.

### SliverPadding
A sliver that applies padding on each side of another sliver.

### SliverPersistentHeader
A sliver whose size varies when the sliver is scrolled to the edge of the viewport opposite the sliver's GrowthDirection.

### SliverToBoxAdapter
A sliver that contains a single box widget.


---


# Painting and effect widgets
These widgets apply visual effects to the children without changing their layout, size, or position.


### BackdropFilter
A widget that applies a filter to the existing painted content and then paints a child. This effect is relatively expensive, especially if the filter...

### ClipOval
A widget that clips its child using an oval.


### ClipPath
A widget that clips its child using a path.

### ClipRect
A widget that clips its child using a rectangle.

### CustomPaint
A widget that provides a canvas on which to draw during the paint phase.

### DecoratedBox
A widget that paints a Decoration either before or after its child paints.


### FractionalTranslation
A widget that applies a translation expressed as a fraction of the box's size before painting its child.

### Opacity
A widget that makes its child partially transparent.


### RotatedBox
A widget that rotates its child by a integral number of quarter turns.

### Transform
A widget that applies a transformation before painting its child.

---


# Scrolling widgets
Scroll multiple widgets as children of the parent.

### CarouselView
A Material carousel widget that presents a scrollable list of items, each of which can dynamically change size based on the chosen layout.


### CustomScrollView
A ScrollView that creates custom scroll effects using slivers.


### DraggableScrollableSheet
A container for a Scrollable that responds to drag gestures by resizing the scrollable until a limit is reached, and then scrolling.



### GridView
A grid list consists of a repeated pattern of cells arrayed in a vertical and horizontal layout. The GridView widget implements this component.

### ListView
A scrollable, linear list of widgets. ListView is the most commonly used scrolling widget. It displays its children one after another in the scroll direction....

### NestedScrollView
A scrolling view inside of which can be nested other scrolling views, with their scroll positions being intrinsically linked.

### NotificationListener
A widget that listens for Notifications bubbling up the tree.

### PageView
A scrollable list that works page by page.

### RefreshIndicator
A Material Design pull-to-refresh wrapper for scrollables.

### ReorderableListView
A list whose items the user can interactively reorder by dragging.

### ScrollConfiguration
Controls how Scrollable widgets behave in a subtree.


### Scrollable
Scrollable implements the interaction model for a scrollable widget, including gesture recognition, but does not have an opinion about how the viewport, which actually displays...


### Scrollbar
A Material Design scrollbar. A scrollbar indicates which portion of a Scrollable widget is actually visible.


### SingleChildScrollView
A box in which a single widget can be scrolled. This widget is useful when you have a single box that will normally be entirely...



---

# Styling widgets
Manage the theme of your app, make your app responsive to screen sizes, or add padding.


### MediaQuery
Establishes a subtree in which media queries resolve to the given data.

### Padding
A widget that insets its child by the given padding.


### Theme
Applies a theme to descendant widgets. A theme describes the colors and typographic choices of an application.


---


# Text widgets
Display and style text.

### DefaultTextStyle
The text style to apply to descendant Text widgets without explicit style.


### RichText
The RichText widget displays text that uses multiple different styles. The text to display is described using a tree of TextSpan objects, each of which...

### Text
A run of text with a single style.

