# Integrity - App Attest (앱 증명)

iOS App Attests는 앱의 신뢰성을 검증하기 위해 Apple이 제공하는 서비스이다. 이 서비스를 사용하면 앱이 신뢰할 수 있는 기기에서 실행되고 있는지 확인할 수 있다. iOS 14부터 도입된 이 서비스는 앱이 악의적인 조작이나 해킹을 방지하고, 서버와의 통신 중에도 보안성을 강화하는데 도움을 줄 수 있다.

## 지원
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- Mac Catalyst 14.0+
- tvOS 15.0+
- watchOS 9.0+

## 아티클 번역. 
- [wwdc2021 : AppAttest & DeviceCheck](https://developer.apple.com/videos/play/wwdc2021/10244/)  
DeviceCheck API를 사용하게 되면 device unique 라서 앱을 삭제하거나, 심지어 폰 컨텐츠 리셋을 해도 남아 있는데, App Attest는 설치할 때마다 달라진다. 

우리가 운영중인 서비스가 있다고 가정해보자. 이때 어떤 앱으로부터 request를 받으면 이 요청이 운영중인 앱에서 온건지 알기 어려울 수 있다.
이때 App Attest를 사용하면 앱이 하드웨어 지원 어설션을 request의 일부로 첨부할 수 있다.
그럼 서버에서는 이 어설션을 이용하여 request가 정품 Apple  app에서 온것인지 확인할 수 있다.


여행 중에 수집품을 발견하도록 장려하는 아름다운 앱을 디자인했는데 수정된 앱으로 집을 떠나지 않고도 모든 것을 수집할 수 있다는 것을 알게 되었다고 상상해 보십시오.
또는 경쟁적인 멀티플레이어 레이싱 게임에서 치트를 사용하여 무제한 부스트를 얻어 다른 사람들이 순위표에서 경쟁하는 것을 보는 플레이어의 좌절감을 상상해 보십시오.
또는 토요일에 일어나서 서버에서 매우 많은 요청 볼륨을 보았지만 조사 후 호출이 앱에서 전혀 오지 않는다는 것을 알게 되어 매우 기쁩니다.
이렇게 App Attest는 앱의 정품 벚던과 수정된 버전을 식별하여 앱 경험과 비즈니스를 보호할 수 있도록 도와준다.

App Attest는 개발자와 개발자의 고객을 보호하기위해 활용할 수 있는 3가지의 주요 속성을 제공한다.
- Genuine Apple device : 애플 정품 기기
- Authentic application identity : 인증된 app ID
- Trustable payload : 신뢰할 수 있는 Payload

App Attest를 사용하면 서비스에서 위 세가지 조건을 충족하여 앱의 적법한 인스턴스에서 요청이 왔는지 확인할 수 있다. 요청은 정품 Apple 기기 에서 왔고, 정품 App을 실행중이며, 페이로드가 변조되지않은 상태이다. 

App Attest의 중심에는 보안키 쌍과 Apple에서 서명한 증명이 있고, 키 쌍이 정품 Apple 기기에서 생성 되었음을 인증한다.

개인키는 App Attest API를 이용하는 Secure Enclave를 통해서만 저장 및 액세스 할 수 있다.

앱이 Apple 기기에서 실행되려면 서명이 되어야한다. 그리고 앱을 무단으로 수정하는 사람은 자신이 제어하는 ID로 앱에 다시 서명해야 한다. 이 때, 필연적으로 App ID는 수정된다. 증명에 앱 ID의 해시를 포함한다. 그래서 앱ID를 증명에 포함된 것과 비교하여 호출자가 수정된 버전을 사용하고 있는지 확인할 수 있다.

요청이 정품기기와 정품앱에서 온 것임을 알았으니 이제 요청 페이로드에 대해 이야기 해보자

서버에 페이로드를 보내기전에 증명된 키를 사용하여 페이로드 다이제스트에 서명하도록 App Attest에 세팅할 수 있다.

이렇게 하면 페이로드의 어설션이 생성된다.
6:26
페이로드의 어설션 = App Attest에 세팅증명된 키 + 무엇>?>??


## 주요과정
- Creat and attest key : 키를 생성하기 / 증명하기
- Generate assertions : assertions 생성
- Verify app identity on the server : 서버에서 App Id 확인

## 작동 흐름
- 클라이언트 앱은 앱 서버로부터 인증 요청을 받는다. 이 인증 요청으로 앱이 신뢰할 수 있는 기기에서 실행되는지 확인한다.
- 클라이언트 앱은 앱 서버로부터 받은 인증 요청을 Apple의 서버로 전송.
- Apple의 서버는 클라이언트 앱에서 전송된 인증 요청을 받는다.
- Apple의 서버는 해당 기기의 고유한 식별자와 함께 앱이 실행 중인지 확인하기 위한 보안 검증을 수행. 이 검증은 기기의 Trusted Execution Environment (TEE)에서 이루어진다.
- Apple의 서버는 결과를 생성하고 해당 결과를 클라이언트 앱으로 전송. 이 결과는 앱이 신뢰할 수 있는 기기에서 실행 중인지 여부를 나타낸다.
- 클라이언트 앱은 Apple의 서버로부터 받은 결과를 앱 서버로 전송.
- 앱 서버는 결과를 확인하고, 필요에 따라 앱의 동작을 조정할 수 있다. 예를 들어, 앱 서버는 인증이 성공한 경우에만 특정 기능을 사용할 수 있도록 허용할 수 있다.

- 앱 : 하드웨어 기반 키 생성
- 앱 -> 백엔드
    - SecureEnclave를 통해 키 생성
    - 백엔드로 챌린지 생성을 요청

### 용어 설명
- 클라이언트 앱
    - 클라이언트 앱은 App Attest를 사용하여 자체적으로 생성한 attestation객체를 서버로 전송한다. 클라이언트 앱은 App Attest를 요청하고, attesttation 객체와 함께 서버로 부터 받은 챌린지를 사용하여 App Attest검증을 수행한다. 클라이언트 앱은 검증결과를 서버로 전달하고, 서버로부터 반환된 Assertion을 받아 앱의 인증여부를 확인할 수 있다.
- 서버
    - 클라이언트 앱으로 부터 전송된 attestation 객체와 챌린지를 사용하여 App Attest검증을 수행한다. 서버는 App Attest를 요청한 클라이언트 앱의 신뢰성을 확인하고, 필요한 추가 검증 로직을 수행한다.서버는 attestation 객체와 챌린지를 결합하여 Apple서버로 전송하여 Apple Attest검증 결과를 요청한다.
- APPLE 서버
    - 서버로 부터 받은 attestation 객체와 챌린지를 사용하여 App Attest 검증을 수행한다. APPLE서버는 attestation 객체의 유효성을 확인하고 클라이언트 앱이 신뢰 할 수 있는 앱인지 여부를 결정한다. 검증 결과에 따라 여기 APPLE서버에서는 서버로부터 온 요청에 대한 인증결과인 Assertion을 생성하여 반환한다. 이 Assertion은 클라이언트 앱의 인증여부를 파악한다. 
- Challenge
    - "Challenge"는 클라이언트 앱이 서버에 전송하여 App Attest 인증을 요청할 때 사용되는 데이터다. 이는 클라이언트 앱과 서버 간의 상호작용에 사용되는 임의의 데이터로, 보안 목적으로 생성된다.
    - Challenge는 클라이언트 앱에서 생성되어 서버로 전달되며, 서버는 해당 Challenge을 사용하여 클라이언트 앱의 요청을 인증하고 검증한다. 서버는 Challenge과 attestation 객체를 결합하여 App Attest 검증을 수행하고, 인증 결과에 따른 Assertion을 클라이언트 앱에 반환한다.
    - Challenge는 클라이언트 앱과 서버 간의 통신에서 중요한 역할을 수행한다. 이를 통해 클라이언트 앱의 요청과 서버의 응답이 일치함을 확인하고, 앱의 신뢰성을 검증할 수 있다.
- Assertion
    - 서버로부터 받은 앱의 인증 결과를 나타내는 것
    - "Assertion"은 서버로부터 반환된 앱의 인증 결과를 나타낸다. 이는 클라이언트 앱이 App Attest 서비스를 통해 서버에 제공한 attestation 객체의 유효성을 검증하고, 그 결과를 서버로부터 전달 받은 것이다.
    - 앱에서 Assertion은 암호화된 형태로 제공되며, 클라이언트 앱은 서버에서 받은 Assertion을 사용하여 앱의 인증 여부를 확인할 수 있다. 
    - 앱은 Assertion을 서버로 전송하여 서버에서 추가적인 검증을 수행하거나, 해당 인증 결과를 사용자에게 보고할 수 있다.


### 다트 예시
```Dart
private func handleAppAttestServiceAttestKey(_ arg: [String: Any?], result: @escaping FlutterResult) {
    guard #available(iOS 14.0, *) else {
        result(flutterError(code: "unavailable",  message: "Only available in iOS 14.0 or newer." details: nil))
        return
    }
    let keyId = arg["keyId"] as! String
    let clientDataHash = (arg["clientDataHash"] as! Flutter StandardTypedData).data
    DcAppAttestService.shared.attestKey(keyId, clientDataHash: clientDataHash) { object, error in
        if let error = error{
            result(getFlutterError(error))
            return
        }
        result(object)
    }
}
```

## AppAttest 에서 확인하는 세가지 
Genuine Apple device: 실제 iOS 디바이스인지 
Authentic application identity: 실제 Developer가 개발한 앱이 맞는지 
Trustable payload: App Attest 할때 보낸 payload 가 변조된 것이 아닌게 맞는지 
 

## 세팅 절차
해당 서비스르르 이용하기 위해서는 Developer사이트에 등록된 App ID가 있어야 한다. 
1. Create an App Attest Key 
2. Attest and verify key
3. Generate and verify assertion 

## 앱의 무결성 설정
앱이 손상되면 변조된 결과를 일으킬 수 있기때문에 자체적으로 보안 검사를 수행해야만 한다. 
- 앱에서 하드웨어 기반 암호화 키를 생성
- AttestService를 이용하여 인증된 키를 상용해 서버요청에 암호화 서명을 한다.

<img width="700" alt="스크린샷 2023-05-16 오후 5 00 59" src="https://github.com/isGeekCode/TIL/assets/76529148/e3711bb1-9d4d-4436-9d59-97d99095fc01">
<p align="center">이미지 출처 : Apple Document</p>  


### Check for availability
모든 기기에서 App Attest 서비스를 할 수 있는게아니기 때문에 서비스 액세스 전에 앱에서 호환성 검사를 실시한다.

```swift
import DeviceCheck

let service = DCAppAttestService.shared

if service.isSupported {
    // Perform key generation and attestation.
} else {
    // Handle callback as untrust device
    print("This device is not trusted.")
}
// Continue with server access.

```

### key pair 생성
앱을 실행하는 각 기기의 각 사용자 계정에 대해 메서드를 호출하여 하드웨어 기반의 고유한 암호화 키 쌍을 생성한다.
```swift
let service = DCAppAttestService.shared

service.generateKey { keyID, error in
    guard error == nil else {
        print("error: \(error?.localizedDescription)")
        return
    }
    if let keyID = keyID {
        print("keyID: \(keyID)")
        // keyID: 3kdkksk335kk21lps+LEffgKFHFjdjhfV
        // Cache keyId for subsequent operations.
    }
}
```

- 성공시, 메서드의 completion Handler가 키에 액세스하는 데 사용할 keyID(식별자)를 반환한다. 
- keyID 없이는 키를 사용할 수 없고 나중에 식별자를 가져올 수 없기 때문에 영구 저장소에 식별자를 기록한다(예: 파일에 기록).
- 장치는 연결된 개인 키를 Secure Enclave에 자동으로 저장한다.

App Attest 서비스는 이 키를 사용하여 서명을 생성할 수는 있지만 그 밖에 어떤 프로세스도 읽거나 수정할 수 없으므로 보안이 보장된다.

- 이 부분 분석 필요
App Clip에서 키 페어를 생성하면 해당 앱에서 동일한 키 페어를 사용합니다. 이를 지원하려면 전체 앱에서 액세스할 수 있는 공유 컨테이너에 식별자를 저장해야 합니다. App Clip과 정식 앱 간의 데이터 공유에 대한 자세한 내용은 App Clip과 정식 앱 간에 데이터 공유를 참조하세요 .

- 보안이 약화되기 때문에 여러 사용자간에 키를 재사용하지 말아야한다.
- 특히 변조된 앱을 실행하는 여러 사용자에게 서비스를 제공하는데에 어려워지기 때문이다. 




### App Attest 서비스 사용준비
보안 보호가 약화되므로 장치의 여러 사용자 간에 키를 재사용하지 마십시오. 특히 손상된 버전의 앱을 실행하는 여러 원격 사용자에게 서비스를 제공하기 위해 손상된 단일 장치를 사용하는 공격을 탐지하기가 어려워지기 떄문이다. [자세한 내용은 Assessing Fraud Risk를 참고](https://developer.apple.com/documentation/devicecheck/assessing_fraud_risk)  

### 키 쌍의 유효성 인증하기
키 쌍을 사용하기전에 이 키쌍의 출처를 증명하기 위해 Apple에 요청하는 과정이다.
증명 결과를 확인하는 앱의 로직을 신뢰할 수 없기 때문에 결과를 서버로 보낸다.
이 절차 중에 재차 공격의 위험을 줄이기 위해 서버에서 고유한 일회성 챌린지의 hash를 포함하게 된다. CryptoKit의 구현을 사용해 생성가능하다.

```swift
import CryptoKit

let challenge =  <# Data from your server. #>
let hash = Data(SHA256.hash(data: challenge))
```

이후 이전 섹션에서 만든 키쌍과 해시를 이용해 증명을 시작한다.
```swift
service.attestKey(keyId, clientDataHash: hash) { attestation, error in
    guard error == nil else { /* Handle error and return. */ }

    // Send the attestation object to your server for verification.
    // if  you communicate with your server by generating text-based HTTPS  queries, convert the attesation object to a Base64-encoded string first
}
```

### request를 이용하여 어설션하기



## 대규모 사용자가 있는 서비스의 경우
대규모 사용자 기반이 있는 경우 단계적으로 App Attest를 활성화하는 것이 좋다. 
앱이 호출하면 (일반적으로 기기당 사용자당 한 번 수행) DeviceCheck 프레임워크는 앱증명을 수행하기 위해 Apple 서버를 호출하게 된다. 
App Attest를 활성화하는 앱 업데이트를 동시에 받는 사용자가 많은 경우, Apple 서버애서 특정 앱의 증명 트래픽을 제한할 수 있다.

## 참고링크
- [AppleDocument: DeviceCheck Framework ](https://developer.apple.com/documentation/devicecheck)
- [Blog - [iOS/WWDC] App Attest & Device Check](https://jooeungen.tistory.com/entry/iOSWWDC-App-Attest-Device-Check)
- [WWDC21: Mitigate fraud with App Attest and DeviceCheck(App Attest와 DeviceCheck로 사기를 방지하자)](https://developer.apple.com/videos/play/wwdc2021/10244/)
- [WWDC21: Safeguard your accounts, promotions, and content(계정, 프로모션 및 콘텐츠 보호)
](https://developer.apple.com/videos/play/wwdc2021/10110)
-[Apple App Attest를 사용하여 iOS 앱 진위 확인](https://blog.restlesslabs.com/john/ios-app-attest)
-[플러터로 구현한 App Attest 발표내용](https://conference.hitb.org/hitbsecconf2021sin/materials/D1T2%20-%20Fooling%20Apple%20AppAttest%20API%20-%20Igor%20Lyrchikov.pdf)
## History
- 230516 : INIT

장점
1) 재생 공격에 대해 유망해 보입니다
2) 특정 기업은 부정 행위 측정 기준을 구현함으로써 혜택을 누릴 수 있습니다
분석, 특히 Apple이 메트릭 데이터 목록을 확장하는 경우
3) 추가 계층으로 변조 방지 보호 기능을 향상시킬 수 있습니다
이미 사용 중인 경우 바이패스 복잡성을 활용하여 보안 강화
구현된 RASP 검사
4) 100%에서 지원되면 업계 표준이 될 수 있음
iOS 기기

단점
1) 손상된 장치에서 응용 프로그램이 이미 실행 중인지 확인할 수 없습니다
2) 키 증명 후 장치가 JailBroken된 경우 모든 새 주장은
변조됨 - Apple의 사기 측정 기준을 사용하더라도 탐지할 수 없음
3) 런타임을 사용한 애플리케이션의 동작 수정에 대해 유용하지 않습니다
계측 프레임워크/디버거
4) 여러 설계 문제 - 구현의 성공 여부는 크게 다음과 같습니다
통합자의 구현
5) 앱 확장이 앱 증명을 지원하지 않음
6) 타사 종속성 - Apple의 백엔드 서버
7) 지원되지 않는 디바이스 수가 여전히 많습니다
