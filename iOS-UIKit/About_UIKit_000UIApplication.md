# [Apple Document] - UIApplication


## 참고링크
- [원문: UIApplication](https://developer.apple.com/documentation/uikit/uiapplication)

<br><br>

iOS앱이 실행될 때, 앱의 중앙에서 제어하기위한 지점이다.

```SWIFT
@available(iOS 2.0, *)
@MainActor open class UIApplication : UIResponder {
```

---

## Overview

모든 iOS앱에는 단 하나의 `UIApplication`이 있다. (혹은 매우 드물게 UIApplication의 subclass가 있을 때도 있다.)  

앱이 실행되면, 시스템은 `UIApplicationMain(_:_:_:_:)`메서드를 호출한다.  

이 메서드는 다른 작업을 수행하고 있을때에도 `shared`로 접근할 수 있는 싱글턴 `UIApplication` 객체를 만든다.  

<br>

`UIApplication`객체는 사용자 이벤트가 들어올 때, 초기 라우팅을 처리한다.  
  
Control 개체(`UIControl` 객체)에 의해 전달된 action message들을 적절한 대상 객체들에게 전달한다.
  
<br><br>

`UIApplication` 객체는 현재 열려있는 Window(UIWindows 객체)들의 목록을 유지하면서, 이를 이용해 앱의 `UIView` 객체들을 찾을 수 있다.  

<br><br>

`UIApplication`클래스는 UIApplicationDelegate 프로토콜을 준수하는 delegate(위임자)를 정의하고 있다. 그래서 프로토콜의 메서드 중 일부를 구현해야 한다.  
이 UIApplication 객체는 `앱을 시작하거나, low-memory 경고, 앱의 종료` 등 중요한 runtime 이벤트를 delegate(위임자)에게 알려서 적절한 응답을 할 수 있는 기회를 제공한다.  

<br><br>
`open(_:options:completionHandler)`메서드를 이용해 다른 앱과 협력하여 email이나 image파일같은 리소스를 처리할 수 있다.  
  
예를 들어, 이메일 URL과 이 메서드를 호출하면 메일앱이 실행되어 메세지를 보여줄 수가 있다.   

---

이 클래스의 API들을 사용해서 아래와 같이 장치별 동작을 관리할 수가 있다.

- 원격 알림 등록 : `registerForRemoteNotifications()`
- UI undo-redo 트리거 : `var applicationSupportsShakeToEdit: Bool`
    - 장치를 흔들면 실행취소-재실행 UI가 표시되는지 여부를 결정하는 Bool값
- URL Scheme을 처리하기 위해 등록된 앱이 있는지 확인 : `canOpenURL(_:)`
- 백그라운드에서 작업을 완료할 수 있도록 앱 실행 확장 :
    - `beginBackgroundTask(expirationHandler:)`
    - `beginBackgroundTask(withName:expirationHandler:)`
- remote-control 이벤트 수신 조정 : 
    - `beginReceivingRemoteControlEvents()`
    - `endReceivingRemoteControlEvents()`
  
<br><br><br>
  
### Subclassing Notes
대부분의 앱들은 UIApplication을 Subclass할 필요가 없다.   

> 대신 AppDelegate를 사용하여 시스템과 App 사이의 상호작용을 관리한다.  

매우 드문 경우이긴 하지만  

시스템이 수신된 이벤트를 처리하기 전에 앱에서 수신 이벤트를 처리해야하는 경우,  

custom event 나 action dispatching 메커니즘을 구현할 수 있다.  이를 수행하려면 UIApplication subclass를 만들고 sendEvent()와 sendAction(_:to:from:for:)를 override해야한다. 중간에 가로챈 이벤트를 다 처리하고 시스템이 다시 처리할 수 있도록 호출하자.
```swift
super.sendEvent(event)
```

이벤트를 가로채는 구현은 아주 아주 특수한 경우에 사용되니 가능하면 하지 말자.
  
<br><br><br>
  
  
## 관련 주제
- Accessing the shared application : shared application 접근하기
- Configuring your app’s behavior : 앱 동작 구성
- Registering for remote notifications : 원격 알림 등록
- Getting the application state : 앱 상태 가져오기
- Getting scene information : 씬 정보 가져오기
- Managing a scene’s life cycle : 씬 라이프사이클 관리
- Managing background tasks : 백그라운드 작업 관리
- Fetching content in the background : 백그라운드에서 콘텐츠 가져오기
- Opening a URL resource : URL 리소스 열기
- Deep linking to custom settings : 사용자 정의 설정으로 딥 링크
- Managing the app’s idle timer : 앱의 유휴 타이머 관리
- Managing state restoration : 상태 복원 관리
- Providing an app’s shortcut items : 앱의 바로 가기 항목 제공
- Accessing protected content : 보호된 콘텐츠 액세스
- Accessing the layout direction : 레이아웃 방향 액세스
- Controlling and handling events : 이벤트 제어 및 처리
- Managing the app’s icon : 앱 아이콘 관리
- Managing the preferred content size : 선호하는 콘텐츠 크기 관리
- Specifying the supported interface orientations : 지원하는 인터페이스 방향 지정
- Tracking controls in the run loop : 런 루프에서 컨트롤 추적
- Detecting screenshots : 스크린샷 감지


## History
- 230807 : 초안작성
