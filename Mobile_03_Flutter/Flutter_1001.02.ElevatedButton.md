# Basics - ElevatedButton

<img src="https://i.imgur.com/93H27JZ.png" width="500" />

<br>

## 🗂️ Widget Catalog Index

```
├ Basics  
│   └ ✅ ElevatedButton ← 현재 문서  
├ Layout  
├ Text  
├ Input  
...
└ Accessibility  
```

<br>

## 개념

`ElevatedButton`은 Material Design에서 제공하는 기본 버튼 위젯이다.  
평면적인 레이아웃에 입체감을 주는 방식으로, **눌렀을 때 살짝 떠오르는 효과**가 있다.  
보통 **강조 버튼**이나 시각적으로 강조하고 싶은 액션에 사용된다.

이 버튼은 on/off 개념의 toggle 버튼과는 다르게, **현재 눌렸는지 여부만 판단하는 단발성 액션 버튼**이다.  
버튼을 누르면 약속된 동작을 실행한다.

<br>

## 동작 방식

- 자식으로 보통 `Text`, `Icon`, `Row` 등을 받아 레이블을 구성한다.
- 눌렸을 때 `elevation`(입체감)이 증가하며, 배경색과 전경색은 스타일로 지정 가능하다.
- `onPressed`에 콜백이 지정되지 않으면 버튼은 **비활성(disabled)** 상태가 된다.
- 스타일 지정은 `styleFrom` 또는 `ButtonStyle` 클래스를 통해 할 수 있다.
- 버튼이 눌리면 약간 떠오르는 듯한 입체 효과가 적용되며, 이는 elevation 속성을 통해 제어할 수 있다. 기본값은 2이며, 눌리면 8까지 증가한다.

<br>

## 생성자

```dart
ElevatedButton({
  Key? key,
  required VoidCallback? onPressed,
  Widget? child,
  ButtonStyle? style,
  ...
})
```

또는 아이콘과 텍스트를 함께 넣고 싶다면:

```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
)
```

아이콘을 포함한 버튼도 스타일을 커스터마이징할 수 있다.  
일반 `ElevatedButton`처럼 `styleFrom` 또는 `ButtonStyle`을 사용하면 된다.

예를 들어, 아이콘 버튼의 색상, 여백, 모양 등을 다음과 같이 설정할 수 있다:

```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.indigo,
    foregroundColor: Colors.white,
    padding: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
    elevation: 6,
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
)
```

<br>

## 주요 스타일 속성 (styleFrom 사용 시)

| 속성명 | 설명 |
|--------|------|
| `foregroundColor` | 텍스트 및 아이콘 색상 |
| `backgroundColor` | 버튼 배경색 |
| `elevation` | 눌렀을 때의 그림자 깊이 |
| `padding` | 버튼 내부 여백 |
| `minimumSize`, `fixedSize`, `maximumSize` | 버튼 크기 조절 |
| `shape` | 버튼의 외곽 모양 (e.g. `RoundedRectangleBorder`) |

`styleFrom` 외에도 `ButtonStyle` 객체를 직접 생성하여 style 속성에 넣을 수 있다.


### styleFrom vs ButtonStyle
- `styleFrom`은 간편한 파라미터 기반 설정용 팩토리 메서드이다.  
  → 자주 사용하는 스타일 속성에 빠르게 접근할 수 있다.
- `ButtonStyle`은 더 세부적인 조정이 가능한 정식 스타일 객체이다.  
  → 복잡한 조건별 스타일 처리나 위젯 상태별 처리에 유리하다.



<br><br>


## onPressed란?

`onPressed`는 버튼이 눌렸을 때 실행할 콜백을 정의하는 속성이다.  
`ElevatedButton`에서 이 속성은 필수이며, null이면 버튼은 비활성화된다.

onPressed는 버튼이 눌렸을 때 실행되는 콜백 함수이다. 이 속성은 null이면 버튼은 비활성화되고, 사용자가 눌러도 반응하지 않는다.

