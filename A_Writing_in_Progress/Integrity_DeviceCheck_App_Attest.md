# Integrity - DeviceCheck & App Attest

앱과 콘텐츠를 보호하기 위해 만들어진 Apple의 강력한 사기 방지 도구인 App Attest 및 DeviceCheck를 사용하는 방법을 알아보자.

앱과 콘텐츠의 무단 수정을 차단하기 위해 App Attest를 앱에 통합하여 배포해보자.

또한 DeviceCheck를 사용하여 앱에서 프리미엄 콘텐츠를 받은 고객과 불법적인 수단을 통해 프리미엄 콘텐츠를 얻은 고객을 구별할 수 있도록 하는 방법을 알아보자.


# DeviceCheck 
애플에서 제공하는 고유한 디바이스 식별을 가능하게 해주는 API 서비스다.
WWDC17에 공개되어 iOS11부터 지원한다. 아쉽게도 해당 영상은 Apple에서 내려갔다.(왜지)

이 API는 애플 클라우드에서 2bit의 저장공간을 제공한다. 그래서 해당 디바이스의 상태를 기록할 수 있다. 이때 앱을 재설치, 아이클라우드 계정 변경, 공장 초기화를 해도 이 2bit는 유지가 된다. 

이 두 bit값의 의미는 개발자가 정의하여 자유롭게 사용이 가능하다. 
세팅할 수 있는 상태는 4가지만 존재한다. 
- 세팅할 수 있는 상태
    - [0, 0]
    - [1, 0]
    - [0, 1]
    - [1, 1]  

<p align="center">
    <a href="https://github.com/isGeekCode/TIL/assets/76529148/405caa0f-089c-49fd-b256-43f41fba71a4" style="text-align: center;">사용예시 - (이미지 출처 : 김종권의 iOS앱 개발 알아가기)</a>
</p>

## DeviceCheck의 흐름
- (App)Token data 생성
- (App -> Backend) token data를 post형식으로 Backend에 데이터 생성
- (Backend -> Apple Server) backend에서 token data를 post형식으로 apple server에 전달 
- (Apple Server -> Backend) apple에서 2bit 응답값과 상태를 Response
- (Backend -> App) backend에서 보관 및 처리, iOS App에서 필요하면 상태 전달
    - (해당 디바이스가 blacklist인지.. 등)


![server-1](https://github.com/isGeekCode/TIL/assets/76529148/efcce0e6-5032-4714-9362-92c2cf8f86dd)


### Token data 생성
앱에서 DeviceCheck모듈안의 generateToken함수를 통해 TokenData 획득
```swift
import DeviceCheck

DCDevice.current.generateToken { dataData, error in
  guard let dataData = dataData else {
    print("token is empty")
    return
  }
  let tokenString = dataData.base64EncodedString()
  print(tokenString) // AgAAAHXbhcMDrOhwYgRYbuTll...+4V94A==
}​
```


## 참고링크
- [AppleDocument: DeviceCheck Framework ](https://developer.apple.com/documentation/devicecheck)

- [Blog - 일회성 제안 또는 평가판을 실행하는 iOS의 완벽한 방법(Swift)](https://medium.com/zrealm-ios-dev/ios-%E5%AE%8C%E7%BE%8E%E5%AF%A6%E8%B8%90%E4%B8%80%E6%AC%A1%E6%80%A7%E5%84%AA%E6%83%A0%E6%88%96%E8%A9%A6%E7%94%A8%E7%9A%84%E6%96%B9%E6%B3%95-swift-c5e7e580c341)
- [Blog - DeviceCheck API 사용 방법, 고유한 디바이스 ID (UDID 대체, Device block)](https://ios-development.tistory.com/848)
- [Blog - iOS 11: The DeviceCheck API](https://medium.com/the-traveled-ios-developers-guide/devicecheck-6f3eafac60e5)
- [Blog - [iOS/WWDC] App Attest & Device Check](https://jooeungen.tistory.com/entry/iOSWWDC-App-Attest-Device-Check)
- [WWDC21: AppAttest and DeviceCheck](https://developer.apple.com/videos/play/wwdc2021/10244/)
- [WWDC21: Safeguard your accounts, promotions, and content
](https://developer.apple.com/videos/play/wwdc2021/10110)
- [한번더 확인해봐야하는 WWDC15:Privacy your Apps](https://developer.apple.com/videos/play/wwdc2015/703/)
- [Blog - Uniquely identify iOS device using DeviceCheck (Tutorial)](https://fluffy.es/devicecheck-tutorial/)

## History
- 230511 : 초안 및 레퍼런스 작성


