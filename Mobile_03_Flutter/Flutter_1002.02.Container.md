# Layout - Single-child : Container

<img src="https://i.imgur.com/DCsQAt2.png" width="500" />

<br>

## 🗂️ Widget Catalog Index

```
├ Basics  
├ Layout  
│   └ Single-child layout widgets  
│       └ ✅ Container ← 현재 문서  
├ Text  
├ ...
└ Accessibility  
```

<br>

## 개념

Container는 Flutter에서 가장 자주 사용하는 다기능 레이아웃 위젯이다.  
빠르게 레이아웃을 꾸미고 싶은 상황에서 가장 먼저 손이 가는 위젯이다. 간단한 시안 구현부터 프로토타입 제작까지 폭넓게 활용된다.  
위치, 크기, 여백, 패딩, 색상, 데코레이션 등을 한 번에 처리할 수 있는 편의 위젯이다.


이 위젯은 내부적으로 여러 위젯(Padding, Align, DecoratedBox 등)을 결합한 구조로 동작한다.  
필요하다면 이러한 기능을 각각의 위젯으로 분리해서 사용할 수 있다.


<br>




## 동작 방식

Container는 아래 순서대로 레이아웃과 페인팅을 처리한다:

1. `margin`: 외부 여백을 적용해 주변 위젯과의 간격을 만든다.
2. `decoration`: 배경 색상이나 테두리 등을 그린다.
3. `padding`: 자식 위젯과 경계 사이의 내부 여백을 준다.
4. `alignment`: 자식 위젯의 정렬 위치를 지정한다.
5. `width`, `height`, `constraints`: 크기와 제약 조건을 설정한다.
6. `transform`: 변형 행렬을 적용해 회전이나 기울이기 등의 효과를 준다.

자식이 없으면 가능한 한 크게 확장된다. 자식이 있으면 자식의 크기에 맞추거나 명시된 제약 조건을 따른다.

또한 크기 관련 속성(`width`, `height`, `constraints`)과 정렬 속성(`alignment`)은 자식 위젯 유무 및 부모 제약에 따라 다르게 동작한다. 


## 생성자

```dart
Container({
  Key? key,
  AlignmentGeometry? alignment,
  EdgeInsetsGeometry? padding,
  Color? color,
  Decoration? decoration,
  Decoration? foregroundDecoration,
  double? width,
  double? height,
  BoxConstraints? constraints,
  EdgeInsetsGeometry? margin,
  Matrix4? transform,
  AlignmentGeometry? transformAlignment,
  Widget? child,
  Clip clipBehavior = Clip.none,
})
```

<br><br>


## 관련 위젯

Container는 다양한 속성을 한 번에 설정할 수 있어 편리하지만, 상황에 따라 더 가벼운 전용 위젯으로 대체할 수 있다. 아래는 각 기능을 담당하는 대표 위젯들이다:

- `Padding`: 내부 여백만 적용할 때 사용한다.
- `Align`: 자식 위젯을 정렬할 때 사용한다.
- `SizedBox`: 고정된 크기나 간격만 필요할 때 사용한다. const 생성이 가능해 성능상 이점이 있다.
- `DecoratedBox`: 배경 색상, 테두리 등 시각적 요소만 적용할 때 사용한다.
- `ConstrainedBox`: 최소/최대 크기 등의 제약 조건을 지정할 때 사용한다.
- `Transform`: 회전, 이동, 크기 조절 등의 변형 효과를 줄 때 사용한다.
- `ColoredBox`: 단순히 배경색만 칠하고 싶을 때 사용한다. Container보다 훨씬 가볍다.
- `IntrinsicWidth`, `IntrinsicHeight`: 자식의 내용에 맞춰 최소한의 크기로 자동 조절할 때 사용한다.

> 참고: `Container(color:)`와 `Container(decoration:)`을 동시에 지정하면 `decoration`이 우선 적용된다.

<br><br>

### 언제 Container를 쓰고, 언제 나눠 쓸까?

- 빠르게 UI를 구성하거나 임시 시안 단계에서는 Container가 유용하다.
- 최적화가 중요한 화면이나, 불필요한 위젯 트리를 줄이고 싶을 땐 전용 위젯으로 나눠 쓰는 것이 좋다.
- 특히 `const` 생성자를 사용할 수 있는 경우(SizedBox 등)는 렌더링 성능에도 이점이 있다.


