# UIApplication - App의 LifeCycle

- UIApplication: 애플리케이션의 라이프 사이클을 관리하는 싱글톤 클래스

화면을 터치하여 앱을 실행시키면 UIApplication이라는 클래스에  오프젝트 하나가 생긴다.
자신의 이벤트를 대행해줄  AppDelegate라는 오브젝트를 만든다.

AppDelegate라는 Object는 개발자가 직접 만들어가는 클래스이다. 
Application의 시동, 종료, Background,Foreground, in-active, active 상태로 다녀오는 것을 관리한다. 

가장먼저 하는 일은 window을 만드는 것이다.
iOS에서는 기본적으로 Single-window이다. 
`하나의 window가 앱 전체를 채우고 있고, 앱을 종료하면 window가 종료된다.`

App에서 사용하는 여러 data들은 AppDelegate가 관리한다. 이는 AppDelegate가 UIApplication으로 부터 앱의 시동과 종료등에 중요한 역할을 위임받고 있고, Singleton에 준하는 Object이기 때문이다. 

# About UI

## TabBar 
- TabBarController라는 객체가 관리한다.
- 화면아래에 탭바, 그 위쪽에는 빈공간이 생긴다. 
- 이 빈공간에 보여주고 싶은 화면을 보여주는 ViewController가 들어가게된다. 
- Window에 TabBarController가 관리하는 View로 채우게 한다. 
### TabBarController
각 탭에 하나씩 ViewController들이 묶인다.

## NavigationBar
일반적인 경우는 TabBar위의 공간을 NavigationController가 관리하는 View로 채운다.
- NavigationController라는 객체가 관리한다.
- 화면상단에 네비게이션바, 그 아래쪽은 빈공간이 생긴다. 
- 이 빈공간에 보여주고 싶은 화면을 보여주는 ViewController가 들어가게된다. 
- Window에 NavigationController가 관리하는 View로 채우게 한다.

### NavigationController
- 네비게이션 컨트롤러는 화면이 좌우로 전환되면서 데이터를 더 자세한 데이터를 넘나들 수 있도록 데이터의 계층을 오르내린다.
- 네비게이션 컨트롤러가 묶인 탭에서는 네비게이션이 된다. 

## TableViewController
업무용이라면 대부분 UITableView를 사용하게 된다. TableViewController는 화면에 UITableView만 존재하는 경우 사용한다.  TableViewController가 

## DetailViewController
TableView의 Cell을 클릭한다면 NavigationController의 빈공간에 내용물을 보여줄 ViewController로 채우게 된다.


# 기본적인 앱의 구조
탭과 네비게이션을 함께 가진 앱에서 탭은 아래처럼 항상 네비게이션의 상위에 있다.
```
─ UIApplication
  └─ AppDelegate
     ├── 앱시동에 필요한 Data 관리
     ├── 앱의 시동, 종료, Foreground, Background 등을 관리
     └── Window
         └── TabBarController
             ├── NavigationController
             │   └── HomeViewController
             │       └── DetailViewController
             ├── NavigationController
             │   └── TableViewController
             │       └── DetailViewController
             └── NavigationController
                 └── TableViewController
                     └── DetailViewController
```
