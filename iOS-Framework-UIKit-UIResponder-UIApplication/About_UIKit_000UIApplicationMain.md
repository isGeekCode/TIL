# [Apple Document] - UIApplicationMain(::::)


- [Apple Doc : UIApplicationMain(::::)](https://developer.apple.com/documentation/uikit/1622933-uiapplicationmain)

<br><br>

UIApplicationMain(::::)은 iOS앱이 시작되기위한 핵심적인 메서드이다.

이 메서드로 UIApplication 싱글턴 객체와 Delegate객체를 만들고, info.plist에서 필요한 nib 파일을 로드하고 메인 이벤트 루프를 실행시킨다.

아주 예전엔 `@UIApplication` 이었고, swift 5.3부터 `@main`이라는 attribute를 통해서  `UIApplicationMain(::::)`을 호출하고 앱을 실행했다. 

이 attribute가 없다면 아래처럼 컴파일 에러가 발생한다.

```
- ERROR!!
    - Entry point (_main) undefined.
      for architecture x86_64
``` 

<br><br>

조금더 설명을 위해 그림을 보자.  

아래와 같은 플로우로 실행된다.  

앱이 처음 실행되면 

- 0. @main / @UIApplication 을 찾는다.
- 1. UIApplicationMain()실행
    - 2. UIApplication 객체 생성 : 싱글턴 `UIApplication`
    - 3. UIApplication의 delegate객체 생성 : `AppDelegate`
    - 4. info.plist로부터 nib 파일을 로드


- 2번 UIApplication
    - 5. RunLoop를 생성하고 관리
    - 6. RunLoop에 대한 정보를 AppDelegate로 전송

- 3번 AppDelegate
    - `application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:` 실행
        - 7. Application Window 생성
        - 7. Root ViewController 생성

<p align="출처: https://oleb.net/blog/2012/02/app-launch-sequence-ios-revisited/">

<img width="600" alt="img1 daumcdn-13" src="https://github.com/isGeekCode/TIL/assets/76529148/43a18ca5-0099-46cc-8abd-05d395cbce22">
</p>

<br><br>

---

이제 문서를 보자.


<br><br>


애플리케이션 개체와 애플리케이션 대리자를 생성하고 이벤트 주기를 설정한다.


## Declaration

```swift
func UIApplicationMain(
    _ argc: Int32,
    _ argv: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>,
    _ principalClassName: String?,
    _ delegateClassName: String?
) -> Int32
```

<br><br>


## Parameters

- argc: Int32 
    - argv의 개수. 대게 main에 해당하는 매개변수다.
- argv: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>
    - argument의 변수 목록. 대게 main에 해당하는 매개변수다.
- principalClassName: String?
    - UIApplication클래스 또는 하위 클래스의 이름이다. nil을 지정하면, UIApplication으로 가정한다.
- delegateClassName: String
    - application delegate가 인스턴스화 되는 클래스 이름이다.
    - 만약 principalClassName이 UIApplication의 하위클래스를 지정하는 경우, 하위 클래스가 delegate로 되고 하위클래스 인스턴스가 앱의 delegate 메세지를 받는다.
    - 앱의 메인 nib파일에서 delegate 객체를 로드하는 경우에는 nil을 지정한다.

## Return Value

Int가 리턴된다고 써있지만 절대 리턴되지않는다. (Apple Doc에 정말로 이렇게 쓰여있다.)
사용자가 홈버튼을 눌러서 앱을 나가면, 앱은 백그라운드로 이동한다. 


## Discussion
이 메서드는 application객체와 delegate 객체를 만들고 설정한다.  
또한 앱의 run loop를 포함하는 main event loop를 만들고 이벤트처리를 시작한다.
Info.plist 파일에  NSMainNibFile 키와 이 값에 대한 유효한 nib 파일이 있다면 load한다. 
return 타입이 정의되어 있지만 return 하지 않는다.


### 관련 토픽

- [Updating your app from 32-bit to 64-bit architecture](https://developer.apple.com/documentation/uikit/app_and_environment/updating_your_app_from_32-bit_to_64-bit_architecture)


<br><br>

## History
- 230809 : 초안작성

