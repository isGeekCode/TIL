# Integrity_PrivacyInfo.xcprivacy 만들기(작성중)
- 관련 링크
    - [(23.12.7) Apple News and Updates - App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx)
    - [(24.2.29) Apple News and Updates - App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=3d8a9yyh)
    - [Apple Support: 타사 SDK 요구 사항 변경 예정
](https://developer.apple.com/kr/support/third-party-SDK-requirements)
    - [WWDC2023 : Get started with privacy manifests](https://developer.apple.com/videos/play/wwdc2023/10060/)
        - [Apple Document: Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files)
        - [Apple Document: Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests)
        - [Apple Document: Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api)
    - [WWDC2022 : Create your Privacy Nutrition Label](https://developer.apple.com/videos/play/wwdc2022/10167)
    - [WWDC2022 : Explore App Tracking Transparency](https://developer.apple.com/videos/play/wwdc2022/10166)
        - [Apple Document : App Store Guidelines: User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
    - [WWDC 2023의 다크호스: 프라이버시 정책이 현실로 다가옵니다](https://www.branch.io/ko/resources/blog/wwdc-2023%EC%9D%98-%EB%8B%A4%ED%81%AC%ED%98%B8%EC%8A%A4-%ED%94%84%EB%9D%BC%EC%9D%B4%EB%B2%84%EC%8B%9C-%EC%A0%95%EC%B1%85%EC%9D%B4-%ED%98%84%EC%8B%A4%EB%A1%9C-%EB%8B%A4%EA%B0%80%EC%98%B5%EB%8B%88/?__cf_chl_rt_tk=KiinSr7TWFFZHjEkvGXwoe5_Ih51JdkK9IAbekYm.0Y-1709797802-0.0.1.1-2026)



위에 관련링크를 보면 애플에서 공지한 [(23.12.7)App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx)글과 [(24.2.29)App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx) 글을 살펴보면 아래와 같은 부분이 있다.  

> 2024년 봄부터 App Store Connect에 새로운 앱 또는 앱 업데이트를 업로드하려면  
> 앱의 개인정보 보호 매니페스트에 앱이 API를 사용하는 방식을 정확하게 반영하는 허용된 사유를 포함하고 있어야 한다  

이 글에서  서드파티 SDK는 앱에 탁월한 기능을 제공하지만 개발자 / 사용자도 모르는 사이에 사용자 개인 정보 보안을 취약하게 만든다고 한다. 

말하는 `Third-party SDK privacy manifest and signatures` 가 뭘까?

<br><br>

이 내용에 앞서 애플에서 새롭게 도입한 PrivacyInfo.xcprivacy 라는 걸 알아보자. 

[(23.12.7)App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx)글을 살펴보면 

[WWDC2023 : Get started with privacy manifests](https://developer.apple.com/videos/play/wwdc2023/10060/)라는 영상에서 이제 프로젝트 파일 내에 PrivacyInfo.xcprivacy라는 파일이 생겼다는 걸 알 수 있다.  

<br><br>

그리고 하단의 나머지 글들과 WWDC20 영상을 살펴보면서 이 파일이 어떤 구조인지 알 수 있게 된다.  
일단 이 PrivacyInfo 파일은 마치 Info.plist와 같은 Dictionary 구조의 소스코드를 Property List로 볼 수 있도록 만든 파일이다.  
그래서 그냥 보면 Info.plist 파일처럼 보인다.  그리고 이미지도 살작 다르게 생겼다.  

<br>

다만 Info.plist와 다른 점은 PrivacyInfo 내부에 정의된 값은 앱 내부에 정의 되어있는 Privacy 정보들을 모두 정의해서 어떤 용도로 사용하고 있는 지를 나타낸다.  

<img width="500" alt="스크린샷 2024-03-07 오후 3 36 27" src="https://github.com/isGeekCode/TIL/assets/76529148/d1ba4282-708a-4fda-bcb5-8f0355fb8bb8">

new file을 통해 PrivacyInfo.xcprivacy 파일을 최초 생성하게 되면 아래와 같이 생성된다.  
위치는 어디에 둬도 상관없다. 나중에 Archiving 후, Appstore Connect로 Upload를 할때, 인증하는 과정에서 PrivacyInfo.xcprivacy파일을 모두 스캔해서 리포트를 작성하기 때문이다.  

<img width="800" alt="스크린샷 2024-03-07 오후 3 37 12" src="https://github.com/isGeekCode/TIL/assets/76529148/eaa65333-445c-4280-852d-c62a054f3aaf">


그럼 이 파일의 구성요소를 살펴보자.  

<br><br>

- NSPrivacyTracking
- NSPrivacyTrackingDomains
- NSPrivacyCollectedDataTypes
- NSPrivacyAccessedAPITypes


이 네가지는 PrivacyInfo.xcprivacy 파일의 주요 키값을 의미하는 Value다 
PrivacyInfo파일을 Property List로 보게 되면 아래와 같이 표시된다.  

- Privacy Tracking Enabled
- Privacy Tracking Domains
- PrivacyCollectedDataTypes
- PrivacyAccessedAPITypes


기본 최상위 구조인 App Privacy Configuration은 Dictionary타입이다. 

여기서 + 버튼을 누르면 아래 그림처럼 추가할 수가 있게 된다.  

<img width="500" alt="스크린샷 2024-03-07 오후 4 46 02" src="https://github.com/isGeekCode/TIL/assets/76529148/bac37aac-66df-4f62-ae55-fb7ee4311d2f">

<br><br>


