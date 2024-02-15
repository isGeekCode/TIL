# UIKit - UIStoryboard

[Apple Document](https://developer.apple.com/documentation/uikit/uistoryboard)
> Interface Builder 스토리보드 리소스 파일에 표현된 디자인 시간 뷰 컨트롤러 그래프의 캡슐화다.

```swift
// iOS 5.0+

@MainActor
class UIStoryboard : NSObject
```

## Overview

UIStoryboard 객체는 앱의 뷰 컨트롤러들의 아카이브 버전을 관리한다.  

디자인 시간에, 당신은 ViewController들의 내용을 시각적으로 구성하고, Xcode에서는 해당 인터페이스를 재생성하는 데 필요한 데이터를 앱의 번들 내 스토리보드 파일에 저장한다.  

프로그래매틱하게 새로운 뷰 컨트롤러를 생성하고 싶을 때,  
먼저 UIStoryboard 객체를 생성하고 적절한 이름과 bundle 정보를 지정한다.  
그런 다음 해당 객체를 사용하여 원하는 특정 ViewController를 인스턴스화한다.

인스턴스화 과정에서,  
UIStoryboard는 init(coder:) 메서드를 사용하여 프로그래매틱하게 ViewController를 생성한다.  

스토리보드는 ViewController의 데이터 아카이브를 해당 메서드에 전달하고,  
그 메서드는 그 데이터를 사용하여 ViewController와 그 뷰들의 상태를 재생성한다.  

만약 해당 ViewController에 대한 커스텀 초기화 메서드가 있다면,  
스토리보드에 선언한 코드블록을 사용하여 ViewController를 인스턴스화하도록 요청할 수 있다.  

이 블록을 사용하여 당신의 커스텀 초기화 메서드를 호출할 수 있으며, ViewController가 필요로 하는 추가 데이터를 전달할 수 있다. 

visionOS 앱의 경우, 기존 스토리보드를 로드할 수는 있지만, 플랫폼에 특정한 콘텐츠를 추가할 수는 없다. 
가능한 한 빨리 인터페이스 코드를 SwiftUI로 마이그레이션하자.

<br><br>

## 스토리보드 객체 가져오기

```swift
init(name: String, bundle: Bundle?)
```
지정한 리소스 파일을 위한 스토리보드 객체를 생성하고 반환한다.  
- name: 스토리보드 파일의 이름
- bundle: 스토리보드 파일이 위치한 번들이다. nil로 설정하게 되면 main번들에서 스토리보드를 찾는다.  

<br><br>

## 초기화된 ViewController Loading(불러오기)
```swift
func instantiateInitialViewController() -> UIViewController?


//사용예
// Main.storyboard에서 초기 뷰 컨트롤러 인스턴스화
if let initialViewController = UIStoryboard(name: "Sub", bundle: nil).instantiateInitialViewController() {
    // 초기 뷰 컨트롤러를 앱의 window의 rootViewController로 설정
    window?.rootViewController = initialViewController
    window?.makeKeyAndVisible()
}
```
스토리보드의 초기 ViewController를 생성하고, 스토리보드에 저장된 데이터로 초기화한다.  
이 메서드는 스토리보드에서 `is Initial View Controller`로 설정된 ViewController를 인스턴스화 한다.  

<br><br>

```swift
func instantiateInitialViewController<ViewController>(creator: ((NSCoder) -> ViewController?)?) -> ViewController?

// 사용예
if let viewController = storyboard.instantiateInitialViewController { coder in
    MyViewController(coder: coder, customProperty: "Custom Value")
} as? MyViewController {
    // 초기화된 viewController 사용
}
```
스토리보드에서 초기 ViewController를 생성하고, 개발자가 제공한 커스텀 초기화 코드를 사용해서 초기화한다.  `creator`블록을 통해서 개발자는 커스텀 초기화 로직을 적용할 수 있다.  

<br><br>

## Instantiating Storyboard View Controller 메서드 
스토리보드에서 ViewController를 인스턴스화 하는데 사용되는 메서드이다.   

```swift
func instantiateViewController(withIdentifier: String) -> UIViewController
Creates the view controller


//예시
let storyboard = UIStoryboard(name: "Main", bundle: nil)
if let viewController = storyboard.instantiateViewController(withIdentifier: "MyViewController") as? MyViewController {
    // viewController를 사용하여 사용자 커스텀 세팅.
    // 예: 네비게이션 컨트롤러에 푸시
    navigationController?.pushViewController(viewController, animated: true)
}

```
스토리보드에서 식별자로 특정 ViewController를 인스턴스화하고, 스토리보드에 정의된 속성으로 초기화한다.  
커스텀 초기화 로직을 추가할 수 없고, 스토리보드에서 설정한 모든 속성이 그대로 적용된다.  



```swift
func instantiateViewController<ViewController>(identifier: String, creator: ((NSCoder) -> ViewController?)?) -> ViewController

let storyboard = UIStoryboard(name: "Main", bundle: nil)
if let viewController = storyboard.instantiateViewController(identifier: "MyViewController") { coder in
    // 커스텀 초기화 로직을 여기에 선언.
    // 예: MyViewController에 커스텀 데이터를 전달
    return MyViewController(coder: coder, customData: "Some Data")
} as? MyViewController {
    // viewController를 사용하여 커스텀 세팅.
    // 예: 네비게이션 컨트롤러에 푸시
    navigationController?.pushViewController(viewController, animated: true)
}

```


------

애플 도큐먼트에서 제공하는 내용은 여기까지다.  

이제 앱실행시 최초 로드할 Storyboard 설정방법을 살펴보자.  

## 초기 Storyboard 설정하기
- 기본적으로 내가 최초 실행되길 원하는 Storyboard파일의 ViewController에는 `is Initial View Controller`를 체크해두어야 한다.  
- initial VC로  커스텀 View Controller 를 사용하는 경우, `Inherit Module From Target` 를 체크해 두어야한다.  


### AppDelegate만 사용하는 경우
- Info.plist
    - Main storyboard file base name ; 원하는 스토리보드 파일의 이름으로 설정한다. 
    
     
### SceneDelegate를 사용하는 경우
역시 Info.plist에  Main storyboard file base name 키값이 존재하지만, 우선순위는 UISceneStoryboardFile가 된다.  
그래서 이곳에 다른 값을 세팅해도 UISceneStoryboardFile 에 명시된 스토리보드를 호출한다.  

- Info.plist
    - UIApplicationSceneManifest
        - UISceneConfigurations
            - UISceneStoryboardFile : 원하는 스토리보드 파일의 이름으로 설정한다.  


