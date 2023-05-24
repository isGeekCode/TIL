# 리젝사유 - 4. Design(디자인)

[AppStore Review GuideLine - 4. Design 링크](https://developer.apple.com/app-store/review/guidelines/#design)

애플 고객들은 간편하고, 세련되고, 혁신적이며, 사용하기 쉬운 제품에 높은 가치를 두고 있으며, 이것이 바로 우리가 앱스토어에서 보고 싶은 것입니다. 훌륭한 디자인을 고안하는 것은 여러분에게 달려 있지만, 앱스토어 승인을 위한 최소 기준은 다음과 같습니다. 또한 앱이 승인된 후에도 앱이 계속 작동하고 신규 및 기존 고객의 관심을 끌 수 있도록 업데이트해야 합니다. 작동이 중지되거나 성능이 저하된 앱은 언제든지 앱스토어에서 제거될 수 있습니다.

 > Apple customers place a high value on products that are simple, refined, innovative, and easy to use, and that’s what we want to see on the App Store. Coming up with a great design is up to you, but the following are minimum standards for approval to the App Store. And remember that even after your app has been approved, you should update your app to ensure it remains functional and engaging to new and existing customers. Apps that stop working or offer a degraded experience may be removed from the App Store at any time.


## Content
- [4.8 Sign in with Apple(애플 로그인)](#48-Sign-in-with-Apple애플-로그인)
    - [리젝사유(230524) - MyNB앱 : 4.8 Design: Sign in with Apple](#리젝사유230524---MyNB앱--48-Design-Sign-in-with-Apple)

# 4.8 Sign in with Apple(애플 로그인)
타사 또는 소셜 로그인 서비스(Facebook Login, Google Sign-In, Twitter로 로그인, LinkedIn으로 로그인, Amazon으로 로그인 또는 WeChat Login)를 사용하여 사용자의 기본 계정을 설정하거나 인증하는 앱도 동등한 옵션으로 Apple로 로그인을 제공해야 합니다. 사용자의 기본 계정은 사용자를 식별하고 로그인하고 사용자의 기능 및 관련 서비스에 액세스할 목적으로 사용자가 사용자의 앱에 설정한 계정입니다.

다음과 같은 경우 Apple에 로그인할 필요가 없습니다:

- 귀하의 앱은 회사 자체 계정 설정 및 로그인 시스템을 독점적으로 사용합니다.
- 귀하의 앱은 사용자가 기존 교육 또는 엔터프라이즈 계정으로 로그인해야 하는 교육, 엔터프라이즈 또는 비즈니스 앱입니다.
- 귀하의 앱은 정부 또는 업계에서 지원하는 시민 식별 시스템 또는 전자 ID를 사용하여 사용자를 인증합니다.
- 귀하의 은은 특정 타사 서비스의 클라이언트이며 사용자는 자신의 콘텐츠에 액세스하려면 메일, 소셜 미디어 또는 다른 타사 계정에 직접 로그인해야 합니다.


### 리젝사유(230524) - MyNB앱 : 4.8 Design: Sign in with Apple

```
# 원문
Your app uses a third-party login service, but does not offer Sign in with Apple. Apps that use a third-party login service for account authentication need to offer Sign in with Apple to users as an equivalent option to provide the sign-in experience App Store users expect.
Specifically, registration tab did not offer Sign up with Apple.

- Please revise your app to offer Sign in with Apple as an equivalent option for account authentication.

Resources
- Review Sign in with Apple sample code. 
- For an overview of design and formatting recommendations for Sign in with Apple, see the Human Interface Guidelines.
- Learn about the benefits of Sign in with Apple.

# 번역
앱이 타사 로그인 서비스를 사용하지만 Apple 로그인을 제공하지 않습니다. 계정 인증에 타사 로그인 서비스를 사용하는 앱은 앱스토어 사용자가 기대하는 로그인 환경을 제공하기 위해 사용자에게 동등한 옵션으로 애플 로그인을 제공해야 합니다.
특히, 등록 탭에서 Apple 가입을 제공하지 않았습니다.

- 계정 인증을 위한 동등한 옵션으로 Apple 로그인을 제공하도록 앱을 수정하십시오.

자원.
- Apple 샘플 코드로 로그인을 검토합니다.
- Apple 로그인에 대한 설계 및 형식 권장 사항에 대한 개요는 휴먼 인터페이스 지침을 참조하십시오.
- Apple 로그인의 이점에 대해 알아보십시오.
```
- 레퍼런스
    - [애플로그인관련 서문](https://developer.apple.com/sign-in-with-apple/)
    - [애플로그인관련 공식문서 및 샘플 코드](https://developer.apple.com/documentation/authenticationservices/implementing_user_authentication_with_sign_in_with_apple)
    - [애플로그인관련 휴먼인터페이스 가이드라인](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)

- 상황  
    - 카카오 로그인은 구현되어있지만 애플로그인은 없어서 리젝된 생황

- 대응  
    - 기존 Apple 로그인 관련 프로젝트 세팅은 되어있으나, 현재 기획을 맡고있는 사업부, 개발부서에는 해당 내용이 기획되어있지않아서 애플로그인 관련 추가 정책 수립 및 개발작업 필요
    - 사업부 답변후 개발작업하기로 함(230524 기준)

# History
- 230524
    - 4 디자인 번역
    - 4.8 애플로그인 번역
    - 리젝사유(230524) - MyNB앱 : 4.8 Design: Sign in with Apple
