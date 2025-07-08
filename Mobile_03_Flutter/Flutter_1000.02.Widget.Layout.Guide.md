## Flutter 개요 - 레이아웃의 이해

  
Flutter의 레이아웃 메커니즘의 핵심은 위젯입니다. Flutter에서는 거의 모든 것이 위젯입니다 — 레이아웃 모델조차도 위젯입니다. Flutter 앱에서 볼 수 있는 이미지, 아이콘, 텍스트는 물론이고, 행(Row), 열(Column), 그리드(Grid)처럼 보이지 않는 위젯들 또한 전부 위젯입니다.


복잡한 레이아웃은 간단한 위젯들을 조합하여 구성할 수 있습니다. 예를 들어, 3개의 아이콘 아래에 각각 라벨이 있는 구조는 `Row` 안에 3개의 `Column`을 넣고, 각 `Column`에 `Icon`과 `Text`를 배치하여 구성할 수 있습니다.

![|700](https://i.imgur.com/wR7YMIS.png)

<br>
<br>

---


## Constraints
`제약조건`

Flutter에서 레이아웃을 이해하려면 제약 조건의 개념을 이해해야 합니다.
  
- **위젯은 부모로부터 제약 조건을 받습니다.**
- **제약 조건은 총 4개의 Double로 구성됩니다.  최소/최대 너비와 최소/최대 높이.**
- **위젯은 받은 제약 조건 범위 안에서 자신이 사용할 크기를 정하고, 그 크기를 부모에게 알려줍니다**
- **부모는 자식이 원하는 크기를 보고, 정렬(Alignment)에 따라 위치를 결정합니다.** 
    -  **정렬은 Center, Row, Column 등의 위젯이나 그 안의 alignment 속성을 이용해 명시적으로 설정할 수 있어요.**
      
이 과정을 요약하면 다음과 같습니다:
> **부모가 자식에게 “이 정도 크기에서 그려봐”라고 제약을 주면,   
>  자식은 그 안에서 크기를 결정하고 부모에게 알려줘요.   
>  그리고 부모는 그 크기를 기반으로 자식을 어디에 위치시킬지 정합니다.**  


이걸 한문장으로 요약하면

- `Constraints go down. Sizes go up. Parent sets the position`
> "제약은 아래로, 크기는 위로, 위치는 부모가 설정한다."

<br><br>

---

## Box Types
`박스유형`

Flutter에서 위젯은 `RenderBox` 객체에 의해 렌더링됩니다. 이 객체는 제약 조건을 처리하는 방식을 결정합니다.
일반적으로 세 가지 유형의 박스가 있습니다:

1. `가능한 한 크게 확장`하려는 박스: `Center`, `ListView`
2. `자식과 같은 크기`를 유지하려는 박스: `Transform`, `Opacity`
3. `특정 크기`를 가지려는 박스: `Image`, `Text`


  

예를 들어, `Container`는 전달된 인자에 따라 다른 방식으로 동작합니다. 아무 값도 지정하지 않으면 가능한 한 크게 렌더링되고, `width` 등을 지정하면 해당 크기를 따릅니다.

  

## Layout a single widget
`단일 위젯 레이아웃`
  
 `Text`나 `Image` 와 같은 visible widget(가시적 위젯)인 단일 위젯을 위치시키려면, `Center` 같은 position을 변경가능한 widget으로 감싸면 됩니다.

```dart
Widget build(BuildContext context) {
  return Center(
    child: BorderedImage(),
  );
}
```


다음 그림은 **왼쪽에 정렬되지 않은 위젯(왼쪽)**과 **가운데 정렬된 위젯(오른쪽)**을 보여줍니다.

  ![](https://i.imgur.com/bNOjRHe.png)

모든 레이아웃 위젯은 다음 중 하나의 속성을 가집니다:

- child 속성: 하나의 자식만 받을 수 있는 위젯에서 사용됩니다.
    예: Center, Container, Padding 등
- children 속성: 여러 개의 자식 위젯을 받을 수 있는 위젯에서 사용됩니다.
    예: Row, Column, ListView, Stack 등


## `Container` 예제

  Container는 레이아웃, 페인팅, 위치 지정, 크기 조절 등을 담당하는 여러 위젯이 결합된 **Convenience widget**(편의용 위젯)입니다.

레이아웃 측면에서 보면, Container는 위젯에 **패딩(padding)**과 **마진(margin)**을 추가하는 데 사용할 수 있습니다.
같은 효과를 내기 위해 Padding 위젯을 사용할 수도 있습니다.


다음 예제에서는 Container를 사용한 경우입니다.

```dart
Widget build(BuildContext context) {
  return Container(
    padding: EdgeInsets.all(16.0),
    child: BorderedImage(),
  );
}
```

  
다음 그림은 **왼쪽에는 패딩이 없는 위젯**, **오른쪽에는 패딩이 적용된 위젯**을 보여줍니다.

![](https://i.imgur.com/rFgocFo.png)


여러 위젯을 조합해서 더 복잡한 레이아웃도 가능합니다:

  

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
가장 흔하게 사용되는 레이아웃 패턴 중 하나는 위젯을 **수직 또는 수평으로 배치하는 것**입니다.
- Row : 위젯을 **수평으로 나열**   (Horizontal)
- Column : 위젯을 **수직으로 나열** (Vertical)



  이 페이지의 첫 번째 그림에서도 두 위젯 모두 사용되었어요.

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
  

라벨을 함께 추가하려면 `Column`을 중첩합니다:


```dart

Widget build(BuildContext context) {
  return Row(
    children: [

      // 첫번째 Column
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

다음 예제에서는 각 위젯의 너비가 **200픽셀**이고, 뷰포트(전체 화면 너비)는 **700픽셀**입니다.
따라서 위젯들은 **왼쪽에 차례로 정렬**되고, 남는 공간은 모두 **오른쪽에 빈 채로 남게 됩니다.**

`mainAxisAlignment`, `crossAxisAlignment`를 사용하여 정렬:

![](https://i.imgur.com/tYyMW3F.png)

Row나 Column 위젯에서 자식 위젯들이 어떻게 정렬될지를 조절하려면,
mainAxisAlignment와 crossAxisAlignment 속성을 사용하면 됩니다.

- Row에서는
    - **main axis(주축)** → **수평 방향 (가로)**
    - **cross axis(교차축)** → **수직 방향 (세로)**
        
- Column에서는
    - **main axis(주축)** → **수직 방향 (세로)**
    - **cross axis(교차축)** → **수평 방향 (가로)**
        
이 두 속성을 조합해 다양한 정렬 방식을 만들 수 있어요.

![](https://i.imgur.com/klyLXjm.png)

mainAxisAlignment을 spaceEvenly로 설정하면,
**각 이미지 사이뿐만 아니라 시작과 끝에도 동일한 간격**으로 **수평 여백**이 나뉘게 됩니다.
즉, 위젯들 사이의 간격뿐 아니라 **양 끝 여백도 포함해 전체적으로 균등하게 분배**되는 방식입니다.



```dart

Widget build(BuildContext context)
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

다음 예제에서는 세 개의 이미지가 세로로 쌓여 있고, 각 이미지는 **높이 100픽셀**입니다.
렌더 박스(여기서는 전체 화면)의 높이는 **300픽셀보다 크기 때문에**,
mainAxisAlignment를 spaceEvenly로 설정하면 

**남는 세로 공간이 각 이미지 사이뿐 아니라, 맨 위와 맨 아래에도 균등하게 나뉘게** 됩니다.

![](https://i.imgur.com/emGNXNN.png)




<br><br>
---



## **Row와 Column 안에서 위젯 크기 조절하기**

레이아웃의 크기가 **기기 화면보다 너무 클 경우**,
해당 영역의 끝에 **노란색과 검정색 줄무늬 경고 표시**가 나타납니다.


예를 들어 이 예제에서는:
- 뷰포트(화면 너비)가 **400픽셀**이고,
- 각 자식 위젯의 너비가 **150픽셀**씩이라서,
    
총 450픽셀 공간이 필요하지만, 400픽셀밖에 없기 때문에
**레이아웃이 넘치는 부분에 경고 패턴이 표시됩니다.**

  ![](https://i.imgur.com/Qad9g4s.png)


Row나 Column 안에서 위젯의 크기를 자동으로 조절하려면 Expanded 위젯을 사용할 수 있습니다.

앞선 예제처럼 이미지들의 가로 길이 합이 렌더 박스를 초과하는 경우,

각 이미지를 Expanded로 감싸면 **가용 공간 안에서 자동으로 균등 분배**되도록 조정됩니다.

즉, **Expanded를 사용하면 자식 위젯들이 남는 공간을 나누어 가지면서, 레이아웃 오버플로우(overflow)를 방지할 수 있습니다.**

  

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

Expanded 위젯은 **자식 위젯이 차지할 공간의 비율**도 조절할 수 있습니다.

예를 들어, 어떤 위젯이 **형제 위젯보다 2배 넓게** 공간을 차지하길 원한다면,
Expanded의 flex 속성을 활용하면 됩니다.

- flex는 **정수형 값**이며, 위젯이 차지할 비율(가중치)을 의미합니다.
- 기본값은 1이고,
- 아래 예제에서는 가운데 이미지의 flex 값을 2로 설정
    **양옆 이미지보다 2배 넓은 공간**을 차지하게 합니다:


```dart
Widget build(BuildContext context) {
  return const Row(
    children: [
      Expanded(
        child: BorderedImage(width: 150, height: 150),
      ),
      Expanded(
        flex: 2,  //!!!!
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

## 📦 DevTools와 레이아웃 디버깅 – Unbounded Constraints**
Flutter에서 가장 흔하게 마주치는 레이아웃 오류 중 하나는 **“Unbounded Constraints”**, 즉 **무한 제약 오류**입니다.

-  무한 제약 오류**부모로부터 크기 제한 없이 무한한 공간(double.infinity)**을 허용받았을 때 발생하는 문제예요.

예를 들어:
- **maxWidth 또는 maxHeight가 무한대로 설정된 경우**
    
- 자식 위젯이 **가능한 한 크게 커지려 할 때**,
    어떤 기준도 없으니 Flutter가 어떻게 배치해야 할지 몰라 **예외를 던지게 됩니다.**

### 🧱 주로 발생하는 상황

1. **Row나 Column 안에서**
2. **ListView, SingleChildScrollView 등 스크롤 가능한 영역 안에서**
3. **스크롤 방향이 중첩된 경우**
    - 예: 가로 스크롤 안에 세로 ListView를 넣는 구조
    - 내부 리스트가 자신을 가능한 한 크게 키우려고 시도 →
        하지만 가로 영역은 무한대 → 오류 발생
  
**Flutter를 처음 시작하는 사람에게 가장 흔한 에러이자, 반드시 이해하고 넘어가야 하는 에러입니다.**

### 🛠️ 해결 방법

- ListView나 Column 등 **크기 무한한 위젯**을 사용할 때는
    자식 위젯에 Expanded, Flexible, 또는 SizedBox를 적절히 사용해서
    **명확한 높이/너비를 지정**해 주세요.

#### **🎮 참고 자료**
- [Decoding Flutter: Unbounded height and width](https://youtu.be/jckqXR5CrPI) — Flutter 팀의 공식 영상도 추천



>  🛠️ Widget Inspector
> 
> Flutter는 다양한 **DevTools 도구 세트**를 제공하며,
> 그중에서도 **“Widget Inspector”**는 **레이아웃을 만들고 디버깅할 때 매우 유용한 도구**입니다.

<br><br>
---


## 스크롤 가능한 위젯들

Flutter에는 **자동 스크롤이 가능한 내장 위젯**들이 많고,
또한 다양하게 **스크롤 동작을 직접 커스터마이즈할 수 있는 위젯**들도 함께 제공합니다.


### ListView
ListView는 Column과 유사한 위젯으로,
그 콘텐츠가 RenderBox보다 길 경우 **자동으로 스크롤 기능을 제공합니다**.

ListView를 사용하는 가장 기본적인 방법은 Column이나 Row를 사용하는 방식과 매우 비슷합니다.
하지만 Column이나 Row와 달리, ListView는 **자식 위젯들이 교차 축(cross axis)의 모든 공간을 차지해야 한다는 제약**이 있습니다.

아래 예제는 그 점을 보여줍니다.

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

<br><br>

ListView는 **리스트 항목의 개수가 많거나(심지어 무한할 수 있는)** 경우에 자주 사용됩니다.

이럴 때는 **ListView.builder()** 를 사용하는 것이 가장 효율적입니다.
builder 생성자는 **화면에 보이는 항목만 동적으로 렌더링**하기 때문에

성능상 유리하고, 큰 데이터셋을 다룰 때에도 부담이 적습니다.

아래 예제에서는 ListView가 **할 일 목록(To-do items)** 을 표시합니다.
이 때 할 일 항목들은 외부의 repository에서 가져오기 때문에

**리스트의 길이가 미리 정해져 있지 않습니다.**

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

Flutter는 **모바일, 태블릿, 데스크톱, 웹 앱**까지 다양한 플랫폼에서 사용되기 때문에,
앱이 **화면 크기나 입력 방식**에 따라 **다르게 동작하도록 조정**해야 할 경우가 많습니다.

이런 작업을 **adaptive(적응형) 또는 responsive(반응형)** 디자인이라고 부릅니다.

그중 `LayoutBuilder`는 **적응형 레이아웃을 만들 때 매우 유용한 위젯**입니다.

> 참고로 LayoutBuilder는 Flutter의 “builder 패턴”을 따르는 위젯 중 하나입니다.
> (예: ListView.builder, FutureBuilder 등)


<br><br>
---

### 📐 Builder 패턴

Flutter에서는 이름에 "builder"가 들어간 위젯이나 생성자를 자주 보게 됩니다.
아래는 그런 대표적인 예시입니다 (완전한 목록은 아닙니다):
- ListView.builder
- GridView.builder
- Builder
- LayoutBuilder
- FutureBuilder


이러한 “builder”들은 각각 **다른 문제를 해결하기 위해 사용**됩니다.
- 예를 들어, ListView.builder는 리스트 항목들을 **지연 렌더링(lazy rendering)** 하는 데 주로 사용되고,
- Builder 위젯은 **깊은 위젯 트리에서 BuildContext에 접근**할 수 있도록 도와줍니다.
    
또한 위젯들의 **사용 목적은 달라도, 동작 방식은 유사**합니다.
- 모든 Builder 위젯이나 생성자는 공통적으로 **builder라는 이름의 매개변수**를 가집니다
    (또는 itemBuilder처럼 비슷한 형태).
- 이 builder 매개변수는 **콜백 함수를 인자로 받으며**, 이 함수가 **실제 위젯을 반환**합니다.
- 이 콜백 함수는 일반적으로 **BuildContext**와 그 외 매개변수(예: index, constraints 등)를 인자로 받습니다.
    


예를 들어,  

LayoutBuilder는 **화면의 크기(BoxConstraints)**에 따라 다른 위젯을 반환하도록 할 수 있습니다.

이 때 builder 콜백은 부모 위젯으로부터 전달받은 **BoxConstraints**와 **BuildContext**를 인자로 받아,

현재 뷰포트(viewport)의 가용 공간에 따라 **적절한 위젯을 반환**합니다.


즉, Builder 패턴은 **UI를 유동적으로 구성하고 최적화된 렌더링을 구현하는 핵심 기법**입니다.

[참고영상 : LayoutBuilder (Flutter Widget of the Week)](https://www.youtube.com/watch?v=IYDVcriKjsw&t=3s)


다음 예제에서는 LayoutBuilder가 반환하는 위젯이
**뷰포트(viewport)의 너비가 600픽셀 이하인지 초과인지에 따라 달라집니다.**

즉,
- **600픽셀 이하**인 경우에는 모바일에 적합한 위젯을,
- **600픽셀 초과**인 경우에는 데스크톱에 적합한 위젯을 보여주는 구조입니다.
    
이렇게 하면 화면 크기에 따라 **반응형 UI**를 쉽게 구현할 수 있습니다.

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


한편, ListView.builder 생성자의 itemBuilder 콜백은
**BuildContext와 int 타입의 인덱스(index)**를 인자로 받습니다.

이 콜백 함수는 **리스트의 각 항목마다 한 번씩 호출**되며,
그때 전달되는 int 값은 **해당 항목의 인덱스 번호**를 의미합니다.

  

예를 들어,
- 첫 번째 호출 때는 0,
- 두 번째 호출 때는 1,
- 세 번째는 2, …
    이런 식으로 순차적으로 호출됩니다.

---

이렇게 하면 **리스트 항목의 위치(index)** 에 따라 특정한 UI나 설정을 제공할 수 있습니다.

앞서 본 ListView.builder 예제에서도 바로 이런 방식으로
각 항목을 동적으로 구성했죠.

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

이 예제 코드는 builder 함수에 전달된 index를 사용하여
todo 항목 리스트 중 **해당 인덱스에 맞는 todo 항목을 가져옵니다.**

그 후, 그 todo의 데이터를 위젯에 표시하는 방식입니다.


이를 예시로 보여주기 위해,

다음 예제에서는 **리스트의 짝수 항목마다 배경색을 변경**해 보여줍니다.

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

