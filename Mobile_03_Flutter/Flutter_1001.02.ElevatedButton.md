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

<br>

## 동작 방식

- 자식으로 보통 `Text`, `Icon`, `Row` 등을 받아 레이블을 구성한다.
- 눌렸을 때 `elevation`(입체감)이 증가하며, 배경색과 전경색은 스타일로 지정 가능하다.
- `onPressed`에 콜백이 지정되지 않으면 버튼은 **비활성(disabled)** 상태가 된다.
- `styleFrom` 메서드를 통해 간단하게 스타일을 지정할 수 있다.

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

<br><br>

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

### 예제 2: 비활성화된 버튼

```dart
ElevatedButton(
  onPressed: null,
  child: Text('Disabled'),
)
```

### 예제 3: 스타일 지정

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

### 예제 4: 아이콘과 함께 사용

```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
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

## History
- 260708 : 초안 작성
