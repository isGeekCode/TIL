# 리젝사유 - 5. Legal(성능)

[AppStore Review GuideLine - 5. Legal 링크](https://developer.apple.com/app-store/review/guidelines/#legal)

Apps must comply with all legal requirements in any location where you make them available (if you’re not sure, check with a lawyer). We know this stuff is complicated, but it is your responsibility to understand and make sure your app conforms with all local laws, not just the guidelines below. And of course, apps that solicit, promote, or encourage criminal or clearly reckless behavior will be rejected. In extreme cases, such as apps that are found to facilitate human trafficking and/or the exploitation of children, appropriate authorities will be notified.



## Content
- [5.1 Privacy(민감성 정보)](#51-Privacy민감성-정보)
    - [5.1.1 Data Collection and Storage(데이터 수집 및 저장)](#511-Data-Collection-and-Storage데이터-수집-및-저장)
        - [리젝사유(230409) - 훗타운app : 5.1.1 - Legal - Privacy - Data Collection and Storage](#리젝사유230409---훗타운app--511---Legal---Privacy---Data-Collection-and-Storage)

## 5.1.1 Data Collection and Storage(데이터 수집 및 저장)


# 5.1 Privacy(민감성 정보)
사용자 개인 정보 보호는 Apple ecosystem에서 가장 중요하며, 개인 데이터를 취급할 때는 고객의 기대는 물론 개인 정보 보호 모범 사례, 관련 법률 및 Apple Developer Program License Agreement의 조항을 준수하도록 *주의*해야 합니다.

## 5.1.1 Data Collection and Storage(데이터 수집 및 저장)

- (i) Privacy Policies(개인 정보 보호 정책)
    - 모든 앱은 개인 정보 보호 정책에 대한 링크를 앱 스토어 연결 메타데이터 필드와 앱 내에 쉽게 액세스할 수 있는 방식으로 포함해야 합니다. 개인 정보 보호 정책은 명확하고 명시적으로 다음을 수행해야 합니다: 앱/서비스가 수집하는 데이터, 수집하는 데이터 및 해당 데이터의 모든 사용 방법을 식별합니다.
    - 분석 도구, 광고 네트워크 및 타사 SDK와 같은 사용자 데이터(본 지침에 따라)를 앱과 공유하는 모든 제3자 및 모든 상위 항목, 사용자 데이터에 액세스할 수 있는 자회사 또는 기타 관련 주체는 앱의 개인 정보 보호 정책에 명시된 대로 사용자 데이터를 동일하거나 동등하게 보호합니다.
    - 데이터 보존/삭제 정책을 설명하고 사용자가 동의를 취소하거나 사용자의 데이터 삭제를 요청하는 방법을 설명합니다.
- (ii) Permission(권한)
    - 사용자 또는 사용 데이터를 수집하는 앱은 수집 시점 또는 수집 직후에 익명으로 간주되는 경우에도 수집에 대한 사용자 동의를 확보해야 합니다.
    - 유료 기능은 이 데이터에 대한 액세스 권한을 사용자에게 부여하거나 요구해서는 안 됩니다. 또한 앱은 고객에게 동의를 철회할 수 있는 쉽고 이해할 수 있는 방법을 제공해야 합니다.
    - 목적 문자열이 데이터 사용을 명확하고 완벽하게 설명하는지 확인합니다. 유럽 연합의 일반 데이터 보호 규정("GDPR") 또는 유사한 법령의 조항에 의존하여 동의 없이 정당한 이익을 위해 데이터를 수집하는 앱은 해당 법률의 모든 조항을 준수해야 합니다.
        - [권한 요청에 대해 자세한 내용](https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy)
- (iii) 데이터 최소화
    - 앱은 앱의 핵심 기능과 관련된 데이터에 대한 액세스만 요청해야 하며 관련 작업을 수행하는 데 필요한 데이터만 수집하여 사용해야 합니다. 가능한 경우 사진 또는 연락처와 같은 보호된 리소스에 대한 전체 액세스를 요청하는 대신 프로세스가 끝난 선택기 또는 공유 시트를 사용합니다
- (iv) Access(액세스)
    - 앱은 사용자의 권한 설정을 존중해야 하며 불필요한 데이터 액세스를 조작, 속임수 또는 강제로 허용하지 않아야 합니다.
        - 예를 들어 소셜 네트워크에 사진을 게시하는 기능이 포함된 앱은 사용자가 사진을 업로드할 수 있도록 하기 전에 마이크 액세스를 요구하지 않아야 합니다. 
    - 가능한 경우 동의를 부여하지 않는 사용자를 위한 대체 솔루션을 제공합니다.
        - 예를 들어 사용자가 위치 공유를 거부할 경우 주소를 수동으로 입력할 수 있는 기능을 제공합니다.
- (v) Account Sign-In(계정 로그인)
    - 앱에 중요한 계정 기반 기능이 없는 경우 로그인 없이 사용할 수 있습니다. 앱이 계정 생성을 지원하는 경우 앱 내에서 계정 삭제도 제공해야 합니다. 앱은 앱의 핵심 기능과 직접 관련되거나 법에 의해 요구되는 경우를 제외하고는 사용자가 개인 정보를 입력하도록 요구하지 않을 수 있습니다. 핵심 앱 기능이 특정 소셜 네트워크(예: Facebook, WeChat, Weibo, Twitter 등)와 관련이 없는 경우 로그인 없이 또는 다른 메커니즘을 통해 액세스를 제공해야 합니다. 기본 프로필 정보를 가져오거나, 소셜 네트워크에 공유하거나, 앱을 사용할 친구를 초대하는 것은 핵심 앱 기능으로 간주되지 않습니다. 앱에는 소셜 네트워크 자격 증명을 해지하고 앱 내에서 앱과 소셜 네트워크 간의 데이터 액세스를 비활성화하는 메커니즘도 포함되어야 합니다. 앱은 자격 증명 또는 토큰을 장치 외부의 소셜 네트워크에 저장할 수 없으며 앱이 사용 중인 동안에는 이러한 자격 증명 또는 토큰을 사용하여 앱 자체에서 소셜 네트워크에 직접 연결할 수 있습니다.
- (vi) 앱을 사용하여 비밀번호 또는 기타 개인 데이터를 몰래 검색하는 개발자는 Apple Developer Program에서 제거됩니다
- (vii) SafariViewController를 사용하여 사용자에게 정보를 시각적으로 표시해야 합니다. 컨트롤러가 다른 보기 또는 계층에 의해 숨겨지거나 가려지지 않을 수 있습니다. 또한 앱은 SafariViewController를 사용하여 사용자의 지식과 동의 없이 사용자를 추적할 수 없습니다.
- (viii) 사용자의 직접적인 동의 없이 또는 사용자의 명시적인 동의 없이 개인 정보를 컴파일하는 앱은 앱 스토어에서 허용되지 않습니다.
- (ix) 규제가 심한 분야(예: 은행 및 금융 서비스, 의료, 도박, 합법적 대마초 사용 및 항공 여행)에서 서비스를 제공하거나 민감한 사용자 정보가 필요한 앱은 개별 개발자가 아니라 서비스를 제공하는 법인이 제출해야 합니다. 대마초의 합법적 판매를 촉진하는 앱은 해당 법적 관할 구역으로 지역 제한되어야 합니다.
- (x) 앱은 사용자가 원하는 기본 연락처 정보(예: 이름 및 이메일 주소)를 요청할 수 있으며, 기능 및 서비스는 정보 제공을 조건으로 하지 않으며, 어린이로부터 정보를 수집하는 제한 사항을 포함하여 본 지침의 다른 모든 조항을 준수합니다.

### 리젝사유(230409) - 훗타운app : 5.1.1 - Legal - Privacy - Data Collection and Storage
```
Additionally, we noticed that your app requests the user’s consent to access the microphone, but doesn’t sufficiently explain the use of the microphone in the purpose string.

To help users make informed decisions about how their data is used, permission request alerts need to explain and include an example of how your app will use the requested information.

- Please revise the purpose string in your app’s Info.plist file for the microphone to explain why your app needs access and include an example of how the user's data will be used.

You can modify your app's Info.plist file using the property list editor in Xcode.

# 번역
우리는 당신의 앱이 마이크에 접근하기 위해 사용자의 동의를 요청하지만 목적 문자열에서 마이크의 사용을 충분히 설명하지 않는다는 것을 알아챘습니다.

사용자가 자신의 데이터가 사용되는 방식에 대한 정보를 바탕으로 결정할 수 있도록 권한 요청 알림은 앱이 요청된 정보를 사용하는 방법을 설명하고 포함해야 합니다.

- 앱의 Info.plist 파일에 있는 목적 문자열을 마이크용으로 수정하여 앱에 액세스해야 하는 이유를 설명하고 사용자의 데이터가 어떻게 사용되는지 예를 포함하십시오.

Xcode의 속성 목록 편집기를 사용하여 앱의 Info.plist 파일을 수정할 수 있습니다.
```


- 상황
    - 보통 해당 내용은 권한 팝업을 띄우지않으면 앱이 죽게 되는 상황이 발생하기 때문에 민감성 정보관련 작업시 info.plist에 세팅을 해야한다.
    - 웹뷰의 고객센터에 문의하기에 사용자 디바이스의 사진첩 및 카메라 스키마를 내려보낸다는 고지가 없었는데 해당 부분에서 리젝이 됐다.
- 대응
    - 어느 부분에서 사용하는지를 확실하게 포함하라고 했기에 이를 반영
    - 기존문구
        ```
        Privacy - Camera Usage Description
이미지 등록을 위해 카메라 접근을 승인해주세요. 설정 - 개인정보보호-카메라 에서도 변경할 수 있습니다. 

Privacy - Microphone Usage Description
동영상 촬영을 위해 마이크 접근을 승인해주세요. 설정 - 개인정보보호 - 마이크 에서도 변경할 수 있습니다.
        ```

    - 개선한 문구
        ```
        Privacy - Camera Usage Description

1:1 문의기능, 바코드 스캐너기능 사용시 고객님의 이미지 등록을 위해 카메라 접근을 승인해주세요.  설정 - 개인정보보호-카메라 에서도 변경할 수 있습니다. 

Privacy - Microphone Usage Description

1:1 문의기능 사용시 동영상 촬영을 위해 마이크 접근을  승인해주세요.  설정 - 개인정보보호-마이크 에서도 변경할 수 있습니다. 
        ```

