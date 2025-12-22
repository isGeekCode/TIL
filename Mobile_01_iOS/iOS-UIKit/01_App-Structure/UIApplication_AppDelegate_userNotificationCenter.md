#dev/mobile/ios

# UIApplication_AppDelegate - userNotificationCenter
AppDelegate클래스는 앱의 전반적인 라이프사이클 관리르 담당하는 클래스다.

그중 UNUserNotificationCenterDelegate 프로토콜을 채택하여, 앱이 백그라운드에서 실행 중일 때 UNUserNotificationCenter에서 수신한 알림을 처리하는 역할을 한다.


## 알림이 수신되는 경우

### 포그라운드일 때 수신하는 함수
userNotificationCenter(_:willPresent:withCompletionHandler:) 

여기서 알림을 즉시 처리하도록 설정하거나, 수신된 알림을 무시할 수 있다.
completionHandler 클로저를 호출하여 알림을 처리가 완료되었음을 시스템에 알리는 작업이 필요하다.


### 백그라운드일 때 수신하는 함수
userNotificationCenter(_:didReceive:withCompletionHandler:) 

위에 willPresent 함수와 동일한 처리를 하지만

앱이 백그라운드에서 실행 중일 때, 유저가 알림을 탭하여 앱을 실행하면, AppDelegate 클래스에서는 didFinishLaunchingWithOptions 메서드 대신 이 함수를 호출하여 알림을 처리한다.
