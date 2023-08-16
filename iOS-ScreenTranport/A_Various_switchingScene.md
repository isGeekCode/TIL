# 정리 : iOS에서의 화면관리 및 전환

iOS를 하게 되면 가장 처음엔 하나의 화면으로만 앱을 만들지만 상황에 따라 여러 개의 화면이 필요해진다. 

이 때, 화면을 전환하기 위해 여러가지 방법을 사용할 수 있는데, 

다양한 방법으로 화면을 구성하고 관리할 수 있다.

사용할 수 있는 방법은 아래와 같다.

- NavigationController를 이용한 화면이동
- TabBarController를 이용한 화면이동
- Segue를 이용한 화면이동
- Code Programming : Present ViewController
- Code Programming : PopOver ViewController
- Code Programming : ViewController Container 사용하기
- SwiftUI에서의 화면이동

또한 아래와 같은 아키텍처를 통해 화면을 관리할 수도 있다.

- MVC패턴
- MVVM패턴
- VIPER패턴
- RIBs 패턴

아래는 관련 정리 링크들이다. 

## UIKit 기반의 화면 전환 방식
- [TIL : 기본적인 iOS앱의 계층구조](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/UIApplication_AppDelegate_AppLifeCycle.md)

### NavigationController를 이용한 화면이동
- [TIL : NavigationController는 Container ViewController 타입이다.](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/Container_ViewController_NavigationController.md)
- [TIL : 화면전환 - UINavigationController 이해하기](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/navigationController.md)
- [TIL : NSObject_UIBarItem: 네비게이션바, 툴바, 탭바를 표시하는 아이템](https://github.com/isGeekCode/TIL/blob/main/iOS-UIKit/NSObject_UIBarItem.md)
- [TIL : WebView - 네비게이션컨트롤러 목록으로 웹뷰 관리하는 방법](https://github.com/isGeekCode/TIL/blob/main/iOS-Networking/WebView_catchNavigation.md)


### TabBarController를 이용한 화면이동

- [TIL : 화면전환 - UITabBarController 이해하기](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/tabbarController.md)
- [TIL : NSObject_UIResponder_UIView_UITabBar](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/NSObject_UIResponder_UIView_UITabBar.md)


### Segue를 이용한 화면이동
- [TIL : Segue를 이용한 화면이동](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/segue.md)

### Code Programming : Present ViewController
### Code Programming : PopOver ViewController
### Code Programming : ViewController Container 사용하기


## SwiftUI 기반의 화면 전환 방식
### TabView를 이요한 화면이동
- [TIL : Layout - SwiftUI: TabView](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-SwiftUI/Layout_SwiftUI_TabView.md)


## 아키텍쳐를 이용한 방법

### MVC패턴
### MVVM패턴
### VIPER패턴
### RIBs 패턴


# History
- 230725: 초안작성
- 230801: 폴더 변경으로 인한 문서 링크 수정
