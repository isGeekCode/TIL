# Flutter_0000_Document_Guide – 문서 구조 가이드


이 문서는 Flutter 학습 문서를 카테고리별로 정리하기 위한 번호 체계를 정의합니다.  

번호는 `0000`, `0100`, `0200`처럼 네 자리 숫자로 구분되며,  
README 정렬 및 검색 편의를 위해 사용됩니다.

<br><br>

---


## 📁 카테고리 번호 체계

| 번호   | 카테고리                   | 설명                                                              |
|--------|----------------|---------------|
| `0000` | [문서 구조 / 가이드 문서](#0000번대--문서-구조-및-가이드-문서)    | 이 문서 포함, 전체 구조 정의용 문서                              |
| `0100` | [개발 환경 세팅 / 설치](#0100번대--개발-환경-세팅--설치)      | Flutter 설치, IDE 설정, FVM 구성 등                               |
| `0200` | [모바일 공통 기능](#모바일 공통 기능)      | Splash 등                               |
| `1000` | [위젯 (Widgets)](#1000번대--위젯-widgets) | 기본 UI 요소, 레이아웃, 입력 등 다양한 위젯 |
| `1300` | [라우팅 & 내비게이션](#1300번대--라우팅--내비게이션)        | 화면 전환, 탭바, 라우터 구성 등       |
| `2000` | [네트워크 & 비동기](#2000번대--네트워크--비동기)          | HTTP 요청, async/await, Dio 등                                    |
| `3000` | [데이터 유틸리티 정리](#3000번대--데이터-유틸리티-정리)        | JSON 파싱, 모델 변환, 포맷 유틸 함수 등 데이터 처리 중심 |
| `4000` | [상태관리 / 앱 구조](#4000번대--상태관리--앱-구조)         | 상태 변경 흐름, setState, Provider 등 구성               |
| `5000` | [플랫폼 기능 연동](#5000번대--플랫폼-기능-연동)            | WebView, 카메라, 갤러리, 공유, 푸시 알림, 위치 정보, 파일 접근 등 디바이스 연동 기능 및 패키지 활용 |
| `6000` | [배포 및 빌드 환경](#6000번대--배포-및-빌드-환경)          | iOS, Android 앱 배포를 위한 릴리즈 빌드, 서명, 업로드 가이드 등   |
| `7000` | [앱 아키텍처](#7000번대--앱-아키텍처)                | MVC, MVP, MVVM, 클린 아키텍처, 레이어 구성, DI 등       |
| `8000` | [트러블슈팅 및 에러 정리](#8000번대--트러블슈팅-및-에러-정리)    | 기능/플러그인/OS 관련 에러 및 해결법 정리 전용 영역                  |
| `9000` | [실험 / 기타](#9000번대--실험--기타)                | 명확히 분류되지 않은 테스트 코드, 샌드박스, 일회성 정리 등        |
|  | [학습 로드맵 가이드](#학습-로드맵-가이드)                | 공식문서 기반 로드맵        |

<br><br>

---


## 0000번대 – 문서 구조 및 가이드 문서

| 번호   | 설명 |
|--------|------|
| `0000` | 문서 구조 가이드 및 번호 체계 정의 |
| `0010` | 문서 작성 및 템플릿 가이드 |

### 0200번대 – 모바일 공통 기능

| 번호   | 설명 |
|--------|------|
| `0200` | 앱의 전반적인 구조 개요                        |
| `0210` | 프로젝트 디렉토리 구조 설명                     |
| `0220` | 앱 실행 구조 (entry-point → runApp 흐름)|
| `0230` | Stateful / Stateless 위젯 흐름 구조     |
| `0270` | 스플래시             |


<br>
  
## 1000번대 – 위젯 (Widgets)

Flutter에서 화면을 구성하는 모든 UI 요소는 위젯으로 표현되며, UI 외에도 입력, 애니메이션, 접근성, 비동기 처리 등 다양한 범위의 위젯들이 존재합니다.  
이 영역은 Flutter 공식 Widget Catalog 분류 체계를 참고하여 실전에서 많이 사용하는 항목을 중심으로 정리합니다.

| 번호   | 설명                                           |
|--------|------------------------------------------------|
| `1000` | 위젯 개요 (Widget 개념, 구조, 빌드 함수 등 기본 소개) |
|   1-12 | Widget Catalog – 위젯 분류별 전체 목록 |
| `1001` | Basics – 가장 기초적인 위젯 구성 요소들 (Text, Button 등) |
| `1001.01` | Drawer – Scaffold 내 사이드 내비게이션 메뉴 구성용 위젯 |
| `1002` | Layout – 레이아웃 구성용 위젯 (Row, Column, Stack 등) |
| `1002.01` | Single-child : Center  |
| `1002.21` | Multi-child : Column  |
| `1003` | Text – 텍스트 표시 및 스타일링 관련 위젯 |
| `1004` | Input – 사용자 입력을 위한 위젯 (TextField, Button, Form 등) |
| `1005` | Assets, Images, and Icons – 이미지, 아이콘, 에셋 관련 구성 요소 |
| `1006` | Scrolling – 스크롤 가능한 콘텐츠를 구성하는 위젯 |
| `1007` | Interaction Models – 제스처 및 터치 반응 처리 위젯 |
| `1008` | Styling – 테마, 반응형 구성, 패딩 등 스타일링 위젯 |
| `1009` | Painting and Effects – 시각적 효과 및 그리기 관련 위젯 |
| `1010` | Animation and Motion – 애니메이션 효과와 트랜지션 처리 |
| `1011` | Async – 비동기 상태를 다루기 위한 위젯 (Future, Stream 등) |
| `1012` | Accessibility – 앱의 접근성을 향상시키는 도구 제공 |

---

## 1300번대 – 라우팅 & 내비게이션

Flutter의 화면 전환, 내비게이션 흐름을 담당하는 기능을 별도 카테고리로 분리하여 관리합니다.  
기본 내비게이션 API부터 고급 라우팅 패키지(go_router 등)까지 포함합니다.

| 번호   | 설명 |
|--------|------|
| `1300` | 라우팅 기본 구조 (`Navigator`, `routes`, `push/pop` 흐름) |
| `1310` | Named Route / Route Settings |
| `1320` | go_router 사용법 |
| `1330` | 탭바 & 바텀 내비게이션 관리 |
| `1340` | 페이지 전환 애니메이션 / Hero 위젯 등 |

---

### 2000번대 – 네트워크 & 비동기

| 번호   | 설명 |
|--------|------|
| `2000` | HTTP 요청, async/await, Dio 등 네트워크 및 비동기 처리 관련 |

---

### 3000번대 – 데이터 유틸리티 정리

| 번호   | 설명 |
|--------|------|
| `3000` | JSON 파싱, 모델 변환, 포맷 유틸 함수 등 데이터 처리 중심 |

---

### 4000번대 – 상태관리 / 앱 구조

| 번호   | 설명 |
|--------|------|
| `4000` | 상태 변경 흐름, setState, Provider 등 구성 |

---

### 5000번대 – 플랫폼 기능 연동

Flutter 앱에서 디바이스(OS 기반) 기능 및 외부 SDK/API를 연동하는 모든 기능을 포함하며, 내부 기능과 외부 연동을 번호로 구분합니다.

#### 📱 5100번대 – Internal Native 연동 (디바이스 기능 기반)

| 번호   | 설명 |
|--------|------|
| `5110` | WebView 연동 (InAppWebView, 다중 창 등) |
| `5120` | 카메라 및 이미지 캡처 |
| `5130` | 갤러리 이미지 선택 (ImagePicker 등) |
| `5140` | 위치 정보 활용 (geolocator 등) |
| `5150` | 파일 저장 및 접근 (path_provider 등) |
| `5160` | 푸시 알림 연동 (Firebase Messaging 등) |

#### 🌐 5200번대 – External Service 연동 (3rd-party SDK/API)

| 번호   | 설명 |
|--------|------|
| `5210` | Firebase 연동 (Auth, Firestore 등) |
| `5220` | Kakao SDK 연동 |
| `5230` | Google Sign-In 연동 |
| `5240` | Apple Sign-In 연동 |
| `5250` | 외부 결제 API 연동 (Iamport, Toss 등) |

#### ⚙️ 5300번대 – Platform Utility (OS 유틸 기능)

| 번호   | 설명 |
|--------|------|
| `5310` | OS 분기 처리 (iOS / Android 플랫폼 구분) |
| `5320` | 시스템 설정 열기 (Wi-Fi, 알림, 앱 설정 등) |
| `5330` | 기기 정보 확인 (Device Info 등) |
| `5340` | 앱 버전, 앱 이름 등 앱 메타데이터 접근 |

<br>
  
### 6000번대 – 배포 및 빌드 환경

| 번호   | 설명 |
|--------|------|
| `6100` | iOS 배포 환경 – 릴리즈 빌드, .ipa 생성, 실기기 설치, TestFlight 업로드 |
| `6200` | Android 배포 환경 – APK/AAB 빌드, 서명, 플레이스토어 업로드 |
| `6300` | 공통 배포 전략 – CI/CD, GitHub Actions, Codemagic 등 |

<br><br>

---

### 7000번대 – 앱 아키텍처

| 번호   | 설명 |
|--------|------|
| `7000` | MVC, MVP, MVVM, 클린 아키텍처, 레이어 구성, DI 등 |

<br><br>

---

### 8000번대 – 트러블슈팅 및 에러 정리

| 번호   | 설명 |
|--------|------|
| `8000` | Flutter 공통 에러 사례 모음 |
| `8100` | WebView 관련 오류 (`Platform not set`, NDK mismatch 등) |
| `8200` | Android 빌드 및 버전 호환 문제 |
| `8300` | iOS 권한 / 앱 설정 관련 이슈 |
| `8400` | 외부 패키지 충돌 및 의존성 문제 |


<br><br>

---

### 9000번대 – 실험 / 기타

| 번호   | 설명 |
|--------|------|
| `9000` | 명확히 분류되지 않은 테스트 코드, 샌드박스, 일회성 정리 등 |

<br><br>

---

## 🗂️ 파일명 규칙

- 파일명은 `Flutter_번호_제목.md` 형식으로 작성
- 제목은 명확하고 구체적으로 작성 (예: `Flutter_100_ListView.md`)
- 각 파일은 해당 카테고리 폴더에 들어있지 않아도 번호로 정렬됨


<br><br>

---

  

## 📌 예시 파일 리스트

- `Flutter_0000_Document_Guide.md`
- `Flutter_0050_Dart_Syntax_Basics.md`
- `Flutter_0100_Basic_Widget.md`
- `Flutter_0200_HTTP_Request.md`
- `Flutter_0300_Provider_Usage.md`
- `Flutter_0400_Navigator_Example.md`
- `Flutter_8100_WebView_PlatformNotSet.md`
- `Flutter_8110_WebView_NDKVersionMismatch.md`
- `Flutter_9999_Sandbox.md`


<br><br>
  
---



## 🧰 트러블슈팅 문서 템플릿

트러블슈팅 문서는 다음 항목 구조로 작성합니다:

| 항목 | 설명 |
|------|------|
| 설치 환경 | 사용한 Flutter/Dart 버전, IDE, OS 등 명시 |
| 발생 상황 | 언제, 어떤 조건에서 문제 발생했는지 설명 |
| 현상 (에러 로그) | 실제 출력된 에러 로그 또는 스크린샷 |
| 원인 분석 | 에러가 발생한 근본적인 원인 분석 |
| 해결 방법 | 코드 예시와 함께 해결법 명시 |
| 참고 링크 | 관련된 문서, 이슈 링크, 토론 링크 등 정리 |


<br><br>

## 📎 참고

이 가이드는 Flutter 문서 관리와 확장을 체계적으로 유지하기 위해 가장 앞에 위치합니다。


### 공식 개발문서 연번
읽어야할 자료를 모았습니다.  
Flutter Docs 순서 그대로 가져왔습니다.  

- 1. Get started
    - 1.1. Set up Flutter
    - 1.2. Install Flutter
        - Overview
        - Install manually
        - upgrade SDK
    - 1.3. Learn Flutter
        - 1.3.1. Introduction
        - 1.3.2. Write your first app
        - 1.3.3. Learn the fundamentals
            - 1.3.3.1. Introduction
            - 1.3.3.2. Intro to Dart
            - 1.3.3.3. Widgets
            - 1.3.3.4. Layout
            - 1.3.3.5. State management
            - 1.3.3.6. Handling user input
            - 1.3.3.7. Networking and data
            - 1.3.3.8. Local data and caching
- 2. User interface
    - 2.1. Introduction
    - 2.2. Widget catalog
        - 2.2.1. Basics 가장 기초적인 위젯 구성 요소들
        - 2.2.2. Layout 레이아웃 구성용 위젯
        - 2.2.3. Text 텍스트 표시 및 스타일링 관련 위젯
        - 2.2.4. Input 사용자 입력을 위한 위젯
        - 2.2.5. Assets, Images and Icons 이미지, 아이콘, 에셋 관련 구성 요소
        - 2.2.6. Scrolling 스크롤 가능한 콘텐츠를 구성하는 위젯
        - 2.2.7. Interaction Models 제스처 및 터치 반응 처리 위젯
        - 2.2.8. Styling 테마, 반응형 구성, 패딩 등 스타일링 위젯
        - 2.2.9. Painting and Effects 시각적 효과 및 그리기 관련 위젯
        - 2.2.10. Animation and Motion 애니메이션 효과와 트랜지션 처리
        - 2.2.11. Async 비동기 상태를 다루기 위한 위젯
        - 2.2.12. Accessibility 앱의 접근성을 향상시키는 도구 제공
    - 2.3. Layout
        - 2.3.1. Introduction
        - 2.3.2. Build a layout
        - 2.3.3. List & Grid
            - 2.3.3.1.  Create and use lists
            - 2.3.3.2. Create a horizontal  list
            - 2.3.3.3. Create a grid view
            - 2.3.3.4. Create a lists with different types of items
            - 2.3.3.5. Create lists with spaced items
            - 2.3.3.6. Work with long lists
        - 2.3.4. Scrolling
            - 2.3.4.1. Overview
            - 2.3.4.2. Use slivers to achieve fancy scrolling
            - 2.3.4.3. Place a floating app bar above a list
            - 2.3.4.4. Create a scrolling parallax effect

    - 2.4. Adaptive & responsive design
        - 2.4.1. Overview
        - 2.4.2. General approach
        - 2.4.3. SafeArea & MediaQuery
        - 2.4.4. Large screens & foldables
        - 2.4.5. User input & accessibility
        - 2.4.6. Capabilities & policies
        - 2.4.7. Automatic platform adaptations
        - 2.4.8. Best practices
        - 2.4.9. Additional resources
    - 2.5. Design & theming
        - 2.5.1. Share styles with themes
        - 2.5.2. Material design
        - 2.5.3. Migrate to Material 3
        - 2.5.4. Text
            - 2.5.4.1. Fonts & typography
            - 2.5.4.2. Use a custom font
            - 2.5.4.3. Export fonts from a package
            - 2.5.4.4. Google Fonts package
        - 2.5.5. Custom graphics
            - 2.5.5.1. Use custom fragment shaders
    - 2.6. Interactivity
        - 2.6.1. Add interactivity to your app
        - 2.6.2. Gestures
            - 2.6.2.1. Introduction
            - 2.6.2.2. Handle taps
            - 2.6.2.3. Drag an object outside an app
            - 2.6.2.4. Drag a Ul element within an app
            - 2.6.2.5. Add Material touch ripples
            - 2.6.2.6. Implement swipe to dismiss
        - 2.6.3. Input & forms
            - 2.6.3.1. Create and style a text field
            - 2.6.3.2. Retrieve the value of a text field
            - 2.6.3.3. Handle changes to a text field
            - 2.6.3.4. Manage focus in text fields Build a form with validation
        - 2.6.4. Display a snackbar
        - 2.6.5. Implement actions & shortcuts
        - 2.6.6. Manage keyboard focus
    - 2.7. Assets & media
        - 2.7.1. Add assets and images 
        - 2.7.2. Display images fror le interne
        - 2.7.3. Fade in images with aceholde
        - 2.7.4. Play and pause a video
        - 2.7.5. Transform assets at build
    - 2.8. Navigation & routing
        - 2.8.1. Overview
        - 2.8.2. Add tabs to your app Navigate to a new screen and back
        - 2.8.3. Send data to a new screen
        - 2.8.4. Return data from a screen
        - 2.8.5. Add a drawer to a screen
        - 2.8.6. Set up deep linking
        - 2.8.7. Set up app links for Android 
        - 2.8.8. Set up universal links for iOS 
        - 2.8.9. Configure web URL strategies
    - 2.9. Animations & transitions
        - 2.9.1. Introduction
        - 2.9.2. Tutorial
        - 2.9.3. Implicit animations
        - 2.9.4. Animate the properties of a container
        - 2.9.5. Fade a widget in and out
        - 2.9.6. Hero animations 
        - 2.9.7. Animate a page route transition
        - 2.9.8. Animate using a physics simulation
        - 2.9.9. Staggered animations 
        - 2.9.10. Create a staggered menu animation
        - 2.9.11. API overview
    - 2.10. Accessibility & internationalization
        - 2.10.1. Accessibility
        - 2.10.2. Internationalization
- 3. Beyond Ul
    - 3.1. Data & backend
        - 3.1.1. State management
        - 3.1.2. Networking & http
        - 3.1.3. Serialization
        - 3.1.4. Persistence
        - 3.1.5. Firebase
        - 3.1.6. Google APIs
    - 3.2. App architecture
        - 3.2.1. Introduction
        - 3.2.2. Architecture concepts
        - 3.2.3. Guide to app architecture
        - 3.2.4. Architecture case study
        - 3.2.5. Recommendations
        - 3.2.6. Design patterns
    - 3.3. Platform integration
    - 3.4. Packages & plugins
        - 3.4.1. Use packages & plugins
        - 3.4.2. Develop packages & plugins
        - 3.4.3. Swift Package Manager
    - 3.5. Testing & debugging
        - 3.5.1. Testing
            - 3.5.1.1. Overview
            - 3.5.1.2. Unit testing
            - 3.5.1.3. Widget testing
            - 3.5.1.4. Integration testing
            - 3.5.1.5. Test a plugin
            - 3.5.1.6. Handle plugin code in tests
        - 3.5.2. Debugging
            - 3.5.2.1. Debugging tools
            - 3.5.2.2. Debug your app programmatically
            - 3.5.2.3. Use a native
            - 3.5.2.4. language debugger
            - 3.5.2.5. Common Flutter errors
            - 3.5.2.6. Handle errors
            - 3.5.2.7. Report errors to a service
    - 3.6. Performance & optimization
        - 3.6.1. Overview
        - 3.6.2. Impeller
        - 3.6.3. Performance best practices
        - 3.6.4. App size
        - 3.6.5. Deferred components
        - 3.6.6. Rendering performance
        - 3.6.7. Performance profiling
        - 3.6.8. Performance profiling for web
        - 3.6.9. Performance metrics
        - 3.6.10. Concurrency and isolates
        - 3.6.11. Performance FAQ
        - 3.6.12. Appendix
    - 3.7. Deployment
        - 3.7.1. Obfuscate Dart code
        - 3.7.2. Create app flavors for Android 
        - 3.7.3. Create app flavors for iOS and macOS
        - 3.7.4. uild and release ar indroid app
        - 3.7.5. Build and release an iOS app
        - 3.7.6. Build and release a macOS app
        - 3.7.7. Build and release a Linux app und and salese a
        - 3.7.8. Build and release a web app
        - 3.7.9. Set up continuous deployment
    - 3.8. Add to an existing app
        - 3.8.1. Introduction
        - 3.8.2. Add to an Android app
        - 3.8.3. Add to an iOS app
        - 3.8.4. Add to a web app
        - 3.8.5. Debug embedded Flutter module
        - 3.8.6. Add multiple Flutter instances
        - 3.8.7. Loading sequence and performance
- 4. Flutter concepts
    - 4.1. Architectural Overview
    - 4.2. Inside Flutter
    - 4.3. Understanding constraints
    - 4.4. Flutter’s build modes
    - 4.5. Hot reload




## History
- 250618 : 초안작성
- 250619 : 트러블슈팅 관련 넘버링 추가
- 250702 : 리팩토링진행 - 모바일 개발 과정과 비슷하게 구성


## 학습 로드맵 가이드

Flutter를 처음 학습하거나 체계적으로 정리하고 싶은 사용자를 위해, 아래와 같은 단계별 로드맵과 함께 문서 번호 참고 범위를 제시합니다.

| 단계 | 학습 주제 | 학습할 공식 개발 문서 연번 |widgetCatalog|
|------|-----------|-------------------------|--|
| 1단계 | 개발 환경 세팅 및 설치 | 1.1, 1.2 ||
| 2단계 | Flutter 기초 개념 이해 | 1.3 : Learn Flutter ||
|| Flutter 기초 개념 이해 | 1.3.3.1 : Introduction ||
|| Flutter 기초 개념 이해 | 1.3.3.2 : Intro to Dart ||
|| Flutter 기초 개념 이해 : 위젯 개념 | 1.3.3.3. Widgets ||
|| Flutter 기초 개념 이해 : 레이아웃 기초 | 1.3.3.4 : Layout ||
|| 기본 위젯 익히기 | |AppBar, ElevatedButton, Icon, Image, Placeholder, Text|
|| 레이아웃 위젯 사용|  |Center, Column, Row, Container |
|| Flutter 렌더링 이해 : 위젯트리 | 1.3.3.3. Widgets , Learn Flutter 깃||
|| Flutter 렌더링 이해 : 요소 트리 | 1.3.3.3. Widgets, Learn Flutter 깃 ||
|| Flutter 렌더링 이해 : 렌더트리 | 1.3.3.3. Widgets, Learn Flutter 깃 ||
|| Flutter 기초 개념 이해 : 상태관리 기초| 1.3.3.5 : State management 중 ||
||StatelessWidget|1.3.3.5 : 상태관리 ||
||내부변수를 사용한 레이아웃 구현|1.3.3.5 : 상태관리 ||
||StatefullWidget|1.3.3.5 : 상태관리 ||
||state사이클 이해 : initState, setState|1.3.3.5 : 상태관리 ||
||버튼 동작 구현|1.3.3.5 : 상태관리|elevatedButton, TextButton|
||네비게이션|2.8. Navigator 1.0, Learn Flutter 깃||
||네비게이션|2.8. Navigator 2.0, Learn Flutter 깃||
||네비게이션|go_router, Learn Flutter 깃||
||네비게이션||Drawer|
||네비게이션||bottomNavigationBar|
||네비게이션||TabBar|
||Using widget constructors|1.3.3.5 : State management||
||Using InheritedWidget|1.3.3.5 : State management||
||Using callbacks|1.3.3.5 : State management||
||Flutter 기초 개념 이해 | 1.3.3.6 : Handling user input||
||Swipe & Slide  |1.3.3.6 : Handling user input| |
||Flutter 기초 개념 이해 | 1.3.3.7 : Networking and data ||
||네트워크 기초 | 3.1.2. 3.1.2.1. - 3.1.2.6. CRUD ||
||네트워크 기초 - Dio 사용하기 | ||
||네트워크 기초 - 직렬화 3.1.3. | ||
||각종 버튼 |1.3.3.6 : Handling user input|FilledButton, Total Button, OutlinedButton, IconButton, FloatingActionButton|
||각종 텍스트 |1.3.3.6 : Handling user input|SeleectableText, RichText, TextField, Form|
||옵션 그룹으로 선택하기  |1.3.3.6 : Handling user input|SegmentedButton, Chip, DropdownMenu, Slider|
||토글관련 위젯 배우기|1.3.3.6 : Handling user input|Checkbox, Switch, Radio, CheckboxListTile, SwitchListTile |
|| 날짜 및 시간 관련 위젯  |1.3.3.6 : Handling user input| DatePickerDialog, TimePickerDialog |
|| 상태관리 심화 |3.1.1. State management||
|| 상태관리 심화 - Using listenables.ChangeNotifier|1.3.3.5 : State management||
|| 상태관리 심화 - Using listenables.ValueNotifier|1.3.3.5 : State management||
|| 아키텍쳐 - MVVM구현하기|1.3.3.5 : State management||
|| Flutter 기초 개념 이해 | 1.3.3.8 : Local data and caching ||


| 3.3.3단계 | 텍스트 출력 및 스타일링 | 2.2.3 (Text) ||
| 3.3.4단계 | 입력 필드 및 버튼 구성 | 2.2.4 (Input) ||
| 3.3.5단계 | 이미지 및 아이콘 활용 | 2.2.5 (Assets) ||
| 3.3.6단계 | 스크롤 가능한 리스트 구성 | 2.2.6 (Scrolling) ||
| 4단계 | 사용자 인터랙션 및 제스처 처리 | 2.6.1 ~ 2.6.6, 2.2.7 ||
| 5단계 | 내비게이션 및 화면 전환 | 2.8.1 ~ 2.8.9 ||
| 6단계 | 네트워크 통신 및 비동기 처리 | 1.3.3.7, 3.1.2, 2.2.11 ||
| 7단계 | 데이터 모델링 및 유틸리티 | 1.3.3.8, 3.1.3, 3.1.4 ||
| 8단계 | 상태관리 및 앱 구조 설계 | 1.3.3.5, 3.1.1, 3.2.1 ~ 3.2.6 ||
| 9단계 | 플랫폼 기능 연동 | 3.3, 3.4.1 ~ 3.4.3 ||
| 10단계 | 디자인 시스템 및 테마 구성 | 2.5.1 ~ 2.5.5, 2.2.8 ||
| 11단계 | 애니메이션 및 트랜지션 적용 | 2.9.1 ~ 2.9.11, 2.2.10 ||
| 12단계 | 접근성 및 반응형 레이아웃 설계 | 2.4.1 ~ 2.4.9, 2.10.1 ||
| 13단계 | 배포 및 빌드 환경 구성 | 3.7.1 ~ 3.7.9 ||
| 14단계 | 아키텍처 및 설계 패턴 학습 | 3.2.1 ~ 3.2.6 ||
| 15단계 | 테스트 및 디버깅 | 3.5.1.1 ~ 3.5.1.6, 3.5.2.1 ~ 3.5.2.7 ||
| 16단계 | 에러 해결 및 트러블슈팅 | 3.6.5 ~ 3.6.6, 8000번대 참고 ||
