# Layout - Multi-child : Row

<img src="https://i.imgur.com/LwwsI74.png" width="500" />

<br><br>

## 🗂️ Widget Catalog Index

```
├ Basics  
├ Layout  
│   └ Multi-child layout widgets  
│       └ ✅ Row ← 현재 문서  
├ Text  
...
└ Accessibility  
```

<br><br>

## 개념
Row는 자식 위젯을 수평으로 나열하는 레이아웃 위젯이다. 자식이 여러 개인 경우 `children` 리스트에 나열한다.  
Row의 가로 공간보다 자식 위젯의 너비가 크면 overflow 경고가 발생한다.


## 생성자
| 속성               | 설명 |
|--------------------|------|
| `children`         | 수평으로 배치할 자식 위젯 리스트 |
| `mainAxisAlignment`| 주 축 방향(가로)의 정렬 방식 |
| `crossAxisAlignment`| 반대 축 방향(세로)의 정렬 방식 |
| `mainAxisSize`     | Row의 전체 가로 길이 설정 (최대/자식 크기만큼) |
| `textDirection`    | 자식 위젯의 배치 순서 (LTR 또는 RTL) |
| `verticalDirection`| 세로 방향의 정렬 순서 |
| `textBaseline`     | `CrossAxisAlignment.baseline` 사용 시 기준선 지정 |

<br>

```dart
Row({
  Key? key,
  MainAxisAlignment mainAxisAlignment = MainAxisAlignment.start,
  MainAxisSize mainAxisSize = MainAxisSize.max,
  CrossAxisAlignment crossAxisAlignment = CrossAxisAlignment.center,
  TextDirection? textDirection,
  VerticalDirection verticalDirection = VerticalDirection.down,
  TextBaseline? textBaseline,
  List<Widget> children = const <Widget>[],
})
```

<br><br>

## 동작 방식
- 자식 위젯을 수평으로 배치한다.
- 가로 방향(main axis)은 기본적으로 왼쪽 정렬된다 (`MainAxisAlignment.start`).
- 세로 방향(cross axis)은 기본적으로 중앙 정렬된다 (`CrossAxisAlignment.center`).
- 각 자식의 크기를 먼저 계산하고, 남은 공간은 `Expanded` 또는 `Flexible`로 감싼 자식에게 분배된다.
- 자식이 많아 공간을 초과하면 노란/검정 스트라이프 경고가 표시된다.
- 스크롤을 지원하지 않으므로 자식이 많은 경우 `ListView`를 사용한다.

<br><br>

### 크기 계산 방식

Row, Column, Center 같은 레이아웃 전용 위젯들은  
자체적으로 크기를 만들지 않고 부모의 제약(constraints) 안에서  
자식 위젯의 크기에 따라 결정되는 구조이다.

정리하면 아래와 같다:

- 직접적인 사이즈가 없다.
- **부모 위젯이 주는 제약 안에서** 자식 위젯의 크기에 따라 크기를 결정한다.
- 자식 위젯이 아무것도 없거나, 크기가 0이면 본인도 작아진다.

예외 상황:
- `mainAxisSize: MainAxisSize.max` (기본값)인 경우,  
  Row나 Column은 주 축 방향으로 가능한 최대 공간을 차지하려 한다.  
  하지만 자식이 없거나 작다면, 눈에 띄지 않을 수 있다.

<br><br>

### 시각적 속성 추가하기

Row는 배경색이나 테두리처럼 시각적 속성을 직접 줄 수 없다.  
이는 Row, Column, Center 등이 레이아웃 전용 위젯이기 때문이다.  
시각적 스타일(배경색, 테두리, 여백 등)을 주고 싶다면 `Container`나 `SizedBox`와 같은 시각적 위젯으로 감싸야 한다.

```dart
Container(
  color: Colors.yellow,
  child: Row(
    children: [
      Icon(Icons.star),
      Text('Flutter'),
    ],
  ),
)
```


이렇게 감싸면 배경색을 포함한 다양한 시각적 속성을 지정할 수 있다.




<br><br>


### 참고: SizedBox vs Container

Row나 Column 같은 레이아웃 위젯을 감쌀 때는 `Container` 외에도 `SizedBox`를 사용할 수 있다.  
두 위젯은 용도와 성능에 차이가 있으며, 단순히 크기만 지정하고 싶다면 `SizedBox`가 더 적절하다.

예를 들어 아래와 같이 단순한 여백이나 크기만 필요할 경우에는:

```dart
SizedBox(
  width: 100,
  child: Row(
    children: [...],
  ),
)
```



<br><br>

## 🧪 Sample Code

### 예제 1: 기본 Row 사용
기본적인 Row 사용법. 아이콘과 텍스트를 나란히 배치한다.
```dart
Row(
  children: [
    Icon(Icons.star),
    Text('Flutter'),
  ],
)
```

<br><br>

### 예제 2: 자식 간 간격 추가 + 정렬
`mainAxisAlignment`를 활용해 자식 사이에 간격을 준 예제.
```dart
Row(
  mainAxisAlignment: MainAxisAlignment.spaceBetween,
  children: [
    Text('A'),
    Text('B'),
    Text('C'),
  ],
)
```

<br><br>

### 예제 3: textDirection 반전
텍스트와 아이콘의 정렬 방향을 오른쪽에서 왼쪽으로 반전.
```dart
Row(
  textDirection: TextDirection.rtl,
  children: [
    Text('오른쪽부터'),
    Icon(Icons.arrow_back),
  ],
)
```


<br><br>

### 예제 4: Overflow 발생 예시 (잘못된 예)
Row 내 텍스트가 너무 길어 overflow가 발생하는 잘못된 예제.
```dart
Row(
  children: [
    FlutterLogo(),
    Text('아주 긴 텍스트입니다. 여기에 계속해서 문장을 추가하면 overflow가 발생합니다.'),
    Icon(Icons.sentiment_very_satisfied),
  ],
)
```


<br><br>

### 예제 5: Expanded를 이용한 공간 분배
Expanded로 텍스트 공간을 자동 분배해 overflow 방지.
```dart
Row(
  children: [
    FlutterLogo(),
    Expanded(
      child: Text('긴 문장은 Expanded로 감싸면 자동으로 줄바꿈 처리됩니다.'),
    ),
    Icon(Icons.sentiment_very_satisfied),
  ],
)
```

<br><br>

## History
- 250711 : 초안 작성
