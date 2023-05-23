# Integrity - App Attest (앱 증명)

iOS App Attests는 앱의 신뢰성을 검증하기 위해 Apple이 제공하는 서비스이다. 이 서비스를 사용하면 앱이 신뢰할 수 있는 기기에서 실행되고 있는지 확인할 수 있다. iOS 14부터 도입된 이 서비스는 앱이 악의적인 조작이나 해킹을 방지하고, 서버와의 통신 중에도 보안성을 강화하는데 도움을 줄 수 있다.

## 지원
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- Mac Catalyst 14.0+
- tvOS 15.0+
- watchOS 9.0+


## WWDC21 - AppAttest & DeviceCheck (번역) 
- [wwdc2021 : AppAttest & DeviceCheck](https://developer.apple.com/videos/play/wwdc2021/10244/)  

### 서문
DeviceCheck API를 사용하게 되면 device unique 라서 앱을 삭제하거나, 심지어 폰 컨텐츠 리셋을 해도 남아 있는데, App Attest는 설치할 때마다 달라진다. 

<img width="800" alt="스크린샷 2023-05-18 오후 3 57 37" src="https://github.com/isGeekCode/TIL/assets/76529148/7c7a30ff-2860-4baa-81a1-b65716a2e4a4">  

우리가 운영중인 서비스의 서버가 있다고 가정해보자.   
이때 어떤 앱으로부터 request를 받으면 이 요청이 운영중인 앱에서 온건지 보장할 수 없다.

App Attest를 사용하면 
앱에서 하드웨어 지원 assertion을 만들어서
request의 일부로 첨부할 수 있다.  


<img width="800" alt="스크린샷 2023-05-18 오후 3 57 46" src="https://github.com/isGeekCode/TIL/assets/76529148/985f484e-3078-413a-8264-939b31e60f50">  
그럼 서버에서는 이 assertion을 이용하여 request가 정품 Apple app에서 온것인지 확인할 수 있다.


### 변조된 앱

몇가지 변조된 앱의 사례를 살펴보자.

1. 여행 중에 특정 아이템을 발견하고 수집하는 위치기반 앱을 디자인했는데 수정된 앱으로 집을 떠나지 않고도 모든 것을 수집할 수 있다는 것을 알게 된 경우

<img width="800" alt="스크린샷 2023-05-18 오후 3 57 37" src="https://github.com/isGeekCode/TIL/assets/76529148/15395163-07c6-48cf-bd2c-b7cf92431e12">  
  
2.  경쟁적인 멀티플레이어 레이싱 게임에서 치트를 사용하여 무제한 부스트를 얻어 다른 사람들이 순위표에서 경쟁하는 경우

<img width="800" alt="스크린샷 2023-05-18 오후 3 57 58" src="https://github.com/isGeekCode/TIL/assets/76529148/97475c1f-d921-49b1-9b4c-2b20672109ac">
  
3.  토요일에 일어나보니 서버에서 엄청나게 많은 요청을 수신한 것을 보았지만, 조사해보니 앱에서 호출이 전혀 오지 않는다는 것을 알게 된 경우

<img width="800" alt="스크린샷 2023-05-18 오후 3 58 06" src="https://github.com/isGeekCode/TIL/assets/76529148/c9c03ba7-b1b8-49c8-87a4-f68817326367">

App Attest 서비스에서는 이런식으로 수정된 버전을 앱의 정품 버전과 식별하여 앱 경험과 비즈니스를 보호할 수 있도록 도와준다.  

## App Attest 서비스의 3가지 특징
App Attest는 개발자와 개발자의 고객을 보호하기위해 아래 3가지의 중요한 포인트를 제공해준다.

- Genuine Apple device : 정품 애플 기기 여부
- Authentic application identity : 인증된 app ID 여부
- Trustable payload : 신뢰할 수 있는 Payload 여부

바꿔말하면 아래와 같다.
- 요청은 정품 Apple 기기에서 왔고
- 정품 App을 실행중이며
- 페이로드가 변조되지않은 상태이다. 

그래서 이 세가지를 충족하여 앱의 적법한 인스턴스에서 요청이 왔는지 확인할 수 있게 된다.
  
  
### 1. 정품 애플 기기 여부 (Genuine Apple device)
- App Attest의 핵심
    - Key pair : 보안키 쌍
    - 애플증명서 : 이 키 쌍이 정품 Apple 기기에서 발생했다는 걸 서명한 애플증명서
  
<img width="800" alt="스크린샷 2023-05-18 오후 3 59 12" src="https://github.com/isGeekCode/TIL/assets/76529148/b84e9c5d-f065-4f61-8800-3a00efbdae60">
  
그리고 발급된 키 쌍 중, 개인 키는 App Attest API를 이용하는 Secure Enclave를 통해서만 접근 / 저장 할 수 있다.

이제 앱에서 서버로 보낼 request에 이 키를 사용하여 서명할 수 있게 되고, 
서버에서는 서명을 통해 받은 request가 정품기기에서 생성된 것인지 확인할 수 있게 된다.

### 2. 인증된 앱 ID 여부 (Authentic application identity)
  
<img width="800" alt="스크린샷 2023-05-18 오후 3 59 29" src="https://github.com/isGeekCode/TIL/assets/76529148/994cf080-b9e9-4603-9983-4eb7d189d618">

Apple기기에서 앱을 실행하기 위해서는 앱에 서명이 필요하다. 그리고 앱을 수정하는 사람은 자신이 제어하는 ID로 다시 앱에 서명해야 한다.
그렇게 되면 반드시 App ID는 수정이 된다. 

<img width="800" alt="스크린샷 2023-05-18 오후 3 59 35" src="https://github.com/isGeekCode/TIL/assets/76529148/4092346c-5f88-4fa8-9ed5-f39417578478">

증명(Attestation)에는 App ID의 해시가 포함되어있다. 
결국 이 App ID를 증명에 포함된 App ID와 비교해서 사용자가 변조된 앱을 사용하고 있는지 확인할 수 있다.

<img width="800" alt="스크린샷 2023-05-18 오후 3 59 41" src="https://github.com/isGeekCode/TIL/assets/76529148/6e07e96f-7c45-4f7a-af24-28360adb4921">
  

이렇게 Request가 정품기기 && 정품앱에서 온 것을 확인했으니 request의 페이로드에 대해 이야기 해보자


### 3. 신뢰할 수 있는 페이로드 여부 (Trustable payload)
페이로드를 신뢰하기 위해 digest의 서명에 대한 어설션을 필요로 한다. 

<img width="800" alt="스크린샷 2023-05-18 오후 3 59 45" src="https://github.com/isGeekCode/TIL/assets/76529148/d639deb0-42e8-49d9-8731-176ea55053d3">


운영중인 서버로 페이로드를 보내기전에, 검증된 키를 사용해서 Payload의 요약(digest)에 서명하는 App Attest를 지시할 수 있다.
그러면 페이로드의 assertion이 생성된다.
  
generate assertion : App Attest에 증명된 키 + 페이로드 요약(digest) 서명

- Assertion data 
    - Signature (서명)
    - Authenticator data (인증자 데이터 섹션)
        - App Identity hash
        - etc properties
  
> 참고
>> 페이로드는 데이터나 메시지의 실제 내용을 가리키며, 다이제스트는 해당 페이로드의 요약 또는 축약된 버전이다. 
>> 다이제스트는 일반적으로 해시 함수를 사용하여 생성된다. 해시 함수는 임의의 크기의 데이터를 고정된 크기의 일련의 바이트로 변환하는 알고리즘이다. 페이로드의 작은 변화가 다이제스트에 큰 변화를 일으키는 특성을 가지고 있다. 
>> 따라서 다이제스트를 통해 페이로드의 무결성을 확인하거나, 페이로드를 식별하거나 비교하는 등의 용도로 사용될 수 있다.


<img width="800" alt="스크린샷 2023-05-18 오후 3 59 57" src="https://github.com/isGeekCode/TIL/assets/76529148/42aab934-5298-4db0-9a6f-f208b2395350">

그리고 앱에서 payload와 assertion을 운영중인 서비스 서버로 전송한다.

서버에서 페이로드에 대한 assertion을 확인하면, 페이로드가 전송 중에 변조되지않았다는 것을 신뢰할 수 있다.

여기까지 App Attest 서비스의 3가지 특징 및 간단한 로직을 설명해 보았다.

## Privacy
  
- 증명은 익명이다.
- 인증키는 설치당 고유값을 가진다.
이제 프라이버시에 대해 이야기해보자

  
<img width="800" alt="스크린샷 2023-05-18 오후 4 00 07" src="https://github.com/isGeekCode/TIL/assets/76529148/d32350ff-d6d1-4e05-b4b0-eacf2ef6406b">


Apple에서는 Privacy가 건강한 앱 생태계의 필수 기반이라고 믿고 있다.
  
그래서 App Attest의 각 요소는 개인 정보 보호를 염두해 두고 구축되었다.
  
또한 이 증명은 추적을 방지하면서 정품 장치에 대한 보증을 제공하도록 설계되었다.

### 증명(Attestations)은 익명이다.

증명(Attestation)은 익명이며 하드웨어 식별자를 포함하지않는다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 00 30" src="https://github.com/isGeekCode/TIL/assets/76529148/70ab7794-9919-4765-81c5-4969968135ac">

  
### 인증키는 설치당 고유값을 가진다.

App Attest키는 앱 설치마다 고유한 값을 가진다. 이 말은 App Attest키는 앱 재설치를 하게되면 유지되지않고 백업되지 않으며 기기간에 동기화 되지 않는다는 말이다.  
그래서 앱 개발자는 앱을 구축할 떄 이 점을 염두해야한다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 00 35" src="https://github.com/isGeekCode/TIL/assets/76529148/bf86fff2-c26f-4f1c-8737-4298c8caf5d8">


## 세팅 절차
 
**App Attest를 앱에 세팅하는 단계 : App-Side**
 1. Create an App Attest Key : App Attest 키 생성
 2. Attest and verify key : 키 증명 및 확인
 3. Generate and verify assertion : 어설션 생성 및 확인

## 1. Create an App Attest Key

### 1.1 App Attest 키 생성
모든 App Attest 호출은 isSupported 속성으로 보호되어야한다.
```swift
let service = DCAppAttestService.shared
if service.isSupported {

    // 키 생성 및 attestation 수행.
    service.generateKey { keyId, error in
        guard error == nil else { /*  Handle the error */ }
        // 후속작업을 위해 keyId을 Cache 
}
    
} else {
    // Handle fallback 신뢰할 수 없는 장치로서 처 리
}
```

App Attest는 Secure Enclave가 있는 장치에서 지원되지만 isSupported가 여전히 false를 반환하는 App Extensions와 같은 경우가 있을 수 있다!! 
때문에 앱에서는 이러한 경우를 정상적으로 처리해야한다. ( isSupported의 else 부분 )
액세스를 곧바로 차단하는 대신에 실패를 위험신호(risk signal)로 사용해야 한다. 8:32

### IsSupported가 false인 경우에 대하여
- 위험 평가를 위한 신호로 사용 (risk assessment)
- 모니터링에서 지원하지않는 기기가 급증하는 반응

방법1. 신뢰할 수 없는 기기 여부
호출자(caller)를 신뢰할 수 없는 것(untrusted)으로 분류한다.
그다음 위험평가 논리(risk assessment logic)에 따라 클라이언트가 중요한 기능을 사용하도록 허용할 지의 여부를 평가한다. 위험평가 논리.... 는 다른 글 참고해보기..

방법2. 모니터링
또다른 접근 방식은 서비스를 호출할 때 App Attest를 지원하지 않는다고 주장하는 장치의 갑작스러운 증가를 모니터링을 하는 것이다.
App Attest를 지원하는 장치의 비율이 갑자기 감소하면 수정된 앱이 확인을 우회하려고 시도하는 신호일 수 있다.
  
이제 App Attest키가 성공적으로 생성되었으므로 계속해서 키를 증명해보자
  
  
## 2. Attest and verify key : 키 증명 및 확인

### 2.1 생성된 키 증명하기
  
<img width="800" alt="스크린샷 2023-05-18 오후 4 01 35" src="https://github.com/isGeekCode/TIL/assets/76529148/4c3cfa14-1cbc-4bd9-9d23-1b19a7ae589c">

### 2.1.1 서버에서 챌린지 발행
중간자 공격 (MITM;man-in-the-middle Attack)이나 재생 공격(Replay Attack)을 방지하려면 일회성 서버 챌린지가 필요하다.
그렇기 때문에 서버에서 앱에 대한 챌린지를 발행한다. 
  
이 챌린지 값은 임의 문자열 또는 UUID이면 충분하다. 서버에서는 이 챌린지 값을 클라이언트(앱)로 보내기전에 저장을 하고 후에 다시 사용한다. 

<img width="800" alt="스크린샷 2023-05-18 오후 4 01 40" src="https://github.com/isGeekCode/TIL/assets/76529148/b4633c89-e6f9-47a5-9586-1b92a5ff192f">


### 2.1.2 챌린지로 해시를 생성

증명(Attestation)을 사용자 계정 혹은 기타 값과 연결하기 위해서는, 그에 해당하는 값을 챌린지와 함께 해시하여 clientDataHash를 만든다.

```swift
// 음.. 요청값(계정) + 타임스탬프?  이렇게 하면 해당값 지정이 가능할까??
let challenge = "textString" //  Challenge string from your server

guard let challengeData = challenge.data(using: .utf8) else { return }
let hash = Data(SHA256.hash(data: challengeData))
```

### 2.1.3 attestKey API 호출

이제 이전 단계에서 만든 keyId와 clientDataHash를 사용하여 attestKey API를 호출할 수 있다.

```swift
// Generate key attestation
appAttesService.attestKey(keyId, clientDataHash: hash) { attestationObject, error in
    guard error == nil else { /* Handle error and return. */ }
    // 검증을 위해 attestationObject를 서비스서버로 전송
}
```

attestKey함수를 사용하면, 개인키를 사용하여 device에 대한 하드웨어 검증 요청(Hardware attestation request)을 생성한다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 02 16" src="https://github.com/isGeekCode/TIL/assets/76529148/30ade3ca-02b3-4483-873f-b0c444f66a7c">  

생성된 request를 확인하기 위해 Apple Server로 제출한다.  
확인이 되면 Apple에서는 익명의 증명 객체(AttestationObject)를 앱으로 반환한다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 02 31" src="https://github.com/isGeekCode/TIL/assets/76529148/a78b0c56-8e6c-49e8-95f2-74f97d7793e9">


### 2.1.4 리턴받은 Attestation과 사용자 정의 페이로드를 서비스 서버로 전송

검증을 위해서 Attestation과 사용자 정의 페이로드를 서비스 서버로 전송.

<img width="800" alt="스크린샷 2023-05-18 오후 4 02 39" src="https://github.com/isGeekCode/TIL/assets/76529148/deb03f70-8fa0-4af1-a46a-fbd9bae535c2">

## 2.2 Verify Key attestation

이제 앱에서 증명을 서버로 보냈으니 확인해보자

증명(attestation)은 웹 인증 표준을 따르며 Apple에서 서명한 인증서 목록, 인증자 데이터 구조, 위험지표 수신(Risk metric receipt) 이렇게 세 부분으로 구성되어있다.
  
   
<img width="800" alt="스크린샷 2023-05-18 오후 4 02 50" src="https://github.com/isGeekCode/TIL/assets/76529148/ccb585b7-9693-4297-8929-87200576c948">


그럼 확인 해야할 중요한 부분을 살펴보자.
- Attestation
    - 인증서 (Certificate)
    - 인증자 데이터 (Authenticator data)
    - 위험측정지표 영수증(Risk metric receipt)
    
### 1. Certificate 섹션

<img width="800" alt="스크린샷 2023-05-18 오후 4 03 05" src="https://github.com/isGeekCode/TIL/assets/76529148/261bff91-6a24-4566-97ae-5cbd19b07451">

인증서 섹션에는 리프(Leap certificate)와 중간 인증서(intermediate cetrificate)가 포함되어있다.
App Attest 루트인증서는 Apple Private PKI 저장소(Repository)에서 사용할 수 있다.

이렇게 전체 인증서 체인의 유효성을 검사하면 장치가 정품 Apple 장치임을 알 수 있다.


### 인증서관련 용어 설명
- 인증서 (Certificate)
    - 인증서는 디지털 신원을 확인하고 신뢰할 수 있는 정보를 제공하는 디지털 문서. 암호화와 인증에 사용되며, 보통 공개키 인증서 형식으로 구성된다. 인증서는 개인 키와 해당 개인 키와 연결된 공개 키, 소유자(서브젝트)의 신원 정보 등을 포함한다.
    
- 리프 인증서 (Leaf Certificate)
    - 리프 인증서는 인증 체인의 가장 하위에 있는 인증서로, 앱 attestation에 사용되는 인증서
    - 앱의 디바이스 고유 식별자와 암호화된 페이로드를 포함하며, 서명되어 있다.

- 중간 인증서 (Intermediate Certificate)
    - 중간 인증서는 리프 인증서와 루트 인증서 사이에 있는 인증서
    - 인증 체인에서 중간 단계의 신뢰를 구축하는 데 사용된다.
    - 보통 루트 인증서로부터 서명된 상위 인증 기관에 의해 발급된다.
    - 앱 attestation에서 중간 인증서는 리프 인증서의 유효성을 검증하고, 신뢰할 수 있는 소스로부터 받은 인증서인지 확인하는 데 사용된다.

- 루트 인증서 (Root Certificate)
    - App Attest 루트 인증서는 앱 attestation에서 사용되는 최상위 인증서.
    - Apple Private PKI 저장소(Repository)에서 사용할 수 있는 인증서로, Apple이 제공하는 인증 기관에 의해 서명된다.
    - 루트 인증서는 앱의 신원을 검증하고 유효성을 확인하여, 보안과 신뢰성을 제공하는 데 사용된다.

- App Private PKI Repository
    - Apple의 사설 공개 키 인프라(Private Key Infrastructure) 저장소.
    - PKI는 암호화와 인증을 위한 키, 인증서 및 관련 서비스를 관리하는 시스템이다.
    - Apple은 앱 attestation과 같은 보안 기능을 위해 독자적인 PKI 시스템을 운영하고 있습니다.
    - Apple Private PKI 저장소는 Apple이 직접 관리하며, 인증서의 발급과 관리에 사용된다.
    - Apple은 자체 인증 기관을 운영하고, 이를 통해 인증서를 발급하고 앱 attestation과 같은 서비스에서 사용할 수 있다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 03 17" src="https://github.com/isGeekCode/TIL/assets/76529148/7f3d4dc5-d7bd-4de7-b2ab-88254c1a40d5">

이전단계 2.1.3 에서 `attestKey()`를 호출하면 clientDataHash 및 기타 데이터에서 nonce라고 하는 일회용 해시가 생성되고, 

이 nonce는 리프인증서에 포함된다.

그리고 변조를 방지하기 위해 nonce를 서버에서 재구성하고, 일치하는지 확인한다.

### 2. Authenticator data 섹션

<img width="800" alt="스크린샷 2023-05-18 오후 4 03 33" src="https://github.com/isGeekCode/TIL/assets/76529148/17dc9b84-dd60-40b4-98ab-23fc199a879f">  

인증자 데이터 섹션에는 `순정 앱에서 보낸 요청인지 식별하는 데`에 사용할 수 있는 앱 ID 해시값과 그밖의 여러 속성이 포함되어 있다.

### 3. Risk metric receipt 
Key Attestation의 마지막 섹션에는 Risk metric receipt이 포함되어있다.

이는 한번 저장한 다음, 나중에 Apple에 위험 메트릭을 요청하는데 사용할 수 있는 영수증이다. 이에 대한 자세한 내용은 뒤에 다루도록하자.

여기까지 이 모든것이 확인되면, 이 App Attest Key가 정품인 것이 증명됐다.
그다음엔 후속요청을 확인하는데 사용할 클라이언트 데이터와 연결된 키를 저장한다.

그런데 여기까지 발생할 수 있는 모든 실패가 잘못된 증명으로 인한 것은 아니다. 
isSupported에서 false를 리턴받거나 ramp up중에 제한되는 경우, 일반적인 네트워크 오류와 같은 시나리오를 적절하게 처리한다. 

그런다음 전체 위험 평가(overall risk assessment)에서 오류를 신호로 통합할 수 있다.
이러한 확인 구현에 대한 자세한 내용은 설명서를 참고 할 것

## 대규모 설치에 관하여

![스크린샷 2023-05-18 오후 4 38 00](https://github.com/isGeekCode/TIL/assets/76529148/79c4f2c9-43bd-4519-b710-676130d7dbbc)

attest-Key API를 호출하면 앱에서 App Attest 서비스로의 네트워크 호출이 생성된다. 이는 앱 인스턴스당 한 번만 발생한다. 그러나 대규모 설치 기반이 있는 경우 집합적으로 앱이 App Attest에 많은 요청을 보낼 수 있다.
리소스를 관리하고 속도제한을 피하려면 전체 설치 기반에서 이 기능을 점진적으로 활성화해야한다.

예를 들어 일일 활성 사용자가 백명이라면 아마 하루정도에 걸쳐 증가할 수 있다.
만약 일일 활성 사용자가 10억명이라면 !! 한달 이상에 걸쳐 증가해야한다.

!! 이말은 아마 기간적이나 양적이나 애플에서 추가할 수 있는 양이 정해져 있다는 말인 것 같다.
  
## 3. Generate and verify assertion : 어설션 생성 및 확인


```swift
// Generate and verify assertions
appAttestService.generateAssertion(keyId, clientDataHash: hash) { assertionObject, error in 
    guard error == nil else {/*Handle error and return */}
    
    // Send assertion object with your server for verification
}
```

### 3.1 Generate assertion
![스크린샷 2023-05-18 오후 4 39 23](https://github.com/isGeekCode/TIL/assets/76529148/9fa8e097-176f-4c09-8a1a-b021462c5eb1)

증명된 키가 있으므로 이제 generateAssertion API호출을 이용하여 앱과 서버간의 민감한 통신을 보호할 수 있다.

이제 어설션 흐름은 Apple서버가 더이상 관련되지않으므로 증명보다 간단해진다.
키를 사용하는 모든 어설션은 장치(device)에서 생성되고 서버에서 검증된다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 05 05" src="https://github.com/isGeekCode/TIL/assets/76529148/1a31d3af-0ff0-449f-b2d6-66a4a957c955">

서버에서 고유한 챌린지를 요청하여 시작한다음 페이로드 다이제스트를  생성하고 generateAssertion을 호출한다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 06 15" src="https://github.com/isGeekCode/TIL/assets/76529148/0ddaa160-6be4-4b3a-a3b4-b5257e0b2302">

generateAssertion은 다이제스트를 사용하여 nonce를 계산하고 App Attest키로 서명한다.

그러면 앱에서 페이로드와 어설션을 서버로 보낼 수 있게된다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 06 19" src="https://github.com/isGeekCode/TIL/assets/76529148/9d4a6cef-edc4-408b-8c68-616196917f6b">


마지막으로 서버에서 페이로드를 확인해야한다. 

### 어설션의 페이로드

<img width="800" alt="스크린샷 2023-05-18 오후 4 06 25" src="https://github.com/isGeekCode/TIL/assets/76529148/7aaee9f9-3a95-4358-a253-94989593c8e0">

어설션의 페이로드에는 이 상위 수준 구조가 포함되어있다.
- Assertion data
    - Signature (서명)
    - Authenticator data (인증자 데이터 섹션)
    
<img width="800" alt="스크린샷 2023-05-18 오후 4 03 05" src="https://github.com/isGeekCode/TIL/assets/76529148/7b689b33-f76a-4185-ae28-524ad9ba83ba">   
    
서명의 유효성을 검사하려면 서버에서 nonce를 재구성하는 프로세스를 역순으로 수행한다.
그 다음 공개키를 이용하여 서명을 확인한다. 
서명이 유요하면 페이로드가 수정되지않았음을 신뢰할 수 있다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 07 15" src="https://github.com/isGeekCode/TIL/assets/76529148/d2e62c7b-20ed-42f0-8249-ffd5738b00d4">
  
    
인증자 데이터 섹션에는 앱 ID 해시가 포함되어있다. 어설션이 정품앱에서 온 것인지 확인하려면 해시를 검증하자

<img width="800" alt="스크린샷 2023-05-18 오후 4 07 22" src="https://github.com/isGeekCode/TIL/assets/76529148/0d7a2458-7e7c-446b-aaf4-3920ba8724b4">
이 인증자 데이터에는 지속적으로 증가하는 카운터도 포함된다.
재생공격 (Replay Attack)으로부터 보호하려면 카운터 값을 서버에 저장하고 후속 요청이 있을 때마다 값이 증가할 것으로 예상하자.


<img width="800" alt="스크린샷 2023-05-18 오후 4 07 30" src="https://github.com/isGeekCode/TIL/assets/76529148/2a2678dc-25e8-48e7-90d7-7e53d2c60324">

키를 사용하면 이제 이 과정을 필요한 만큼 반복할 수 있다.
어설션 생성은 Apple 서버를 호출하지 않지만 약간의 대기시간을 추가하는 암호화 작업이다.
App Attest를 앱에 통합할 때 이 점을 앱 디자인에 고려해야한다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 07 46" src="https://github.com/isGeekCode/TIL/assets/76529148/14948890-efb2-4027-b5f1-13d89e1c904b">

어설션은 중요하지만 빈도가 낮은 호출이나 추가 대기시간 및 필요한 계산을 처리할 수 있는 호출에 적합하다.
빈번한 실시간 네트워크 명령의 경우 어설션이 적합하지않을 수 있다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 07 50" src="https://github.com/isGeekCode/TIL/assets/76529148/3156a0d9-6370-4408-8014-b69056772a27">

이렇게 하면 App Attest의 기본 구현이 완료됐다.
여기까지의 구현만으로도 들어오는 서버 request를 원본 인지 수정된 것인지 분류하고, 이 사기 감지 신호를 비즈니스 로직에 합칠 수 있다.

하지만 추가적으로 해야하는게 있다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 08 02" src="https://github.com/isGeekCode/TIL/assets/76529148/c1d3184d-6497-4228-a662-f2ae6821351a">

공격자가 한 기기를 이용하여 많은 수의 App Attest키를 생성하고 이 기기를 이용하여 조작된 많은 앱과 서버간의 통신을 제공함으로서 App Attest를 우회하려고 시도할 수가 있다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 08 05" src="https://github.com/isGeekCode/TIL/assets/76529148/13cf4439-2a54-498a-966f-cc641a9de93d">

이러한 동작을 감지하는데 도움이 되도록  Apple 에서는 기기에서 생성된 대략적인 키 수를 제공하는 App Attest Risk Metric Service라는 서비스를 제공한다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 08 23" src="https://github.com/isGeekCode/TIL/assets/76529148/07c6dce3-e1d5-452c-92e8-b2598334b1e8">

attestKey는 증명(attestation)과 위험 메트릭 영수증을 반환한다. 
서버는 해당 영수증을 서비스에 제출하고 새 영수증으로 교환할 수 있다.

이 새로운 영수증에는 위험지표(risk metric)가 포함된다.
그래서 주기적으로 해당 앱/device 쌍에 대해 업데이트된 메트릭에 대한 최신 영수증을 사용할 수 있다.

다음은 영수증 구조에 대한 개요다.

### Risk metric receipt
- Payload
- Certificate chain
- Signature
 <img width="800" alt="스크린샷 2023-05-18 오후 4 08 29" src="https://github.com/isGeekCode/TIL/assets/76529148/eac09339-018e-4788-99b5-79eb5f390551">

이건 PKCS7 컨테이너다. 더 자세한 내용은 DeviceCheck Framework 공식문서의 Assessing Fraud 아티클을 참조하자.

## App Clips
<img width="800" alt="스크린샷 2023-05-18 오후 4 08 36" src="https://github.com/isGeekCode/TIL/assets/76529148/c6abdb1d-f67b-44a0-a3f6-962852c7175f">
iOS15의 App Clip에 App Attest 지원이 추가되었다.

<img width="800" alt="스크린샷 2023-05-18 오후 4 08 42" src="https://github.com/isGeekCode/TIL/assets/76529148/dffe7d63-2ae6-427d-907b-de394c582923">
App Clip에서 전체 앱으로의 원활한 업그레이드를 지원하기 위해 App Clip과 full app 은 App AttestContext에서 동일한 App ID를 공유한다.  
서버측에서 앱 ID를 확인할 때 이 점을 명심하자.
App Clip이 수동으로 제거되거나 만료되면 full 앱이 제거될 때와 마찬가지로 해당키가 무효화 된다.

## Keys to success
- Importance of server-side validation
- One-time server challenges
- Failures as signals
이제 App Attest의 성공을 위한 핵심을 기억하자

- device가 아닌 서버에서 유효성을 검사한다.
    - Validation 코드를 비활성화 하도록 앱을 수정할 수 있다.
- 네트워크 재생공격(replay attack)을 방지하기 위해 Flow에 일회성 서버 챌린지를 적용한다.
- isSupported에서 false를 리턴받거나, ramp up중에 제한되어지는 것, 또는 일반적인 네트워크 오류와 같은 시나리오를 적절하게 처리한다. 
    - 그리고 위험평가에서 실패를 신호로 통합한다.

<img width="600" alt="스크린샷 2023-05-18 오후 4 54 47" src="https://github.com/isGeekCode/TIL/assets/76529148/c5bd14cf-1ea5-4843-a8b5-89d0bee72012">
-끝-



## 보안 키 쌍
- 개인키는 앱네 secure Enclave에 보관되다가 App Attest 서비스와의 통신에 사용된다. 
- 공개키는 앱에서 App Attest 요청을 생성할때 Apple서버로 전송된다. 
- 이 키쌍은 보안을 강화하기위해 모두 개발자가 직접 볼수가 없도록 설계되어있다.

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
    - 서버로부터 받는 challenge 값은 서버에서 클라이언트 앱으로 전달되는 임의의 데이터이다. 이 데이터는 앱의 무결성을 확인하기 위한 고유한 challenge 데이터로 사용된다. 서버는 이 challenge 값을 클라이언트 앱에게 전달하고, 클라이언트 앱은 해당 challenge 값을 사용하여 암호학적인 해시를 생성한다.
    - challenge 값은 보안을 강화하기 위해 서버에서 생성되어야한다. 이 값은 각 클라이언트 앱마다 고유해야 하며, 예측할 수 없는 난수 또는 임의의 데이터로 구성되어야 한다. as.
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



## 코드 예시
```
import DeviceCheck
import CryptoKit

let service = DCAppAttestService.shared

if service.isSupported {
    service.generateKey { keyId, error in
        guard error == nil else {
            // 오류 처리
            return
        }
        
        // keyId를 사용하여 필요한 작업 수행
        // keyId를 저장하여 이후 작업에 사용
        
        // 예시로 keyId를 출력
        print("Generated keyId: \(keyId)")
        
        // 서버로부터 challenge를 받는 로직 구현
        fetchChallenge { challenge, error in
            guard let challenge = challenge, error == nil else {
                // 도전 데이터 요청 오류 처리
                return
            }
            
            let hash = Data(SHA256.hash(data: challenge))
            
            service.attestKey(keyId, clientDataHash: hash) { attestation, error in
                guard error == nil else {
                    // 오류 처리
                    return
                }
                
                // attestation 객체를 서버로 전송하여 검증합니다.
                // 서버에서 추가적인 검증 절차를 수행합니다.
                
                // 예시로 attestation 객체 출력
                print("Attestation: \(attestation)")
                
                // 서버로 attestation 객체를 전송하는 로직 구현
            }
        }
    }
}

/// 서버로부터 challenge를 요청하는 함수
func fetchChallenge(completion: @escaping (Data?, Error?) -> Void) {
    guard let url = URL(string: "http://서버주소/challenge") else {
        completion(nil, NSError(domain: "InvalidURL", code: 0, userInfo: nil))
        return
    }
    
    URLSession.shared.dataTask(with: url) { data, response, error in
        guard let data = data, error == nil else {
            completion(nil, error)
            return
        }
        
        completion(data, nil)
    }.resume()
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
