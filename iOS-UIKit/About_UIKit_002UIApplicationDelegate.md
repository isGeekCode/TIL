# [Apple Document] - AppDelegate, UIApplicationDelegate

- [Apple Document : delegate 변수](https://developer.apple.com/documentation/uikit/uiapplication/1622936-delegate)
- [Apple Document : UIApplicationDelegate 프로토콜](https://developer.apple.com/documentation/uikit/uiapplicationdelegate)

<br><br>

AppDelegate에 대하여 알려면 일단 AppDelegate.swift의 내용을 살펴보자.


## iOS13 이전의 AppDelegate

먼저 iOS13 이전의 구조를 알아보고 현재 구조를 알아보자.  
이해를 위해서는 먼저 이 부분부터 파악하는 것이 좋다.  

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow? // iOS13부터 SceneDelegate로 이동
}
```

AppDelegate.swift파일은 아래 두가지 기능을 한다.

- 파일 상단의 @main에 의해 UIApplicationMain(::::)를 실행시킨다.
- AppDelegate 클래스를 정의한다. -> Application의 delegate

<br>

좀더 자세한 설명을 하자면    
- 파일 상단의 @main에 의해 UIApplicationMain(::::)를 실행시킨다.
    - 이 메서드는 UIApplication 싱글턴 객체와 delegate객체를 생성한다.
        - 생성된 UIApplication 객체는 Run Loop를 생성하고 관리한다.
        - Run Loop에 대한 정보는 AppDelegate로 전송한다.
- AppDelegate 클래스를 정의한다 -> Application의 delegate
    - 앱의 Content를 그린다.
    - 앱의 상태변화에 따라 반응하는 window를 만든다.


<br><br>

AppDelegate 클래스는 프로젝트를 생성하면 자동으로 생성된다.  

특별한 경우가 아니면 이미 생성되어있는 이 클래스를 사용한다. 

이 AppDelegate클래스는 UIResponder를 상속하고 있고, UIApplicationDelegate 프로토콜을 채택하고 있다.

UIResponder에 대한 설명은 아래 링크를 참고하자.
- [TIL : UIResponder와 Responder Chain](https://github.com/isGeekCode/TIL/blob/main/iOS-UIKit/NSObject_UIResponder_.md)

<br><br><br>


### window

AppDelegate는 window라는 하나의 프로퍼티를 포함하고 있다.  
이 window는  App의 window의 reference를 저장한다. 이 window는  앱의 Root이며 여기서 앱의 모든 contents가 그려진다.   
window가 optional타입인 것을 보면, 경우에 따라 화면이 비어있을 수도 있다는 것을 보여준다.  

<br><br><br>

## Apple Document

### var delegate
delegate는 아래와 같이 선언되어있다.
```swift
unowned(unsafe) var delegate: UIApplicationDelegate? { get set }

```
모든 앱에는 앱관련 메세지에 응답하기위한 앱대리자 개체가 있어야한다.

예를 들어, 앱실행이 완료되고 포그라운드 또는 백그라운드 실행상태가 변경될 때, 이 대리자에게 알려준다.  

마찬가지로 시스템에서 오는 앱관련 메세지는 종종 처리를 위해서 이 AppDelegate로 라우팅된다. 

반드시 UIApplicationDelegate를 채택해야한다. 

<br><br>

### UIApplicationDelegate 프로토콜

```swift
@MainActor
protocol UIApplicationDelegate
```

<br>

AppDelegate는 앱에 공유된 동작을 관리한다. 이 객체는 사실상 앱의 Root 객체이고, 시스템광의 상호작용을 관리하기 위해 작동한다. 
UIKit은 App의 실행 사이클 초반에 UIApplication객체와 AppDelegate를 생성한다.

 
AppDelegate객체를 이용하여 아래 작업을 처리한다. 

- 앱의 중앙 데이터 구조 초기화
- 앱의 장면 구성
- 메모리 부족 경고, 다운로드 완료 알림 등 앱 외부에서 발생하는 알림에 응답
- 앱 자체를 대상으로 하고 앱의 장면, 보기 또는 보기 컨트롤러에 특정하지 않은 이벤트에 응답
- Apple 푸시 알림 서비스와 같은 시작 시 필요한 서비스에 등록

<br><br>


## App's Life-cycle : 앱의 생명주기

AppDelegate는 아래와 같은 delegate 메서드를 갖고있다.

```SWIFT
// 앱이 처음 시작될 때 실행
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool

// 앱이 active -> inactive 상태로 변할 때 실행
func applicationWillResignActive(_ application: UIApplication)

// 앱이 background 상태로 들어가고 나면 실행
func applicationDidEnterBackground(_ application: UIApplication)

// 앱이 background -> foreground 로 변할 때 실행
func applicationWillEnterForeground(_ application: UIApplication)

// 앱이 active 상태가 되고나면 실행
func applicationDidBecomeActive(_ application: UIApplication)

// 앱이 종료될 때 실행
func applicationWillTerminate(_ application: UIApplication)
```

자세한 내용은 아래 링크를 참고하자.

- [Apple Document: App's Life-Cycle : 앱의 생명주기](https://github.com/isGeekCode/TIL/blob/main/iOS-UIKit/About_UIKit_003AppLifeCycle.md)

<br><br><br>

## iOS13이후의 AppDelegate

위에서 보여준 수명 주기에 관련된 메서드는 모두 SceneDelegate로 이동하게 된다.  

Scene이라는 개념이 등장하면서 SceneDelegate라는 객체가 생성되었다.   

Scene기반 처리를 SceneDelegate에서 처리하기 때문에 

iOS13이상에서부턴 Scene에 대한 이해도가 있어야한다. 

한편, AppDelegate는 앱의 생명주기에 대한 부담을 덜어 경량화 되었다.


<br><br>

## History
- 230809 : 초안작성
