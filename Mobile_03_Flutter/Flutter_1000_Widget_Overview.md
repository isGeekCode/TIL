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

- Accessibility 
- Animation and motion
- Assets, images, and icons
- Async
- Basics
- Input
- Interaction models
- Layout
- Painting and effects
- Scrolling
- Styling
- Text

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

