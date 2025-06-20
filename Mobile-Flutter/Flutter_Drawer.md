# Flutter - Drawer : GNB / 사이드바

보통 앱에서는 햄버거 버튼이라 부르는 석삼자 모양 버튼을 누르면 사이드바가 나타난다.

Flutter에서는 Drawer라고 부르는 Widget을 통해 만들 수 있다.

만드는 방법은 단순하게 아래와 같은 방법으로 선언할 수 있다.

## Drawer 카테고리

```
Drawer
- ListView
-- UserAccountDrawerHeader
   - currentAccountPicture
   - accountName
   - accountEmail
   - onDetailsPressed
   - decoration
   - otherAccountPictures
-- ListTile
   - Icon
   - Text
   - onTop
```


### 선언
```dart
drawer: Drawer()


class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Drawer')),
      body: Center(child: Text('My Page!')),
      // 이부분
      drawer: Drawer(),
    );
  }
}

```
### 적용화면
https://user-images.githubusercontent.com/76529148/233841435-87890310-731b-47df-a44b-c4f92fe4dbca.mov


## ListView
보통은 여기에 ListView위젯을 선언한다. 그리고 ListView의 헤더에 원하는 UI를 세팅한다.

### ListView위치

```dart
class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Drawer')),
      body: Center(child: Text('My Page!')),
      // 이부분
      drawer: Drawer(
      //예시
        child: ListView(...),
      )
      
    );
  }
}

```

### 통상적인 구조
보통은 Drawer의 children에 원하는 Widget들을 배열안에 담아서 세팅한다.
```
drawer: Drawer(
    child: ListView(
    padding: EdgeInsets.zero,
    children: <Widget>[
      UserAccountsDrawerHeader(
        currentAccountPicture: CircleAvatar(
          // 현재 계정 이미지 set
          backgroundImage: Icons('assets/profile.png'),
          backgroundColor: Colors.white,
        ),
        otherAccountsPictures: <Widget>[
          //  이미지 서클 set
          CircleAvatar(
            backgroundColor: Colors.white,
            backgroundImage: AssetImage('assets/profile2.png'),
          ),
          // CircleAvatar(
          //   backgroundColor: Colors.white,
          //   backgroundImage: AssetImage('assets/profile2.png'),
          // )
        ],
        accountName: Text('isGeekCode'),
        accountEmail: Text('bang.hyeonseok.dev@gmail.com'),
        onDetailsPressed: () {
          print('arrow is clicked');
        },
        decoration: BoxDecoration(
            color: Colors.red[200],
            borderRadius: BorderRadius.only(
                bottomLeft: Radius.circular(40.0),
                bottomRight: Radius.circular(40.0))),
      ),
      ListTile(
        leading: Icon(
          Icons.home,
          color: Colors.grey[850],
        ),
        title: Text('Home'),
        onTap: () {
          print('Home is clicked');
        },
        trailing: Icon(Icons.add),
      ),
      ListTile(
        leading: Icon(
          Icons.settings,
          color: Colors.grey[850],
        ),
        title: Text('Setting'),
        onTap: () {
          print('Setting is clicked');
        },
        trailing: Icon(Icons.add),
      ),
    ] // Widget
  ), // ListView
)// Drawer
```


