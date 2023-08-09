# [Apple Document] - Managing your app’s life cycle : 앱의 생명주기 관리

- [Apple Document : Managing your app’s life cycle](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)

<br><br>

## Overview

앱의 현재 상태는 `언제든 수행할 수 있는 작업`과 `수행할 수 없는 작업`을 결정한다.  

예를 들어, Foreground에 있는 앱은 사용자의 주의를 끌고 있기 때문에, CPU를 포함하고 있는 시스템리소스보다 우선도가 높다.  

그와 반대로 background에 있는 앱은 화면밖에 숨겨져있기 때문에 가능한 적은 작업을 수행해야하고, 가급적이면 아무것도 수행하지 말아야한다.  

앱의 상태가 변경되면, 그에 따른 동작을 조절해야 한다.  

앱의 상태가 변하면, UIKit은 그에 맞는 `Delegate`의 메서드를 호출한다. 
- iOS13이상 : `UISceneDelegate`객체를 이용하여 Scene-base 앱의 생명주기 이벤트에 반응한다. 
- iOS12이하 : `UIApplicationDelegate`객체를 이용하여 앱의 생명주기 이벤트에 반응한다. 

> 앱에서 Scene에 대한 지원을 활성화하면 `SceneDelegate`를 사용한다.   

<br><br><br>

## Scene-based App 기반의 Life-cycle 동작

앱에서 `Scene`을 지원하는 경우, `UIKit`은 각 Scene에 대하여 별도의 Life-cycle 이벤트를 제공한다.  

Scene는 디바이스에서 실행되는 앱 UI의 한 인스턴스를 나타낸다.  

사용자가  각 앱에 대해 여러 장면을 만들고, 이를 별도로 표시하거나 숨길 수 있다.  

각 Scene마다 고유한 Life-cycle이 있기 때문에, 각 Scene의 상태가 다르 수 있다.  

예를 들어,   
- 한 Scene이 foreground에 있고,  
- 다른 Scene은 Background에 있거나 suspended에 있는 상태일 수 있다.  


> IMPORTANT
> scene 지원은 선택기능이다.
> 기본 지원을 사용하려면 앱에서 지원을 사용하려면 app의 `Info.plist` 파일에 `UIApplicationSceneManifest` 키를 사용하면 된다.
> [Specifying the Scenes Your App Support](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/specifying_the_scenes_your_app_supports) 을 참고할 것.

<br><br>

아래 그림은 Scene의 상태 전환을 보여준다.  

사용자 또는 시스템이 앱에 대한 새 `Scene`을 요청하면 UIKit은 `Scene`을 생성하고 `Unattached`상태로 둔다.  
사용자가 요청한 `Scene`은 `foreground`로 빠르게 이동하고, 화면에 나타난다.  

시스템이 요청한 `Scene`은 일반적으로 이벤트를 처리할 수 있도록 `background`로 이동한다.  

예를 들어, 시스템은 위치 이벤트를 처리하기 위하여 `background`에서 `scene`을 시작할 수 있다.  

사용자가 앱의 UI를 닫으면 UIKit은 연결된 `Scene`을 `background`의 상태로 두고, 결국은 `suspended`상태로 변경된다.  

UIKit은 언제든지  `background` 또는 `suspended` 상태의 `Scene`을 연결 해제하여 리소스를 회수하고,  

해당 `Scene`을 `Unattached` 상태로 되돌릴 수 있다.  
 
<img width="600" alt="스크린샷 2023-08-09 오후 3 19 58" src="https://github.com/isGeekCode/TIL/assets/76529148/40a06a49-03e1-4182-abed-d5846cd3396a">

<br><br>

scene transition을 사용하면 다름 작업을 수행할 수 있다.
- UIKit이 scene을 앱에 연결하면, scene의 초기 UI를 구성하고 scene에 필요한 데이터를 로드한다.
- Foreground로 상태가 전환될 때 UI를 구성하고 사용자와 상호 작용할 준비를 한다. 
    - [Preparing Your UI to Run in the Foreground](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_foreground) 문서 참고
- foreground-active 상태를 벗어나면 데이터를 저장하고 앱 동작을 조용하게(quiet)하게한다.
    - [Preparing your UI to run in the background](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background) 문서 참고
- background 상태에 들어가면, 중요한 작업을 완료하고, 가능한 많은 메모리를 확보하고 앱 스냅샷을 준비한다. 
    - [Preparing Your UI to Run in the background](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background) 문서를 참고
