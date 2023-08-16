# [Apple Document] - About the app launch sequence : 앱의 실행되는 순서에 관하여

앱 실행 시 시스템이 코드를 실행하는 순서를 확인해보자.

- [Apple Doc : About the app launch sequence](https://developer.apple.com/documentation/uikit/uiview#1652798)

<br><br>

앱의 실행은 복잡한 단계의 순서(시퀀스)를 포함하며, 그 대부분은 시스템이 자동적으로 처리한다.  

  
실행 시퀀스동안, 

UIKit은 앱의 app delegate의 메서드를 호출함으로 사용자 상호작용에 대비하고,  

앱이 요구하는 특정 작업들을 실행할 수 있도록 한다. 

아래의 그림을 통해 시퀀스를 살펴보자.  

<img width="600" alt="스크린샷 2023-08-16 오전 11 14 26" src="https://github.com/isGeekCode/TIL/assets/76529148/72037855-41fd-4377-aab7-71a9c2cc7414">

<br><br>

- 1. user나 시스템이 앱을 실행 시, 시스템은 앱을 `prewarm`시킨다.
    - iOS15 이후 버전에서는, 시스템은 디바이스 상태에 따라서 앱을 `prewarm` 시킬 수 있는데, 앱이 사용가능한 상태가 되기 전까지 사용자가 기다리는 시간을 최소화하기 위해 nonrunning 애플리케이션 프로세스들을 실행한다.
- 2. 시스템이 Xcode에서 제공하는 `main()` 함수를 실행한다.
- 3. `main()` 함수는 `UIApplication`인스턴스와 `app delegate` 인스턴스를 생성하는 `UIApplicationMain(_:_:_:_:)`을 호출한다.
- 4. UIKit은 `Info.plist`파일이나 target의 커스텀 프로퍼티 탭에 정의된 `default storyboard`를 로드해온다. 만약 앱이 이런 단계를 스킵한다면 `storyboard`를 사용하지 않는다.
- UIKit이 app delegate에 있는 `application(_:willFinishLaunchingWithOptions:)` 메소드를 호출한다.
- UIKit이 app의 `ViewController`들과 `app delegate`에 있는 추가적인 메소드들을 실행하기 위해 [UI Restoration](https://developer.apple.com/documentation/uikit/view_controllers/preserving_your_app_s_ui_across_launches/about_the_ui_restoration_process) 을 진행한다.
- UIKit이 app delegate에 있는 `application(_:didFinishLaunchingWithOptions:)` 메소드를 호출한다


## Prewarming(예열)을 위해 앱을 준비하기

iOS 15 이후, 시스템은 기기의 상황에 따라서 당신의 앱을 prewarm(예열)한다. 
- 실행 중이지 않은 앱의 프로세스를 시작해, 사용자가 앱이 사용 가능해질 때 까지 기다려야 하는 시간을 줄인다.  

Prewarming은 앱의 시작 시퀀스에서 `main()` 이 `UIApplicationMain(_:_:_:_:)` 을 호출하기 전까지의 과정을 실행시킨다.  

이는 시스템이 앱을 완전히 시작하는 것에 필요할 것으로 예측되는 저수준의(low-level) 구조물들을 만들거나 캐싱할 기회를 제공한다.  

> 앱의 시작 동안 시스템이 필요로 하는 저수준의 구조물들에 대한 더 많은 정보에 대해서는, WWDC 세션 영상인 App Startup Time: Past, Present, and Future 를 참조하자.  

시스템이 당신의 앱을 prewarm하고 난 다음에는, 앱이 시작하고 시퀀스를 다시 시작할 때 까지 그 시작 시퀀스를 멈춤(paused) 상태로 남겨 둘 수도 있으며, 또는 리소스를 다시 가져오기 위해 prewarm된 앱을 메모리로부터 제거할 수도 있습다.   

시스템은 기기가 재부팅된 이후에, 그리고 시스템의 상황이 허락할 때 주기적으로 당신의 앱을 prewarm할 수 있다.  


만약 앱이 `UIApplicationMain(::::)` 호출 전에 코드를 실행한다면, `load()`와 같은 static 이니셜라이저처럼 사용 가능한 서비스와 리소스에 대해 가정을 하지 말아야 한다.
- [load()](https://developer.apple.com/documentation/objectivec/nsobject/1418815-load)

예를 들어, 키체인 아이템은 데이터 보호 정책으로 인해 잠금 해제된 기기를 필요로 하며, 사전 준비 단계는 기기가 잠금 상태일 때에도 발생한다.  

특정 서비스나 리소스에 대한 액세스가 코드에 의존하는 경우, 해당 코드를 시작 시퀀스의 나중 부분으로 이동시켜야 한다.

앱을 prewarming하는 것은 prewarming 단계가 완료된 시점과 사용자 또는 시스템이 앱을 완전히 시작시키는 시점 사이에 불확실한 시간차가 발생한다.  

이러한 이유로 MetricKit을 사용하여 사용자 주도의 시작 및 재개 시간을 정확하게 측정하는 것이 좋으며, 시작 시퀀스의 여러 지점에 직접 signpost를 설정하는 것보다 더 신뢰할 수 있다.


<br><br>

## History
- 230816 : 초안작성

