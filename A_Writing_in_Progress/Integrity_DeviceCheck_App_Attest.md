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

![img1 daumcdn-12](https://github.com/isGeekCode/TIL/assets/76529148/405caa0f-089c-49fd-b256-43f41fba71a4)
  
<p align="center">사용예시 - (이미지 출처 : 김종권의 iOS앱 개발 알아가기)</p>  


## DeviceCheck의 흐름
- 1. (App)장치 식별을 위한 임시 토큰 생성
- 2. (App -> Backend) token data를 post형식으로 Backend에 데이터 생성
- 3. (Backend -> Apple Server) backend에서 token data를 post형식으로 apple server에 전달 
- 4. (Apple Server -> Backend) apple에서 2bit 응답값과 상태를 Response
- 5. (Backend -> App) backend에서 보관 및 처리, iOS App에서 필요하면 상태 전달
    - (해당 디바이스가 blacklist인지.. 등)

![server-1](https://github.com/isGeekCode/TIL/assets/76529148/efcce0e6-5032-4714-9362-92c2cf8f86dd)


### 1. (App)장치 식별을 위한 임시 토큰 생성

앱에서 DeviceCheck모듈안의 generateToken함수를 통해 TokenData 획득
```swift
import DeviceCheck

if DCDevice.current.isSupported { 
    DCDevice.current.generateToken { dataData, error in
      guard let dataData = dataData else {
        print("token is empty: \(error!.localizedDescription)")
        return
      }
      let tokenString = dataData.base64EncodedString()
      print(tokenString) // AgAAAHXbhcMDrOhwYgRYbuTll...+4V94A==
      
      // deviceToken은 Back-end로 가서 애플서버를 거쳐 다시 App으로 
    }​
}
// 시뮬레이터는 isSupported를 통과하지 않기때문에 테스트를 하려면 실제 디바이스를 사용한다.
```

### DeviceCheck Key 생성방법
DeviceCheck API를 사용하기 위해서는 Apple Developer 에서 DeviceCheck 키를 발급해야한다. 

- [Apple Developer Website](Developer.apple.com/account)에 들어간다.
- 인증서, 식별자 및 프로파일 카테고리 - 키 를 클릭한다. 
- 키 페이지에서 `+`버튼을 클릭
- 구분할 키 이름 입력 / DeviceCheck 체크박스를 체크 / Continue를 누른다.
- `Confirm`버튼 클릭
- 생성된 p8형식의 개인키(privateKey)를 다운로드 한다.
    - 이 파일은 최초 1회만 받을 수 있기때문에 잘 보관하자.
    
### DeviceCheck Flow를 위한 준비물
- Team ID
- Key ID
- privateKey.p8

### Apple 사양의 JWT(JSON Web Token)형식 생성
- 알고리즘 : ES256
```
//HEADER:
{
  "alg": "ES256",
  "kid": Key ID
}
//PAYLOAD:
{
  "iss": Team ID,
  "iat": 요청 타임스탬프 (Unix Timestamp,EX:1556549164),
  "exp": 만료 타임스탬프 (Unix Timestamp,EX:1557000000)
}
//타임스탬프는 반드시 정수 형식이어야 한다
```
결합된 JWT 문자열: xxxxxx.xxxxxx.xxxxxx

### Apple 서버로 데이터 전송
APNS 푸시 브로드캐스트와 마찬가지로 두종류의 환경(운영, 개발)이 있다.

1. 개발 환경: https://api.devicecheck.apple.com
2. 운영 환경: https://api.development.devicecheck.apple.com

제공되는 API 경로는 아래 3가지이다. 
- 기본도메인/v1/query_two_bits
- 기본도메인/v1/update_two_bits 
- 기본도메인/v1/validate_device_token

### 1. 저장되어있는 데이터 쿼리 요청하기
- 기본도메인/v1/query_two_bits

```
//Headers:
Authorization: Bearer xxxxxx.xxxxxx.xxxxxx (조합된 JWT 문자열)

//Content:
device_token:deviceToken (조회할 deviceToken)
transaction_id:UUID().uuidString (쿼리 식별자, 여기서 직접 UUID로 표시)
timestamp: 요청 타임스탬프（"밀리세컨드"）（EX: 1556549164000）
```

### Response 목록
query_two_bits 및 update_two_bits를 통해 사용하여 서버와 통신할 때 아래 표에 나열된 응답 코드 중 하나를 받을 수 있다.

<img width="800" alt="스크린샷 2023-05-11 오후 2 02 38" src="https://github.com/isGeekCode/TIL/assets/76529148/54eea091-9f6e-4d89-ae65-4518e463fc2a">

<p align="center">
    <a href="https://developer.apple.com/documentation/devicecheck/dcdevice" style="text-align: center;">출처 : Apple Document : DeviceCheck </a>
</p> 

### Response 내용
```
{
  "bit0": Int(0 또는 1),
  "bit1": Int(0 또는 1),
  "last_update_time": String："최종 수정 시간 YYYY-MM"
  // 최종 수정 시간은 "연-월"로만 표시될 수 있다.
}
```
### 1. 저장되어있는 데이터 쿼리 update하기
- 기본도메인/v1/update_two_bits
```
//Headers:
Authorization: Bearer xxxxxx.xxxxxx.xxxxxx (조합된 JWT 문자열)

//Content:
device_token:deviceToken (조회할 deviceToken)
transaction_id:UUID().uuidString (쿼리 식별자, 여기서 직접 UUID로 표시)
timestamp: 요청 타임스탬프（"밀리세컨드"）（EX: 1556549164000）
bit0: Int(0 또는 1),
bit1: Int(0 또는 1),
```

- Response 종류는 위와 동일

### Response 내용
update를 할때에는 따로 반환내용이 없다. 반환값이 200일 경우, update성공이다. 


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
- [서버단 API (Chinese)](https://qiita.com/owen/items/85dff1e45083d2805140)
## History
- 230511 : 초안 및 레퍼런스 작성


