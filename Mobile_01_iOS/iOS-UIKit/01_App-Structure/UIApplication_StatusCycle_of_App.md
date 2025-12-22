# UIApplication_AppDelegate - UIApplicationDelegate : 앱의 상태 / 생명주기(Life-Cycle)

- [WWDC19: Architecting Your App for Multiple Windows 앱 / 씬의 생명주기](https://developer.apple.com/videos/play/wwdc2019/258/)
- [코더스하이: 앱의 생명주기](https://www.youtube.com/watch?v=7GlwS2lOKbE)


#dev/mobile/ios

<br><br>

UIApplication은 애플리케이션의 라이프 사이클을 관리하는 싱글톤 클래스를 말한다.  

<br><br>

### 앱의 생명주기라는 개념은 왜 필요할까? 

아래 동작을 상상해보자.  

- 아이폰 앱 게임 중
- 전화 수신
- 앱에선 자동으로 통화화면으로 전환
- 실행중이던 앱은 잠시 비활성화 상태로 전환

단순한 동작이지만, 이 외에도 다양한 주기가 존재한다.  
Apple에서는 이 주기에 실행되는 메서드로 만들어 호출한다. 

이제 개발자는 특정 상황에 어떤 메서드가 호출되는지를 이해하고,   
그에 맞게 구현하기만 하면된다.  


<br><br>

화면을 터치하여 앱을 실행시키면 UIApplication이라는 클래스에 오프젝트 하나가 생긴다.
자신의 이벤트를 대행해줄  AppDelegate라는 오브젝트를 만든다.

AppDelegate라는 Object는 개발자가 직접 만들어가는 클래스이다. 
Application의 시동, 종료, Background,Foreground, in-active, active 상태로 다녀오는 것을 관리한다. 

가장먼저 하는 일은 window을 만드는 것이다.
iOS에서는 기본적으로 Single-window이다. 
`하나의 window가 앱 전체를 채우고 있고, 앱을 종료하면 window가 종료된다.`

App에서 사용하는 여러 data들은 AppDelegate가 관리한다. 이는 AppDelegate가 UIApplication으로 부터 앱의 시동과 종료등에 중요한 역할을 위임받고 있고, Singleton에 준하는 Object이기 때문이다. 

아이폰에서 주 화면에 현재 앱이 얼마만큼 점유하고 있느냐에 따라 앱의 상태가 달라진다. 


<br><br>

## UIApplicationDelegate
- 앱의 상태(Life-Cycle)
- App Life-Cycle 이벤트에 응답하는 Delegate함수

[참고링크](https://sujinnaljin.medium.com/ios-ios-12-%EC%9D%B4%ED%95%98%EC%9D%98-app-life-cycle%EA%B3%BC-uiapplicationdelegate-93b7acc82cde)


<br><br>

## 앱의 상태(Life-Cycle)

- Not-Running(Terminated)
- InActive(Foregound)
- Active(Foregound)
- Running(Background)
- Suspend(Background)

<br>

### Not-Running(Terminated)
앱이 시작되지않은상태

<br>

### InActive(Foregound)
Active상태로 들어오거나 나갈때 잠시 거치는 상태이다. 앱을 사용중에 푸시가 오거나 전화가 온다면 갑자기 잠시 화면이 바뀔때가 있다. 이때가 바로 이 상태이다. 

<br>

### Active(Foregound)
앱이 돌아가고 일반 적인 상태라고 생각하면 된다. 

<br>

### Running(Background)
여전이 앱은 돌아가고 있는 상태이다. 이 상태는 잠시 들어온 것일 수도 있고 여기에 있다가 Suspend상태로 넘어갈 수도 있다.

만약 앱이 실행중이다가 다른 앱의 푸시를 누르거나 전화를 하게 되면 전환되어 백그라운드에서 돌고 있게 된다. 이 시간이 길게 유지되지는 않는다. 약15분정도 뒤에는 Apple에서 아이폰의 CPU와 배터리를 위해 자동으로 앱을 suspend처리한다. 
예를 들어 백그라운드에서 음악을 실행하거나, 걸어온 길을 트래킹 하는 등의 동작이라고 볼수 있따.

<br>

### Suspend(Background)
 백그라운드 상태에서 활동을 멈춘 상태. 빠른 재실행을 위하여 메모리에 적재된 상태지만 실질적으로 동작하고 있지는 않다. 메모리가 부족할때 비로소 시스템이 강제종료하게 된다.

<br><br>

## App Life-Cycle 이벤트에 응답하는 Delegate함수

### applicationWillEnterForeground(_:)
- 상태 : Background -> InActive
- 앱이 Background 에서 Foreground로 진입할 것임을 delegate에게 알립니다.
- 이곳에서 disk 로부터 리소스를 로드하고 네트워크에서 데이터를 가져온다.
- 백그라운드로 진입할 때 작업한 많은 내용을 취소할 수도 있다.
- 언제나 앱을 InActive 상태에서 Active상태로 이동시키는 applicationDidBecomeActive(_:)를 뒤이어 호출한다.


<br>

### applicationDidBecomeActive(_:)
- 상태 : InActive -> Active
- 앱은 사용자나 시스템에 의해 실행됨으로써 Active 상태가 될 수도 있지만, 일시적으로 앱을 InActive 상태로 만드는 interruption (수신 전화 or SMS 메시지 등) 을 무시함으로써 Active 상태로 되돌아갈 수도 있다.
- 이곳에서 앱이 InActive 상태인 동안 일시 중지되었던(혹은 아직 시작되지 않은) 작업들을 재개합니다(ex. 타이머 재시작). 이전에 앱이 Background에 있었다면 앱의 사용자 인터페이스를 새로 고치는 데도 사용할 수 있다.
- Activation 상황에서 적합한 작업 내용은 이곳의 Configure Your User Interface and Initial Tasks at Activation을 참고

<br>

### applicationWillResignActive(_:)
- 상태 : Active -> InActive
- 앱을 Background 상태로 전환하기 시작할 때나, 수신 전화나 SMS 메시지와 같은 일시적인 interruption 으로 인해 InActive 상태로 전환될 수 있다.
- InActive 상태의 앱은 Active 또는 Background 상태로 전환되기를 기다리는 동안 최소한의 작업만 수행해야 한다.
- 이곳에서 타이머 비활성화, 게임 일시 중지 등 진행 중인 작업을 중단하고, 사용자의 데이터를 저장할 수 있다.
- Deactivation 상황에서 적합한 작업 내용은 이곳의 Quiet Your App upon Deactivation을 참고하세요

<br>

### applicationDidEnterBackground(_:)
- 상태 : Background
- 앱은 여러 가지 이유로 Background 상태로 이동한다.
    - 사용자가 Foreground 앱을 종료하면 UIKit이 앱을 Suspend 시키기 전에 Background 상태로 잠시 이동한다.
    - 혹은 시스템이 앱을 Background 상태로 직접 launch할 수도 있고, suspended 된 앱을 Background로 이동시켜 중요한 작업을 수행할 시간을 줄 수 있다.
- 앱이 Background에 있을 때는 가능한 적은 일을 수행해야하며, 가급적이면 아무 작업도 수행하지 않는 것이 좋다. **약 5초 전에 메서드가 반환되지 않으면 앱이 종료되고 메모리에서 제거된다.**
- 최종 작업을 수행하는 데 추가 시간이 필요한 경우 최대한 빨리 beginBackgroundTask(expirationHandler:)를 호출하여 시스템에 추가 실행 시간을 요청한다.
- 이곳에서 공유 리소스를 해제, 타이머 무효화 등의 작업을 수행한다. 앱 상태 정보(app state information)를 저장하여 나중에 앱이 종료(terminated) 되는 경우 앱을 현재 상태로 복원(restore)할 수 있다.
- 백그라운드로 전환 시 적합한 작업 내용은 이곳의 Release Resources upon Entering the Background을 참고.
- 앱이 백그라운드로 들어가고 delegate method가 return되면 UIKit은 앱의 현재 사용자 인터페이스의 스냅샷을 만든다. 시스템은 app switcher 에서 해당 이미지를 표시하고, 앱을 다시 Foreground로 가져올 때도 일시적으로 표시한다. 이때 비밀번호나 신용카드 번호와 같은 민감한 사용자 정보가 포함되어서는 안되므로 인터페이스에 이러한 정보가 포함되어 있으면 Background에 들어갈 때 view에서 제거해야 한다.


<br><br>

## SceneDelegate

iOS13이후, Scene이라는 개념이 추가되면서 SceneDelegate가 생겼다.  

기존에는 한번에 한가지의 앱만 실행할 수 있었으나,  
Scene이라는게 생겨나면서 ipad에 여러개의 앱을 동시에 동작시키는게 가능해졌다.  
여러개의 Scnee(창)을 띄우고 있어도 결국에는 유저가 실제로 동작시키고 있는 것은 하나의 Scene이다. 

<br>

### SceneDelegate 의 역할
- 다른 Scene으로 넘어가거나, 그런 시점들을 파악하기 위한 대리자 역할이다.  
- Scene(멀티태스킹의 창)의 개념이 도입되면서 AppDelegate의 역할에서 몇가지를 SceneDelegate로 보내게 된다.  


기존 AppDelegate에서 전부 관리하던 앱의 생명주기에서 
앱의 생명주기 + Scene의 생명주기 로 나뉘어지게 된다.  

<br>

### AppDelegate에서 관리하는 메서드
- Not running -> Active : didFinishLaunchingWithOptions
- Suspended -> Not running : didDiscardSceneSessions


### SceneDelegate에서 관리하는 메서드
- Inactive -> Active : sceneDidBecomeActive
- Active -> Inactive : sceneWillResignActive
- Forground -> Background :
    - sceneWillEnterForeground
    - sceneDidEnterBackground
- Background -> Suspended : sceneDidDisconnect

<br>

### 기존 AppDelegate

- Not running -> Active : didFinishLaunchingWithOptions
- Suspended -> Not running : willTerminate

- Inactive -> Active : didBecomeActive
- Active -> Inactive : willResignActive
- Forground -> Background :
    - willEnterForeground
    - didEnterBackground
- Background -> Suspended : sceneDidDisconnect

