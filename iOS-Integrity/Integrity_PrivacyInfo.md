# Integrity_개인정보 보호 매니페스트 PrivacyInfo.xcprivacy 만들기

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

<br><br>


위에 관련링크를 보면 애플에서 공지한 게시글 [(23.12.7)App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx)와 [(24.2.29)App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx) 를 살펴보면 아래와 같은 부분이 있다.  

> 2024년 봄부터 App Store Connect에 새로운 앱 또는 앱 업데이트를 업로드하려면  
> 앱의 개인정보 보호 매니페스트에 앱이 API를 사용하는 방식을 정확하게 반영하는 허용된 사유를 포함하고 있어야 한다  

이 글에서  서드파티 SDK는 앱에 탁월한 기능을 제공하지만 개발자 / 사용자도 모르는 사이에 사용자 개인 정보 보안을 취약하게 만든다고 한다. 

여기서 말하는 `Third-party SDK privacy manifest and signatures` 가 뭘까?

<br><br>

이 내용에 앞서 애플에서 새롭게 도입한 PrivacyInfo.xcprivacy 라는 걸 알아보자. 

[(23.12.7)App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx)글을 살펴보면 

[WWDC2023 : Get started with privacy manifests](https://developer.apple.com/videos/play/wwdc2023/10060/)라는 영상에서 이제 프로젝트 파일 내에 PrivacyInfo.xcprivacy라는 파일이 생겼다는 걸 알 수 있다.  

일단 이 PrivacyInfo 파일은 마치 Info.plist와 같은 Dictionary 구조의 소스코드를 Property List로 볼 수 있도록 만든 파일이다.  
그래서 그냥 보면 Info.plist 파일처럼 보인다.  그리고 이미지도 살작 다르게 생겼다.  

<br>

다만 Info.plist와 다른 점은 PrivacyInfo 내부에 정의된 값은 앱 내부에 정의 되어있는 Privacy 정보들을 모두 정의해서 어떤 용도로 사용하고 있는 지를 나타낸다.  

<br><br>

new file을 통해 PrivacyInfo.xcprivacy 파일을 최초 생성하게 되면 아래와 같이 생성된다.  
위치는 어디에 둬도 상관없다. 나중에 Archiving 후, Appstore Connect로 Upload를 할때, 인증하는 과정에서 PrivacyInfo.xcprivacy파일을 모두 스캔해서 리포트를 작성하기 때문이다.  

<img width="500" alt="스크린샷 2024-03-07 오후 3 36 27" src="https://github.com/isGeekCode/TIL/assets/76529148/d1ba4282-708a-4fda-bcb5-8f0355fb8bb8">

<br><br>
아래는 생성한 파일이다. 

<img width="800" alt="스크린샷 2024-03-07 오후 3 37 12" src="https://github.com/isGeekCode/TIL/assets/76529148/eaa65333-445c-4280-852d-c62a054f3aaf">

<br><br>

그럼 이 파일의 App Privacy Configuration Dictionary에 들어갈 Key값을 살펴보자.  

<br><br>

- NSPrivacyTracking
- NSPrivacyTrackingDomains
- NSPrivacyCollectedDataTypes
- NSPrivacyAccessedAPITypes
  
<br>
이 네가지는 PrivacyInfo.xcprivacy 파일의 주요 키값을 의미하는 Value다.   
PrivacyInfo파일을 Property List로 보게 되면 아래와 같이 표시된다.  

- Privacy Tracking Enabled
- Privacy Tracking Domains
- PrivacyCollectedDataTypes
- PrivacyAccessedAPITypes

<br>
기본 최상위 구조인 App Privacy Configuration은 Dictionary타입이다. 

여기서 + 버튼을 누르면 아래 그림처럼 추가할 수가 있게 된다.  

<img width="500" alt="스크린샷 2024-03-07 오후 4 46 02" src="https://github.com/isGeekCode/TIL/assets/76529148/bac37aac-66df-4f62-ae55-fb7ee4311d2f">

<br><br>

그럼 이 키값들을 하나씩 살펴보자.  

<br><br>

## Privacy Tracking Enabled
- [ Apple AppStore - 사용자 개인정보 보호 및 데이터 사용](https://developer.apple.com/app-store/user-privacy-and-data-use/)

이 키에 대한 값은 Bool타입이다.  

이는 앱 또는 타사 SDK가 ATT프레임워크에 정의된 대로 추적에 대해 데이터를 사용하는지 여부를 나타내는 값이다.  

<img width="500" alt="스크린샷 2024-03-08 오전 8 36 45" src="https://github.com/isGeekCode/TIL/assets/76529148/d1fe9622-f9ab-4acd-ac2b-cae613e299ba">

<br><br>

## Privacy Tracking Domains
- [ Apple AppStore - 사용자 개인정보 보호 및 데이터 사용](https://developer.apple.com/app-store/user-privacy-and-data-use/)

앱 또는 타사 SDK가 추적에 참여하는 인터넷 도메인을 나열한 배열이다.  

<br>
사용자가 ATT 프레임워크를 통해 추적권한을 부여하지 않은 경우에는 이러한 도메인으로의 네트워크 요청이 실패한다.  

-> 이는 [WWDC2023 Get started with privacy manifests : 앱 추적 투명성](https://developer.apple.com/videos/play/wwdc2023/10060)
중에서도 아래 이미지처럼 소개가 된다.  

<img width="500" alt="스크린샷 2024-03-05 오후 1 26 16" src="https://github.com/isGeekCode/TIL/assets/76529148/c01b7309-4026-4c32-9c1c-48dc62769348">

<br>
iOS17자체에서는 아무리 도메인에서 추적을 한다고 해도 사용자가 추적권한 얼럿에서 허용하지 않았다면,  OS단에서 추적을 끊는다는 것이다.  

그러니 추적권한을 허용하면 추적에 참여할 인터넷 도메인을 기입하면 된다.  

<br><br>


<img width="500" alt="스크린샷 2024-03-08 오전 8 36 27" src="https://github.com/isGeekCode/TIL/assets/76529148/92fe623e-a028-4b00-baa3-b0a38f4ff96f">


<br><br>

## Privacy Nutrition Label Types

앱 또는 타사 SDK가 수집하는 데이터의 유형을 설명하는 Dictionary를 담은 배열이다.  
<br>
Privacy Nutrition Label Types에 들어갈 각각의 배열 안에는 데이터의 유형을 하나씩 어떤 용도로 사용하는지 정의한 내용이 담겨있다. 

- Collected Data Types
- Linked to User
- Used for Tracking
- Collection Purposes

<img width="512" alt="dark-horse-1" src="https://github.com/isGeekCode/TIL/assets/76529148/0dcaf96b-2f4e-4e9c-9d25-e58b7c0e9614">

<br><br>

### Collected Data Types
- [Apple App Store의 앱 개인정보 보호 세부정보](https://developer.apple.com/app-store/app-privacy-details/)

위 글을 보면 Types of data 에서 정의한 타입들과 이에 대한 설명이 나와있다.  

그리고 이 내용은 App Store Connect에서 앱 타겟을 만들 때, 게시한 앱 개인정보 세부사항과 일치하는 내용이기도 하다. 

<br><br>

### Linked to User
> 사용자와 연결된 데이터

이 부분에는 Bool타잆 값이 들어간다.  

이 데이터가 사용자와 연결이 되어있는지 여부를 표시하는 부분이다

<br><br>

### Used for Tracking

이 부분은 말 그대로 이 데이터가 추적에 사용되는지 여부를 Bool값으로 표시하는 부분이다.  

<br><br>

### Collection Purposes
해당 데이터가 어떤 용도로 쓰이는 지를 기입하는 배열이다.  
용도를 서술형으로 개발자가 작문할 필요는 없다.  

<br>

<img width="624" alt="스크린샷 2024-03-08 오전 9 01 38" src="https://github.com/isGeekCode/TIL/assets/76529148/97028fdc-00a8-4754-8f79-17e8838ac95c">

<br><br>

그림에서 나오는 것 처럼 미리 문구가 정의되어있다.  
이 값들에 대한 설명은 [Apple App Store의 앱 개인정보 보호 세부정보](https://developer.apple.com/app-store/app-privacy-details/)글의 `Data use` 챕터에 정의되어있다.  

<br>
- Third-party advertising : 제3자의 광고 
- Developer’s advertising or marketing : 개발자의 광고 또는 마케팅
- Analytics : 앱 분석
- Product personalization : 제품 개인화
- App functionality : 앱 기능
- Other purposes : 기타 목적


<br><br>


## Privacy Accessed API Types
- [Apple Article : Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api)  
- [Apple Support: 타사 SDK 요구 사항 변경 예정](https://developer.apple.com/kr/support/third-party-SDK-requirements)

이 앱에서 사용하고 있는 API들의 사용이유를 정의한 배열이다.  

<br>
이 배열안에는 Dictionary타입으로 SDK를 포함하여 앱내에서 사용하고 있는 API를 정의하고 사용용도를 포함하고 있다.  

> 여기서 말하는 API란 우리가 일반적으로 정보를 `GET / POST` 형태로 하는 네트워크 요청을 말하는 것이 아니라 Apple에서 제공한 UserDefault 같은 API를 말한다.  

- Privacy Accessed API Type : 앱내에서 사용하고 있는 API 타입
- Privacy Accessed API Reasons : 앱내에서 사용하고 있는 API 사용 목적

<br><br>

### Privacy Accessed API Type
[Apple Article : Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api) 라는 글을 살펴보면 각 카테고리 별 API들에 해당하는 Privacy Accessed API Type 의 Value를 알 수 있다.  

<br>

각 카테고리는 아래와 같다.  

- File timestamp APIs 
- System boot time APIs
- Disk space APIs
- Active keyboard APIs
- User defaults APIs

<br><br>


<img width="800" alt="스크린샷 2024-03-08 오전 9 26 13" src="https://github.com/isGeekCode/TIL/assets/76529148/1e2bb4cf-88e8-4ee6-a34e-53dd69202a1c">

위 이미지는 참고링크 중 File timestamp APIs 파트를 보여주는 이미지다.  
첫부분에 PrivacyInfo.xcprivacy 파일에 어떻게 정의하면 되는지 쓰여있다.  

그리고 어떤 메서드들이 해당되는지 나열되어있고, 마지막으로 NSPrivacyAccessedAPITypeReasons에 들어갈 목적들이 나열되어있다.   
`DDA9.1` 와 같은 코드 값과 이 코드에 대한 설명이 나와있다.  

<br><br>

### Privacy Accessed API Reasons
방금 위에서 언급한 부분에서 코드값과 코드에 대한 설명이 나와있지만,  실제로 기입하는 부분에는 
특별한 구조로 들어가게 된다.  

Xcode15.2 까지는 `{코드값}: {사용목적을 의미하는 문장}`의 형태로 들어가게 된다.  
그런데 24.3.6 자로 공식 배포된 Xcode 15.3 을 살펴보면
`{API카테고리} - {코드값}: {사용목적을 의미하는 문장}`형태로 프리셋이 되어있기 때문에 
영작을 할 걱정은 안해도 된다.  

아래 이미지처럼 미리 정의되어있다.  

<img width="800" alt="스크린샷 2024-03-08 오전 9 35 54" src="https://github.com/isGeekCode/TIL/assets/76529148/a7ed8381-e96c-46f2-b9dc-8a3a9ea0b8bf">

<br><br>


> ‼️해당하는 사유가 없다면?
>> - [(23.12.7) Apple News and Updates - App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx)
>> 위 링크 중 사용자에게 직접적인 이익을 제공하지만 기존의 허용된 사유 목록에 없는 사용 사례가 있다면 새로운 사유로 추가하기 위해 요청을 제출할 수 있는 부분이 마련되어있다.  



여기서 중요한 것은 이 사유 중에 앱에서 사용하는 사유와 서드파티 라이브러리에서 사용하는 사유가 함께 들어있다는 것이다.  

여기서 알 수 있는 것은 두가지이다.  

1. 우리가 숨쉬듯 사용하는 UserDefault, TimeStamp 등을 사용한다면 용도를 명시해야한다는 것
2. 서드파티 SDK에서도 이 API들을 내부적으로 사용한다면 해당된 내용이 SDK내부의 privacyInfo에 있든,  개발자가 구현한 앱 내부의 privacyInfo에든 서드파티에서 사용한다는 이유가 기입되어있어야 한다는 것이다.   

어?? 서드파티에서 하는 건 어떻게 할 수 없지 않나? 라고 앱개발자가 의문을 가질 수 있지만,  

<br>

😂

Apple에서는 앱을 만드는 개발자는 앱 내에서 어떤 정보를 수집하는지, 앱 내에서 어떤 사이트가 어떤 정보를 수집하는지, 앱이든 서드파티 라이브러리든 앱 내 API를 이용해 정보를 저장하는지 전부 전부 앱 개발자 책임이라는 입장이다.!!!

실제로  [WWDC2023 : Get started with privacy manifests](https://developer.apple.com/videos/play/wwdc2023/10060/) 세션에서 아래와 같은 말을 한다.  

<img width="600" alt="스크린샷 2024-03-05 오전 10 45 11" src="https://github.com/isGeekCode/TIL/assets/76529148/90faed57-f51c-44e7-b9e3-e96408373cf1">

<br><br>

### 해당되는 SDK들
- [Apple Support : 타사 SDK 요구 사항 변경 예정](https://developer.apple.com/kr/support/third-party-SDK-requirements/)
- [(23.12.7) Apple News and Updates - App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=r1henawx)
- [(24.2.29) Apple News and Updates - App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=3d8a9yyh)

놀랍게도 우리가 자주 사용하는 Alamofire, Kingfisher, Firebase, RxSwift, RealmSwift. Snapkit, Lottie 등등 명시되어있다.  그리고 글을 살펴보면, 이밖의 SDK에서도 관련 API를 사용한다면 PrivacyInfo에 기입해야한다는 걸 알 수 있다.  

목록에 Firebase Analytics만 없다!!! 하지만.. Firebase Core는 있지롱.. Firebase Analytics는 Firebase Core에서 호출한다.  고로.. 구글 애널리틱스 / GA4 를 사용하는 앱도 무조건 넣어야한다는 것..


일단 SDK에서 사용하는 API가 어떤 게 있는지, 또 어떤 목적으로 사용하는지는 앱 개발자가 알 수 있는 방법이 한정되어있다.  그렇기 때문에 가장 좋은 방법은 SDK에서 PrivacyInfo를 추가한 업데이트를 하는 것이다.  

다행히도 Kingfisher 7.10.0 , Alamofire 5.9.0 , Snapkit 5.7.0 , 네비버로그인 4.2.0 , Lottie 4.4.1  이 SDK 들은 현재 24.3.8 일자로 모두 추가가 되었다.  

gifu나 Kingfisher는 둘다 gif를 보여주고 캐싱처리가 가능한 SDK인데 한쪽만 관련업데이트가 있다면, 교체해주거나 앱개발자가 직접 앱 내 PrivacyInfo에 서드파티가 사용한다는것을 명시해줘야한다.  
<br>
협조적으로 SDK내 PrivacyInfo 파일을 추가해주는 곳이 있는 반면,  
잘 못 업데이트한 경우도 있다.  
<br>
네이버로그인같은 경우, 발빠르게 업데이트 했지만, 키값을 잘못 사용하여 배포했기에 아래 언급할 Privacy Report단계에서 에러를 리턴했다.  
현재에는 네이버로그인도 바로 다음 버전 업데이트로 정상 동작하고 있다.  

<br>

[구글 애널리틱스](https://support.google.com/analytics/answer/10285841?hl=ko) 처럼 `데이터 공개 요건`을 언급하며 어떤 것들을 다루는지 문서만 만드는 경우도 있다.  
현재에는 구글에서도 SDK내 업데이트까지 완료하였다.   

<br>
만약 이렇게 어떤 것들을 다루는지 문서만 업로드하거나,  아무것도 언급이 없다면
앱 개발자가 스스로.. 리젝을 당해가며 PrivacyInfo파일을 수정해나가면서 실험하는 일이 생기지 않을까 싶다.  


<br><br>

## Privacy Report 
프라이버시 보고서는 앱 및 서드파티 SDK에 포함된 PrivacyInfo 파일에 보고된 값을 기반으로 Xcode에서 생성하는 PDF 파일이다.  

<img width="800" alt="스크린샷 2024-03-08 오전 10 16 07" src="https://github.com/isGeekCode/TIL/assets/76529148/69899311-30a5-401b-8836-6681683044a3">

<br><br>

앱을 아카이빙하고 Organizer 에서 해당 타겟 - Generate Privacy Report  단계로 클릭을 하면 아래와 같은 pdf가 생성된다.  

<img width="800" alt="스크린샷 2024-03-08 오전 10 16 07" src="https://github.com/isGeekCode/TIL/assets/76529148/5e2fe482-c0ec-4277-843c-b68e86fd4a56">

<br><br>

Apple에서는 여러 해 동안 Privacy Nutrition Label, 데이터 유형, 용도를 정의해 왔기 때문에 기술적으로 전혀 새로운 내용은 아니다.  

그렇기 때문에 최근 게시한 [(24.2.29) Apple News and Updates - App Store 앱 제출을 위한 개인정보 보호 관련 업데이트](https://developer.apple.com/kr/news/?id=3d8a9yyh) 글에서는 
이번에도 유예 기간을 의미하는 것만 같은 뉘앙스를 풍기고 있다.  

마치 예전 2022년에 회원가입이 있는경우 탈퇴 버튼을 추가하지 않으면 리젝사유가 된다는 유예기간을 주었던 것처럼 말이다.  
> 하지만 유예기간이 점점 연장되긴 했지

<br><br>

2024년 3월 13일 부터는 사유가 필요한 API를 사용하는 신규 / 업데이트 앱을 업로드할 때, 개인정보 보호 매니페스트(PrivacyInfo.xcprivacy)파일이 누락되면 이메일을 보내준다고 한다. 

2024년 5월 1일 부터는 API를 허용된 사유에 따라 사용하지 않는 경우 다른 대안을 찾아야한다.  

흔히 사용되는 타사 SDK 목록에 새로운 타사 SDK를 추가하는 경우 이러한 API, 개인정보 보호 매니페스트, 서명 요건이 해당 SDK에 적용된다. 개인정보 보호 매니페스트가 포함된 버전의 SDK를 사용해야 한다. 또한 SDK가 바이너리 종속성으로 추가된 경우 서명도 필요하다.

<br><br>

## History 
- 240306: 초안작성
- 240308: PrivacyInfo API 내용 추가
