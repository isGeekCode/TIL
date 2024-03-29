# Xcode에서 디버그뷰 활성화하기 :Firebase, GA4

디버그뷰는 파이어 베이스에서 제공하는 디버그 도구로서, 앱 내에 설치한 로그를 출력하는 도구이다. 
특히 웹과의 소통에 따라 반응하여 로깅작업을 진행할 때, 주로 사용한다. 

- 디버그뷰 살펴보기
- 디버그뷰 세팅하기
    - 프로젝트 세팅하기
        - Firebase Console에서 프로젝트 생성
        - GA4에서 프로젝트 생성
        - Firebase에 Ga4로 연동하기
    - 앱에 설치하기
        - CocoaPods
        - 그 외
- 디버그뷰 활성화하기
    - 스키마에 속성값 넣기(개발용)
    - 속성값을 코드로 직접 삽입하기

<br><br>

# 디버그뷰 살펴보기

- 구글 FireBase Console에 접속하여 아래 이미지처럼 디버그 뷰 페이지에 진입한다. 
<img width="255" alt="스크린샷 2023-10-19 오전 9 35 12" src="https://github.com/isGeekCode/TIL/assets/76529148/e7166da3-279e-41dd-b10e-40a3b3691544">

- 세팅을 마쳤더라도 처음 디버그뷰 페이지에 진입하면 아무런 동작을 하지않는다. 로그를 하나 임의로 넣어줘야한다. 

<br>
<br>

- 디버그뷰가 활성화 되면 아래 이미지처럼 입력된 로그가 출력이 된다. 
<img width="500" alt="스크린샷 2023-10-19 오전 9 14 28" src="https://github.com/isGeekCode/TIL/assets/76529148/c04c4af2-c0d3-4bb4-98c7-f7661e973b07">

<br><br>

# 디버그뷰 세팅하기


## 프로젝트 세팅하기

