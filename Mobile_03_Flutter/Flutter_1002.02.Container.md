# Layout - Single-child : Container

<img src="https://i.imgur.com/yD0YOaE.png" width="500" />

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



## 관련 위젯

Container의 구성 요소를 세분화해서 사용할 수 있는 위젯은 다음과 같다:

- `Padding`: 내부 여백만 지정할 때 사용한다.
- `Align`: 자식 위젯의 정렬만 필요할 때 사용한다.
- `SizedBox`: 특정 크기만 지정할 때 사용한다.
- `DecoratedBox`: 배경이나 테두리 등 시각적 요소만 적용할 때 사용한다.
- `ConstrainedBox`: 제약 조건만 줄 때 사용한다.
- `Transform`: 회전, 이동, 크기 변경 등 변형을 적용할 때 사용한다.
- `AnimatedContainer`: Container의 속성이 변경될 때 애니메이션 효과를 주고 싶을 때 사용한다.

> 참고: `Container(color:)`와 `Container(decoration:)`을 동시에 지정하면 `decoration`이 우선한다.

<br>



## 🧪 Sample Code

아래 예제들은 Container의 주요 속성을 하나씩 설명하며, 마지막 예제는 각각의 역할을 전용 위젯으로 나누어 사용하는 방식이다.

### 예제 1: 배경색과 크기 지정 (기본 사용)
```dart
Container(
  color: Colors.amber,
  width: 100,
  height: 100,
)
```

### 예제 2: margin과 padding 적용
```dart
Container(
  margin: EdgeInsets.all(10),
  padding: EdgeInsets.all(16),
  color: Colors.blue,
  child: Text('Hello Container'),
)
```

### 예제 3: 정렬과 크기 제약
```dart
Container(
  alignment: Alignment.center,
  constraints: BoxConstraints.expand(height: 100),
  color: Colors.green,
  child: Text('Centered Text'),
)
```

### 예제 4: 변형 효과 (회전)
```dart
Container(
  transform: Matrix4.rotationZ(0.1),
  color: Colors.purple,
  child: Text('Rotated'),
)
```

### 예제 5: Container 기능을 전용 위젯으로 나눈 예
Container는 내부적으로 Padding, Align, DecoratedBox 등을 조합해서 동작한다. 이 예제는 해당 기능을 각각의 위젯으로 분리한 구조를 보여준다.
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

<br><br>

## History
- 250711 : 초안 작성
