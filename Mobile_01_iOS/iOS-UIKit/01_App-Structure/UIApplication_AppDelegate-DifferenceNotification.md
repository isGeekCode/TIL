# UIApplication_AppDelegate - 헷갈릴수 있는 두 함수(didReceive형제)

#dev/mobile/ios


푸시알림을 받기위해 세팅하다보면 두가지 함수에서 고민을 하게 된다. 바로 아래 두 함수다.

- didReceiveRemoteNotification:fetchCompletionHandler:
- userNotificationCenter(_:didReceive:withCompletionHandler:)

## 표기방법

### didReceiveRemoteNotification:fetchCompletionHandler:

```
// swift
func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    // 알림 처리
    completionHandler()
}

// objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler {
    // 알림 처리
    completionHandler();
}
```
### userNotificationCenter(_:didReceive:withCompletionHandler:)

```
// swift
func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    // 알림 처리
    completionHandler()
}

// objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler {
    // 알림 처리
    completionHandler();
}
```

## 용도

- 1. didReceiveRemoteNotification:fetchCompletionHandler
- 2. userNotificationCenter(_:didReceive:withCompletionHandler:)

### 1번함수의 용도
- 실시간 데이터 업데이트
- 백그라운드에서의 데이터 뒷처리작업
- 백그라운드 동기화
- 원격알림을 통한 알림 전달

### 2번함수의 용도
- 로컬 알림: 앱에서 로컬로 발생시키는 알림
    - 예시: 알람, 일정 등록 등
- 원격 알림: 서버에서 앱으로 전송하는 알림
    - 예시: 메시지, 이벤트 등
- 알림 액션: 사용자가 알림에 대해 수행할 수 있는 작업
    - 예시: 확인, 답장, 삭제 등
- 알림 카테고리: 관련된 알림 액션을 그룹화하여 사용자에게 제공

### 차이점
이 둘은 각각 용도가 `유사`하지만 엄연히 다른 동작을 하게 되어있다. 기존에는 1번 함수만 있었지만 앱의 기능이 많아짐에 따라 iOS10부터 푸시를 위한 UNUserNotificationCenter 라는 객체와 그 객체의 함수들을 위임하기 위한 UNUserNotificationCenterDelegate가 생성됐다.이 메서드를 사용하여 다양한 유형의 알림과 액션을 처리할 수 있다. 

관련링크는 userNotificationCenterDelegate를 참고
TODO: 수정필요

### 푸시관련
iOS10 이후부터는 푸시관련 동작은 2번함수에 일임하면된다.

이때 `content-available` 값과 `mutable-content`값을 받게 되는 경우가 있다.