- Scene의 연결이 끊어질때, scene과 연결된 모든 공유 리소스를 정리한다.
- Scene과 관련된 이벤트 외에도 `UIApplicationDelegate`객체를 이용하여 앱을 시작할때 응해야한다.   
    앱 시작시 수행할 작업에 대해서는 [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/app_and_environment/responding_to_the_launch_of_your_app) 문서를 참고
> UI의 Life-cycle은 SceneDelegate에서 처리하지만 앱 시작에 관련해선 AppDelegate에서 처리한다.  

<br><br><br>

## App 기반의 Life-cycle 동작

iOS 12이전 버전과 Scene을 지원하지 않는 앱에서 UIKit은 모든 Life-cycle 이벤트를 UIApplication 객체에 제공한다.  

`App Delegate`는 별도의 화면에 표시되는 화면을 포함하여 앱의 모든 `Window`를 관리한다.  

결과적으로 앱 상태의 전환은 외부 디스플레이의 콘텐츠를 포함한 앱 전체 UI에 영향을 준다.  

아래 그림은 `App Delegate` 객체와 관련된 상태 전환을 보여줍니다.
 
앱이 실행된 후,  시스템은 UI가 화면에 표시 될지의 여부에 따라,  

앱을 `inactive` 또는 `background` 상태로 전환한다.  

`foreground`로 앱을 시작할 때 시스템은 앱을 자동으로 `active` 상태로 전환한다.

그 후 앱이 종료될떄까지 `active`와 `background` 사이에서 상태가 변한다.

<img width="600" alt="스크린샷 2023-08-09 오후 3 20 05" src="https://github.com/isGeekCode/TIL/assets/76529148/2dfd0444-9272-4811-9f13-17ddcc905cdc">
  
앱 전환을 사용하여 다음 작업을 수행할 수 있다.

- 앱 실행 시, 앱의 데이터 구조와 UI를 초기화합니다. 
    - [Responding to the Launch of Your App](https://developer.apple.com/documentation/uikit/app_and_environment/responding_to_the_launch_of_your_app) 문서를 참고
- 앱이 활성화 되었을때 UI구성을 오나료하고 사용자와 상호 작용할 준비를 합니다. 
    - [Preparing Your UI to Run in the Foreground](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_foreground) 문서를 참고
- 비활성화되면 데이터를 저장하고 앱 동작을 조용하게 합니다.
    - [Preparing Your UI to Run in the Background](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background) 문서를 참고하
- background 상태로 들어가자마자 중요한 작업을 완료하고 가능한 많은 메모리를 확보한 후 앱 스냅샷을 준비합니다.
    - [Preparing Your UI to Run in the Background](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background) 문서를 참고
- 종료 시 모든 작업을 즉시 중지하고 공유 리소스를 해제합니다. 
    - [applicationWillTerminate(:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623111-applicationwillterminate) 문서를 참고

<br><br><br>


## Respond to Other Significant Events(기타 이벤트 응답)

Life-cycle 이벤트 처리 외에도 앱은 아래와 같이 나열된 이벤트를 처리할 준비가 되어있어야 한다.  
 
UIApplicationDelegate 객체를 사용하여 이러한 이벤트 대부분을 처리한다.  

<br><br>

| Event                             | Description                                                                         | 참고링크             |
|:----------------------------------|-------------------------------------------------------------------------------------|:------------------:|
| Memory Warnings                   | 앱이 메모리 사용량이 너무 높을때 수신됩니다. 앱에서 사용하는 메모리 양을 줄인다.                         | - [Responding to memory warnings](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle/responding_to_memory_warnings) |
| Protected data becomes<br>available/unavailable       | 사용자가 기기를 잠그거나 잠금 해제할때 수신된다. | - [applicationProtectedDataDidBecomeAvaiable(_:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623044-applicationprotecteddatadidbecom) <br>
  - [applicationProtectedDataWillBecomeUnavailable(_:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623019-applicationprotecteddatawillbeco) |  
  
| Handoff Tasks                     | [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) 객체를 처리해야 할 때 수신된다.                         | - [application(_:didUpdate:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622963-application) |
| Time Changes                      | 전화 통신사가 시간 업데이트를 보내는 경우와 같이 여러가지 다른 시간 변경에 대해 수신된다.  | - [applicationSignificantTimeChange(_:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622992-applicationsignificanttimechange) |
| Open URLs                         | 앱에서 리소스를 열어야 할 때 수신된다.                                     | - [application(_:open:options:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623112-application) |



<br><br><br>

## History
- 230809 : 초안작성
- 230810 : 기타 이벤트 응답 추가

