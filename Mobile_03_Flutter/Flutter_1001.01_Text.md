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
| `textAlign` | 텍스트 정렬 방식 (`left`, `right`, `center`, `justify`, `start`, `end`) |
| `maxLines` | 최대 줄 수 제한 |
| `overflow` | 넘칠 경우 처리 방식 (ellipsis, fade 등) |
| `softWrap` | 줄바꿈 허용 여부 |
| `textScaler` | 텍스트 크기 조절 방식 (textScaleFactor는 deprecated) |

<br>

> `maxLines: 0`으로 설정하면 아무 텍스트도 표시되지 않는다.  
> 줄 수 제한이 없게 하려면 `maxLines`를 생략하거나 null로 설정해야 한다.
>
> 텍스트가 컨테이너보다 넘칠 경우 `overflow` 속성 없이 기본 상태라면  
> **다음 줄로 줄바꿈(wrapping)** 된다. 하지만 `maxLines`가 설정되어 있고 넘친다면,  
> `overflow` 속성에 따라 `ellipsis(...)`, `fade`, `clip` 등의 방식으로 처리된다.



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


### 텍스트 비교

아래 예제는 여러 종류의 텍스트 속성을 한 화면에서 비교하기 위한 구성이다.  
특히 줄 수 제한, 생략(`overflow`), 줄바꿈(`softWrap`) 여부를 시각적으로 확인할 수 있도록 구성되어 있다.

```dart
return  Scaffold(
  body: SafeArea(
    child: Center(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [

          Text('기본 텍스트'),
          SizedBox(height: 8),

          Text(
            '파란색 + 크기 20 + Bold',
            style: TextStyle(color: Colors.blue, fontSize: 20, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 8),

          Text(
            '한 줄만, 넘치면 말줄임표 (ellipsis 처리)',
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          ),
          SizedBox(height: 8),

          Text(
            '줄바꿈 없이 fade 처리됨 - softWrap: false',
            softWrap: false,
            overflow: TextOverflow.fade,
          ),
          SizedBox(height: 8),

          Text.rich(
            TextSpan(
              text: 'Hello',
              children: [
                TextSpan(
                  text: ' beautiful ',
                  style: TextStyle(fontStyle: FontStyle.italic),
                ),
                TextSpan(
                  text: 'world!',
                  style: TextStyle(fontWeight:FontWeight.bold),
                ),
              ],
            ),
          ),
          SizedBox(height: 16),

          Divider(),

          Text(
            '✅ 줄바꿈 테스트 (기본)',
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          Text(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
          ),
          SizedBox(height: 12),

          Text(
            '✅ 줄 수 제한 + ellipsis\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(color: Colors.red),
          )
        ],
      ),
    )
  )
);
```

→ 한 화면에서 `softWrap`, `maxLines`, `overflow` 동작을 시각적으로 비교할 수 있습니다.

- 스크린샷   
<img src="https://i.imgur.com/g25qdOd.png" width="500" />


<br>

## 선택 및 상호작용

`Text`는 기본적으로 유저가 선택하는 기능이 없다. 즉, 유저가 아무리 터치하거나 드래그를 해도 아무 반응이 없다는 말이다. 

`GestureDetector`는 텍스트에 터치 이벤트(예: 탭)를 추가하고 싶을 때 사용하는 위젯이다.  
단순히 텍스트를 누르면 반응하는 UI를 만들고 싶다면 `GestureDetector` 또는 `InkWell`을 사용할 수 있다.

아래 예시는 텍스트를 눌렀을 때 콘솔에 "Text tapped!" 라는 로그를 출력합니다.  
단, 이 방식은 텍스트 선택 기능을 제공하진 않으며, 순수한 터치 인터랙션에만 사용된다.

```dart
GestureDetector(
  onTap: () {
    print("Text tapped!");
  },
  child: Text('Tap Me'),
)
```



만약 선택 가능한 텍스트를 만들고 싶다면 다음과 같은 위젯을 사용할 수 있다

- `SelectionArea`: 여러 개의 텍스트 위젯을 감싸서 영역 전체를 선택할 수 있다.
- `SelectableText`: 단일 텍스트를 선택 가능하게 만들어주는 위젯.
  ⚠️ iOS에서는 `SelectableText` 단독 사용 시 시스템 context menu와 충돌로 인해 에러가 발생할 수 있으므로, 가능한 `SelectionArea`로 감싸는 방식이 더 안정적.


```dart
SelectionArea(
  child: Column(
    children: [
      Text('이 텍스트는'),
      Text('모두 선택 가능!'),
    ],
  ),
)

// 혹은  
SelectionArea(
  child: Column(
    children: [
      Text('이 텍스트도 선택 가능'),
    ],
  ),
),

SelectionArea(
  child: Text('단일 텍스트'),
)
```


<br>


## 관련 위젯

- `DefaultTextStyle`: 자식 위젯들의 기본 텍스트 스타일 지정
- `RichText`: 텍스트 스타일을 더 정교하게 제어 가능  
- `SelectableText`: 복사/선택 가능한 텍스트
    - SelectionArea를 사용하는 것을 추천
- `TextButton`: 클릭 가능한 텍스트 형태 버튼  
- `TextStyle`: 폰트, 크기, 색상 등 스타일 지정

<br><br>

## History
- 260707 : 초안 작성
