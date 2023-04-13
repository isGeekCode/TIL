# Integrity - 인증서(.p8, .p12 / Development, Distribution / Producation SSL / Development SSL )


## 앱과 관련된 정보는 Apple Developer에서 확인 가능

[Apple Developer 사이트링크](https://developer.apple.com/)에서 Account를 클릭

- 앱스토어 등록시 관련된 정보를 보려면 App Store Connect에서 확인이 가능하다.
- 개발, 테스트 및 배포하는데 필요한 인증서, 식별자, 프로파일 및 기기관리 
- 베타 소프트 웨어 등등의 추가 리소스 확인 가능

인증서의 종류에는 p8과 p12가 있으며, 각각의 용도에 따라 Development Certificate과 Distribution Certificate이 있다. 또한 SSL 인증서는 HTTPS 프로토콜을 사용하기 위해 필요한 인증서로, Production SSL Certificate와 Development SSL Certificate가 있다.

인증서를 생성하는 방법에도 차이가 있으며, 각각의 생성 방식에 따라 p8 형식과 p12 형식으로 나누어진다.

## 앱 개발시 필수적인 인증서

- 개발자 인증서(Development Certificate)
    - 앱 개발 및 테스트에 필요한 인증서. 이 인증서는 디바이스에 앱을 설치하거나 디버그하기 위해 사용된다. 개발자가 개발 중인 앱을 테스트하고, Xcode와 같은 개발 도구를 사용하여 디바이스에 앱을 설치하거나 디버그하는 데 필요하다.

- 배포 인증서(Distribution Certificate)
    - 앱을 앱스토어 또는 기업 배포 시스템에 업로드하고 배포할 때 사용된다.


## 추가적으로 사용하는 인증서

- Apple Push Notification Service (APNs) 인증서
    - iOS에서 푸시 알림을 보내기 위해 사용된다. APNs 인증서는 앱의 서버에서 APNs 서버로 보내는 모든 푸시 알림에 대한 보안 인증을 제공한다.

- + 인터넷 인증서
    - 인터넷 연결이 필요한 경우 사용된다. HTTPS와 같은 보안 연결을 설정하거나 네트워크 연결에 대한 보안 인증을 제공하는 데 사용된다.


## 인증서 생성하기
인증서를 생성하기 전에는 자신이 개발하고자 하는 앱의 용도와 기능에 따라 적절한 인증서를 선택해야 한다.
일단 너무 종류가 많기때문에 여기서 당황할 수 있다. 위에서 말했듯이 보통 사용하는 인증서는 몇개 밖에 없다. 아래는 인증서 생성할 수 있는 전체 리스트이니  걱정하지 말자...

### 소프트웨어관련 인증서
iOS 앱 뿐만 아니라 macOS, watchOS, tvOS 앱을 개발하고 배포할 때도 사용하는 인증서. Xcode에서 빌드 및 서명할 때 사용된다. 또한, 앱을 Ad Hoc 또는 App Store로 배포할 때도 사용된다.

- Apple Development
    - iOS, macOS, tvOS, watchOS 앱의 개발 버전을 서명하는 데 사용된다. 개발자가 자신의 디바이스에서 앱을 테스트하거나, 외부 테스터들에게 앱을 배포할 때 사용된다.

- Apple Distribution
    - iOS, macOS, tvOS, watchOS 앱을 앱스토어나 Ad Hoc 배포 시스템에 제출하기 전에 서명하는 데 사용된다. 이 인증서는 앱의 무결성을 검증하고, 앱이 신뢰할 수 있는 앱임을 보장한다.

- iOS App Development
    - iOS 앱의 개발 버전을 서명하는 데 사용된다.

- iOS Distribution (App Store and Ad Hoc)
    - iOS 앱을 앱스토어나 Ad Hoc 배포 시스템에 제출하기 전에 서명하는 데 사용된다. 이 인증서는 앱의 무결성을 검증하고, 앱이 신뢰할 수 있는 앱임을 보장한다.

- Mac Development
    - macOS 앱의 개발 버전을 서명하는 데 사용된다.

- Mac App Distribution
    - macOS 앱을 Mac App Store에 제출하기 전에 서명하는 데 사용된다. 이 인증서는 앱의 무결성을 검증하고, 앱이 신뢰할 수 있는 앱임을 보장한다.

- Mac Installer Distribution
    - macOS Installer Package를 Mac App Store에 제출하기 전에 서명하는 데 사용된다.

- Developer ID Application
    - macOS 앱을 Mac App Store 이외의 곳에서 배포하기 위해 서명하는 데 사용된다. 이 인증서는 앱의 무결성을 검증하고, 앱이 신뢰할 수 있는 앱임을 보장된다.


### 서비스관련 인증서

- Apple Push Notification service SSL (Sandbox)
    - 앱의 개발 버전에서 Apple Push Notification 서비스(Sandbox)를 사용하기 위해 필요한 인증서. 이 인증서는 앱에서 원격으로 알림을 보내는 데 사용된다.

- Apple Push Notification service SSL (Sandbox & Production)
    - 앱의 개발 버전과 배포 버전에서 Apple Push Notification 서비스(Sandbox 및 Production)를 사용하기 위해 필요한 인증서. 이 인증서는 앱에서 원격으로 알림을 보내는 데 사용된다. HTTP/2를 사용하는 경우, 동일한 인증서를 사용하여 앱 알림을 전송하고, ClockKit complication 데이터를 업데이트하고, 백그라운드 VoIP 앱의 수신 활동을 알릴 수 있다.

- Pass Type ID Certificate
    - Apple Wallet에 있는 Pass에 업데이트를 보내기 위해 필요한 인증서.

- Order Type ID Certificate
    - Apple Wallet에서 표시되는 주문 정보 페이로드를 업데이트하고 전송하기 위해 필요한 인증서.

- Website Push ID Certificate
    - 웹 사이트에서 Push 알림을 보내기 위해 필요한 인증서.

- Swift Package Collection Certificate
    - Swift Package Collection을 배포하기 위해 필요한 인증서.

- WatchKit Services Certificate
    - ClockKit complication 데이터를 업데이트하고 백그라운드 VoIP 앱의 수신 활동을 알리기 위해 필요한 인증서.

- VoIP Services Certificate
    - 백그라운드 VoIP 앱의 수신 활동을 알리기 위해 필요한 인증서.

- Apple Pay Payment Processing Certificate
    - 애플 페이 결제 처리를 위해 필요한 인증서. 이 인증서는 애플에서 상인/개발자에게 보내는 앱 트랜잭션 데이터를 복호화하는 데 사용된다.

- Apple Pay Merchant Identity Certificate
    - 애플 페이 결제 처리 서버에 대한 클라이언트 TLS 인증서로, 상인/개발자를 인증하는 데 사용된다.

# .p8인증서와 .p12인증서
Apple에서는 대부분의 인증서를 p12 형식으로 만들어야 하지만, 몇몇 인증서는 p8 형식으로도 만들 수 있다.

## p12
- 개인키와 공개키가 함께 포함되어있다.
- 개인키를 보호하기 위해 비밀번호로 암호화 되어있다. 때문에 개발자가 이 비밀번호를 알고 있어야 인증서 사용이 가능하다.
- 보안성이 높은 방식으로 저장되어야 하며, 개발자가 직접 보관하거나 안전한 곳에 저장해야 한다. 이러한 보안 조치를 취하지 않으면, 개인 키가 유출될 수 있으며, 이는 애플의 서비스에 접근할 수 있는 권한을 갖게 되는 등의 보안 위협이 될 수 있다.

## p8
- 기존에는 p12인증서만 사용하다가 WWDC2016에서 처음 소개되었다. 보안성이 높아졌고, 개발자가 Apple의 서비스와 상호작용하는 데 있어서 더욱 효율적이고 간편한 방법을 제공하기 위해 만들어졌다.
- p8 인증서는 토큰 기반의 인증 방식을 사용하며 주로 Apple Push Notification 서비스, Swift Package Collection배포, 애플 페이 결제 처리를 위해 사용한다.
- p8 인증서는 개인 키만을 포함하기 때문에, p12 인증서와는 달리 개인 키를 보호하기 위한 비밀번호가 필요하지 않다. 따라서, 개발자가 p8 인증서를 사용할 때는 `개인 키`를 보호하기 위한 조치를 취해야 한다.

### 유효기간의 차이
- p8 
    - 영구적으로 사용가능
    - 생성시 한번만 다운로드 받을 수 있다.
- p12
    - 개발용 : 365일
    - 배포용 : 395일

### 생성제한
- p8 
    - 한 계정당 최대 10개의 p8인증서 생성가능
    - 개발자가 다수의 앱을 개발하거나 다른 팀원과 함께 작업하는 경우, 여러 개의 계정을 만들어 p8 인증서를 생성하거나, 하나의 계정을 공유하여 개발을 진행하게 됩니다.
- p12
    - 한 계정당 최대 3개의 p12인증서 생성가능

## 생성되어있는 인증서들을 보는 방법

- Apple Developer 계정에 로그인.
- Certificates, Identifiers & Profiles 페이지로 이동.
- 왼쪽 탐색 메뉴에서 해당 인증서 또는 키를 선택.
- 선택한 항목의 상세 정보 페이지에서 "Type" 또는 "Certificate Type"을 확인.
    - "Type" 또는 "Certificate Type"이 "Apple Development"이면, 해당 인증서 또는 키는 Development Certificate이며, p8 또는 p12 형식.
    - "Type" 또는 "Certificate Type"이 "Apple Distribution"이면, 해당 인증서 또는 키는 Distribution Certificate이며, p12 형식.
    - "Type" 또는 "Certificate Type"이 "iOS App Development"이면, 해당 인증서 또는 키는 iOS 앱의 개발용 인증서이며, p12 형식.
    - "Type" 또는 "Certificate Type"이 "iOS Distribution (App Store and Ad Hoc)"이면, 해당 인증서 또는 키는 iOS 앱의 배포용 인증서이며, p12 형식.
    - "Type" 또는 "Certificate Type"이 "Apple Push Notification service SSL (Sandbox)" 또는 "Apple Push Notification service SSL (Sandbox & Production)"이면, 해당 인증서 또는 키는 Push Notification 서비스를 위한 인증서이며, p8 형식.
