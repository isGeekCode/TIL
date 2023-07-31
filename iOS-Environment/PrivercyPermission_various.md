# Privacy - 여러가지 접근권한요청

- [다양한 접근권한](#다양한-접근권한)
- [앱 추적 투명성](#앱-추적-투명성)


앱을 만들고 테스트를 하다보면

갑작스런 쓰레드에러가 나는 경우가 있다.

UIView를 그리는데 있어 에러가는 경우는 Xcode에서 친절하게 보라색으로 표시해주지만

카메라, 사진첩 등 따로 권한을 요청해야만 하는 경우가 있다.

웹뷰를 사용하는 경우, 웹에서 따로 실행시켜준다면 넘어갈 수 있지만

- 사진을 찍는 경우: 카메라 사용 권한
- 동영상을 찍는 경우: 마이크 사용 권한

위와 같은 내용 뿐만 아니라 정말 다양한 권한들이 있다.

### 세팅방법

info.plist에 내용을 추가 하기만하면 정상작동한다.

![스크린샷_2022-11-17_오후_1 42 10](https://user-images.githubusercontent.com/76529148/202377586-909a4144-d614-4c8a-b359-4f43f777635b.png)

### 다양한 접근권한

아래와 같이 다양한 권한이 존재한다.

[애플 문서](https://developer.apple.com/documentation/bundleresources/information_property_list/protected_resources)

- 블루투스 : Privacy - Bluetooth Always Usage Description
- 캘린더 : Privacy - Calendars Usage Description
- 미리알림 : Privacy - Reminders Usage Description
- 카메라 : Privacy - Camera Usage Description
- 마이크 : Privacy - Microphone Usage Description
- 연락처 : Privacy - Contacts Usage Description
- FaceID : Privacy - Face ID Usage Description
- Desktop 폴더 : Privacy - Desktop Folder Usage Description
- Document 폴더 : Privacy - Documents Folder Usage Description
- 네트워크 볼륨파일 : Privacy - Network Volumes Usage Description
- 이동식 볼륩 : Privacy - Removable Volumes Usage Description
- FileProvider도메인 : Privacy - Access to a File Provider Domain Usage Description
- 건강 기록 : Privacy - Health Records Usage Description
- 건강 공유 : Privacy - Health Share Usage Description
- 상태업데이트 : Privacy - Health Update Usage Description
- 위치사용 : Privacy - Location Usage Description
- 위치 항상 사용 및 앱 사용시 사용: Privacy - Location Always and When In Use Usage Description
- 위치 사용 포그라운드에서 앱 사용시 : Privacy - Location When In Use Usage Description
- 위치에 대한 임시 액세스 요청 : Privacy - Location Temporary Usage Description Dictionary
- 미디어 라이브러리 : Privacy - Media Library Usage Description
- 모션 : Privacy - Motion Usage Description
- 로컬 네트워크 : Privacy - Local Network Usage Description
- NFC스캔 : Privacy - NFC Scan Usage Description
- 사진첩에 추가 : Privacy - Photo Library Additions Usage Description
- 사진첩 사용 : Privacy - Tracking Usage Description
- 사용추적 : Privacy - AppleEvents Sending Usage Description
- 시스템관리 : Privacy - System Administration Usage Description
- Siri사용 : Privacy - Siri Usage Description
- 음성인식 : Privacy - Speech Recognition Usage Description
- Video Subscriber계정 : Privacy - Video Subscriber Account Usage Description
- ID 사용 : Privacy - Identity Usage Description

### 앱 추적 투명성
- 앱 추적 투명성(ATT: App Tracking Transparency)
iOS 14.5부터 ATT프레임워크가 추가되면서 사용자에게 명시적인 허가를 받아야만 기기의 광고 ID (IDFA: IDentifier for Advertising)에 접근할 수 있게 되었다.

광고 ID는 사용자에게 맞춤형 광고 (예: 최근에 조회한 상품의 연관 상품을 보여주는 등)를 제공할 때 필요하다.

앱 투명성 프레임워크를 사용하면 사용자에게 추적(Tracking) 권한을 요청할 수 있는데, 사용자가 권한을 허용해야만 앱에서 광고 ID에 접근할 수 있게 된다.

추적 권한은 단 한번만 요청할 수 있는데, 앱을 완전히 삭제하고 재설치하지 않는 한 다시 권한을 요청할 수 없다. 따라서 적절한 시점에, 권한이 필요한 상세한 이유를 사용자에게 충분히 제공한 다음 권한을 요청해야한다.

앱 투명성 프레임워크에서는 권한을 요청할 때 사용자에게 보여줄 문구를 지정할 수 있다. 

Info.plist의 NSUserTrackingUsageDescription 키 (Privacy - Tracking Usage Description)에 추적 권한이 필요한 이유를 기재하면 된다, 
다음 스크린샷에서 보는 것처럼 권한 요청 다이얼로그에 문구가 표시되는 것을 확인할 수 있다.

### 코드



```
import AppTrackingTransparency


// 실행위치 예 1. AppDelegate
// iOS14 때에는 didFinishLaunchingWithOptions 함수에 넣었지만 iOS15.0.1이후론 아래와 같이 바뀌었다. (기존위치에선 실행이 되다가 닫혀버린다)

class AppDelegate {
  func applicationDidBecomeActive(_ application: UIApplication) { 
    requestTrackingAuthorization()
  }
}
// 실행위치 예 2. ViewController 생명주기

// 실행위치 예 3. buttonAction 



// 추적 접근 요청 메서드
private func requestTrackingAuthorization() {
    if #available(iOS 14, *) {
      if ATTrackingManager.trackingAuthorizationStatus == .notDetermined {
        ATTrackingManager.requestTrackingAuthorization(completionHandler: { _ in
            // switch status {
            //     case .authorized:
            //     case .denied:
            //     case .notDetermined:
            //     case .restricted
            // }
    })
      }
    }
}
```

### SwiftUI 코드

세부내용은 위와 동일
```
import AppTrackingTransparency
import SwiftUI

struct ContentView: View {
  var body: some View {
    VStack {
      Text("Hello, world!")../Xcode/PrivercyPermission_various.md
        .padding()
    }
    .onReceive(NotificationCenter.default.publisher(for: UIApplication.didBecomeActiveNotification)) { _ in
      ATTrackingManager.requestTrackingAuthorization(completionHandler: { _ in
      })
    }
  }
}

```
  
### 스크린샷
    
<img width="300" alt="IMG_3880" src="https://github.com/isGeekCode/TIL/assets/76529148/3ae77e89-d19f-42f2-9969-46b91c3db338">
