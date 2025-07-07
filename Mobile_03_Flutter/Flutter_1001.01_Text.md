# Basics - Text

<img src="https://i.imgur.com/93H27JZ.png" width="500" />

<br>

## 🗂️ Widget Catalog Index

```
├ Basics  
│   └ ✅ Text ← 현재 문서  
├ Layout  
├ Input  
├ Text  
│   └ ✅ Text ← 현재 문서  
...
└ Accessibility  
```

※ 이 위젯은 공식적으로는 Text 카테고리에 속해있지만, 워낙 기본적인 위젯이라 Basics 섹션에도 함께 포함되어 있다.  
왜 이렇게 만들었는지는 불명확하지만, Widget Catalog 상에서 누락된 위젯들도 있어 향후 정리는 따로 진행 예정.

<br>

## 개념

`Text` 위젯은 **한 줄 또는 여러 줄의 문자열**을 화면에 표시하는 가장 기본적인 Flutter 위젯이다.  
기본적으로 하나의 스타일(TextStyle)을 적용하며,  
레이아웃 제약에 따라 자동 줄바꿈(wrapping) 또는 생략(ellipsis) 등의 처리가 가능하다.

<br>

## 동작 방식

- `Text("문자열")` 형태로 간단하게 문자열을 출력할 수 있다.
- `style`을 지정하지 않으면 상위 `DefaultTextStyle`을 상속받는다.
- overflow나 줄바꿈 동작은 `maxLines`, `softWrap`, `overflow`로 제어 가능하다.
- 다양한 스타일을 혼합하려면 `Text.rich()` 생성자를 사용해야 한다.
- 텍스트 선택은 기본적으로 불가능하며, `SelectableText` 또는 `SelectionArea`로 감싸야 선택 가능하다.

<br>

## 생성자

`Text()` 생성자는 단일 스타일의 문자열을 빠르게 출력할 수 있는 기본 생성자다.  
 
```dart
Text(
  'Hello World',
  style: TextStyle(fontSize: 16, color: Colors.black),
  textAlign: TextAlign.center,
  maxLines: 2,
  overflow: TextOverflow.ellipsis,
)
```

또는 여러 스타일을 섞으려면 `Text.rich` 를 사용한다.  

`Text.rich()`는 내부적으로 `RichText` 위젯을 사용해 여러 개의 `TextSpan`을 구성할 수 있게 해준다. 


```dart
Text.rich(
  TextSpan(
    text: 'Hello',
    children: [
      TextSpan(
        text: ' beautiful ',
        style: TextStyle(fontStyle: FontStyle.italic),
      ),
      TextSpan(
        text: 'world',
        style: TextStyle(fontWeight: FontWeight.bold),
      ),
    ],
  ),
)
```

둘 다 동일한 `Text` 클래스의 생성자이지만, `Text.rich()`는 다채로운 스타일 조합과 상호작용 처리를 위한 시작점이 된다.


<br>

## 주요 속성

| 속성 | 설명 |
|------|------|
| `style` | 텍스트 스타일 (색상, 크기 등) |
| `textAlign` | 텍스트 정렬 방식 |
| `maxLines` | 최대 줄 수 제한 |
| `overflow` | 넘칠 경우 처리 방식 (ellipsis, fade 등) |
| `softWrap` | 줄바꿈 허용 여부 |
| `textScaler` | 텍스트 크기 조절 방식 (textScaleFactor는 deprecated) |

<br>

## 🧪 Sample Code

### 예제 1: 기본 텍스트 출력

```dart
Text('Hello Flutter!')
```

→ 기본 텍스트 출력 예시.  

텍스트는 별도로 스타일을 지정하지 않으면 상위 위젯에서 지정한 `DefaultTextStyle`을 자동으로 상속받는다.  
보통은 앱의 `MaterialApp` 또는 `Scaffold` 같은 기본 구조에서 정의된 스타일이 적용된다.

<br><br>
---

### 예제 2: 텍스트 스타일 지정 (`style`)

```dart
Text(
  'Styled Text',
  style: TextStyle(
    color: Colors.blue,
    fontSize: 20,
    fontWeight: FontWeight.bold,
  ),
)
```

→ 글자 크기, 색상, 굵기 등을 지정할 수 있다.

<br><br>
---

### 예제 3: 정렬 방식 지정 (`textAlign`)

```dart
Text(
  'Aligned Text',
  textAlign: TextAlign.center,
)
```

→ 텍스트를 중앙 정렬한 예시입니다. `TextAlign.right`, `left`, `justify` 등도 사용할 수 있다.

<br><br>
---

### 예제 4: 줄 수 제한 + 생략 (`maxLines`, `overflow`)

```dart
Text(
  'Hello $_name, how are you?',
  maxLines: 1,
  overflow: TextOverflow.ellipsis,
)
```

→ 한 줄만 출력하고, 넘칠 경우 `…` 으로 생략한다.

<br><br>
---

### 예제 5: 줄바꿈 비허용 (`softWrap: false`)

```dart
Text(
  'This text will not wrap to the next line.',
  softWrap: false,
  overflow: TextOverflow.fade,
)
```

→ 줄바꿈 없이 텍스트를 한 줄에 유지하며 fade 효과로 넘침을 처리한다.


<br><br>
---

### 예제 6: 텍스트 크기 스케일링 (`textScaler`)

```dart
Text(
  'Scaled Text',
  textScaler: TextScaler.linear(1.5),
)
```

→ 텍스트 크기를 1.5배로 조정한다. `textScaleFactor`는 deprecated 되었으며, `textScaler`를 사용.

<br><br>
---

### 예제 7: 스타일 혼합 (`Text.rich`)

```dart
Text.rich(
  TextSpan(
    text: 'Hello',
    children: [
      TextSpan(
        text: ' beautiful ',
        style: TextStyle(fontStyle: FontStyle.italic),
      ),
      TextSpan(
        text: 'world',
        style: TextStyle(fontWeight: FontWeight.bold),
      ),
    ],
  ),
)
```

→ 단일 텍스트 내에서 다양한 스타일을 조합하려면 `Text.rich()` 사용.

<br>

## 선택 및 상호작용

- `Text`는 기본적으로 선택 불가능하다.  
  → 선택 가능하게 하려면 `SelectionArea` 또는 `SelectableText` 사용

- 클릭 이벤트 처리: `GestureDetector` 또는 `InkWell`로 감싸서 사용

```dart
GestureDetector(
  onTap: () {
    print("Text tapped!");
  },
  child: Text('Tap Me'),
)
```

<br>


## 관련 위젯

- `RichText`: 텍스트 스타일을 더 정교하게 제어 가능  
- `SelectableText`: 복사/선택 가능한 텍스트  
- `TextButton`: 클릭 가능한 텍스트 형태 버튼  
- `DefaultTextStyle`: 자식 위젯들의 기본 텍스트 스타일 지정
- `TextStyle`: 폰트, 크기, 색상 등 스타일 지정

<br><br>

## History
- 260707 : 초안 작성
