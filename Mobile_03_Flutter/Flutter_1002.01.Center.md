# Layout - Single-child : Center

<img src="https://i.imgur.com/yD0YOaE.png" width="500" />

<br>

## 🗂️ Widget Catalog Index

```
├ Basics  
├ Layout  
│   └ Single-child layout widgets  
│       └ ✅ Center ← 현재 문서  
├ Text  
├ ...
└ Accessibility  
```

<br>

## 개념

자식(child)을 중앙에 배치하는 단일 자식 위젯(single-child widget)이다.  
부모 위젯의 공간 안에서 가로/세로 중앙에 자식 위젯을 위치시킨다.  
하나의 자식만 가질 수 있다.

<br>




## 동작 방식

### 크기 계산 규칙

`Center`는 자식의 위치뿐 아니라, 자신의 크기도 상황에 따라 결정된다.  
아래는 Center 위젯이 자식과 부모의 제약에 따라 크기를 계산하는 방식이다:

<br><br>

#### ▸ Case 1: 부모의 제약이 있음 (`BoxConstraints.tight` 등)
- Center는 가능한 한 부모의 크기를 최대한 확장한다.
- 자식은 중앙에 배치된다.

```dart
// Scaffold → body → Center
Scaffold(
  body: Center(
    child: Text('Hello'),
  ),
)
```

이 경우 Center는 화면 전체 크기를 차지하며, 텍스트는 가운데 위치한다.

<br><br>

#### ▸ Case 2: 부모의 제약이 없음 (UnconstrainedBox 등)
- Center는 자식의 크기를 따라간다 (shrink-wrap).
- 자식만큼만 공간을 차지하며, 위치는 부모 기준으로 중앙에 정렬된다.

```dart
UnconstrainedBox(
  child: Center(
    child: Container(width: 100, height: 100, color: Colors.red),
  ),
)
```

<br><br>

#### ▸ Case 3: `widthFactor`, `heightFactor`가 설정된 경우
- Center의 크기는 자식의 크기 × 해당 factor로 결정된다.
- 부모의 제약이 있어도 factor를 기준으로 자식 대비 확장된 크기를 갖는다.

```dart
Center(
  widthFactor: 2.0,
  heightFactor: 1.5,
  child: Container(
      width: 80, 
      height: 60, 
      color: Colors.green),
)
```

→ Center는 너비 160, 높이 90 크기를 갖는다.

❗ 참고: 부모의 제약이 지나치게 작으면 factor를 곱해도 그 이상 커지지 않을 수 있다.

<br><br>

## 생성자

### 파라미터 설명

- `child`  
  Center 안에 배치할 자식 위젯을 지정한다.  
  자식은 하나만 가질 수 있으며, 보통 텍스트, 버튼, 이미지 등 다양한 위젯이 올 수 있다.

- `widthFactor`  
  자식의 너비에 곱해질 배수값을 설정한다.  
  `null`일 경우, 부모 constraints에 따라 최대 너비를 사용한다.  
  예: `widthFactor: 2.0` → 자식 너비의 2배로 Center 크기 설정

- `heightFactor`  
  자식의 높이에 곱해질 배수값을 설정한다.  
  `null`일 경우, 부모 constraints에 따라 최대 높이를 사용한다.

이 두 factor는 일반적인 정중앙 배치 외에,
Center 자체의 크기를 조절하고 싶은 경우 유용하게 활용된다.

```dart
Center({
  Key? key,
  double? widthFactor,
  double? heightFactor,
  Widget? child
})

```

## 관련 위젯

### 🧩 Align vs Center

`Center`는 자식 위젯을 항상 **정중앙**에 위치시키는 데 비해,  
`Align`은 `alignment` 값을 통해 **보다 자유로운 위치 배치**가 가능하다.  
예를 들어 좌측 상단 배치는 다음과 같이 가능하다:

```dart
Align(
  alignment: Alignment.topLeft,
  child: Text('Top Left'),
)
```

간단한 중앙 정렬은 `Center`를 사용하고,  
복잡한 위치 지정이 필요하면 `Align`을 고려한다.

<br>



## 🧪 Sample Code

`Center` 위젯은 다음과 같은 경우에 유용하게 사용된다:

- 텍스트, 아이콘, 버튼 등을 화면 정중앙에 배치하고 싶을 때
- 부모 위젯의 크기가 제한되어 있고, 그 안에서 자식을 정렬할 때
- 자식 위젯의 크기를 기준으로 `Center`의 크기를 조절하고 싶을 때 (with widthFactor, heightFactor)

아래는 대표적인 예시들이다.

### 예제 1: 텍스트를 화면 중앙에 배치

```dart
Center(
  child: Text('Hello, Flutter!'),
)
```

### 예제 2: 버튼을 중앙에 배치

```dart
Center(
  child: ElevatedButton(
    onPressed: () {},
    child: Text('Click Me'),
  ),
)
```

### 예제 3: 크기를 두 배로 설정 (widthFactor, heightFactor 사용)

```dart
Center(
  widthFactor: 2.0,
  heightFactor: 2.0,
  child: Container(
    width: 100,
    height: 100,
    color: Colors.blue,
  ),
)
```

위 코드는 자식 위젯의 크기를 기준으로 Center 자체의 크기를 조정하고 싶을 때 사용한다.

<br><br>

## History
- 260707 : 초안 작성
