# Integrity - App Attest (앱 증명)

iOS App Attests는 앱의 신뢰성을 검증하기 위해 Apple이 제공하는 서비스이다. 이 서비스를 사용하면 앱이 신뢰할 수 있는 기기에서 실행되고 있는지 확인할 수 있다. iOS 14부터 도입된 이 서비스는 앱이 악의적인 조작이나 해킹을 방지하고, 서버와의 통신 중에도 보안성을 강화하는데 도움을 줄 수 있다.

DeviceCheck API를 사용하게 되면 device unique 라서 앱을 삭제하거나, 심지어 폰 컨텐츠 리셋을 해도 남아 있는데, App Attest는 설치할 때마다 달라진다. 


## 지원
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- Mac Catalyst 14.0+
- tvOS 15.0+
- watchOS 9.0+

## 작동 흐름
- 클라이언트 앱은 앱 서버로부터 인증 요청을 받는다. 이 인증 요청으로 앱이 신뢰할 수 있는 기기에서 실행되는지 확인한다.
- 클라이언트 앱은 앱 서버로부터 받은 인증 요청을 Apple의 서버로 전송.
- Apple의 서버는 클라이언트 앱에서 전송된 인증 요청을 받는다.
- Apple의 서버는 해당 기기의 고유한 식별자와 함께 앱이 실행 중인지 확인하기 위한 보안 검증을 수행. 이 검증은 기기의 Trusted Execution Environment (TEE)에서 이루어진다.
- Apple의 서버는 결과를 생성하고 해당 결과를 클라이언트 앱으로 전송. 이 결과는 앱이 신뢰할 수 있는 기기에서 실행 중인지 여부를 나타낸다.
- 클라이언트 앱은 Apple의 서버로부터 받은 결과를 앱 서버로 전송.
- 앱 서버는 결과를 확인하고, 필요에 따라 앱의 동작을 조정할 수 있다. 예를 들어, 앱 서버는 인증이 성공한 경우에만 특정 기능을 사용할 수 있도록 허용할 수 있다.


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
}
```




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


## History
- 230516 : INIT
