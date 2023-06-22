# 리젝사유 - 2. Performance(성능)

[AppStore Review GuideLine - 2. Performance 링크](https://developer.apple.com/app-store/review/guidelines/#performance)

## Content
- [2.1 Performance: App Completeness(앱 완전성)](#21-performance-app-completeness앱-완전성)
    - [리젝사유(230409) - 훗타운app : 2.1 Performance - App Completeness](#리젝사유230409---훗타운app--21-Performance---App-Completeness)
    - [리젝사유(230409) - 훗타운app : 2.1 Information Needed](#리젝사유230409---훗타운app--21-information-needed)
    - [리젝사유(230510) - 라드씨엔에스app : 2.1 Information Needed](#리젝사유230510---라드씨엔에스app--21-information-needed)
    - [리젝사유(230622) - MyNBapp : 2.1 Information Needed](#리젝사유230622---MyNBapp--21-information-needed)
- [2.3 Performance - Accurate Metadata(정확한 메타데이터)](#23-performance---accurate-metadata정확한-메타데이터)  
    - [리젝사유(230409) - 훗타운app : 2.3 Performance - Accurate Metadata](#230409---훗타운app--23-performance---Accurate-metadata)
    - [2.3.3 (스크린샷)](#233-스크린샷)
        - [리젝사유(230407) - 훗타운app : 2.3.3 Screenshots should show the app in use(스크린샷 사용)](#리젝사유230407---훗타운app--233-screenshots-should-show-the-app-in-use스크린샷-사용)

[Top](#)

# 2.1 Performance: App Completeness(앱 완전성)
- 사전 주문할 수 있도록 만든 앱을 포함하여 App Review에 제출하는 것은 필요한 모든 메타데이터와 완벽하게 작동하는 URL이 포함된 최종 버전이어야 합니다.
- 앱을 제출하기 전에 placeholder 텍스트, 빈 웹 사이트 및 기타 임시 콘텐츠를 제거해야 합니다.
- 앱을 제출하기 전에 장치에서 버그 및 안정성 테스트를 거쳤는지 확인하고 앱에 로그인이 포함된 경우 데모 계정 정보를 포함하고 백엔드 서비스를 활성화하시기 바랍니다. 
- 법적 또는 보안 의무로 인해 데모 계정을 제공할 수 없는 경우, Apple의 사전 승인을 받아 데모 계정 대신 기본 제공 데모 모드를 포함할 수 있습니다. 
- 데모 모드가 앱의 전체 기능을 표시하는지 확인하십시오. 
- 앱에서 인앱 구매를 제공하는 경우 완전하고 최신이며 검토자가 볼 수 있는지 확인하거나 검토 노트에 이유를 설명하십시오.
- 또한 앱심사를 소프트웨어 테스트용으로 사용하지 마세요. 
- 충돌이 발생하거나 명백한 기술적 문제를 나타내는 불완전한 앱 번들 및 바이너리는 거부됩니다

[Top](#)

### 리젝사유(230409) - 훗타운app : 2.1 Performance - App Completeness
```
We discovered one or more bugs in your app. 
Specifically, “서비스 점검 안내” message was displayed in the Home. 
Also, we were unable to register or log in using Sign in with Apple.
Additionally, an error message was displayed when we tapped on the Chat tab.

# 번역
앱에서 하나 이상의 버그를 발견했습니다. 
구체적으로 홈에 "홈" 메시지가 표시되었습니다. 
또한, 애플 로그인을 사용하여 등록하거나 로그인할 수 없습니다.
또한 채팅 탭을 누르면 오류 메시지가 표시됩니다.
```

- 상황
    - 웹뷰관련 앱이었는데 심사를 등록하는 시점에선 정상동작을 했지만, 심사를 하는 시점에 웹에서 서비스 점검 안내 메세지를 띄워서 리젝
- 대응
    - 심사중에 서비스 점검 안내 화면이 뜨지 않도록 조치

[Top](#)

### 리젝사유(230409) - 훗타운app : 2.1 Information Needed
  
```
We’re looking forward to completing the review of your app, but we need more information to continue.

Please provide detailed answers to the following questions in your reply to this message in App Store Connect:

- Does your app include a blocking mechanism that is the ability to block abusive users from the service? If so, where can we locate the feature in the app?

# 번역
귀하의 앱 검토를 완료하기를 고대하고 있지만 계속하려면 추가 정보가 필요합니다. 
- 귀하의 앱에는 악의적인 사용자를 서비스에서 차단할 수 있는 차단 메커니즘이 포함되어 있습니까? 그렇다면 앱에서 기능을 어디에서 찾을 수 있습니까?
```


- 상황  
    - 커뮤니티 기능이 있는 앱은 악의적인 사용자를 차단할 수 있는 로직이 들어있어야한다. 심사관이 이를 확인 할 수 없어서 요청

- 대응  
    - 앱 내 차단기능의 동영상을 찍어서, 메모와 함께 제출

[Top](#)

### 리젝사유(230510) - 라드씨엔에스app : 2.1 Information Needed
```
We’re looking forward to continuing our review, but we need more information about your business model and your users to help you find the best distribution option for your app. 

Please review the following questions and provide as much detailed information as you can for each question.

1. Is your app restricted to users who are part of a single company? This may include users of the company's partners, employees, and contractors.
2. Is your app designed for use by a limited or specific group of companies? 
- If yes, which companies use this app? 
- If not, can any company become a client and utilize this app?
3. What features in the app, if any, are intended for use by the general public?
4. How do users obtain an account?
5. Is there any paid content in the app and if so who pays for it? For example, do users pay for opening an account or using certain features in the app?

# 번역

귀하의 앱 검토를 완료하기를 고대하고 있지만 계속하려면 추가 정보가 필요합니다.
  1. 앱이 단일 회사에 속한 사용자로 제한되어 있습니까? 여기에는 회사의 파트너, 직원 및 계약자의 사용자가 포함될 수 있습니다. 
  2. 앱이 제한적이거나 특정 회사 그룹에서 사용하도록 설계되었습니까? 
    - 있다면 어떤 회사에서 이 앱을 사용하나요? 
    - 그렇지 않다면 아무 회사나 클라이언트가 되어 이 앱을 활용할 수 있나요? 
  3. 일반 대중이 사용할 수 있는 앱의 기능은 무엇입니까? 
  4. 사용자는 어떻게 계정을 얻습니까?
  5. 앱에 유료 콘텐츠가 있습니까? 그렇다면 누가 비용을 지불합니까? 예를 들어, 사용자는 계정을 개설하거나 앱의 특정 기능을 사용하는 데 비용을 지불합니까? 
```

- 상황  
    - 사실상 인하우스 앱은 기업용배포를 해야하는데 편의상 사용해온 앱.

- 대응  
    - 메모에 아래 내용을 추가하여 앱 심사 제출
    ```
    - Guideline 2.1 - Information Needed
        - 앱의 사용자는 자사, 자사 이외에 파트너사의 사원들, 협력업체의 사원들이 사용합니다.
        - 일반 사용자가 사용하기 위한 앱 기능은 출퇴근, 회의실 예약, 휴가신청, 조회, 직원조회가 있습니다.
        - 사용자는 자사에서 계정을 발급합니다.
        - 앱에 유료기능이 없기 때문에 콘텐츠 비용이 존재하지 않습니다.  
    ```

[Top](#)

### 리젝사유(230622) - MyNBapp : 2.1 Information Needed
```
We're looking forward to completing our review, but we need more information to continue. Your app uses the AppTrackingTransparency framework, but we are unable to locate the App Tracking Transparency permission request when reviewed on iOS 16.5.

Next Steps

Please explain where we can find the App Tracking Transparency permission request in your app. The request should appear before any data is collected that could be used to track the user.

If you've implemented App Tracking Transparency but the permission request is not appearing on devices running the latest OS, please review the available documentation and confirm App Tracking Transparency has been correctly implemented.

If your app does not track users, update your app privacy information in App Store Connect to not declare tracking. You must have the Account Holder or Admin role to update app privacy information.

Resources 

- Tracking is linking data collected from your app with third-party data for advertising purposes, or sharing the collected data with a data broker. Learn more about tracking. 
- See Frequently Asked Questions about the requirements for apps that track users.
- Review developer documentation for App Tracking Transparency.

# 번역

검토를 완료하기를 고대하고 있지만 계속하려면 더 많은 정보가 필요합니다. 앱에서 앱 추적 투명성 프레임워크를 사용하지만 iOS 16.5에서 검토할 때 앱 추적 투명성 권한 요청을 찾을 수 없습니다.

당신의 앱에서 앱 추적 투명성 권한 요청을 어디서 찾을 수 있는지 설명해 주세요. 사용자를 추적하는 데 사용할 수 있는 데이터를 수집하기 전에 요청이 나타나야 합니다.

앱 추적 투명성을 구현했지만 최신 OS를 실행하는 장치에 권한 요청이 나타나지 않는 경우 사용 가능한 설명서를 검토하고 앱 추적 투명성이 올바르게 구현되었는지 확인하십시오.

앱이 사용자를 추적하지 않는 경우 앱 스토어 연결의 앱 개인 정보를 업데이트하여 추적을 선언하지 마십시오. 앱 개인 정보를 업데이트하려면 계정 소유자 또는 관리자 역할이 있어야 합니다.


- 추적은 앱에서 수집한 데이터를 광고 목적으로 타사 데이터와 연결하거나 수집한 데이터를 데이터 브로커와 공유하는 것입니다. 추적에 대해 자세히 알아봅니다. 
- 사용자를 추적하는 앱에 대한 요구 사항은 자주 묻는 질문을 참조하십시오.
- 앱 추적 투명성에 대한 개발자 문서를 검토합니다.
```

- Apple 제공 링크
    - [추적 : 앱 수집 데이터를 광고목적으로 공유하는 것에 대하여](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/3547037-requesttrackingauthorization)
    - [사용자를 추적하는 앱에 대한 요구 사항](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)  
    - [앱 추적 투명성에 대한 개발자 문서](https://developer.apple.com/documentation/apptrackingtransparency)  
  
- 상황  
    - 사실상 앱내 해당 내용이 들어가있지만 심사관이 해당 내용을 확인하지 못한 상황.
  
- 대응  
    - 해당 권한팝업의 스크린샷과 경로를 설명하여 회신함
  
[Top](#)


# 2.3 Performance - Accurate Metadata(정확한 메타데이터)
- 사용자가 앱을 다운로드하거나 구입할 때, 앱에 대하여 명확히 알 수 있도록 민감성 정보, 앱 설명, 스크린샷 및 미리보기를 포함한 모든 앱 메타데이터를 표기해야합니다. 그래서 앱의 핵심 경험을 정확하게 반영하고 새 버전으로 최신 상태로 유지해야 합니다.

### 리젝사유(230409) - 훗타운app : 2.3 Performance - Accurate Metadata
```
We noticed that your app's metadata includes the following information, which is not relevant to the app's content and functionality:

“배송대행” feature in the app’s description.

#번역
앱의 메타데이터에는 앱의 콘텐츠 및 기능과 관련이 없는 다음 정보가 포함되어 있습니다:

앱 설명에 있는 "배송대행" 기능입니다.
```

- 상황
    - 배송대행관련 앱을 심사하는데 해당 내용으로 리젝되었다.

- 대응
    - 해당 내용에는 대응 하지않았음

[Top](#)

## 2.3.3 (스크린샷)
- 스크린샷에는 제목 아트, 로그인 페이지 또는 시작 화면뿐만 아니라 사용 중인 앱이 표시되어야 합니다. 또한 텍스트 및 이미지 오버레이(예: 애니메이션 터치 포인트 또는 Apple Pencil 등의 입력 메커니즘을 시연하기 위한 것)를 포함하고 터치 바와 같은 장치에서 확장된 기능을 표시할 수 있습니다


### 리젝사유(230407) - 훗타운app : 2.3.3 Screenshots should show the app in use(스크린샷 사용)
```
We noticed that your screenshots do not sufficiently show your app in use. 

- Specifically, your 4.7-inch iPhone, 4-inch iPhone, and 3.5-inch iPhone screenshots do not show the current version of the app in use.

To help users understand your app’s functionality and value, your screenshots should highlight your app's core concept. For example, a gaming app should feature screenshots that capture actual gameplay within the app.
```
- 상황
    - 이 앱은 신규프로젝트를 기존에 배포했던 다른 앱 프로젝트 Bundle ID에 세팅하는 것으로 기획이 수정되었다. 신규프로젝트에 맡게 앱 정보를 모두 수정했는데,  앱정보 `미디어 관리에서 모든 크기 보기`를 누르면 모든 디스플레이에 대한 스크린샷세팅화면으로 이동할 수 있다.  
- 대응
    - 이곳에 4형 디스플레이와, 3.5형 디스플레이 이미지가 있었기 떄문에 삭제하며 상황 종료


[Top](#)

# History
- 230407
    - 리젝사유(230407) - 훗타운app : 2.3.3 Screenshots should show the app in use(스크린샷 사용)
- 230510
    - 2.1 앱 완전성 번역
    - 2.3 정확한 메타데이터 번역
    - 2.3.3 스크린샷 번역
    - 리젝사유(230409) - 훗타운app : 2.3 Performance - Accurate Metadata
    - 리젝사유(230409) - 훗타운app : 2.1 Performance - App Completeness
    - 리젝사유(230409) - 훗타운app : 2.1 Information Needed
    - 리젝사유(230510) - 라드씨엔에스app : 2.1 Information Needed


[Top](#)

