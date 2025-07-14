## Flutter 개요 - 레이아웃의 이해

Flutter의 레이아웃 메커니즘 핵심은 위젯이다. Flutter에서는 거의 모든 것이 위젯이며, 레이아웃 모델도 위젯으로 구성된다. 앱에서 보이는 이미지, 아이콘, 텍스트뿐 아니라 행(Row), 열(Column), 그리드(Grid) 같은 보이지 않는 위젯도 모두 위젯이다.

복잡한 레이아웃은 간단한 위젯 조합으로 구성한다. 예를 들어, 3개의 아이콘 아래 각각 라벨이 있는 구조는 `Row` 안에 3개의 `Column`을 넣고, 각 `Column`에 `Icon`과 `Text`를 배치하여 구성한다.

![|700](https://i.imgur.com/wR7YMIS.png)

<br>
<br>

---

## Constraints
`제약조건`

Flutter에서 레이아웃 이해를 위해 제약 조건 개념을 반드시 알아야 한다.

- **위젯은 부모로부터 제약 조건을 받는다.**
- **제약 조건은 최소/최대 너비와 최소/최대 높이의 4개 Double 값으로 구성된다.**
- **위젯은 받은 제약 조건 범위 내에서 자신이 사용할 크기를 정하고, 그 크기를 부모에게 알린다.**
- **부모는 자식이 원하는 크기를 보고, 정렬(Alignment)에 따라 위치를 결정한다.**
    - **정렬은 Center, Row, Column 등의 위젯이나 그 안의 alignment 속성으로 명시적으로 설정한다.**

요약하면:
> **부모가 자식에게 “이 정도 크기에서 그려라”라는 제약을 주면,  
> 자식은 그 안에서 크기를 결정해 부모에게 알려준다.  
> 부모는 그 크기를 기반으로 자식을 어디에 위치시킬지 결정한다.**

한 문장으로 정리하면

- `Constraints go down. Sizes go up. Parent sets the position`
> "제약은 아래로, 크기는 위로, 위치는 부모가 설정한다."

<br><br>

---

## Box Types
`박스유형`

Flutter에서 위젯은 `RenderBox` 객체에 의해 렌더링되며, 이 객체는 제약 조건 처리 방식을 결정한다. 일반적으로 세 가지 유형의 박스가 있다:

1. `가능한 한 크게 확장`하려는 박스: `Center`, `ListView`
2. `자식과 같은 크기`를 유지하려는 박스: `Transform`, `Opacity`
3. `특정 크기`를 가지려는 박스: `Image`, `Text`

예를 들어, `Container`는 전달된 인자에 따라 다르게 동작한다. 아무 값도 지정하지 않으면 가능한 한 크게 렌더링되고, `width` 등을 지정하면 해당 크기를 따른다.

<br><br>

## Layout a single widget
`단일 위젯 레이아웃`

`Text`나 `Image` 같은 가시적 위젯을 위치시키려면, `Center` 같은 위치 변경 가능한 위젯으로 감싼다.

```dart
Widget build(BuildContext context) {
  return Center(
    child: BorderedImage(),
  );
}
```

<br><br>

다음 그림은 좌측 정렬된 위젯과 가운데 정렬된 위젯을 비교한 예시이다.

![](https://i.imgur.com/bNOjRHe.png)

모든 레이아웃 위젯은 다음 중 하나의 속성을 가진다:

- child 속성: 하나의 자식만 받는 위젯에서 사용한다.
    예: Center, Container, Padding 등
- children 속성: 여러 자식을 받는 위젯에서 사용한다.
    예: Row, Column, ListView, Stack 등

<br><br>

## `Container` 예제

Container는 레이아웃, 페인팅, 위치 지정, 크기 조절 등을 담당하는 여러 위젯이 결합된 **Convenience widget**이다.

레이아웃 측면에서 Container는 위젯에 **패딩(padding)**과 **마진(margin)**을 추가하는 데 사용한다. 같은 효과를 내기 위해 Padding 위젯을 사용할 수도 있다.

다음 예제는 Container를 사용한 경우이다.

```dart
Widget build(BuildContext context) {
  return Container(
    padding: EdgeInsets.all(16.0),
    child: BorderedImage(),
  );
}
```

다음 그림은 패딩이 없는 위젯과 패딩이 적용된 위젯을 비교한 예시이다.

![](https://i.imgur.com/rFgocFo.png)

여러 위젯을 조합해 더 복잡한 레이아웃도 구성할 수 있다:

```dart
Widget build(BuildContext context) {
  return Center(
    child: Container(
      padding: EdgeInsets.all(16.0),
      child: BorderedImage(),
    ),
  );
}
```

<br><br>
---

## 수평/수직으로 여러 위젯 배치하기
가장 흔한 레이아웃 패턴은 위젯을 **수직 또는 수평으로 배치하는 것**이다.
- Row : 위젯을 **수평으로 나열** (Horizontal)
- Column : 위젯을 **수직으로 나열** (Vertical)

아래 코드는 Row를 사용해 3개의 위젯을 수평으로 나열한 예시이다.

```dart
Widget build(BuildContext context) {
  return Row(
    children: [
      BorderedImage(),
      BorderedImage(),
      BorderedImage(),
    ],
  );
}
```

![](https://i.imgur.com/99qhO6B.png)

라벨을 함께 추가하려면 `Column`을 중첩한다:

```dart
Widget build(BuildContext context) {
  return Row(
    children: [
      Column(
        children: [
          BorderedImage(),
          Text('Dash 1'),
        ],
      ),
      // ... 반복
    ],
  );
}
```

![](https://i.imgur.com/oaufh3b.png)

<br><br>
---

## **Row와 Column 안에서 위젯 정렬하기**

각 위젯 너비가 **200픽셀**이고, 뷰포트 너비가 **700픽셀**일 때, 위젯들은 **왼쪽에 차례로 정렬**되고 남는 공간은 오른쪽에 빈 채로 남는다.

`mainAxisAlignment`, `crossAxisAlignment`를 사용해 정렬한다:

![](https://i.imgur.com/tYyMW3F.png)

Row와 Column 위젯에서 자식 위젯 정렬은 다음과 같다.

- Row
    - **main axis(주축)** → **수평 방향 (가로)**
    - **cross axis(교차축)** → **수직 방향 (세로)**
- Column
    - **main axis(주축)** → **수직 방향 (세로)**
    - **cross axis(교차축)** → **수평 방향 (가로)**

두 속성 조합으로 다양한 정렬 방식 구현 가능하다.

![](https://i.imgur.com/klyLXjm.png)

`mainAxisAlignment`를 `spaceEvenly`로 설정하면, 각 이미지 사이뿐 아니라 시작과 끝에도 동일한 간격으로 수평 여백이 분배된다.

```dart
Widget build(BuildContext context) {
  return Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    children: [
      BorderedImage(),
      BorderedImage(),
      BorderedImage(),
    ],
  );
}
```

![](https://i.imgur.com/WdfgcUn.png)

세 개의 이미지가 세로로 쌓이고 각 이미지 높이가 100픽셀이며, 렌더 박스 높이가 300픽셀보다 크면, `mainAxisAlignment`를 `spaceEvenly`로 설정할 경우 남는 세로 공간이 각 이미지 사이와 맨 위, 맨 아래에 균등하게 분배된다.

![](https://i.imgur.com/emGNXNN.png)

<br><br>
---

## **Row와 Column 안에서 위젯 크기 조절하기**

레이아웃 크기가 기기 화면보다 클 경우, 끝에 **노란색과 검정색 줄무늬 경고 표시**가 나타난다.

예시:
- 뷰포트 너비가 **400픽셀**
- 각 자식 위젯 너비가 **150픽셀**씩
- 총 450픽셀 공간 필요하지만 400픽셀밖에 없어 레이아웃 오버플로우 발생

![](https://i.imgur.com/Qad9g4s.png)

Row나 Column 안에서 위젯 크기를 자동 조절하려면 `Expanded` 위젯을 사용한다.

이미지들의 가로 길이 합이 렌더 박스를 초과하면, 각 이미지를 `Expanded`로 감싸면 가용 공간 안에서 균등 분배된다.

즉, `Expanded` 사용 시 자식 위젯들이 남는 공간을 나누어 가지며 레이아웃 오버플로우를 방지한다.

```dart
Widget build(BuildContext context) {
  return const Row(
    children: [
      Expanded(
        child: BorderedImage(width: 150, height: 150),
      ),
      Expanded(
        child: BorderedImage(width: 150, height: 150),
      ),
      Expanded(
        child: BorderedImage(width: 150, height: 150),
      ),
    ],
  );
}
```

![](https://i.imgur.com/Aolthgx.png)

`Expanded`는 자식 위젯이 차지할 공간 비율도 조절한다.

예를 들어, 어떤 위젯이 형제 위젯보다 2배 넓게 공간을 차지하려면 `Expanded`의 `flex` 속성을 사용한다.

- `flex`는 정수형이며 위젯이 차지할 비율(가중치) 의미
- 기본값은 1
- 아래 예제는 가운데 이미지의 `flex` 값을 2로 설정해 양옆 이미지보다 2배 넓은 공간 차지

```dart
Widget build(BuildContext context) {
  return const Row(
    children: [
      Expanded(
        child: BorderedImage(width: 150, height: 150),
      ),
      Expanded(
        flex: 2,
        child: BorderedImage(width: 150, height: 150),
      ),
      Expanded(
        child: BorderedImage(width: 150, height: 150),
      ),
    ],
  );
}
```

![](https://i.imgur.com/YWdGuMd.png)

<br><br>
---

## 📦 DevTools와 레이아웃 디버깅 – Unbounded Constraints

Flutter에서 자주 발생하는 레이아웃 오류 중 하나는 **“Unbounded Constraints”** 즉, 무한 제약 오류이다.

- 무한 제약 오류는 부모로부터 크기 제한 없이 무한한 공간(double.infinity)을 허용받았을 때 발생한다.

예시:
- `maxWidth` 또는 `maxHeight`가 무한대로 설정된 경우
- 자식 위젯이 가능한 한 크게 커지려 할 때 기준이 없어 Flutter가 배치 방법을 몰라 예외 발생

### 주로 발생하는 상황

1. Row나 Column 안에서
2. ListView, SingleChildScrollView 등 스크롤 가능한 영역 안에서
3. 스크롤 방향이 중첩된 경우
    - 예: 가로 스크롤 안에 세로 ListView 구조
    - 내부 리스트가 자신을 가능한 한 크게 키우려고 시도하나 가로 영역은 무한대라 오류 발생

초보자가 가장 자주 마주치는 에러이며 반드시 이해해야 한다.

### 해결 방법

- ListView나 Column 등 크기 무한한 위젯 사용 시
- 자식 위젯에 Expanded, Flexible, SizedBox 등으로 명확한 높이/너비 지정 필요

#### 참고 자료
- [Decoding Flutter: Unbounded height and width](https://youtu.be/jckqXR5CrPI)

> 🛠️ Widget Inspector  
> Flutter는 다양한 DevTools 도구를 제공하며, 그중 “Widget Inspector”는 레이아웃 디버깅에 매우 유용하다.

<br><br>
---

## 스크롤 가능한 위젯들

Flutter에는 자동 스크롤 가능한 내장 위젯들이 많고, 스크롤 동작을 직접 커스터마이즈할 수 있는 위젯도 제공한다.

### ListView

ListView는 Column과 유사하며, 콘텐츠가 RenderBox보다 길 경우 자동으로 스크롤 기능을 제공한다.

ListView 기본 사용법은 Column이나 Row와 유사하나, 자식 위젯이 교차 축(cross axis)의 모든 공간을 차지해야 한다는 제약이 있다.

아래 예제는 ListView 기본 사용 예시이다.

```dart
Widget build(BuildContext context) {
  return ListView(
    children: [
      BorderedImage(),
      BorderedImage(),
      BorderedImage(),
    ],
  );
}
```

![](https://i.imgur.com/aALykgS.png)

<br>

ListView는 리스트 항목이 많거나 무한할 수 있는 경우에 자주 사용한다.

이럴 때는 **ListView.builder()**를 사용한다.  
builder 생성자는 화면에 보이는 항목만 동적으로 렌더링해 성능상 유리하며 큰 데이터셋 처리에 적합하다.

아래 예제는 ListView로 할 일 목록(To-do items)을 표시한다.  
할 일 항목은 외부 repository에서 가져오며, 리스트 길이는 미리 정해져 있지 않다.

```dart
final List<ToDo> items = Repository.fetchTodos();

Widget build(BuildContext context) {
  return ListView.builder(
    itemCount: items.length,
    itemBuilder: (context, idx) {
      var item = items[idx];
      return Padding(
        padding: const EdgeInsets.all(8.0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(item.description),
            Text(item.isComplete),
          ],
        ),
      );
    },
  );
}
```

![](https://i.imgur.com/6OPddDl.png)

<br><br>

### Adaptive Layouts  반응형 레이아웃

Flutter는 모바일, 태블릿, 데스크톱, 웹 앱까지 다양한 플랫폼에서 사용되므로, 화면 크기나 입력 방식에 따라 다르게 동작하도록 조정해야 할 때가 많다.

이 작업을 **adaptive(적응형)** 또는 **responsive(반응형)** 디자인이라 한다.

`LayoutBuilder`는 적응형 레이아웃 구현에 유용한 위젯이다.

> 참고로 LayoutBuilder는 Flutter의 “builder 패턴”을 따르는 위젯 중 하나이다.  
> (예: ListView.builder, FutureBuilder 등)

<br><br>
---

### 📐 Builder 패턴

Flutter에서 이름에 "builder"가 포함된 위젯이나 생성자를 자주 사용한다. 대표적인 예시는 다음과 같다:

- ListView.builder
- GridView.builder
- Builder
- LayoutBuilder
- FutureBuilder

이들 “builder”는 각각 다른 문제를 해결하기 위해 사용한다.

- ListView.builder는 리스트 항목을 지연 렌더링(lazy rendering)하는 데 사용한다.
- Builder 위젯은 깊은 위젯 트리에서 BuildContext 접근을 돕는다.

동작 방식은 유사하다.

- 모든 Builder 위젯이나 생성자는 공통적으로 `builder`라는 매개변수를 가진다 (또는 `itemBuilder`처럼 비슷한 형태).
- `builder` 매개변수는 콜백 함수를 인자로 받으며, 함수가 실제 위젯을 반환한다.
- 콜백 함수는 일반적으로 `BuildContext`와 추가 매개변수(예: index, constraints 등)를 인자로 받는다.

예를 들어, `LayoutBuilder`는 화면 크기(BoxConstraints)에 따라 다른 위젯을 반환한다.

builder 콜백은 부모 위젯으로부터 전달받은 `BoxConstraints`와 `BuildContext`를 인자로 받아 현재 뷰포트 가용 공간에 따라 적절한 위젯을 반환한다.

즉, Builder 패턴은 UI를 유동적으로 구성하고 최적화된 렌더링 구현에 핵심 기법이다.

[참고영상 : LayoutBuilder (Flutter Widget of the Week)](https://www.youtube.com/watch?v=IYDVcriKjsw&t=3s)

다음 예제는 `LayoutBuilder`가 뷰포트 너비가 600픽셀 이하인지 초과인지에 따라 다른 위젯을 반환한다.

- 600픽셀 이하일 때는 모바일용 위젯 반환
- 600픽셀 초과일 때는 데스크톱용 위젯 반환

```dart
Widget build(BuildContext context) {
  return LayoutBuilder(
    builder: (BuildContext context, BoxConstraints constraints) {
      if (constraints.maxWidth <= 600) {
        return _MobileLayout();
      } else {
        return _DesktopLayout();
      }
    },
  );
}
```

![](https://i.imgur.com/dzNrXg8.png)

<br><br>

한편, `ListView.builder` 생성자의 `itemBuilder` 콜백은 `BuildContext`와 `int` 타입 인덱스(`index`)를 인자로 받는다.

이 콜백 함수는 리스트 각 항목마다 한 번씩 호출되며, 전달되는 `int` 값은 해당 항목 인덱스 번호를 의미한다.

- 첫 호출: 0
- 두 번째 호출: 1
- 세 번째 호출: 2
- ...

---

이 방식으로 리스트 항목 위치(index)에 따라 특정 UI나 설정을 제공할 수 있다.

앞서 본 `ListView.builder` 예제도 이 방식으로 각 항목을 동적으로 구성한다.

```dart
final List<ToDo> items = Repository.fetchTodos();

Widget build(BuildContext context) {
  return ListView.builder(
    itemCount: items.length,
    itemBuilder: (context, idx) {
      var item = items[idx];
      return Padding(
        padding: const EdgeInsets.all(8.0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(item.description),
            Text(item.isComplete),
          ],
        ),
      );
    },
  );
}
```

이 예제는 builder 함수에 전달된 index를 사용해 todo 항목 리스트에서 해당 인덱스의 항목을 가져와 데이터를 위젯에 표시한다.

다음 예제는 리스트 짝수 항목마다 배경색을 변경해 보여준다.

```dart
final List<ToDo> items = Repository.fetchTodos();

Widget build(BuildContext context) {
  return ListView.builder(
    itemCount: items.length,
    itemBuilder: (context, idx) {
      var item = items[idx];
      return Container(
        color: idx % 2 == 0 ? Colors.lightBlue : Colors.transparent,
        padding: const EdgeInsets.all(8.0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(item.description),
            Text(item.isComplete),
          ],
        ),
      );
    },
  );
}
```

## HISTORY
- 250612: 초안작성
