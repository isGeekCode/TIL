# Layout - Multi-child : Column

<img src="https://i.imgur.com/F9CuRgC.png" width="500" />

<br>

## 🗂️ Widget Catalog Index

```
├ Basics  
├ Layout  
│   └ Multi-child layout widgets  
│       └ ✅ Column ← 현재 문서  
├ Text  
...
└ Accessibility  
```

<br>

## 개념

`Column`은 여러 자식 위젯을 수직 방향(Top → Bottom)으로 배치하는 다자식 레이아웃 위젯이다.  
`mainAxis`는 세로 방향이며, `crossAxis`는 가로 방향을 의미한다.  
자식 수에 제한은 없으나, **높이 공간이 제한된 부모 안에서 너무 많은 자식을 넣으면 오버플로우가 발생할 수 있다.**

<br>

## 동작 방식
Column은 자식 위젯들을 위에서 아래로 순서대로 배치하면서,
1. 고정 크기 자식(일반 위젯)은 먼저 그대로 배치하고
2. 남은 공간은 Expanded나 Flexible이 나눠서 차지하게 만드는 구조다.



<br>

### 주요 속성

- `mainAxisAlignment`: 세로 방향 정렬 (start, center, end, spaceBetween 등)  
- `crossAxisAlignment`: 가로 방향 정렬 (start, center, end, stretch 등)  
- `mainAxisSize`: Column의 전체 높이를 자식 합으로 할지 (`min`) 또는 최대까지 확장할지 (`max`) 결정

<br><br>

## 생성자

```dart
Column({
  Key? key,
  MainAxisAlignment mainAxisAlignment = MainAxisAlignment.start,
  MainAxisSize mainAxisSize = MainAxisSize.max,
  CrossAxisAlignment crossAxisignment = CrossAxisAlignment.center,
  List<Widget> children = const <Widget>[],
})
```

<br><br>

## 🧪 Sample Code


### 예제 1: 크기 최소화 + 왼쪽 정렬

```dart
Column(
  crossAxisAlignment: CrossAxisAlignment.start,
  mainAxisSize: MainAxisSize.min,
  children: <Widget>[
    Text('Line 1'),
    Text('Line 2'),
    Text('Line 3'),
  ],
)
```

→ 자식 높이만큼만 Column이 차지하고, 텍스트는 좌측 정렬됨

- 첨부사진 1  
![|400](https://i.imgur.com/NX187KZ.png)


<br><br>

### 예제 2: 기본 세로 배치 + 남은 공간 채우기 (Expanded 사용)

```dart
Column(
  children: <Widget>[
    Text('Deliver features faster'),
    Text('Craft beautiful UIs'),
    Expanded(
      child: FittedBox(
        child: FlutterLogo(),
      ),
    ),
  ],
)
```

→ 두 개의 텍스트는 위쪽에 고정 배치되고, 마지막 로고는 `Expanded`를 통해 남은 공간을 모두 채워 아래쪽에 배치된다.

- 첨부사진2  

![400](https://i.imgur.com/TG85Rm8.png)



<br><br>


## ⚠️ Column 사용 시 주의사항

`Column`은 세로로 자식을 배치하는 데 매우 유용하지만, 다음과 같은 점에 주의해야 한다:

- `Column` 자체는 스크롤 기능이 없다.  
  → 자식이 많아 공간을 넘는 경우 `ListView`로 대체하는 것이 좋다.

- `Expanded`, `Flexible`을 사용할 땐 부모 위젯의 높이 제약(BoxConstraints)을 꼭 확인해야 한다.  
  예를 들어 `ListView`나 다른 `Column` 안에 있는 `Column`은 **무제한 높이(infinite height)** 를 가지게 되는데,  
  이 상태에서 `Expanded`를 사용하면 Flutter는 공간을 계산할 수 없어 런타임 에러를 발생시킨다.

#### 🚫 잘못된 예 (런타임 오류 발생):

```dart
ListView(
  children: [
    Column(
      children: [
        Text("Hello"),
        Expanded( // ❌ 오류 발생
          child: Container(color: Colors.red),
        ),
      ],
    ),
  ],
)
```

#### ✅ 해결 방법

- `Expanded`를 제거하거나,  
- `Column`에 명시적인 높이 제약을 주는 위젯(`SizedBox`, `Container(height: ...)`, `Expanded` 등)으로 감싸서 사용해야한다.

> ℹ️ `Expanded` 위젯의 작동 방식과 다양한 활용법은 **별도 문서에서 자세히 다룰 예정.**




## 관련 위젯

- `Row` : 수평 방향 다자식 레이아웃  
- `Flex` : 방향을 지정할 수 있는 Column/Row 추상 위젯  
- `ListView` : 스크롤 가능한 세로 리스트  
- `Expanded`, `Flexible` : 남은 공간을 분배하는 방식  
- `Spacer` : `flex`값 기반 간격 조절 전용 위젯

<br><br>

## History
- 250707 : 초안 작성

