# AppStore - 인증서에 관하여


## 앱과 관련된 정보는 Apple Developer에서 확인 가능

[Apple Developer 사이트링크](https://developer.apple.com/)에서 Account를 클릭

- 앱스토어 등록시 관련된 정보를 보려면 App Store Connect에서 확인이 가능하다.
- 개발, 테스트 및 배포하는데 필요한 인증서, 식별자, 프로파일 및 기기관리 
- 베타 소프트 웨어 등등의 추가 리소스 확인 가능


## 앱 개발시 필수적인 인증서

- iOS 개발자 인증서(iOS Development Certificate)
    - iOS 앱 개발 및 테스트에 필요한 인증서. 이 인증서는 iOS 디바이스에 앱을 설치하거나 디버그하기 위해 사용된다. 개발자가 개발 중인 앱을 테스트하고, Xcode와 같은 개발 도구를 사용하여 디바이스에 앱을 설치하거나 디버그하는 데 필요하다.

- iOS 배포 인증서(iOS Distribution Certificate)
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