### FireBase Console에서 프로젝트 생성
만약 최초상태라면 아래 링크에서 프로젝트를 생성하자.
- [FireBase Console](https://console.firebase.google.com/u/0/?hl=ko)

프로젝트 내 iOS앱 추가
- iOS를 클릭하여 앱 추가 진행
- 번들 ID와 닉네임(선택사항), App Store ID(선택사항) 입력
- Info.plist 다운로드 후 파일을 프로젝트의 하위로 복사한다.

### GA4에서 프로젝트 생성
파이어베이스가 아닌 구글 아날리틱스 에서도 디버그뷰를 볼 수 있다.

- [애널리틱스 어드민페이지](https://analytics.google.com) 에서  계정을 만든다
    - 참고링크 : [애널리틱스 고객센터](https://support.google.com/analytics/answer/9304153?hl=ko#zippy=%2Cios-%EC%95%B1-%EB%98%90%EB%8A%94-android-%EC%95%B1)
    
- 데이터 스트림 추가하기
    - 속성 열에서 데이터 스트림 > 스트림 추가를 클릭.
    - iOS 번들 ID와 앱이름, AppStore ID를 입력하고 앱 등록 클릭
    - 안내에 따라 앱의 구성파일을 다운로드
    - 통신 확인 (꼭 하지않아도 된다.)
    - 마침을 클릭
    
<img width="400" alt="158YAnucIrUyFRCYn4DXpxRTn19Jdkk0g0dj" src="https://github.com/isGeekCode/TIL/assets/76529148/046ddc2c-7e75-4758-873a-9a61e8df255f">

- 하단 속성을 누르고 디버그뷰 클릭

디버그뷰 활성화는 파이어베이스와 동일하다.




<img width="600" alt="스크린샷 2023-10-20 오후 12 35 29" src="https://github.com/isGeekCode/TIL/assets/76529148/dc43eab3-7db1-4f5e-91e5-e429a16c4faf">

<br><br>

### Firebase에 Ga4로 연동하기
기존의 FireBase로만 연동하거나, 다른 아날리틱스에서 연결을 수정하는 경우가 있다.

- Firebase 프로젝트
- 프로젝트 설정 > 통합
- Google 애널리틱스 카드에서 연결 보기를 클릭
- 기존의 애널리틱스 연결을 삭제
- 안내에 따라 새 애널리틱스 연결을 설정

애널리틱스 카드는 아래와 같은 부분을 말한다. 
<img width="600" alt="스크린샷 2023-10-20 오후 12 42 42" src="https://github.com/isGeekCode/TIL/assets/76529148/2908e58e-7a28-4144-8dad-d0a711bb2878">


<br><br>

## 앱에 설치하기
Firebase Analytics 설치

### CocoaPods
디버그뷰를 사용하기 위해선 Firebase Analytics SDK가 필요하다.

- 최초사양
    - Xcode 10.1 이상 
    - iOS 최소 버전  8.0 이상
    - CocoaPods 1.4.0 이상

```swift
// Podfile이 없는 경우 
pod init

// Podfile에 코드를 추가
pod 'Firebase/Analytics'

// 명령어 실행으로 Pod설치
pod install
```

<br><br>

### Without CocoaPods

1. framework 복사
- "FirebaseAnalytics"와 “Firebase.h” 디렉토리의 각 framework를 프로젝트 내비게이터 창으로 드래그한다.
- 나타나는 대화 상자에서 프레임 워크를 추가 할 대상 옆에 확인 표시가 있고 "Copy items if needed"를 선택해야 한다.
- Swift의 경우 “module.modulemap” 까지 포함하여 프로젝트 내부로 포함시킵니다


2. 프로젝트 설정에서 Build Settings 탭에서 "Other Linker Settings" 필드에 “-ObjC”를 추가한다.

3. 프로젝트 설정에서 Build Settings 탭에서 “Import Paths” 필드에 해당 modulemap 파일 경로를 설정한다.

4. BridingHeader 파일에 , “Firebase.h” 파일을 import한다.

5. 프로젝트 설정에서 Build Phases 탭에서 “Link Binary With Libraries”에서 FIrbaseAnalytics 폴더의 프레임워크를 추가한다.

<br><br>


## 디버그뷰 활성화하기

<br><br>

### 스키마에 속성값 넣기(개발용)

Product > Scheme > Edit Scheme > Arguments Tab에서 실행 명령어를 속성값으로 추가한다.

실행하고 싶은 속성값의 왼쪽 체크부분을 활성화하여 빌드하면된다. 

<img width="600" alt="스크린샷 2023-10-19 오전 9 50 24" src="https://github.com/isGeekCode/TIL/assets/76529148/2198998a-29d8-4e47-909c-f5d86c382178">



비활성화 코드는 아래처럼 두가지 경우가 있으나 참고하자.

```swift

// 활성화
-FIRAnalyticsDebugEnabled

// 비활성화 코드
-noFIRAnalyticsDebugEnabled

// 혹은 
-FIRAnalyticsDebugDisabled
```

<br><br>

### 속성값을 코드로 직접 삽입하기
위에서 소개한 방법은 Xcode로 빌드하는 환경에서만 동작을 확인할 수가 있다.

하지만 상황에 따라 QA팀이나 외부업체에서 디버그뷰를 확인해야하는 경우가 있다. 

이런 경우, 아래와 같이 코드로 직접 삽입을 통해 속성값을 실행시킬 수 있다.
비활성화를 위해선 다시 비활성화 속성값을 실행시켜야하니 기억하자.


- Swift코드
```swift
// TestFlight환경에서 사용하기위한 속성 삽입

// Firebase DebugView 활성화
var args = ProcessInfo.processInfo.arguments
args.append("-FIRDebugEnabled")
ProcessInfo.processInfo.setValue(args, forKey: "arguments")

FirbaseApp.configure()

// Firebase DebugView 비활성화

// Firebase DebugView 활성화
var args = ProcessInfo.processInfo.arguments
args.append("-FIRDebugDisabled")
ProcessInfo.processInfo.setValue(args, forKey: "arguments")

FirbaseApp.configure()
```

- Objective-C 코드
```swift

// Firebase DebugView 활성화
NSArray *args = NSProcessInfo.processInfo.arguments;
NSMutableArray *newArgs = [args mutableCopy];
[newArgs addObject: [NSString stringWithFormat: @"%s", "-FIRDebugEnabled"]];
[[NSProcessInfo processInfo] setValue: newArgs forKey: @"arguments"];

[FIRApp configure];


// Firebase DebugView 비활성화
NSArray *args = NSProcessInfo.processInfo.arguments;
NSMutableArray *newArgs = [args mutableCopy];
[newArgs addObject: [NSString stringWithFormat: @"%s", "-FIRDebugDisabled"]];
[[NSProcessInfo processInfo] setValue: newArgs forKey: @"arguments"];

[FIRApp configure];
    
```


### 활성화 마지막 단계
위에 표시된 작업을 모두 완료했음에도 디버그뷰가 동작하지 않는 경우,

이벤트를 날려보아야한다. 

Crashlytics에서 최초 연동을 위해 Error를 강제로 삽입하는 것 처럼 이벤트를 넣어주어야 연동이 완료된다.

- Swift
```swift
// 로그만 필요한 경우
Analytics.logEvent("testLog", parameters: nil)

// 파라미터를 사용하는 경우
let userId = "user123"
let parameters = ["user_id": userId]

// 이벤트를 로그로 기록
Analytics.logEvent("testLog", parameters: parameters)

``` 

- Objective-c
```swift
// 파라미터가 없는 경우

@import FirebaseAnalytics;

[FIRAnalytics logEventWithName:@"testLog" parameters:nil];



// 파라미터가 있는 경우

@import FirebaseAnalytics;

NSDictionary *parameters = @{@"user_id": @"user123", @"action": @"background"};
[FIRAnalytics logEventWithName:@"testLog" parameters:parameters];

``` 

<br><br>

## History
- 231019 : 초안작성
- 231020 : GA4 세팅방법 추가
