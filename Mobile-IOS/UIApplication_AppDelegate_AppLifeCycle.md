# UIApplication - 탭바컨트롤러 / 네비게이션컨트롤러 / 기본적인 ios 앱의 계층구조

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
