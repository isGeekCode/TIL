# [Apple Document] - Responding to the launch of your app : 앱 실행에 대한 응답

#dev/mobile/ios

- [Apple Document : Managing your app’s life cycle](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)

<br><br>

앱의 데이터 구조를 초기화 하고, 앱이 실행되도록 준비하며 시스템의 모든 launch-time 요청에 응답한다.

## Overview

사용자가 홈화면에서 앱 아이콘을 탭하면 시스템에서 그 앱을 실행한다.  

만약 앱이 특정한 이벤트를 요청한 경우, 시스템은 해당 이벤트를 처리하기 위해 백그라운드에서 앱을 실행 시킬 수도 있다.   

Scene 기반 앱의 경우, Scene중 하나가 화면에 나타나거나 작업을 수행해야할 때도 시스템이 앱을 실행한다.  

모든 앱에는 UIApplication 객체를 나타내는 프로세스가 있다.  

또한 앱에는 UIApplicationDelegate프로토콜을 준수하는 app Delegate 객체를 가지고 있으며, 이 객체는 해당 프로세스 내에서 발생하는 중요한 이벤트에 응답한다.  


심지어 Scene기반의 앱들도 App Delegate를 활용하여 앱 시작 및 종료와 같은 기본 이벤트를 관리한다.  

앱 시작시, UIKit은 자동으로 UIApplication객체와 AppDelegate를 생성한다.  


<br><br><br>

## Provide a Launch Storyboard(Launch 스토리보드를 제공하다)

사용자가 디바이스에서 앱을 처음 시작하면 앱이 UI를 표시할 준비가 될 때까지  

시스템은 launch storyboard를 보여준다.  

launch storyboard를 표시하면 사용자에게 앱이 실행 중이고, 어떤 작업을 수행중인지 확인시켜줄 수 있다.

 
앱이 자체적으로 초기화되고, UI를 빠르게 준비하는 경우 사용자는 launch storyboard를 잠깐동안 볼 수 있다.  

 

Xcode 프로젝트에는 사용자가 커스터마이징 할 수 있는 기본 launch storyboard가 자동으로 포함되어있고,   

필요에 따라 launch storyboard를 추가 할 수 있다.



### 프로젝트에 새로운 launch storyboard를 추가하려면

1. Xcode 프로젝트를 연다.
2. File -> New -> File을 선택
3. Launch Screen 리소스를 프로젝트에 추가
4. launch storyboard에 View를 추가하고 Auto layout constraints를 이용하여 기본 환경에 맞게 크기를 조정하고 배치한다.

UIKit은 사용 가능한 공간에 View를 맞추기 위해 제약 조건을 사용하여 제공하는 내용을 정확하게 표시한다.

> iOS 13 이상에서는 항상 앱에 대한 launch storyboard를 제공한다. 
> static launch image를 사용하지 말것!

<br><br><br>

## Initialize Your App's Data Structures(앱의 데이터 구조 초기화)
다음 방법 중 하나 또는 두가지 모두의 방법으로 앱의 launch-time 초기화 코드를 넣을 수 있다.

 
- application (_:willFinishLaunchingWithOptions:)
- application (_:didFinishLaunchingWithOptions:)
 
UIKit은 app's launch cycle이 시작 될 때 이러한 메서드를 호출한다. 이를 사용하여 아래와 같은 작업을 할 수 있습니다.

 
- 앱의 데이터 구조를 초기화한다.
- 앱에 실행하는데 필요한 리소스가 있는지 확인한다.
- 앱이 처음 시작될 때 일회성 설정을 수행한다.
    - 예를 들어, 쓰기 가능한 디렉토리에 템플릿 또는 사용자 수정 가능 파일을 설치한다.  

- 앱에서 사용하는 모든 중요한 서비스에 연결한다.
    - 예를 들어 앱이 원격 알림을 지원하는 경우 Apple Push Notification Service에 연결한다.  

씬 기반(scene-based) 앱이 아닌 경우 UIKit은 앱시작시, 자동으로 default user interface를  로드한다.


<br><br><br>

## Move Long-Running Task off the Main Thread (긴 시간의 task를 Main Thread에서 제외시키기)

사용자가 앱을 실행하면 빠르게 실행하여 좋은 인상을 남겨야 한다.  

UIKit은 application (_:didFinishLaunchingWithOptions:) 메서드가 반환될 때까지 앱의 인터페이스를 표시하지 않는다.  

해당 메서드 또는 application (_:willFinishLaunchingWithOptions:) 메서드에서 long-running task를 수행하면 앱이 사용자에게 느리게 보일 수 있다.  

시스템이 앱의 백그라운드 실행 시간을 제한하기 때문에 백그라운드로 시작할 때 빠르게 돌아오는것도 중요하다.  

앱 초기화에 중요하지 않은 작업을 launch-time sequnce 밖으로 이동시키자.  

예를 들면,  

- 앱에 즉시 필요하지 않은 기능의 초기화를 연기시키자.
- 중요하고 장기간 실행되는 작업은 앱의 메인 쓰레드에서 다른곳으로 이동시키자. 
    - 이를 테면,  global dispatch queue 와 비동기 처리가 있다.

<br><br><br>

## Determine Why Your App Lauched(앱이 실행된 이유를 확인하자)

UIKit은 앱을 시작할 때 앱이 시작된 이유에 대한 정보와 함께 `launch option dictionary`를 application (_:didFinishLaunchingWithOptions:) 와 application (_:willFinishLaunchingWithOptions:) 메서드에 전달한다.  


해당 dictionary 키는 즉시 수행할 중요한 작업을 나타낸다.  


예를 들어,  사용자가 다른 곳에서 시작했고 앱에서 계속하려는 작업을 반영할 수 있다.

항상 launch options dictionary를 확인하여 에상되는 키를 확인하고 해당 키의 존재에 적절하게 대응해야 한다.




<br><br><br>

## History
- 230810 : 초안작성