StackOverflow에서도 [`SizedBox`는 Container보다 성능상 이점이 있으며](https://stackoverflow.com/questions/55716322/flutter-sizedbox-vs-container-why-use-one-instead-of-the-other),  
의도에 맞는 전용 위젯을 사용하는 것이 Flutter 성능 최적화에 도움이 된다고 언급되어 있다.

그럼 네스팅이 깊어지지 않을까? 코드가 오히려 더 보기 어려워지지 않을까?  
실제로 복잡한 구조에서는 Container 하나로 빠르게 작성하는 게 더 가독성이 좋을 수 있다.  
하지만 유지보수성과 렌더링 성능을 고려하면, 가능한 경우 전용 위젯으로 분리하는 습관이 도움이 된다.

  

| 목적 | 권장 위젯 |
|------|-----------|
| 고정 크기 설정 | `SizedBox` |
| 내부 여백만 필요 | `Padding` |
| 배경 색상만 지정 | `ColoredBox` |
| 정렬만 필요 | `Align` |
| 제약 조건만 줄 때 | `ConstrainedBox` |
| 애니메이션 포함 | `AnimatedContainer` |
| 복잡한 스타일(그림자, 테두리 등) | `DecoratedBox` |


<br><br>
---



## 🧪 Sample Code

아래 예제들은 Container의 주요 속성을 하나씩 설명하며, 마지막 예제는 각각의 역할을 전용 위젯으로 나누어 사용하는 방식이다.

### 예제 1: 배경색과 크기 지정 (기본 사용)
```dart
Container(
  color: Colors.amber,
  width: 100,
  height: 100,
)

// 또는 SizedBox + ColoredBox 조합으로 표현 가능
SizedBox(
  width: 100,
  height: 100,
  child: ColoredBox(
    color: Colors.amber,
  ),
)
```


<br><br>

### 예제 2: margin과 padding 적용
```dart
Container(
  margin: EdgeInsets.all(10),
  padding: EdgeInsets.all(16),
  color: Colors.blue,
  child: Text('Hello Container'),
)

// 또는 Padding + ColoredBox 조합으로 구현 가능
Padding(
  padding: EdgeInsets.all(10),
  child: ColoredBox(
    color: Colors.blue,
    child: Padding(
      padding: EdgeInsets.all(16),
      child: Text('Hello Container'),
    ),
  ),
)
```

<br><br>

### 예제 3: 정렬과 크기 제약
```dart
Container(
  alignment: Alignment.center,
  constraints: BoxConstraints.expand(height: 100),
  color: Colors.green,
  child: Text('Centered Text'),
)

// 또는 ConstrainedBox + Align + ColoredBox 조합으로 구현 가능
ConstrainedBox(
  constraints: BoxConstraints.expand(height: 100),
  child: ColoredBox(
    color: Colors.green,
    child: Align(
      alignment: Alignment.center,
      child: Text('Centered Text'),
    ),
  ),
)
```

<br><br>

### 예제 4: 변형 효과 (회전)
```dart
Container(
  transform: Matrix4.rotationZ(0.1),
  color: Colors.green,
  child: Text('Rotated'),
)

// 또는 Transform + ColoredBox 조합으로 구현 가능
Transform.rotate(
  angle: 0.1,
  child: ColoredBox(
    color: Colors.green,
    child: Text('Rotated'),
  ),
)
```

<br><br>

### 예제 5: 최소/최대 제약 설정
```dart
ConstrainedBox(
  constraints: BoxConstraints(minWidth: 100, maxWidth: 200),
  child: Text('길이가 제한된 텍스트'),
)
```


<br>

## 어떤 위젯이 상위에 있어야 할까?

Container는 내부적으로 Padding, Align, DecoratedBox 등을 조합해 동작한다.
이러한 기능을 각각 전용 위젯으로 나눠서 사용할 때에도 위젯 간의 순서와 상위 구조는 중요하다.

Flutter는 부모 → 자식 방향으로 제약(Constraints)을 전달하고,
자식 → 부모 방향으로 실제 크기를 보고한다.
따라서 크기나 위치를 결정하는 위젯이 더 상위에 있어야 한다.


```dart
Padding(
  padding: EdgeInsets.all(8),
  child: DecoratedBox(
    decoration: BoxDecoration(color: Colors.orange),
    child: SizedBox(
      width: 100,
      height: 100,
      child: Align(
        alignment: Alignment.center,
        child: Text('Decomposed'),
      ),
    ),
  ),
)

```


이 구조에서:
- Padding: 외부 여백 적용 (가장 바깥)
- DecoratedBox: 배경 및 테두리 적용
- SizedBox: 크기 고정
- Align: 자식 정렬
- Text: 실제 내용 표시


이처럼 시각적 효과(Padding, Decoration)는 바깥쪽,
크기와 정렬(SizedBox, Align)은 안쪽에 배치하는 것이 일반적이다.



<br><br>

## History
- 250711 : 초안 작성
- 250714 : 세부위젯 분리에 관련된 내용 추가