```dart
ElevatedButton(
  onPressed: () {
    print("버튼이 눌렸습니다");
  },
  child: Text('Press Me'),
)
```

- `null`이면 버튼은 비활성 상태가 되며, 클릭할 수 없다.

  
```dart
ElevatedButton(
  onPressed: null,
  child: Text('Disabled'),
)
```

// 별도 함수로 정의해도 된다
```dart
void handleClick() {
  print("clicked");
}

ElevatedButton(
  onPressed: handleClick,
  child: Text('Press'),
)
```

> ⚠️ `onPressed`는 생략할 수 없으며, null을 명시적으로 지정해야 비활성 상태가 된다.

<br>
<br>



## 🧪 Sample Code

### 예제 1: 기본 ElevatedButton

```dart
ElevatedButton(
  onPressed: () {
    print("Button pressed");
  },
  child: Text('Click Me'),
)
```

### 예제 2: 버튼 비활성화 처리

```dart
ElevatedButton(
  onPressed: null,
  child: Text('Disabled'),
)
```

### 예제 3-1: 스타일 지정 : styleFrom

```dart
ElevatedButton(
  onPressed: () {},
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.green,
    foregroundColor: Colors.white,
    elevation: 4,
    padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
  child: Text('Styled Button'),
)
```

### 예제 3-2: 스타일 지정 : ButtonStyle

```dart
ElevatedButton(
  onPressed: () {},
  style: ButtonStyle(
    backgroundColor: WidgetStateProperty.all(Colors.red),
    foregroundColor: WidgetStateProperty.all(Colors.white),
  ),
  child: Text('Custom Style'),
)
```

  
### 예제 4: 아이콘 버튼

```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
)
```


### 예제 4-1: 아이콘 버튼 스타일 지정 : styleFrom

```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.indigo,
    foregroundColor: Colors.white,
    padding: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
    elevation: 6,
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
)
```


### 예제 5: 상태 변화 예제 (setState 사용)

```dart
int counter = 0;

ElevatedButton(
  onPressed: () {
    setState(() {
      counter++;
    });
  },
  child: Text('Count: \$counter'),
)
```

<br>

## 관련 위젯

- `TextButton` – 배경 없이 텍스트로만 구성된 버튼  
- `OutlinedButton` – 외곽선만 있는 버튼  
- `FilledButton` – 배경은 있으나 elevation은 없음  
- `IconButton` – 아이콘만 있는 버튼  
- `ButtonStyleButton` – 커스텀 버튼 구현용 베이스 클래스

<br><br>

## ElevatedButtonTheme 활용법

- `ElevatedButtonTheme`를 사용하면 트리 하위의 모든 `ElevatedButton`에 공통 스타일을 지정할 수 있다.
- 앱 전체에 버튼 스타일을 일괄 적용하고 싶을 때 유용하다.

```dart
ElevatedButtonTheme(
  data: ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      backgroundColor: Colors.teal,
      foregroundColor: Colors.white,
    ),
  ),
  child: MyApp(), // 하위 모든 버튼에 적용됨
)
```

## ✅ FilledButton과의 차이
- `ElevatedButton`: 기본적으로 눌렀을 때 elevation이 생기며 입체감이 강조된다.
- `FilledButton`: 배경은 있으나 elevation이 없고, 평면적인 느낌이다.
→ Flat하고 미니멀한 UI를 만들고 싶다면 `FilledButton`도 고려할 수 있다.

### ✅ iconAlignment 속성
- `ElevatedButton.icon`에서 `iconAlignment` 속성을 통해 아이콘의 정렬 위치를 조정할 수 있다.
- 아이콘과 텍스트 배치 위치를 더 정밀하게 컨트롤하고 싶을 때 사용한다.

### 고급 주제
- `statesController`를 사용한 버튼 상태 직접 제어
- `MaterialStatesController`를 활용한 상태 기반 커스텀 스타일링
- 키보드 포커스, 마우스 hover 등 다양한 상태에 따른 반응 처리

<br>

## History
- 260708 : 초안 작성
