# Basics - Scaffold, AppBar

<img src="https://i.imgur.com/0NEWWhg.png" width="500" />

<br>

## 🗂️ Widget Catalog Index

```
├ Basics  
│   └ ✅ Scaffold ← 현재 문서  
├ Layout  
├ Text  
├ Input  
...
└ Accessibility  
```

<br>

## Scaffold 전체 구조 설명

Scaffold는 앱 전체 레이아웃의 뼈대를 제공하는 Material 위젯이다. 

주요 구성요소는 appBar, body, floatingActionButton, bottomNavigationBar, drawer, bottomSheet 등이며, 각각 속성으로 지정한다.

**참고:** Scaffold의 세부 위젯들은 별도의 문서로 다룰 예정.

- 각 부분의 명칭  
<img src="https://i.imgur.com/2VeTzUX.png" width="500" />

- 동작  
<img src="https://i.imgur.com/zeqpAI7.png" width="300" />
  

<br><br>  
  
- **AppBar**  
앱 상단에 위치하는 머리말 영역으로, 제목, 탐색 버튼, 액션 버튼 등을 포함한다. Scaffold의 `appBar` 속성에 전달되어 화면 최상단에 고정된다.   

AppBar는 자동으로 SafeArea 처리를 하며, Drawer가 있으면 자동으로 햄버거 메뉴 버튼을 표시하고, 이전 라우트가 있으면 뒤로가기 버튼을 자동으로 추가한다.    

필요시 `automaticallyImplyLeading: false`로 이 동작을 막을 수 있다.   

필요시 TabBar를 추가할 수 있다.  이 탭바는 주로 안드로이드에서 사용하며, 해당 페이지의 세부 카테고리를 표현할 때 사용한다.  


- **Body**  
콘텐츠 영역.  
기본적으로 키보드에 의해 리사이징된다.  
필요 시 resizeToAvoidBottomInset 제어.  
SafeArea로 노치 영역 회피 가능.  
  
- **FloatingActionButton (FAB)**   
화면에 떠 있는 액션 버튼으로, `floatingActionButton` 속성에 전달된다.    
위치는 `floatingActionButtonLocation`으로 조정할 수 있다.    
FAB와 BottomAppBar가 함께 있을 때는 FAB notch가 표현되고, BottomSheet가 화면의 70% 이상을 덮으면 FAB이 점점 작아지며 사라지는 애니메이션 효과가 나타난다.
  
- **BottomNavigationBar 및 BottomAppBar**  
화면 하단에 배치되는 네비게이션 바 또는 커스텀 바.  
BottomAppBar는 FAB notch를 표현할 수 있고, 자유롭게 버튼, 아이콘, 텍스트 등을 배치할 수 있다.    
`shape` 속성으로 FAB notch 모양을 지정하며, `floatingActionButtonLocation`과 위치를 맞춰줘야 한다.

- **Drawer**   
화면 좌측에서 슬라이드하여 나타나는 내비게이션 메뉴.  
ScaffoldState로 제어.  

- **BottomSheet**  
  하단에서 나타나는 시트. bottomSheet 속성 또는 ScaffoldState로 제어.
  
  
---

## ⚠️ 사용 시 유의사항

- **ScaffoldState 활용**  
  Drawer, BottomSheet 열기 위해 ScaffoldState 사용. GlobalKey 또는 Scaffold.of(context) 활용.
  
    
- **중첩된 Scaffold 지양하기**  
  하나의 화면에 Scaffold는 하나만 사용. TabBarView 등에서는 공유 구조 권장.  
  
  
- **SafeArea 적극 활용하기**  
  body에 SafeArea 직접 사용해야 노치 대응됨.  
  
<br><br>
---



## 🧪 Sample Code

- Scaffold 기본 구조 예제


```dart
Scaffold(
  appBar: AppBar(
    title: Text('Scaffold Example'),
  ),
  body: Center(
    child: Text('Hello Scaffold'),
  ),
  floatingActionButton: FloatingActionButton(
    onPressed: () {},
    child: Icon(Icons.add),
  ),
  bottomNavigationBar: BottomAppBar(
    child: Container(height: 50),
  ),
);
```

- TabBar + BottomAppBar + FAB 조합 예제. 상단 탭과 하단 바, FAB 위치 조정까지 포함.


```dart
import 'package:flutter/material.dart';

void main () {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: DefaultTabController( // ✅ 탭 컨트롤러 추가
        length: 3, // 탭 개수 지정
        child: MainScreen(),
      ),
    );
  }
}

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Tab Example'),
        bottom: TabBar( // ✅ AppBar 아래 탭 추가
          tabs: [
            Tab(icon: Icon(Icons.home), text: 'Home'),
            Tab(icon: Icon(Icons.star), text: 'Favorites'),
            Tab(icon: Icon(Icons.person), text: 'Profile'),
          ],
        ),
      ),
      body: TabBarView( // ✅ 탭 뷰 연결
        children: [
          Center(child: Text('Home Screen')),
          Center(child: Text('Favorites Screen')),
          Center(child: Text('Profile Screen')),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          print('FAB pressed');
        },
        child: Icon(Icons.add),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
      bottomNavigationBar: BottomAppBar(
        shape: CircularNotchedRectangle(),
        notchMargin: 6.0,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            IconButton(icon: Icon(Icons.home), onPressed: () {}),
            SizedBox(width: 48), // FAB 공간 확보
            IconButton(icon: Icon(Icons.settings), onPressed: () {}),
          ],
        ),
      ),
    );
  }
}
```


---

## History
- 250714 : 초안 작성
