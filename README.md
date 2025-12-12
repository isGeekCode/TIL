# TIL
> Today I Learned

개발자로서 성장하는 하루하루를 기록하기위해 만든 공간입니다.

  2단계를 통해 학습, 복습하고 있습니다 ✨
  1단계. GitHub에 메모 ✨
  2단계. 블로그에 정리해서 게시 ✨


_446 TILs and counting..._

---

# TOC  
👇 각 항목별 **상세 콘텐츠**로 이동하세요.

## 🚧 In Progress
- [A_Writing_in_Progress](#a_writing_in_progress)

# Mobile 목차

## Mobile 공통 기능 목차

앱 개발에서 공통적으로 필요한 기능들을 정리합니다.  
(예: Splash 화면, UserDefaults, 퍼미션 처리 등)

- [Mobile 공통 기능 구현](#mobile-공통-기능-구현) (5)
    - [Mobile iOS 공통 기능 구현](#mobile-ios-공통-기능-구현) (2)
    - [Mobile Android 공통 기능 구현](#mobile-android-공통-기능-구현)
    - [Mobile Flutter 공통 기능 구현](#mobile-flutter-공통-기능-구현)

# Mobile - iOS

## iOS - UIKit 목차

- [📦 UIKit 기반 앱](#-ios---uikit-기반-앱) (76)
    - [📦 UIKit - 앱의 구조와 실행 흐름](#-uikit---앱의-구조와-실행-흐름) (4) - 어떻게 실행되는가
    - [🎨 UIKit - UI 구성 요소 설계](#-uikit---ui-구성-요소-설계) (56) - 어떤 뷰로 구성되는가
    - [🎨 UIKit - 레이아웃과 배치 전략](#-uikit---레이아웃과-배치-전략) (5) - 어떻게 배치할까
    - [🕹 UIKit - 이벤트 & 입력 처리 흐름](#-uikit---이벤트--입력-처리-흐름) - 어떤 입력을 어떻게 처리할까
    - [🔀 UIKit - 화면 전환 흐름](#-uikit---화면-전환-흐름) (8) - 어떤 흐름으로 이동할까
    - [🧠 UIKit - 데이터의 흐름과 상태 관리](#-uikit---데이터의-흐름과-상태-관리) - 데이터는 어떻게 전달되고, 상태는 어떻게 UI에 반영되는가
    - [🎨 UIKit - 애니메이션 & 뷰 효과 구성](#-uikit---애니메이션--뷰-효과-구성) - 어떻게 그려지는가
    - [🧠 UIKit - 메모리 관리](#-uikit---메모리-관리)

## iOS - SwiftUI 목차

- [📦 SwiftUI 기반 앱](#-ios---swiftui-기반-앱) (15)
    - [📦 SwiftUI - 앱의 구조와 실행 흐름](#-swiftui---앱의-구조와-실행-흐름) (1) - 어떻게 실행되는가
    - [🎨 SwiftUI - UI 구성 요소 설계](#-swiftui---ui-구성-요소-설계) (12) - 어떤 뷰로 구성되는가
    - [🎨 SwiftUI - 레이아웃과 배치 전략](#-swiftui---레이아웃과-배치-전략) - 어떻게 배치할까
    - [🕹 SwiftUI - 이벤트 & 입력 처리 흐름](#-swiftui---이벤트--입력-처리-흐름) - 어떤 입력을 어떻게 처리할까
    - [🔀 SwiftUI - 화면 전환 흐름](#-swiftui---화면-전환-흐름) - 어떤 흐름으로 이동할까
    - [🧠 SwiftUI - 데이터의 흐름과 상태 관리](#-swiftui---데이터의-흐름과-상태-관리) - 데이터는 어떻게 전달되고, 상태는 어떻게 UI에 반영되는가
    - [🎨 SwiftUI - 애니메이션 & 뷰 효과 구성](#-swiftui---애니메이션--뷰-효과-구성) - 어떻게 그려지는가
    - [🧠 SwiftUI - 메모리 관리](#-swiftui---메모리-관리)

## iOS - 공통
- [🔗 UIKit / SwiftUI - 상호 연동](#-uikit--swiftui-상호-연동) (4)


## iOS - 기능 개발 핵심 목차

- [🌐 iOS - 통신 & 네트워킹](#-ios---통신--네트워킹) (23)
- [🔧 iOS - 시스템 기능 & 네이티브 API](#-ios---시스템-기능--네이티브-api) (20)
  - [🔔 iOS - 푸시 알림 및 백그라운드 처리](#-ios---푸시-알림-및-백그라운드-처리)
- [🔌 iOS - 플랫폼 네이티브 기능 연동](#-ios---플랫폼-네이티브-기능-연동) (18)
- [🔗 iOS - 서드파티 라이브러리 연동](#-ios---서드파티-라이브러리-연동) (17)


## iOS - 앱 아키텍쳐 및 성능 목차
- [iOS - 앱 아키텍쳐 및 성능](#ios---앱-아키텍쳐-및-성능) (31)
    - [🏗 iOS - 아키텍처 및 모듈 설계](#-ios---아키텍처-및-모듈-설계) (19)
    - [🔀 iOS - 동시성 처리](#-ios---동시성-처리) (8)
    - [🧱 iOS - Deprecated API 마이그레이션 기록](#-ios---deprecated-api-마이그레이션-기록) (4)


## iOS - 시스템 및 운영 배포 목차
- [iOS - 시스템 및 운영 배포](#ios---시스템-및-운영-배포) (19)
    - [🔧 iOS - 시스템 환경 설정](#-ios---시스템-환경-설정) (6)
    - [🚀 iOS - 배포](#-ios---배포) (12)
    - [🚀 iOS - CI/CD](#-ios---cicd)
    - [🧯 iOS - 운영 이슈 문제 해결](#-ios---운영-이슈-문제-해결) (1)

## iOS - 테스트 및 도구 목차
- [iOS - 테스트 및 도구](#-ios---테스트-및-도구) (7)
    - [🧰 iOS - 개발 보조 도구 및 구성 관리](#-ios---개발-보조-도구-및-구성-관리) (6)
    - [🧪 iOS - 앱 테스트 구성 요소](#-ios---앱-테스트-구성-요소) (1)


## 🎨 iOS - 그래픽 렌더링 & 시각 효과 목차
- [iOS - 그래픽 렌더링 & 시각 효과](#ios---그래픽-렌더링--시각-효과) (11)
    - [🖼 iOS - Core Graphics - 직접 드로잉 처리](#-ios---core-graphics---직접-드로잉-처리)
    - [💫 iOS - Core Animation - 저수준 애니메이션 처리](#-ios---core-animation---저수준-애니메이션-처리) (1)
    - [🎮 iOS - Metal - 고성능 GPU 렌더링](#-ios---metal---고성능-gpu-렌더링)
    - [🌈 iOS - Core Image - 이미지 필터링 및 효과](#-ios---core-image---이미지-필터링-및-효과)
    - [🕹 iOS - SceneKit & ARKit - 3D 및 증강현실](#-ios---scenekit--arkit---3d-및-증강현실)

## iOS - 보안 및 저장 목차
- [🛡 iOS - 보안 및 데이터 저장 기술](#-ios---보안-및-데이터-저장-기술) (11)

## iOS - 컨퍼런스 인사이트
- [🏛 국내 컨퍼런스 정리](#-국내-컨퍼런스-정리)
    - [Let'Swift](#letswift)
    - [Let us:Go!](#let-usgo)
    - [asyncSwift](#asyncswift)
    - [realm 아카데미 iOS](#realm-아카데미-ios)
    - [Meetup](#async-swift)
    - [adiOS](#adiOS)

- [🌍 해외 컨퍼런스 정리](#-해외-컨퍼런스-정리)
    - [WWDC](#wwdc)

## iOS - 샘플 앱 목차
- [🧾 iOS - 샘플 앱](#-ios---샘플-앱) (3)



<br><br>

---

# Mobile - Android

## Android - View System 기반 앱 목차

- [📦 View 기반 앱](#-android---view-기반-앱)
    - [📦 View - 앱의 구조와 실행 흐름](#-view---앱의-구조와-실행-흐름) - 어떻게 실행되는가
    - [🎨 View - UI 구성 요소 설계](#-view---ui-구성-요소-설계) - 어떤 뷰로 구성되는가
    - [🎨 View - 레이아웃과 배치 전략](#-view---레이아웃과-배치-전략) - 어떻게 배치할까
    - [🕹 View - 이벤트 & 입력 처리 흐름](#-view---이벤트--입력-처리-흐름) - 어떤 입력을 어떻게 처리할까
    - [🔀 View - 화면 전환 흐름](#-view---화면-전환-흐름) - 어떤 흐름으로 이동할까
    - [🧠 View - 데이터의 흐름과 상태 관리](#-view---데이터의-흐름과-상태-관리) - 데이터는 어떻게 전달되고, 상태는 어떻게 UI에 반영되는가
    - [🎨 View - 애니메이션 & 뷰 효과 구성](#-view---애니메이션--뷰-효과-구성) - 어떻게 그려지는가
    - [🧠 View - 메모리 관리](#-view---메모리-관리)

## Android - Jetpack Compose 기반 앱 목차

- [📦 Compose 기반 앱](#-android---compose-기반-앱)
    - [📦 Compose - 앱의 구조와 실행 흐름](#-compose---앱의-구조와-실행-흐름) - 어떻게 실행되는가
    - [🎨 Compose - UI 구성 요소 설계](#-compose---ui-구성-요소-설계) - 어떤 뷰로 구성되는가
    - [🎨 Compose - 레이아웃과 배치 전략](#-compose---레이아웃과-배치-전략) - 어떻게 배치할까
    - [🕹 Compose - 이벤트 & 입력 처리 흐름](#-swiftui---이벤트--입력-처리-흐름) - 어떤 입력을 어떻게 처리할까
    - [🔀 Compose - 화면 전환 흐름](#-compose---화면-전환-흐름) - 어떤 흐름으로 이동할까
    - [🧠 Compose - 데이터의 흐름과 상태 관리](#-compose---데이터의-흐름과-상태-관리) - 데이터는 어떻게 전달되고, 상태는 어떻게 UI에 반영되는가
    - [🎨 Compose - 애니메이션 & 뷰 효과 구성](#-swiftui---애니메이션--뷰-효과-구성) - 어떻게 그려지는가
    - [🧠 Compose - 메모리 관리](#-compose---메모리-관리)

## Android - 공통
- [🔗 View System / Compose 상호 연동](#-view-system---compose-상호-연동)


## Android - 기능 개발 핵심 목차

- [🌐 Android - 통신 & 네트워킹](#-android---통신--네트워킹)
- [🔧 Android - 시스템 기능 & 네이티브 API](#-android---시스템-기능--네이티브-api)
  - [🔔 Android - 푸시 알림 및 백그라운드 처리](#-android---푸시-알림-및-백그라운드-처리)
- [🔌 Android - 플랫폼 네이티브 기능 연동](#-android---플랫폼-네이티브-기능-연동)
- [🔗 Android - 서드파티 라이브러리 연동](#-android---서드파티-라이브러리-연동)


## Android - 앱 아키텍쳐 및 성능 목차
- [Android - 앱 아키텍쳐 및 성능](#android---앱-아키텍쳐-및-성능)
    - [🏗 Android - 아키텍처 및 모듈 설계](#-android---아키텍처-및-모듈-설계)
    - [🔀 Android - 동시성 처리](#-android---동시성-처리)
    - [🧱 Android - Deprecated API 마이그레이션 기록](#-android---deprecated-api-마이그레이션-기록)


## Android - 시스템 및 운영 배포 목차
- [Android - 시스템 및 운영 배포](#android---시스템-및-운영-배포)
    - [🔧 Android - 시스템 환경 설정](#-android---시스템-환경-설정)
    - [🚀 Android - 배포](#-android---배포)
    - [🚀 Android - CI/CD](#-android---cicd)
    - [🧯 Android - 운영 이슈 문제 해결](#-android---운영-이슈-문제-해결)

## Android - 테스트 및 도구 목차
- [Android - 테스트 및 도구](#-android---테스트-및-도구)
    - [🧰 Android - 개발 보조 도구 및 구성 관리](#-android---개발-보조-도구-및-구성-관리)
    - [🧪 Android - 앱 테스트 구성 요소](#-android---앱-테스트-구성-요소)


## 🎨 Android - 그래픽 렌더링 & 시각 효과 목차
- [Android - 그래픽 렌더링 & 시각 효과](#android---그래픽-렌더링--시각-효과)
    - [🖼 Android - Canvas & Paint](#-android---canvas--paint) - 직접 드로잉 처리
    - [💫 Android - Animator / MotionLayout](#-android---animator--motionlayout) - 애니메이션 처리
    - [🎮 Android - OpenGL / Vulkan](#-android---opengl--vulkan) - 고성능 그래픽
    - [🌈 Android - BlendMode / RenderScript](#-android---blendmode--renderscript) - 이미지 필터 및 색상 효과
    - [🕹 Android - ARCore / Sceneform](#-android---arcore--sceneform) - AR 및 3D 렌더링

## Android - 보안 및 저장 목차
- [🛡 Android - 보안 및 데이터 저장 기술](#-ios---보안-및-데이터-저장-기술) (11)


## Android - 샘플 앱 목차
- [🧾 Android - 샘플 앱](#-ios---샘플-앱) (3)


<br><br>

---




# Mobile - Flutter 목차

- [Mobile Flutter 공통 기능 구현](#mobile-flutter-공통-기능-구현)

## Flutter 목차
- [📦 Flutter - 앱의 구조와 실행 흐름](#-flutter---앱의-구조와-실행-흐름) (2)
- [🎨 Flutter - UI 구성 요소 설계](#-flutter---ui-구성-요소-설계) (11)
    - [Basic Widgets](#basic-widgets) (5) - 가장 기초적인 위젯 구성 요소들 (Text, Button 등)
    - [Layout Widgets](#layout-widgets) (5) - 레이아웃 구성용 위젯 (Row, Column, Stack 등)
    - [Text Widgets](#text-widgets) (1) - 텍스트 표시 및 스타일링 관련 위젯
    - [Input Widgets](#input-widgets) - 사용자 입력을 위한 위젯 (TextField, Button, Form 등)
    - [Assets, Images, and Icons](#images-and-icons) - 이미지, 아이콘, 에셋 관련 구성 요소
    - [Scrolling Widgets](#scrolling-widgets) - 스크롤 가능한 콘텐츠를 구성하는 위젯
    - [Interaction Models](#interaction-models) - 제스처 및 터치 반응 처리 위젯
    - [Styling Widgets](#styling-widgets) - 테마, 반응형 구성, 패딩 등 스타일링 위젯
    - [Painting and Effects](#painting-and-effects) - 시각적 효과 및 그리기 관련 위젯
    - [Animation and Motion](#animation-and-motion) - 애니메이션 효과와 트랜지션 처리
    - [Async Widgets](#async-widgets) - 비동기 상태를 다루기 위한 위젯 (Future, Stream 등)
    - [Accessibility Widgets](#accessibility-widgets) - 앱의 접근성을 향상시키는 도구 제공
    

- [📐 Flutter - 레이아웃과 배치 전략](#-flutter---레이아웃과-배치-전략) (3)
- [🕹 Flutter - 이벤트 & 입력 처리 흐름](#-flutter---이벤트--입력-처리-흐름)
- [🔀 Flutter - 화면 전환 흐름](#-flutter---화면-전환-흐름) (1)
- [🧠 Flutter - 데이터의 흐름과 상태 관리](#-flutter---데이터의-흐름과-상태-관리) (5)
- [🎨 Flutter - 애니메이션 & 뷰 효과 구성](#-flutter---애니메이션--뷰-효과-구성)
- [🧠 Flutter - 메모리 관리 및 성능 최적화](#-flutter---메모리-관리-및-성능-최적화)



## Flutter - 기능 개발 핵심 목차
- [🌐 Flutter - 통신 & 네트워킹](#-flutter---통신--네트워킹) (4)
- [🔧 Flutter - 시스템 기능 & 네이티브 API](#-flutter---시스템-기능--네이티브-api)
  - [🔔 Flutter - 푸시 알림 및 백그라운드 처리](#-flutter---푸시-알림-및-백그라운드-처리)
- [🔌 Flutter - 플랫폼 네이티브 기능 연동](#-flutter---플랫폼-네이티브-기능-연동)
- [🔗 Flutter - 서드파티 라이브러리 연동](#-flutter---서드파티-라이브러리-연동)

## Flutter - 앱 아키텍쳐 및 성능 목차
- [Flutter - 앱 아키텍쳐 및 성능](#flutter--앱-아키텍쳐-및-성능)
    - [🏗 Flutter - 아키텍처 및 모듈 설계](#-flutter---아키텍처-및-모듈-설계)
    - [🔀 Flutter - 동시성 처리](#-flutter---동시성-처리)
    - [🧱 Flutter - Deprecated API 마이그레이션 기록](#-flutter---deprecated-api-마이그레이션-기록)


## Flutter - 시스템 및 운영 배포 목차
- [Flutter - 시스템 및 운영 배포](#flutter---시스템-및-운영-배포) (8)
    - [🔧 Flutter - 시스템 환경 설정](#-flutter---시스템-환경-설정) (3)
    - [🚀 Flutter - 배포](#-flutter---배포) (1)
    - [🚀 Flutter - CI/CD](#-flutter---cicd)
    - [🧯 Flutter - 운영 이슈 문제 해결](#-flutter---운영-이슈-문제-해결) (4)

## Flutter - 테스트 및 도구 목차
- [Flutter - 테스트 및 도구](#-flutter---테스트-및-도구)
    - [🧰 Flutter - 개발 보조 도구 및 구성 관리](#-flutter---개발-보조-도구-및-구성-관리)
    - [🧪 Flutter - 앱 테스트 구성 요소](#-flutter---앱-테스트-구성-요소)


## 🎨 Flutter - 그래픽 렌더링 & 시각 효과 목차
- [🎨 Flutter - 그래픽 렌더링 & 시각 효과 목차]
    - [🖼 CustomPainter](#-custompainter) (1) - drawLine, drawRect 등으로 직접 도형을 그리는 방법
    - [💫 AnimationController & Tween] - 커스텀 애니메이션 처리
    - [🎮 Flutter + OpenGL / Unity 통합] - 고성능 그래픽 또는 3D 렌더링이 필요한 경우 외부 엔진 연동 방법
    - [🌈 ImageFilter & BlendMode] - 이미지 필터와 색상 효과 등 이미지 시각 효과 적용
    - [🕹 Flutter AR & 3D 시도 사례] - ARKit, SceneKit처럼 AR 기능은 외부 플러그인 기반 접근 정리

⸻


## Flutter - 보안 및 저장 목차
- [🛡 Flutter - 보안 및 데이터 저장 기술](#-flutter---보안-및-데이터-저장-기술)


## Flutter - 샘플 앱 목차
- [🧾 Flutter - 샘플 앱](#-flutter---샘플-앱)



<br><br>

---

# 🌐 Web  
- [HTML Samples](#web-html-sample)
- [CSS Patterns](#web-css-patterns)
- [React](#web-react)



<br><br>

---  

# 📚 Programming Language Reference  

- [🧬 Languages](#-languages)
    - [Lang-Swift](#lang-swift) (51)
    - [Lang-Objective-C](#lang-objective-c)
    - [Lang-Ruby](#lang-ruby) (3)
    - [Lang-Dart](#lang-dart) (7)
    - [Lang-TypeScript](#lang-typescript)
    - [Lang-JavaScript](#lang-javascript)
    - [Lang-SQL](#lang-sql)


### Markup & Style
- [Lang-Markdown](#lang-markdown) (5)
- [Lang-HTML](#lang-html)
- [Lang-CSS](#lang-css)


<br><br>

---

- [🖥️ Computer Science](#-computer-science)
    - [📚 Basics](#-basics) (2) - 컴퓨터 과학의 기초 개념, 비트와 바이트, 논리 게이트 등
    - [⚙️ Hardware](#-hardware) - CPU, 메모리, 저장장치 등 하드웨어 구성 요소
    - [🧩 Software](#-software) (5) - 운영체제, 컴파일러, 소프트웨어 개발의 기반
    - [📐 Algorithms](#-algorithms) (18) - 문제 해결을 위한 알고리즘과 패턴
    - [📦 Data Structure](#-data-structure) (5) - 배열, 리스트, 트리 등 자료 구조
    - [🌐 Networking](#-networking) (7) - 인터넷, TCP/IP, OSI 7계층 등 네트워크 원리
    - [🧮 Programming Paradigms](#-programming-paradigms) (3) - 명령형, 함수형, 객체지향 등 프로그래밍 방식
    - [🎯 Design Patterns](#-design-patterns) (2) - 재사용 가능한 소프트웨어 설계 패턴 (싱글턴, 팩토리, 옵저버 등)
    - [🏛 Architecture Patterns](#-architecture-patterns) - 앱의 구조를 구성하는 고수준 설계 패턴 (MVC, MVVM 등)
    - [🛡 Security & Cryptography](#-security--cryptography) - 인증, 암호화, 보안 위협 대응 방법
    - [🗄 Database](#-database) - 데이터베이스 기본 개념과 SQL 활용
    - [🧠 AI / Machine Learning](#-ai--machine-learning) (28) - 인공지능의 기본 개념과 머신러닝 모델
    
      
### ⚙️ DevOps / Tools

- [Tools](#tools) (1)
- [CI_CD](#ci_cd)
- [Docs](#docs)
- [Git](#git) (20)


## 🌐 Other Topics

- [About-IT](#about-it)
- [Conference](#conference)


## 🤖 AI & Errors

- [About-Error](#about-error)

---


## 🧭 Personal Meta
- [Insight](#insight)
- [Self-Review](#self-review)


<br><br>

---


# Detail TILs
세부 Topic들이 입력되는곳

### [A_Writing_in_Progress](#a_writing_in_progress)
- [Design Pattern - Command 패턴(작성예정)](A_Writing_in_Progress/Architecture_201_De_Command.md)
- [Design Pattern - Composite 패턴(작성예정)](A_Writing_in_Progress/Architecture_201_De_Composite.md)
- [Design Pattern - Factory method 패턴(작성예정)](A_Writing_in_Progress/Architecture_201_De_Factory.md)
- [Design Pattern - Mediator 패턴(작성예정)](A_Writing_in_Progress/Architecture_201_De_Mediator.md)
- [Design Pattern - Strategy 패턴(작성예정)](A_Writing_in_Progress/Architecture_201_De_Strategy.md)
- [[Apple Documentation Archive] Auto Layout Guide(작성중)](A_Writing_in_Progress/Devpedia_AutolayoutGuide.md)
- [[Apple Documentation Archive] Coordinate System : View의 좌표계(작성중)](A_Writing_in_Progress/Devpedia_coordinateSystem.md)
- [Integrity - App Attest (앱 증명)](A_Writing_in_Progress/Integrity.AppAttest.md)
- [Integrity - KeyChain](A_Writing_in_Progress/Integrity_KeyChain.md)
- [Integrity - Secure Enclave](A_Writing_in_Progress/Integrity_secureEnclave.md)
- [소켓이란](A_Writing_in_Progress/TIL220420_socket.md)

<br><br>


### [About-Error](#about-error)
- [[StoryBoard] - Unknown class ViewControllerC in Interface Builder file](About-Error/StoryBoard_InheritModuleFromTarget.md)
- [Git Error - command line tools are already installed (사실 git 에러 아님)](About-Error/gitError_CommandLineTool.md)
- [Git Error - RPC failed; curl 18 transfer closed with...](About-Error/gitError_RPCfailed.md)
- [GitLab Error - You won't be able to pull or push project code via SSH until ...](About-Error/gitLabError_SSHKey.md)
- [SourceTree Error - 시도때도 없이 꺼지는 현상](About-Error/sourceTreeError_fatalError.md)
- [Terminal Error - xcrun: error: active developer path...](About-Error/terminalError_xcrunError.md)
- [Xcode Error - Presenting view controllers on detached view controllers is discouraged.](About-Error/xcodeError_Alert_In_UIViewController_Init.md)
- [Xcode Error - Build input file cannot be found:](About-Error/xcodeError_BuildInputFile.md)
- [Xcode Error - The CFBundleShortVersionString of an app extension (‘1.0’) must match that of its containing parent app](About-Error/xcodeError_CFBundleShortVersionString.md)
- [Xcode Error - Command PhaseScriptExecution failed with a nonzero exit code](About-Error/xcodeError_CommandPhaseScript.md)
- [Xcode Error - Launching _AppName_ is taking longer than expected](About-Error/xcodeError_Launching_is_taking_longer_than.md)
- [Xcode Error - Unable to process request - PLA Update available](About-Error/xcodeError_UnableProcess.md)
- [Xcode Error - Unknown class @@ in Interface Builder file.](About-Error/xcodeError_UnknownClassInInterface.md)
- [Xcode Error - Assistant가 작동하지 않을때 체크해야할 것](About-Error/xcodeError_XcodeAssistant.md)
- [Xcode Error - Cannot be opened because it is in a future Xcode project file format.](About-Error/xcodeError_cannotBeOpened.md)
- [Xcode Error - iPhone is busy: Making Apple Watch ready for development](About-Error/xcodeError_makingAppleWatch.md)
- [Xcode Error - maximumViewportInset cannot be larger than frame](About-Error/xcodeError_viewResizing.md)
- [Xcode Error - warning: libobjc.A.dylib is being read from process memory...](About-Error/xcodeError_warningLibObjc.md)
- [Xcode Error - xcode-select: error: tool 'xcodebuild' requires Xcode](About-Error/xcodeError_xcodeBuild.md)

### [Sample-App-List](#sample-app-list)
- [sample App - 투두리스트](Sample-App-List/sample_000todoList.md)
- [sample App - 그림판앱](Sample-App-List/sample_001pictureApp.md)
- [Sample App : 설정앱 - SwiftUI](Sample-App-List/sample_002SettingApp_SwiftUI.md)
- [Sample App : 설정앱 - UIKit(Code)](Sample-App-List/sample_002SettingApp_UIKit.md)
- [Sample App : 네트워킹과정 앱 - SwiftUI [Data parse, URLSession, completion, Singleton, Error, Result, Generic]](Sample-App-List/sample_010networkingApp_SwiftUI.md)
- [Block6 앱 만들기](Sample-App-List/sample_blockSix.md)

### [About-IT](#about-it)
- [써드파티(Third party)](About-IT/Third_party.md)
- [Apple Document Words - 단어장](About-IT/iOS_words.md)
- [IT용어 - 공수, mm , m/m , 공수 계산하기](About-IT/mm.md)



## ASIS
- [Data Structure - 다양한 데이터 구조, iOS에서 사용하는 데이터 구조](ComputerScience/DataStructure.md)
- [iOS에서 메모리구조 : Code / Data / Heap / Stack](ComputerScience/memoryStructure.md)
- [터미널 - 커스텀 함수 및 환경변수 설정하기](ComputerScience/Terminal_customization.md)
- [Terminal 기초 사용법](ComputerScience/Terminal_manual.md)
- [iOS의 Virtual Memory에 대하여](ComputerScience/VirtualMemory.md)
- [Data Structure - Stack과 Queue](ComputerScience/cs_001_stackQeueue.md)
- [Dynamic Programming (DP): 동적프로그래밍](ComputerScience/dynamicProgramming.md)


### [Conference](#conference)
- [Let us: Go! 2022 가을 - 221105(미참석)](Conference/Conference2022_LetUsGo2022_3Fall.md)
- [iOS Daejeon Club - 230325(참석)](Conference/Conference2023_IOSDaejonCodingClub_230325.md)
- [Let us: Go! 2023 봄 - 2304(미참석)](Conference/Conference2023_LetUSGo2023_1Spring.md)


## Mobile 공통 기능 구현
아래와 같이 매칭합니다.
```
📁 Mobile_00_Common/
  ├── MobileCommon_000.Splash.md
  ├── MobileCommon_001.LocalMemory.md
  └── ...

📁 Mobile_01_iOS/
  ├── iosCommon_000.Splash.md
  ├── iosCommon_001.UserDefault.md
  └── ...

📁 Mobile_02_Android/
  ├── androidCommon_000.Splash.md
  ├── androidCommon_001.SharedPreference.md
  └── ...

📁 Mobile_03_Flutter/
  ├── flutterCommon_000.Splash.md
  ├── flutterCommon_001.SharedPreference.md
  └── ...
```

- [App 공통 구성 요소 -  Intro](Mobile_00_Common/MobileCommon_000.Intro.md)
- [App 공통 구성 요소 - Splash](Mobile_00_Common/MobileCommon_001.Splash.md)
- [App 공통 구성 요소 - Local Storage](Mobile_00_Common/MobileCommon_002.LocalStorage.md)
- [App 공통 구성 요소 - DeepLink](Mobile_00_Common/MobileCommon_003.DeepLink.md)
- [App 공통 구성 요소 - WebView–Native 통신](Mobile_00_Common/MobileCommon_004.WebViewNativeCommunication.md)

<br>

# Mobile iOS

## Mobile iOS 공통 기능 구현
- [iOS - 스플래시 화면 구현 가이드 (정적 & 동적)](Mobile_01_iOS/iOSCommon_001.SplashScreen.md)
- [iOS -WebView–Native 통신](Mobile_01_iOS/iOSCommon_004.WebViewNativeCommunication.md)
## 기초 개념
- [iOS_Hierachy - Foundation](Mobile_01_iOS/iOS-Hierachy/IOS_Hierachy_Foundation.md)
- [iOS_Hierachy - UIKit](Mobile_01_iOS/iOS-Hierachy/IOS_Hierachy_UIKit.md)


## 📦 iOS - UIKit 기반 앱
### 📦 UIKit - 앱의 구조와 실행 흐름
- [[Apple Document] - UIApplicationMain(::::)](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_000UIApplicationMain.md)
- [[Apple Document] - UIApplication 싱글턴 객체](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_001UIApplication.md)
- [[Apple Document] - AppDelegate, UIApplicationDelegate 프로토콜](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_002UIApplicationDelegate.md)
- [[Apple Document] - Managing your app’s life cycle : 앱의 생명주기 관리](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_003AppLifeCycle.md)
- [[Apple Document] - Responding to the launch of your app : 앱 실행에 대한 응답](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_004LaunchStoryboard.md)
- [[Apple Document] - About the app launch sequence : 앱의 실행되는 순서에 관하여](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_005AppLaunchSequnce.md)
- [앱의 구동에 관하여](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/AppLaunching_About.md)
- [UIApplication_AppDelegate - 헷갈릴수 있는 두 함수(didReceive형제)](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate-DifferenceNotification.md)
- [UIApplication_AppDelegate - userNotificationCenter](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate_userNotificationCenter.md)
- [UIApplication_AppDelegate - UIApplicationDelegate : 앱의 상태 / 생명주기(Life-Cycle)](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_StatusCycle_of_App.md)


### 🎨 UIKit - UI 구성 요소 설계
- UIKit 기반 화면에서 **어떤 UI 컴포넌트를 배치하고 구성하는지**에 초점을 맞춘 문서들입니다.
- [[Apple Document] - About App Development with UIKit](Mobile_01_iOS/iOS-Framework-UIKit/About_UIKit_.md)
- [UIKit기반 앱의 간단한 화면 인터페이스 구조](Mobile_01_iOS/iOS-Framework-UIKit/About_UIKit_050WindowsAnsScreens_Screens_SimpleUIKitInterface.md)
- [읽어야할 개발자 문서](Mobile_01_iOS/iOS-Framework-UIKit/About__Document_Recommended.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(0) : Intro](Mobile_01_iOS/iOS-Framework-UIKit/About__UIKit_Tutorial00_Today00.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(1) : Creating a list View](Mobile_01_iOS/iOS-Framework-UIKit/About__UIKit_Tutorial00_Today01.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(2) : Adopting collection views](Mobile_01_iOS/iOS-Framework-UIKit/About__UIKit_Tutorial00_Today02.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(3) : Displaying cell info](Mobile_01_iOS/iOS-Framework-UIKit/About__UIKit_Tutorial00_Today03.md)
- [Container ViewController Type - Navigation Controller](Mobile_01_iOS/iOS-Framework-UIKit/Container_ViewController_NavigationController.md)
- UIView 기반 컴포넌트
    - [Layout - UIView에 대하여](Mobile_01_iOS/iOS-Framework-UIKit/Layout_About_UIView.md)
    - [UIView 클래스](Mobile_01_iOS/iOS-Framework-UIKit/UIView_Class.md)
    - [Layout - CodeUI: UIView, UILabel](Mobile_01_iOS/iOS-Framework-UIKit/Layout_CodeUI_UILabel_UIView.md)
    - [Layout - CodeUI: UILabel 고정폭 지정 이유 및 방법](Mobile_01_iOS/iOS-Framework-UIKit/Layout_CodeUI_UILabel_Width_Fix.md)
    - [현재기기의 화면크기 측정하기 + 콤바인을 이용한 반응형레이아웃 만들기](Mobile_01_iOS/iOS-Framework-UIKit/Layout_currentDeviceCheck&useCombineReactiveAutoLayout.md)
    - [UIView - UIPickerView](Mobile_01_iOS/iOS-Framework-UIKit/View_UIPickerView.md)
    - [UIView - UIProgressView](Mobile_01_iOS/iOS-Framework-UIKit/View_UIProgressView.md)
    - [UIView - UITabBar](Mobile_01_iOS/iOS-Framework-UIKit/View_UITabBar.md)
    - [UIView - UIActivityIndicatorView 사용법](Mobile_01_iOS/iOS-Framework-UIKit/View_UIActivityIndicatorView.md)
    - [UIKit - UISearchBar](Mobile_01_iOS/iOS-Framework-UIKit/UIKit_UITextField_UISearchBar.md)
    - UIImageView
        - [View - UIImageView 핵심 가이드](Mobile_01_iOS/iOS-Framework-UIKit/View_UIImageView.md)
        - [UIImageView - 이미지 다운로드 세팅](Mobile_01_iOS/iOS-Framework-UIKit/View_UIImageView_Download.md)

- UIScrollView 기반 컴포넌트
    - [UIScrollView 소개](Mobile_01_iOS/iOS-Framework-UIKit/View_UIScrollView.md)
    - [UICollectionView - 프로퍼티 옵저버 didSet과 isSelected](Mobile_01_iOS/iOS-Framework-UIKit/ios_CollectionViewCell.md)
    - [UICollectionView 사용법](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_00_howToMake.md)
    - [UICollectionView with DiffableDataSource](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_30_Diffable.md)
    - [UICellAccessory 정리](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_41_-UICellAccessory.md)
    - [UITableView - 템플릿](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_00_Template.md)
    - [UITableView - 기본 생성](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_01_basic.md)
    - [UITableView - 커스텀 셀](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_02_CustomTableViewCell.md)
    - [UITableView - Section 구현](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_03_Section.md)
    - [UITableView - 셀 선택, 삭제, 상호작용](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_04_select_UI.md)
    - [UITableView - 동적 셀 높이](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_05_AutomaticDimension.md)
    - [UITableView - editingStyle](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_10_editingStyle.md)
    - [[Apple Document] UITableViewCell](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_40_UITableViewCell.md)
    - [UITableViewCell - accessoryType](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_41_UITableViewCell_Delegate_AccessoryType.md)
    - [UITableView - 경계선 없는 셀](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_50_excludeOutline.md)
    - [UITableView - 확장/접기 셀](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_80_FlexibleTableViewCell.md)
    - [UITableView - SwiftUI 구성](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_81_SwiftUI_Configuration.md)

- UIControl 기반 컴포넌트
    - [[Apple Document] UIControl.Event 살펴보기](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/About_UIControl_030_event.md)
    - [UIButton](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIButton.md)
    - [UIDatePicker](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIDatePicker.md)
    - [UIRefreshControl](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIRefreshControl.md)
    - [UISegmentedControl](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISegmentedControl.md)
    - [UISlider](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISlider.md)
    - [UISwitch](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISwitch.md)
    - [UITextField](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UITextField.md)

- UIViewController 기반 구성 요소
    - [UIViewController 소개](Mobile_01_iOS/iOS-Framework-UIKit/UIViewController_Overview.md)
    - [UIViewController 생성자 정리](Mobile_01_iOS/iOS-Framework-UIKit/UIViewController_Initializers.md)
    - [UIViewController의 Life-cycle](Mobile_01_iOS/iOS-Framework-UIKit/UIViewController_Lifecycle.md)
    - [UIActivityViewController : 공유하기 기능](Mobile_01_iOS/iOS-Framework-UIKit/UIViewController_UIActivityViewController.md)
    - [UIAlertController : 장문 얼럿 만들기](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIAlertController_LongText.md)
    - [PHPickerController 사용하기 (iOS14+)](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIViewController/PHPickerViewController.md)
    - [UIImagePickerController 사용하기 (iOS14-)](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIViewController/UIImagePickerController.md)
    - [UITableViewController 정리](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIViewController/UITableViewController.md)
    - [UIKit에서 RootViewController 찾기](Mobile_01_iOS/iOS-Framework-UIKit/SearchingRootVC.md)

- 시스템 & 유틸리티
    - [MessageUI란](Mobile_01_iOS/iOS-Framework-UIKit/MessageUI.md)
    - [MessageUI - MFMailComposeViewController](Mobile_01_iOS/iOS-Framework-UIKit/MessageUI_sendMail.md)
    - [MessageUI - MFMessageComposeViewController](Mobile_01_iOS/iOS-Framework-UIKit/MessageUI_sendSMS.md)
    - [UIDevice 정리](Mobile_01_iOS/iOS-Framework-UIKit/UIKit_UIDevice.md)
    - [NSDate - Timezone: UTC, GMT, KST](Mobile_01_iOS/iOS-Framework-UIKit/NSDate_Timezone.md)
    - [Timer 구현하기](Mobile_01_iOS/iOS-Framework-UIKit/Timer_Guide.md)
    - [UIBarItem & UITabBarItem](Mobile_01_iOS/iOS-Framework-UIKit/UIBarItem_Guide.md)
    - [UIFont 정리](Mobile_01_iOS/iOS-Framework-UIKit/UIFont_Guide.md)
    - [UILongPressGestureRecognizer](Mobile_01_iOS/iOS-Framework-UIKit/UIGestureRecognizer_LongPress.md)

[\- 👆목차로 돌아가기 \-](#ios---uikit-목차)


### 🎨 UIKit - 레이아웃과 배치 전략
- [Layout - 오토레이아웃의 개념](Mobile_01_iOS/iOS-Framework-UIKit/Layout_About_AutoLayout.md)
- [UIKit - UIStoryboard](Mobile_01_iOS/iOS-Framework-UIKit/About_UIKIt_010_UIStoryboard.md)
- [Layout - CGRectMake는 뭘까](Mobile_01_iOS/iOS-Framework-UIKit/Layout_CGRectMake.md)
- [Layout - Hierarchy of UIView (feat. addSubView)](Mobile_01_iOS/iOS-Framework-UIKit/Layout_addSubView.md)
- [CGPoint, CGSize, CGRect](Mobile_01_iOS/iOS-Framework-UIKit/UIKit_CGPoint_CGSize_CGRect.md)

[\- 👆목차로 돌아가기 \-](#ios---uikit-목차)


### 🕹 UIKit - 이벤트 & 입력 처리 흐름

[\- 👆목차로 돌아가기 \-](#ios---uikit-목차)

### 🔀 UIKit - 화면 전환 흐름
- [정리 : iOS에서의 화면관리 및 전환](Mobile_01_iOS/iOS-ScreenTranport/A_Various_switchingScene.md)
- [기본적인 iOS 앱의 구조 / 탭바컨트롤러 / 네비게이션컨트롤러](Mobile_01_iOS/iOS-ScreenTranport/Application_BasicStructure.md)
- [화면전환 - UINavigationController 이해하기](Mobile_01_iOS/iOS-ScreenTranport/navigationController.md)
- [present - CodeUI to StoryBoard](Mobile_01_iOS/iOS-ScreenTranport/presentCodeUIToStoryboard.md)
- [present - UIKit to SwiftUI](Mobile_01_iOS/iOS-ScreenTranport/present_UIKitToSwiftUI.md)
- [Segue를 이용한 화면이동](Mobile_01_iOS/iOS-ScreenTranport/segue.md)
- [Show는 push와 present의 추상화 메서드](Mobile_01_iOS/iOS-ScreenTranport/showPushPresent.md)
- [화면전환 - UITabBarController 이해하기](Mobile_01_iOS/iOS-ScreenTranport/tabbarController.md)

[\- 👆목차로 돌아가기 \-](#ios---uikit-목차)


### 🧠 UIKit - 데이터의 흐름과 상태 관리

[\- 👆목차로 돌아가기 \-](#ios---uikit-목차)

### 🎨 UIKit - 애니메이션 & 뷰 효과 구성

[\- 👆목차로 돌아가기 \-](#ios---uikit-목차)

### 🧠 UIKit - 메모리 관리

[\- 👆목차로 돌아가기 \-](#ios---uikit-목차)

<br>

### 🔁 UIKit - 주요 사이클
- [UIView의 Drawing Cycle (Layout Cycle)](Mobile_01_iOS/iOS-Framework-UIKit/UIView_DrawingCycle.md)
- [UIResponder와 Responder Chain](Mobile_01_iOS/iOS-Framework-UIKit/UIResponder_ResponderChain.md)
- [UIViewController의 Life-cycle](Mobile_01_iOS/iOS-Framework-UIKit/UIViewController_Lifecycle.md)


<br>

## 📦 iOS - SwiftUI 기반 앱

### 📦 SwiftUI - 앱의 구조와 실행 흐름
- [Layout - SwiftUI: State와 바인딩](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_State.md)

### 🎨 SwiftUI - UI 구성 요소 설계
- [Layout - SwiftUI: Text](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_001_Text.md)
- [Layout - SwiftUI: Image](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_002_Image.md)
- [Layout - SwiftUI: Button](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_003_Button.md)
- [Layout - SwiftUI: Spacer](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_004_Spacer.md)
- [Layout - SwiftUI: Padding](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_005_Padding.md)
- [Layout - SwiftUI: HStack, VStack, ZStack](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_010_Stack.md)
- [Layout - SwiftUI: NavigationView](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_011_NavigationView.md)
- [Layout - SwiftUI: TabView](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_012_TabView.md)
- [SwiftUI - Control에 대하여](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_020_Control.md)
- [SwiftUI - View 프로토콜](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_030_View.md)
- [Layout - SwiftUI: Color](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_Color.md)
- [Layout - SwiftUI: List](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_List.md)
- [Layout - SwiftUI: ScrollView](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_ScrollView.md)

### 🎨 SwiftUI - 레이아웃과 배치 전략

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)

### 🕹 SwiftUI - 이벤트 & 입력 처리 흐름

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)

### 🔀 SwiftUI - 화면 전환 흐름

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)

### 🧠 SwiftUI - 데이터의 흐름과 상태 관리

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)

### 🎨 SwiftUI - 애니메이션 & 뷰 효과 구성

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)

### 🧠 SwiftUI - 메모리 관리

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)

### 🔁 SwiftUI - 주요 사이클
- [SwiftUI View 생명주기 정리](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_ViewLifecycle.md)
- [Layout - SwiftUI: State와 바인딩](Mobile_01_iOS/iOS-Framework-SwiftUI/SwiftUI_State.md)

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)

## 🔗 UIKit / SwiftUI 상호 연동

- [UIKit으로 구현된 화면에 SwiftUI View를 추가하기 : UIHostingController](Mobile_01_iOS/iOS-Framework-SwiftUI_UIKit/PreviewProvider_UIHostingController.md)
- [UIKit에서 SwiftUI의 Preview 사용하기](Mobile_01_iOS/iOS-Framework-SwiftUI_UIKit/PreviewProvier.md)
- [UIKit에서 SwiftUI의 Preview관련 함수 만들어 사용하기](Mobile_01_iOS/iOS-Framework-SwiftUI_UIKit/PreviewProvier3.md)
- [SwiftUI에서 UIKit 사용하기 : UIViewRepresentable, UILabel, WebView](Mobile_01_iOS/iOS-Framework-SwiftUI_UIKit/UIViewResentable_UIKit.md)

[\- 👆목차로 돌아가기 \-](#ios---swiftui-목차)



----

<br>

## 🎯 iOS - 핵심 개발
### 🌐 iOS - 통신 & 네트워킹
- [네트워크 통신의 이해](Mobile_01_iOS/iOS-Networking/About_Networking.md)
- [NSObject - URLSession](Mobile_01_iOS/iOS-Networking/About_URLSession.md)
- [Network Programming - RESTful APIs 사용하기](Mobile_01_iOS/iOS-Networking/Network_RestfulAPI.md)
- [Notifications - IOS에서 사용하는 알림의 종류](Mobile_01_iOS/iOS-Networking/Apple_Notification.md)
- [개념 - 페이로드(Payload)](Mobile_01_iOS/iOS-Networking/Concept_payload.md)
- [Cookie란](Mobile_01_iOS/iOS-Networking/Cookie_about.md)
- [Cookie - cookieAcceptPolicy (쿠키수락정책)](Mobile_01_iOS/iOS-Networking/Cookie_cookieAcceptPolicy.md)
- [네트워킹 - 각종 URL의 유효성 검사](Mobile_01_iOS/iOS-Networking/URL_ValidationCheck.md)
- 웹뷰 구현
    - [WKWebView 사용하기, 구성 요소 살펴보기](Mobile_01_iOS/iOS-Networking/WebView_00_INTRO.md)
    - [WebView - 웹뷰에 스크립트를 적용시키는 방법](Mobile_01_iOS/iOS-Networking/WebView_Adjust_Script.md)
    - [WebView - Delegate method](Mobile_01_iOS/iOS-Networking/WebView_Delegate.md)
    - [WebView - App에서 웹페이지를 여는 3가지 방법](Mobile_01_iOS/iOS-Networking/WebView_basic_use.md)
    - [WebView - 네비게이션컨트롤러 목록으로 웹뷰 관리하는 방법](Mobile_01_iOS/iOS-Networking/WebView_catchNavigation.md)
    - [WebView - Safari로 웹뷰 디버깅하는 방법](Mobile_01_iOS/iOS-Networking/WebView_commute_with_Web.md)
    - [WebView - createWebViewWith : blank로 새창열기](Mobile_01_iOS/iOS-Networking/WebView_createWebViewWith.md)
    - [WebView - 자주 사용하는 메서드](Mobile_01_iOS/iOS-Networking/WebView_often_use_delegate_method.md)
    - [WebView - 스와이프로 리프레시 세팅](Mobile_01_iOS/iOS-Networking/WebView_swipe_refresh.md)
    - [webview - 바운스 효과 제거하기](Mobile_01_iOS/iOS-Networking/Webview_how_to_stop_bounce.md)
    - [WebView - WKWebsiteDataStore 사용하여 웹뷰의 데이터관리하기](Mobile_01_iOS/iOS-Networking/Cookie_WebView_WKWebsiteDataStore.md)
    - [Cookie - 현재 웹뷰로 쿠키 가져오기](Mobile_01_iOS/iOS-Networking/Cookie_cookie_call.md)
    - [Cookie - ios에서 쿠키 다루기](Mobile_01_iOS/iOS-Networking/Cookie_AdjustCookie.md)
    - [Cookie - WKProcessPool를 사용해 여러 웹뷰에서 쿠키 공유하기](Mobile_01_iOS/iOS-Networking/Cookie_Cookie_sharing.md)
- 웹뷰 디버깅
    - [WebView - PC에서 사용중인 내부망을 Iphone으로 연결시키는 방법](Mobile_01_iOS/iOS-Networking/WebViewZ_intranet.md)

[\- 👆목차로 돌아가기 \-](#ios---기능-개발-핵심-목차)


## 🔧 iOS - 시스템 기능 & 네이티브 API

- [볼륨버튼 캐치하기](Mobile_01_iOS/iOS-Development/Detect_SystemVolume.md)
- [AudioToolbox - 롱프레스와 햅틱진동 구현하기 (Feat.Long press)](Mobile_01_iOS/iOS-Development/Third_AudioToolBox_HapticAndLongpress.md)

### 🔔 iOS - 푸시 알림 및 백그라운드 처리


[\- 👆목차로 돌아가기 \-](#ios---기능-개발-핵심-목차)


### 🔌 iOS - 플랫폼 네이티브 기능 연동
- 시간 관련
    - [Date - Date로 두 개의 시간차 구하기](Mobile_01_iOS/iOS-Development/Date_getTimeInterval.md)
- CLLocation
    - [CLLocation - 위치정보 사용하기](Mobile_01_iOS/iOS-Framework-CoreLocation/CLLocation_a_howToUse.md)
    - [CoreLocation - 비콘 조회하기](Mobile_01_iOS/iOS-Framework-CoreLocation/CLLocation_beacon.md)
- BLE
    - [Bluetooth, BLE, Beacon, iBeacon](Mobile_01_iOS/iOS-Framework-CoreLocation/CoreLocation_iBeacon.md)
- AVFoundation
    - [AVFoundation - AVPlayer 사용하기](Mobile_01_iOS/iOS-Foundation/AVFoundation_AVPlayer.md)
    - [AVFoundation - TTS : Text-To-Speech](Mobile_01_iOS/iOS-Foundation/AVFoundation_AVSpeechSynthesizer.md)
    - [AVFoundation - Barcode Scanner 구현하기](Mobile_01_iOS/iOS-Foundation/AVFoundation_BarcodeScan.md)
- Foundation
    - [Calendar - 캘린더로 두 개의 날짜 비교하기](Mobile_01_iOS/iOS-Foundation/Calendar_getDateInterval.md)
    - [FileManager - 파일 다운로드하기](Mobile_01_iOS/iOS-Foundation/FileManager_fileDownload.md)
    - [FileManager - 사용하기](Mobile_01_iOS/iOS-Foundation/FileManager_introduce.md)
    - [Foundation - JSONSerialization(1): 직렬화 Intro](Mobile_01_iOS/iOS-Foundation/Foundation_JSONSerialization00.md)
    - [Foundation - JSONSerialization(3):  Decode JSONData](Mobile_01_iOS/iOS-Foundation/Foundation_JSONSerialization_Decode.md)
    - [Foundation - JSONSerialization(2): Encode JSONData](Mobile_01_iOS/iOS-Foundation/Foundation_JSONSerialization_Encode.md)
    - [String Protocol - String to Data](Mobile_01_iOS/iOS-Foundation/StringProtocol_stringToData.md)
    - [타임스탬프 구현하기](Mobile_01_iOS/iOS-Foundation/TIL220914_TimeStamp.md)
    - [CMTime](Mobile_01_iOS/iOS-Foundation/cmtime.md)
- Core Animation
- Photo
    - [PhotoKit - Introduce](Mobile_01_iOS/iOS-Framework-PhotoKit/photokit_000_intro.md)
- 색상관련
    - [hex값을 UIcolor로 변환하는 방법](Mobile_01_iOS/iOS-Extensions/TIL221025_convertHexToUIColor.md)


[\- 👆목차로 돌아가기 \-](#ios---기능-개발-핵심-목차)



## 🔗 iOS - 서드파티 라이브러리 연동
- [External Link (외부링크) - 커스텀 앱스키마 만들기, 사용하기](Mobile_01_iOS/iOS-Development/ExternalLink_CustomScheme.md)
- [iOS - 패키지 의존성 관리 도구: CocoaPods, Carthage, SPM](Mobile_01_iOS/iOS-Library/About_A_iOS_Package.md)
- [About Swift PackageManager](Mobile_01_iOS/iOS-Library/About_SPM.md)
- [CocoaPods 사용하기](Mobile_01_iOS/iOS-Library/About_cocoaPods_basic.md)
- [About CocoaPods Error 방지하기](Mobile_01_iOS/iOS-Library/About_cocoaPods_error.md)
- Convention
    - [Convention - SwiftLint 세팅하기](Mobile_01_iOS/iOS-Library/Convention_SwiftLint.md)
    - [Convention - SwiftLint 세부설정하기](Mobile_01_iOS/iOS-Library/Convention_SwiftLintCustomRule.md)
- [라이브러리 - 카카오 SDK 사용하기](Mobile_01_iOS/iOS-Library/Library_A_kakaoSDK.md)
- [라이브러리 - swiftSoup](Mobile_01_iOS/iOS-Library/Library_SwiftSoup.md)
- [ReactiveX: RxSwift Introduce](Mobile_01_iOS/iOS-Library/RxSwift_Introduce.md)
- Analytics
    - [Xcode에서 디버그뷰 활성화하기 :Firebase, GA4](Mobile_01_iOS/iOS-Environment/firebase_debugView.md)
- Push
    - [Push - 핑거푸시](Mobile_01_iOS/iOS-Library/Push_fingerPush.md)
- UI/UX
    - [라이브러리 - GIFu 사용하기](Mobile_01_iOS/iOS-Library/Library_Gifu.md)
    - [Library - Hero](Mobile_01_iOS/iOS-Library/Library_Hero.md)
    - [라이브러리 - Kingfisher 사용하기](Mobile_01_iOS/iOS-Library/Library_Kingfisher.md)
- SNS
    - [SNS Login - Kakao](Mobile_01_iOS/iOS-Library/SNSLogin_kakao.md)
    - [SNS Login - Naver](Mobile_01_iOS/iOS-Library/SNSLogin_naver.md)

[\- 👆목차로 돌아가기 \-](#ios---기능-개발-핵심-목차)


<br>

## iOS - 앱 아키텍쳐 및 성능

### 🏗 iOS - 아키텍처 및 모듈 설계
- 디자인패턴
    - [디자인패턴이란](Mobile_01_iOS/iOS-Architecture/Architecture_100_De_Intro_.md)
    - [Cocoa Design Pattern - Delegate 델리게이트 패턴](Mobile_01_iOS/iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Delegate.md)
    - [Cocoa Design Pattern - Observer 옵저버 패턴](Mobile_01_iOS/iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Observer.md)
    - [Cocoa Design Pattern - Singleton (싱글톤 패턴)](Mobile_01_iOS/iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Singleton.md)
    - [KVC와 KVO](Mobile_01_iOS/iOS-Development/KVC_KVO.md)

- 아키텍쳐패턴
    - [아키텍쳐패턴이란, 디자인패턴과 아키텍쳐의 차이](Mobile_01_iOS/iOS-Architecture/Architecture_200_Arc_Intro.md)
    - [MVC -> MVP -> MVVM : Caculator](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVCToMVPToMVVM_Calculator.md)
    - [MVC -> MVP -> MVVM : ColorSelectApp](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVCToMVPToMVVM_ColorSwitchApp.md)
    - [MVC to MVVM : 01. UTC 오늘, 현재, 내일 시간보기](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVCToMVVM_01_UTC.md)
    - [MVC to MVVM : 02. TableVC 클릭시 텍스트 변경](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVCToMVVM_02_Task.md)
    - [VC -> MVC : Custom UICollectionView](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVC_CollectionView.md)
    - [Architecture - IOS MVC의 한계](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVC_Massive.md)
    - [Architecture - MVC: 전통적인 MVC구조로 HTTP사용하기](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVC_traditional.md)
    - [Architecture - 간단한 MVVM구조 예제](Mobile_01_iOS/iOS-Architecture/Architecture_301_MVVM_simpleExample.md)
    - [단방향 데이터 플로우(Unidirectial Data Flow, UDF)](Mobile_01_iOS/iOS-Architecture/Architecture_401_UnidirectialDataFlow.md)
    - [ReactorKit - 예제: CountApp](Mobile_01_iOS/iOS-Architecture/Architecture_402_RxSwift_ReactorKit_CountApp.md)
    - [Clean Architecture(클린 아키텍쳐)](Mobile_01_iOS/iOS-Architecture/Architecture_601_CleanArchitecture.md)
    - [데이터 바인딩이란](Mobile_01_iOS/iOS-Architecture/Data_Binding_about.md)
    - [Architecture - 비즈니스 로직이란](Mobile_01_iOS/iOS-Architecture/aboutBusinessLogic.md)

[\- 👆목차로 돌아가기 \-](#ios---앱-아키텍쳐-및-성능-목차)



### 🔀 iOS - 동시성 처리
- 동시성 개념 이해
    - [프로그래밍에서 동기 비동기 개념에 대한 이해](Mobile_01_iOS/iOS-Concurrency/About_000_Sync_vs_Async_Basics.md)
    - [비동기처리가 필요한 이유](Mobile_01_iOS/iOS-Concurrency/About_001_Async_vs_Concurrent_Concepts.md)
    - [비동기(Async), 동시(Concurrent)의 개념](Mobile_01_iOS/iOS-Concurrency/About_002_async_concurrent_2.md)
    
- GCD 기반 API (Grand Central Dispatch)
    - [동시성 프로그래밍 : Concurrency 톺아보기](Mobile_01_iOS/iOS-Concurrency/GCD_001_Overview.md)
    - [GCD - DispatchGroup](Mobile_01_iOS/iOS-Concurrency/GCD_010_DispatchGroup.md)
    - [GCD - DispatchWorkItem](Mobile_01_iOS/iOS-Concurrency/GCD_011_DispatchWorkItem.md)
- Operation 기반 API (Foundation 계열)
    - [GCD - OperationQueue를 이용한 비동기 작업](Mobile_01_iOS/iOS-Concurrency/Concurrency_020_OperationQueue.md)
- Swift Concurrency (언어 기반 동시성)
    - [Swift Concurrency - Async / Await / Task](Mobile_01_iOS/iOS-Concurrency/SwiftConcurrency_Overview.md)
- Objective-C 기반 비동기 호출
    - `※ 현재는 거의 사용하지 않음`
    - [performSelector를 이용한 비동기 작업 ](Mobile_01_iOS/iOS-Concurrency/Concurrency_030_performSelector.md)

[\- 👆목차로 돌아가기 \-](#ios---앱-아키텍쳐-및-성능-목차)

<br><br>


### 🧱 iOS - Deprecated API 마이그레이션 기록
- [UIAlertView Deprecated in iOS 9, Replaced by UIAlertController in iOS 10.0](Mobile_01_iOS/iOS-Framework-Migration/AlertView.md)
- [MPMoviePlayerController Deprecated in iOS 10, Replaced by AVPlayerViewController in iOS 7](Mobile_01_iOS/iOS-Framework-Migration/MPMoviePlayer.md)
- [NSURLConnection Deprecated in iOS 9, Replaced by URLSession in iOS 7](Mobile_01_iOS/iOS-Framework-Migration/NSURLConnection.md)
- ['setVolume:' is deprecated: first deprecated in iOS 7.0 - Use MPVolumeView for volume control.](Mobile_01_iOS/iOS-Framework-Migration/mpmusicplayer.md)

[\- 👆목차로 돌아가기 \-](#ios---앱-아키텍쳐-및-성능-목차)


## iOS - 시스템 및 운영 배포
### 🔧 iOS - 시스템 환경 설정
- [Info.plist : (값 가져오기, 권한)](Mobile_01_iOS/iOS-Environment/InfoPlist.md)
- [Info.plist - App Version 가져오기](Mobile_01_iOS/iOS-Environment/InfoPlist_appVersion.md)
- [Privacy - 여러가지 접근권한요청](Mobile_01_iOS/iOS-Environment/PrivercyPermission_various.md)
- [Framework란 무엇인가](Mobile_01_iOS/iOS-Framework-Management/FrameworkM_00_about.md)
- [XCFramework 생성하기](Mobile_01_iOS/iOS-Framework-Management/FrameworkM_00_initial.md)
- 로컬라이징
    - [로컬라이징](Mobile_01_iOS/iOS-Development/Localization.md)

[\- 👆목차로 돌아가기 \-](#ios---시스템-및-운영-배포-목차)

<br><br>

### 🚀 iOS - 배포
- [App Store Connect - 배포된 앱을 삭제하는 2가지 방법](Mobile_01_iOS/iOS-AppStore/AppStore_AppDismiss.md)
- [AppStore - 앱 생성하기](Mobile_01_iOS/iOS-AppStore/AppStore_AppInit.md)
- [AppStore - 수출 규정 준수 정보](Mobile_01_iOS/iOS-AppStore/AppStore_AppUseNonExempt.md)
- [AppStore - 버전정보 수정하기](Mobile_01_iOS/iOS-AppStore/AppStore_ChangeVersionInfo.md)
- [AppStore - 긴급 심사 요청(Request Expedited Review)](Mobile_01_iOS/iOS-AppStore/AppStore_expeditedReview.md)
- [앱심사 - 수출 규정 관련 문서가 누락됨(Missing Compliance) / 우회처리](Mobile_01_iOS/iOS-AppStore/AppStore_missing_Compliance.md)
- [리젝사유 - 2. Performance(성능)](Mobile_01_iOS/iOS-AppStore/Reject_2_Performance.md)
- [리젝사유 - 4. Design(디자인)](Mobile_01_iOS/iOS-AppStore/Reject_4_Design.md)
- [리젝사유 - 5. Legal(법률)](Mobile_01_iOS/iOS-AppStore/Reject_5_Legal.md)
- [테스트플라잇 - 외부 테스팅 (External Testing)](Mobile_01_iOS/iOS-AppStore/TestFlight_externalTester.md)
- [appStoreReceiptURL](Mobile_01_iOS/iOS-Environment/DetectingDeploymentEnvironment.md)
- [.ipa 파일 만들기](Mobile_01_iOS/iOS-Environment/How_to.make_ipa.md)

[\- 👆목차로 돌아가기 \-](#ios---시스템-및-운영-배포-목차)


<br><br>

### 🚀 iOS - CI/CD

[\- 👆목차로 돌아가기 \-](#ios---시스템-및-운영-배포-목차)

<br><br>

### 🧯 iOS - 운영 이슈 문제 해결
- [Signing - Release 빌드에서 Distribution 프로필 매칭 오류 해결](Mobile_01_iOS/iOS-Environment/Signing_Release_Distribution.md)

[\- 👆목차로 돌아가기 \-](#ios---시스템-및-운영-배포-목차)

<br><br>

## 🧪 iOS - 테스트 및 도구
### 🧰 iOS - 개발 보조 도구 및 구성 관리
- [How to Set - 세로모드 고정 (Potrait)](Mobile_01_iOS/iOS-Environment/How_to_set_potrait_mode.md)
- [Xcode 주석사용법](Mobile_01_iOS/iOS-Environment/PragmaMark.md)
- [XCode - 전처리문 사용하기](Mobile_01_iOS/iOS-Environment/PreprocessorCommand.md)
- [Scheme - Debug / Release 빌드 분리하기](Mobile_01_iOS/iOS-Environment/Scheme_Separate_BuildSet.md)
- [iOS DeviceSupport - 테스트 디바이스 iOS 수동 업데이트](Mobile_01_iOS/iOS-Environment/iOSDeviceSupport_Manually_update.md)
- [Xcode - 빌드된 app파일은 어디에 있을까](Mobile_01_iOS/iOS-Environment/Bundle_derivedData.md)

[\- 👆목차로 돌아가기 \-](#ios---테스트-및-도구-목차)


<br><br>

### 🧪 iOS - 앱 테스트 구성 요소
- [Testable한 코드 만들기1 - VC -> MVC -> MVP](Mobile_01_iOS/iOS-TDD/testable_mvc_mvp.md)

[\- 👆목차로 돌아가기 \-](#ios---테스트-및-도구-목차)

<br><br>

## iOS - 그래픽 렌더링 & 시각 효과
- UI가 **어떻게 그려지고 표현되는가**에 대한 개념과 Core Animation, 마스크 등 렌더링 중심 자료를 모았습니다.

- [dp와 pt에 대하여 (Feat. 포인트란)](Mobile_01_iOS/iOS-RelatedImage/DP_PT.md)
- [화면캡처 - 특정화면을 이미지로 저장하기](Mobile_01_iOS/iOS-RelatedImage/imageSave.md)
- [PNG와 JPG에 대하여](Mobile_01_iOS/iOS-RelatedImage/png_jpg.md)
- [View - UIView 마스크 입문 (두 개의 UIView로 이해하기)](Mobile_01_iOS/iOS-Framework-UIKit/View_Mask_BasicExample.md)
- [UIView 투명 영역 구현: 마스크 vs 딤 오버레이](Mobile_01_iOS/iOS-Framework-UIKit/View_Mask_vs_DimOverlay.md)
- UIKit 레이어 & 시각 효과
    - [Layout - 이미지 컨텐츠 모드 (ContentMode)](Mobile_01_iOS/iOS-Framework-UIKit/Layout_ImageContentMode.md)
    - [Layout - CodeUI: CustomShadow(feat.CustomClass)](Mobile_01_iOS/iOS-Framework-UIKit/Layout_CodeUI_CustomShadow.md)
    - [Layout - StoryboardUI: CornerRadius](Mobile_01_iOS/iOS-Framework-UIKit/Layout_StoryboardUI_CornerRadius.md)
    - [CGColor에 대하여](Mobile_01_iOS/iOS-Framework-UIKit/UIColor_CGColor.md)
    - [UIView - Layer란 무엇인가(작성중)](Mobile_01_iOS/iOS-Framework-UIKit/UIView_Layer.md)

### 🖼 iOS - Core Graphics - 직접 드로잉 처리

[\- 👆목차로 돌아가기 \-](#-ios---그래픽-렌더링--시각-효과-목차)

<br><br>

### 💫 iOS - Core Animation - 저수준 애니메이션 처리
- [Core Animation 프레임워크(작성중)](Mobile_01_iOS/iOS-Framework-CoreAnimation/About_CA_000_.md)

[\- 👆목차로 돌아가기 \-](#-ios---그래픽-렌더링--시각-효과-목차)


<br><br>

### 🎮 iOS - Metal - 고성능 GPU 렌더링

[\- 👆목차로 돌아가기 \-](#-ios---그래픽-렌더링--시각-효과-목차)


<br><br>

### 🌈 iOS - Core Image - 이미지 필터링 및 효과

[\- 👆목차로 돌아가기 \-](#-ios---그래픽-렌더링--시각-효과-목차)

<br><br>

### 🕹 iOS - SceneKit & ARKit - 3D 및 증강현실

[\- 👆목차로 돌아가기 \-](#-ios---그래픽-렌더링--시각-효과-목차)

<br><br>

## 🛡 iOS - 보안 및 데이터 저장 기술
- 저장
    - [userDefault](Mobile_01_iOS/iOS-Foundation/AboutUserDefualt.md)
    - [IOS에 있어서 Caching](Mobile_01_iOS/iOS-Development/ios_caching.md)
- 보안
    - [Integrity - 앱 설치환경 체크](Mobile_01_iOS/iOS-Integrity/Integrity_Build_Environment.md)
    - [Integrity - 인증서(.p8, .p12 / Development, Distribution / Producation SSL, Development SSL)](Mobile_01_iOS/iOS-Integrity/Integrity_Certificate.md)
    - [Integrity - 인증서와 프로비저닝 프로파일 (Certificate & Provisioning Profile) 관리하기](Mobile_01_iOS/iOS-Integrity/Integrity_Certificate_Provisioning.md)
    - [Integrity - DeviceCheck](Mobile_01_iOS/iOS-Integrity/Integrity_DeviceCheck.md)
    - [Integrity_개인정보 보호 매니페스트 PrivacyInfo.xcprivacy 만들기](Mobile_01_iOS/iOS-Integrity/Integrity_PrivacyInfo.md)
    - [Integrity - UUID / UDID / IDFA / IDFV](Mobile_01_iOS/iOS-Integrity/Integrity_UUID_UDID_IDFA.md)
    - [Integrity - APN 인증키(.p8) 발급받기](Mobile_01_iOS/iOS-Integrity/Integrity_apn_p8.md)
    - [Integrity - 중간자 공격(man-in-the-middle attack)](Mobile_01_iOS/iOS-Integrity/Integrity_manInTheMiddleAttack.md)
    - [Integrity - 리플레이 공격(Replay attack)](Mobile_01_iOS/iOS-Integrity/Integrity_replayAttack.md)

[\- 👆목차로 돌아가기 \-](#ios---보안-및-저장-목차)

<br>

## 📱 iOS - 샘플 앱
### 개발 템플릿

- 라이브러리 연동 샘플
- 기능 구현 단위 샘플
    - [DynamicSplash 세팅하기](Mobile_01_iOS/iOS-CustomLogic/splash_dynamicSplash.md)
    - [Login Logic (feat. UserDefault)](Mobile_01_iOS/iOS-CustomLogic/Login_Logic.md)
    
### 토이 프로젝트
- 연구
    - [선언형 UIKit 만들기](Mobile_01_iOS/iOS-Extensions/UIKitLikeSwiftUI.md)
- 앱 개발
    - 언제나 가지
    - 맷대맷
    - 기억나데어
    - 스트레치업
    - Rythmic Word

[\- 👆목차로 돌아가기 \-](#ios---샘플-앱-목차)

<br><br>
---

# Mobile-Android
### Mobile Android 공통 기능 구현
- [Android - 스플래시 화면 구현 가이드 (정적 & 동적)]() 미완


## Android - View System 기반 앱

### 📦 View - 앱의 구조와 실행 흐름

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)

### 🎨 View - UI 구성 요소 설계

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)

### 🎨 View - 레이아웃과 배치 전략

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)

### 🕹 View - 이벤트 & 입력 처리 흐름

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)

### 🔀 View - 화면 전환 흐름

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)

### 🧠 View - 데이터의 흐름과 상태 관리

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)

### 🎨 View - 애니메이션 & 뷰 효과 구성

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)


### 🧠 View - 메모리 관리

[\- 👆목차로 돌아가기 \-](#android---view-system-기반-앱-목차)


<br>

## Android - Jetpack Compose 기반 앱

### 📦 Compose - 앱의 구조와 실행 흐름

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)

### 🎨 Compose - UI 구성 요소 설계

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)


### 🎨 Compose - 레이아웃과 배치 전략

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)


### 🕹 Compose - 이벤트 & 입력 처리 흐름

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)


### 🔀 Compose - 화면 전환 흐름

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)

### 🧠 Compose - 데이터의 흐름과 상태 관리

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)

### 🎨 Compose - 애니메이션 & 뷰 효과 구성

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)


### 🧠 Compose - 메모리 관리

[\- 👆목차로 돌아가기 \-](#android---jetpack-compose-기반-앱-목차)

<br><br>
---

## Android - 기능 개발 핵심
### 🌐 Android - 통신 & 네트워킹

[\- 👆목차로 돌아가기 \-](#android---기능-개발-핵심-목차)

### 🔧 Android - 시스템 기능 & 네이티브 API

[\- 👆목차로 돌아가기 \-](#android---기능-개발-핵심-목차)

### 🔔 Android - 푸시 알림 및 백그라운드 처리

[\- 👆목차로 돌아가기 \-](#android---기능-개발-핵심-목차)

### 🔗 Android - 서드파티 라이브러리 연동

[\- 👆목차로 돌아가기 \-](#android---기능-개발-핵심-목차)


## Android - 앱 아키텍쳐 및 성능
### 🏗 Android - 아키텍처 및 모듈 설계

[\- 👆목차로 돌아가기 \-](#android---앱-아키텍쳐-및-성능-목차)

### 🔀 Android - 동시성 처리

[\- 👆목차로 돌아가기 \-](#android---앱-아키텍쳐-및-성능-목차)

### 🧱 Android - Deprecated API 마이그레이션 기록

[\- 👆목차로 돌아가기 \-](#android---앱-아키텍쳐-및-성능-목차)

## Android - 시스템 및 운영 배포 
### 🔧 Android - 시스템 환경 설정

[\- 👆목차로 돌아가기 \-](#android---시스템-및-운영-배포-목차)

### 🚀 Android - 배포

[\- 👆목차로 돌아가기 \-](#android---시스템-및-운영-배포-목차)

### 🚀 Android - CI/CD

[\- 👆목차로 돌아가기 \-](#android---시스템-및-운영-배포-목차)


### 🧯 Android - 운영 이슈 문제 해결

[\- 👆목차로 돌아가기 \-](#android---시스템-및-운영-배포-목차)


## Android - 테스트 및 도구
### 🧰 Android - 개발 보조 도구 및 구성 관리

[\- 👆목차로 돌아가기 \-](#android---테스트-및-도구-목차)


### 🧪 Android - 앱 테스트 구성 요소

[\- 👆목차로 돌아가기 \-](#android---테스트-및-도구-목차)

## Android - 그래픽 렌더링 & 시각 효과

### 🖼 Android - Canvas & Paint
직접 드로잉 처리

[\- 👆목차로 돌아가기 \-](#-android---그래픽-렌더링--시각-효과-목차)


### 💫 Android - Animator / MotionLayout
애니메이션 처리

[\- 👆목차로 돌아가기 \-](#-android---그래픽-렌더링--시각-효과-목차)


### 🎮 Android - OpenGL / Vulkan
고성능 그래픽

[\- 👆목차로 돌아가기 \-](#-android---그래픽-렌더링--시각-효과-목차)


### 🌈 Android - BlendMode / RenderScript
이미지 필터 및 색상 효과

[\- 👆목차로 돌아가기 \-](#-android---그래픽-렌더링--시각-효과-목차)


### 🕹 Android - ARCore / Sceneform
AR 및 3D 렌더링


[\- 👆목차로 돌아가기 \-](#-android---그래픽-렌더링--시각-효과-목차)

⸻


## 🛡 Android - 보안 및 데이터 저장 기술

[\- 👆목차로 돌아가기 \-](#android---보안-및-저장-목차)


## 🧾 Android - 샘플 앱

[\- 👆목차로 돌아가기 \-](#android---샘플-앱-목차)


### Mobile-Android-ASIS
- [Android Studio 완전삭제](Mobile_02_Android/AndroidStudio_delete.md)
- [Android - Basic : 안드로이드의 기본 앱구조](Mobile_02_Android/Android_Basic_AppStructure.md)
- [Android - WebView : 앱에서 웹으로 JavaScript 보내기](Mobile_02_Android/Android_WebView_Sending_JS.md)


<br><br>
---


# Mobile-Flutter

- [Flutter - Tils 문서 작성 가이드](Mobile_03_Flutter/Flutter_0000.DocumentGuide.md)
- [Flutter - 설치 및 환경 세팅 가이드](Mobile_03_Flutter/Flutter_0100.Setup.md)
- [Flutter - Widget Catalog](Mobile_03_Flutter/Flutter_1000.01.Widget.Overview.md)
- [Flutter - 세부 로드맵](https://github.com/isGeekCode/TIL/blob/main/Mobile_03_Flutter/Flutter_0000.DocumentGuide.md#%ED%95%99%EC%8A%B5-%EB%A1%9C%EB%93%9C%EB%A7%B5-%EA%B0%80%EC%9D%B4%EB%93%9C)
<br><br>
---

## Mobile Flutter 공통 기능 구현
- Flutter - Splash 구현


<br><br>
---

## 📦 Flutter - 앱의 구조와 실행 흐름

- [Flutter의 App 실행 흐름 이해하기](Mobile_03_Flutter/Flutter_0050.App.StartLogic.md)
- [Flutter - Stateful Widgets의 생명주기](Mobile_03_Flutter/Flutter_3101_Stateful_Lifecycle.md)

[\- 👆목차로 돌아가기 \-](#flutter-목차)


<br><br>

## 🎨 Flutter - UI 구성 요소 설계
### Basic Widgets
가장 기초적인 위젯 구성 요소들 

- [Flutter - 기본 위젯 4종 (Text, Icon, Image, Box)](Mobile_03_Flutter/Flutter_1001.00.Basic4Widget.md)
- [Flutter - Drawer : GNB / 사이드바](Mobile_03_Flutter/Flutter_1001.01.Drawer.md)
- [Flutter - ElevatedButton](Mobile_03_Flutter/Flutter_1001.02.ElevatedButton.md)
- [Flutter - Scaffold & AppBar](Mobile_03_Flutter/Flutter_1001.03.ScaffoldAppBar.md)
- [Flutter - Toggle Switch](Mobile_03_Flutter/Flutter_1004.01.ToggleSwitch.md)  
  
  
### Text Widgets
텍스트 표시 및 스타일링 관련 위젯
- [Flutter - Text](Mobile_03_Flutter/Flutter_1001.01.Text.md)
  
### Layout Widgets
레이아웃 구성용 위젯
- Single-child
    - [Flutter - Layout : Center](Mobile_03_Flutter/Flutter_1002.01.Center.md)
    - [Flutter - Layout : Container](Mobile_03_Flutter/Flutter_1002.02.Container.md)
        - 포함된 내용
            - SizedBox
            - ColoredBox
            - Padding
            - Align

- Multi-child
    - [Flutter - Layout : Column](Mobile_03_Flutter/Flutter_1002.21.Column.md)
    - [Flutter - Layout : Row](Mobile_03_Flutter/Flutter_1002.22.Row.md)
    - [Flutter - Layout: ListView](Mobile_03_Flutter/Flutter_1002.26.ListView.md)
  
### Assets, Images, Icons
텍스트 표시 및 스타일링 관련 위젯  
  
### Scrolling Widgets
스크롤 가능한 콘텐츠를 구성하는 위젯
  
### Interaction Models
제스처 및 터치 반응 처리 위젯  
  
- [](Mobile_03_Flutter/Flutter_1004_TextField_Basics.md)



### Styling Widgets
테마, 반응형 구성, 패딩 등 스타일링 위젯
  
### Painting and Effects
시각적 효과 및 그리기 관련 위젯  

  
### Animation and Motion
애니메이션 효과와 트랜지션 처리
  
    
### Async Widgets
비동기 상태를 다루기 위한 위젯
  
    
### Accessibility Widgets
앱의 접근성을 향상시키는 도구 위젯

 
[\- 👆목차로 돌아가기 \-](#flutter-목차)


<br><br>

## 📐 Flutter - 레이아웃과 배치 전략
- [Flutter - 레이아웃의 이해](Mobile_03_Flutter/Flutter_1000.02.Widget.LayoutGuide.md)
- [레이아웃 구현전략](Mobile_03_Flutter/Flutter_LayoutStrategy.md)
- 케이스 스터디
	- [Three Cards Example - Container & BoxDecoration 실전 예제](Mobile_03_Flutter/Flutter_1010.Layout.CaseStudy.ThreeCards.md)
	- [클론코딩 - iOS 설정앱](Mobile_03_Flutter/Flutter_1011.Layout.CaseStudy.SettingPage.md)

[\- 👆목차로 돌아가기 \-](#flutter-목차)

<br><br>
---

## 🕹 Flutter - 이벤트 & 입력 처리 흐름

[\- 👆목차로 돌아가기 \-](#flutter-목차)

<br><br>


## 🔀 Flutter - 화면 전환 흐름
- [Flutter - 화면 전환(Navigator) 1.0](Mobile_03_Flutter/Flutter_1300.Navigator.Basics.md)
- [Flutter - Dialog](Mobile_03_Flutter/Flutter_1341_AlertDialog_Basics.md)

[\- 👆목차로 돌아가기 \-](#flutter-목차)

<br><br>

## 🧠 Flutter - 데이터의 흐름과 상태 관리
- [Flutter - 상태관리 개요](Mobile_03_Flutter/Flutter_4000.StateManagement.Overview.md)
- [Flutter - 상태관리 기본 구조 이해 : Stateless와 Stateful](Mobile_03_Flutter/Flutter_4001.Stateful_Basics.md)
- [Flutter - 상태관리 : setState 기본 개념과 활용법](Mobile_03_Flutter/Flutter_4003_setState_Basics_Practice.md)
- [Flutter - 상태관리 : Listenables 활용법](Mobile_03_Flutter/Flutter_4004_using.Listenables.md)
- [Flutter - 상태관리 : InheritedWidget 활용법](Mobile_03_Flutter/Flutter_4005_using.InheritedWidget.md)

[\- 👆목차로 돌아가기 \-](#flutter-목차)

<br><br>

## 🎨 Flutter - 애니메이션 s& 뷰 효과 구성

[\- 👆목차로 돌아가기 \-](#flutter-목차)

<br><br>

## 🧠 Flutter - 메모리 관리 및 성능 최적화

[\- 👆목차로 돌아가기 \-](#flutter-목차)

<br><br>
---

## Flutter - 기능 개발 핵심
### 🌐 Flutter - 통신 & 네트워킹
- [Flutter - 네트워크 통신 기초 (RESTful API 중심)](Mobile_03_Flutter/Flutter_2000.Networking.Basics.md)
- [Flutter - 네트워크 통신 : Dio를 이용한 모듈 구현)](Mobile_03_Flutter/Flutter_2002.Dio.Basics.md)
- [Flutter - 웹뷰구현 : inappwebview 세팅(권장)](Mobile_03_Flutter/Flutter_5011.WebViewInappwebview.md)
- [Flutter - 웹뷰구현 : webview_flutter 세팅](Mobile_03_Flutter/Flutter_5012.WebViewIntegration.md)

[\- 👆목차로 돌아가기 \-](#flutter---기능-개발-핵심-목차)


<br><br>

### 🔧 Flutter - 시스템 기능 & 네이티브 API

[\- 👆목차로 돌아가기 \-](#flutter---기능-개발-핵심-목차)

<br><br>

### 🔔 Flutter - 푸시 알림 및 백그라운드 처리

[\- 👆목차로 돌아가기 \-](#flutter---기능-개발-핵심-목차)

<br><br>

### 🔗 Flutter - 서드파티 라이브러리 연동

[\- 👆목차로 돌아가기 \-](#flutter---기능-개발-핵심-목차)

<br><br>
---


## Flutter - 앱 아키텍쳐 및 성능
### 🏗 Flutter - 아키텍처 및 모듈 설계

[\- 👆목차로 돌아가기 \-](#flutter---앱-아키텍쳐-및-성능-목차)

<br><br>


### 🔀 Flutter - 동시성 처리

[\- 👆목차로 돌아가기 \-](#flutter---앱-아키텍쳐-및-성능-목차)

<br><br>

### 🧱 Flutter - Deprecated API 마이그레이션 기록

[\- 👆목차로 돌아가기 \-](#flutter---앱-아키텍쳐-및-성능-목차)

<br><br>
---

## Flutter - 시스템 및 운영 배포 
### 🔧 Flutter - 시스템 환경 설정
- [Flutter – Flavor를 이용한 빌드 환경 분리](Mobile_03_Flutter/Flutter_6012.BuildFlavorSetupGuide.md)
- [Flutter – Logger 함수](Mobile_03_Flutter/Flutter_6101_UTIL.DevLogger.md)
- [Flutter – TimeTracker 함수](Mobile_03_Flutter/Flutter_6101_UTIL.TimeTracker.md)


[\- 👆목차로 돌아가기 \-](#flutter---시스템-및-운영-배포-목차)


<br><br>

### 🚀 Flutter - 배포
- [Flutter - iOS 릴리즈 빌드 및 .ipa 생성](Mobile_03_Flutter/Flutter_6101.iOSIPABuildManual.md)

[\- 👆목차로 돌아가기 \-](#flutter---시스템-및-운영-배포-목차)

<br><br>

### 🚀 Flutter - CI/CD

[\- 👆목차로 돌아가기 \-](#flutter---시스템-및-운영-배포-목차)

<br><br>

### 🧯 Flutter - 운영 이슈 문제 해결
- [Flutter Error - Trouble Shooting Template](Mobile_03_Flutter/Flutter_8000.TroubleShootTemplate.md)
- [Flutter Error - WebView_PlatformNotSet : WebViewPlatform.instance 오류](Mobile_03_Flutter/Flutter_8101.WebView.PlatformNotSet.md)
- [Flutter Error - WebView_NDKVersionMismatch : Android NDK 버전 불일치](Mobile_03_Flutter/Flutter_8102.WebView.NDKVersionMismatch.md)
- [Flutter Error - Entrypoint doesn't contain...](Mobile_03_Flutter/Flutter_8103.EntryPoint.md)

[\- 👆목차로 돌아가기 \-](#flutter---시스템-및-운영-배포-목차)

<br><br>
----


## Flutter - 테스트 및 도구
### 🧰 Flutter - 개발 보조 도구 및 구성 관리

[\- 👆목차로 돌아가기 \-](#flutter---테스트-및-도구-목차)

<br><br>

### 🧪 Flutter - 앱 테스트 구성 요소

[\- 👆목차로 돌아가기 \-](#flutter---테스트-및-도구-목차)

<br><br>
---

## 🎨 Flutter - 그래픽 렌더링 & 시각 효과
### 🖼 CustomPainter
drawLine, drawRect 등으로 직접 도형을 그리는 방법
- [Flutter - 삼각형 View 그리기 : CustomPainter](Mobile_03_Flutter/Flutter_1009.01.ViewTriangle.md)

<br><br>

### 💫 AnimationController & Tween
커스텀 애니메이션 처리

<br><br>

### 🎮 Flutter + OpenGL / Unity 통합
고성능 그래픽 또는 3D 렌더링이 필요한 경우 외부 엔진 연동 방법

<br><br>

### 🌈 ImageFilter & BlendMode
이미지 필터와 색상 효과 등 이미지 시각 효과 적용

<br><br>

### 🕹 Flutter AR & 3D 시도 사례 
ARKit, SceneKit처럼 AR 기능은 외부 플러그인 기반 접근 정리


[\- 👆목차로 돌아가기 \-](#-flutter---그래픽-렌더링--시각-효과-목차)

<br><br>
---


## 🛡 Flutter - 보안 및 데이터 저장 기술

[\- 👆목차로 돌아가기 \-](#flutter---보안-및-저장-목차)


<br><br>
---

## 🧾 Flutter - 샘플 앱

[\- 👆목차로 돌아가기 \-](#flutter---샘플-앱-목차)
- 테스트
    - [Flutter - 웹뷰에서 새창열기테스트](Flutter_9991.WebView.WindowOpen.Test)

<br><br>
---

## 🌐 Web Development


<br><br>
---

# 🧬 Languages


## 📚 Programming Language  


### Lang-Swift
- [Swift에 대한 소개](Lang-Swift/About_Swift000Intro_.md)
- [Swift문법 기초](Lang-Swift/About_Swift001Basic_.md)
- [Swift - 변수와 상수](Lang-Swift/Swift_1-1_LetVar.md)
- [Swift - 기본 타입](Lang-Swift/Swift_1-2_Types.md)
- [Swift - 조건문과 반복문](Lang-Swift/Swift_1-3_Control.md)
- [Swift - 함수](Lang-Swift/Swift_1-4_Function.md)
- [Swift - 옵셔널](Lang-Swift/Swift_1-5_Optional.md)
- [Swift - 저장 프로퍼티와 연산 프로퍼티](Lang-Swift/Swift_2-1_Property.md)
- [Swift - Getter와 Setter](Lang-Swift/Swift_2-2_GetSet.md)
- [Swift - 프로퍼티 옵저버 (willSet, didSet)](Lang-Swift/Swift_2-3_Observer.md)
- [Swift - 접근 제어자 (private, internal, public 등)](Lang-Swift/Swift_2-4_Access.md)
- [Swift - Class와 Struct](Lang-Swift/About_Swift001ClassAndStruct.md)
- [Swift - Initialization에 대해 알아보기](Lang-Swift/About_Swift002Init.md)
- [Playground에서 UIView를 그려보자](Lang-Swift/About_Swift005Playground.md)
- [Swift - Array 모아보기](Lang-Swift/About_Swift010Array.md)
- [Swift_Sequence Protocol](Lang-Swift/About_Swift020SequenceProtocol.md)
- [Attribute - @frozen](Lang-Swift/Attribute_frozen.md)
- [Swift - Codable 다루기](Lang-Swift/Codable.md)
- [Do - Try - Catch](Lang-Swift/DoTryCatch.md)
- [Swift - Collection_Array : prefix() `안전한 사용`](Lang-Swift/Swift_collection_Array_prefix.md)
- [random함수를 이용해 Random한 숫자 뽑아내기](Lang-Swift/Swift_collection_Array_random.md)
- [Swift - Subscript(작성중)](Lang-Swift/Swift_collection_Subscript.md)
- [안전하게 배열에 접근하는 방법](Lang-Swift/TIL220310_contactArraySafely.md)
- [[Common Method] 로그 관련 함수](Lang-Swift/TIL220318_aboutLogMethod.md)
- [# 여러개의 Action을 한번에 추가하기](Lang-Swift/TIL220404_forEach.md)
- [mutating 과 구조체](Lang-Swift/TIL220413_mutating.md)
- [텍스트인코딩에 관하여](Lang-Swift/TIL220517_aboutTextEncoding.md)
- [배열안에 담긴 url 유효성 검사](Lang-Swift/TIL220520_aboutCheckArrayComponent.md)
- [이미지의 형태](Lang-Swift/TIL220915_KindsOfImageFormats.md)
- [Xcode 디버깅으로 변수변화 캐치하기](Lang-Swift/TIL221026_howToDebugging.md)
- [Understanding Closures in Swift : 클로저 톺아보기](Lang-Swift/UnderstandingClosures.md)
- [enum 사용법](Lang-Swift/aboutEnum.md)
- [저장프로퍼티 - 프로퍼티(1)](Lang-Swift/aboutProperty1.md)
- [연산프로퍼티 - 프로퍼티(2)](Lang-Swift/aboutProperty2.md)
- [프로퍼티 옵저버(willSet / didSet) - 프로퍼티(2.5)](Lang-Swift/aboutProperty205.md)
- [타입프로퍼티(static) - 프로퍼티(3)](Lang-Swift/aboutProperty3.md)
- [타입메서드, 클래스메서드, 인스턴스 메서드](Lang-Swift/aboutPropertyWith_static.md)
- [파일경로 String으로에서 확장자 추출하기](Lang-Swift/bringToExtensionName.md)
- [고차함수 - Higher Order Function : Map, Filter, Reduce, Sort, FlatMap](Lang-Swift/higherOrderFuction.md)
- [Special Literal](Lang-Swift/specialLiteral.md)
- [Splite과 Component](Lang-Swift/splite_component_map.md)
- [Swift - 스위프트에서 사용하는 패턴들](Lang-Swift/swift_a_swift_patterns.md)
- [case let : for case let 익숙해지기](Lang-Swift/swift_caseLet_for.md)
- [Switch case let, If case let, guard case let](Lang-Swift/swift_caseLet_switch_if_guard.md)
- [Swift - Collection_Int : signum()](Lang-Swift/swift_collection_Int_signum.md)
- [Closure 톺아보기](Lang-Swift/swift_firstClassClosureMaster.md)
- [1급 객체](Lang-Swift/swift_firstClassObject.md)
- [Swift - 키워드 defer](Lang-Swift/swift_keywordDefer.md)
- [Swift - 키워드 inout](Lang-Swift/swift_keywordInout.md)
- [Swift - Mirror 사용하기](Lang-Swift/swift_mirror.md)
- [Swift - Range 함수 사용하기](Lang-Swift/swift_range.md)
- [Swift - 참조(Strong, weak, unowned)](Lang-Swift/swift_reference_weak_unowned.md)
- [Array - 특정값이 동일하거나 포함한 경우 찾기 :  firstIndex()](Lang-Swift/swift_replacingArrayIndexValue..md)

### [Lang-Objective-C](#ios-lang-objective-c)
- [Objc - Objc 프로젝트에서 Swift 라이브러리 사용하기](Lang-Objective-C/Objc_Bridging_SwiftInObjc.md)
- [ObjC - Control Flow : Switch문](Lang-Objective-C/Objc_ControlFlow.md)
- [Objc - 라이브러리 : 직접 파일삽입된 라이브러리 제거작업](Lang-Objective-C/Objc_DeleteFramework.md)
- [ObjC - NSDictionary to NSString](Lang-Objective-C/Objc_DicToStr.md)
- [ObjC - 로그찍기](Lang-Objective-C/Objc_Log.md)
- [Objc - c언어와 objective-c의 차이, 발전](Lang-Objective-C/TIL220421_aboutObjectiveC.md)


### Lang-Dart
- [Dart - Intro](Lang-Dart/Dart_0000.Intro.md)
- [Dart - 변수와 상수 / 컴파일과 런타임](Lang-Dart/Dart_0001.Variable.md)
- [Dart - 콜렉션 타입](Lang-Dart/Dart_0002.Collection.md)
- [Dart - 함수정의 및 호출 / 1급 객체](Lang-Dart/Dart_0003.method.md)
- [Dart - Flow Control](Lang-Dart/Dart_0004.FlowControl.md)
- [Dart - 싱글턴 패턴](Lang-Dart/Dart_3010.Singleton.Basics.md)
- [Dart - 팩토리 패턴](Lang-Dart/Dart_3011.Factory.md)

### Lang-Ruby
- [Install: Ruby](Lang-Ruby/Install_Ruby.md)
- [RubyGems - Package Manager :　gem 관리하기](Lang-Ruby/ManageGem.md)
- [Ruby - 버전관리 : RVM, Rbenv 사용법](Lang-Ruby/ManageRuby.md)



## Markup & Style

### Lang-Markdown
- [마크다운 - HTML사용하기](Docs/Docs_MarkDown_CSS.md)
- [마크다운에서 Toggle(Expander control) 기능 사용하기](Docs/HTML_Toggle.md)
- [마크다운 - 이미지 사이즈 세팅하기](Docs/MarkDown_Image.md)
- [마크다운 - TOC기능 만들기 (Table Of Contents)](Docs/MarkDown_TOC.md)
- [마크다운 - 표 만들기 (Table)](Docs/MarkDown_Table.md)


### Lang-HTML

### Lang-CSS


<br><br>
---

# 🖥️ Computer Science

## 📚 Basics
- [트랜지스터의 원리](ComputerScience/221024_transister.md)
- [2진법,10진법,16진법](ComputerScience/Basics/221021_baseRadix.md)

## ⚙️ Hardware

## 🧩 Software
- [여러가지 버전관리정책](ComputerScience/VersionLint.md)
- [애자일 방법론 이해하기](ComputerScience/methodology_agile.md)
- [MVP: Minimum Viable Product](ComputerScience/MVP.md)
- [직렬화(Serialization)](ComputerScience/Serialization.md)
- [Virtual Memory - Page File Swap](ComputerScience/VirtualMemory_PageFileSwap.md)

## 📐 Algorithms
- [문제풀이 인사이트](Algorithm/000_algorithm_a_problem_solving_insights.md)
- [복잡도 정리](Algorithm/algorithm_000_essential_TimeComplexity.md)
- [필수 알고리즘 - 그리디 (Greedy)](Algorithm/algorithm_006_esssential_Greedy.md)
- [구현 정리](Algorithm/strategy_001_basic_implementation.md)
- [그래프 정리 (stack, queue, 재귀, bfs, dfs)](Algorithm/strategy_002_basic_graph_search.md)
- [알고리즘이란](Algorithm/About_Algorithm.md)
- [알고리즘 - 선택정렬 : Selection Sort](Algorithm/algorithm00_selectionSort.md)
- [알고리즘 - 버블정렬 : Bubble Sort(작성중)](Algorithm/algorithm01_bubbleSort.md)
- [알고리즘 템플릿](Algorithm/algorithm_000_AQuck.md)
- [필수 알고리즘 - BFS: 너비 우선 탐색(Breath-first search)](Algorithm/algorithm_000_essential_BFS.md)
- [필수 알고리즘 - 백트래킹](Algorithm/algorithm_002_essential_BackTracking.md)
- [필수 알고리즘 - 시뮬레이션](Algorithm/algorithm_003_essential_simulation.md)
- [필수 알고리즘 - 투 포인터](Algorithm/algorithm_004_essential_twoPointer.md)
- [필수 알고리즘 - 이진탐색 (Binary Search)](Algorithm/algorithm_005_essentail_binarySearch.md)
- [필수 알고리즘 - DP (Dynamic programming)](Algorithm/algorithm_007_essential_DP.md)
- [필수 알고리즘 - MST (Minimum Spanning Tree)](Algorithm/algorithm_008_essential_mst.md)
- [필수 알고리즘 - 플로이드 (Floyd)](Algorithm/algorithm_0091_essentail_Floyd.md)
- [필수 알고리즘 - 다익스트라 (Dijkstra)](Algorithm/algorithm_009_essential_Dijkstra.md)

## 📦 Data Structure
- [자료구조를 왜 공부해야하는지](Algorithm/algorithm00_00_dataStructure.md)
- [기본 자료 구조 - 배열](Algorithm/000_algorithm_dataStructure_essential_array.md)
- [기본 자료 구조 - 연결 리스트 (Linked List)](Algorithm/001_algorithm_dataStructure_essential_linkedList.md)
- [기본 자료 구조 - 스택 (Stack)](Algorithm/002_algorithm_dataStructure_essential_stack.md)
- [기본 자료 구조 - 큐 (Queue)](Algorithm/003_algoritym_dataStructure_essential_queue.md)

## 🌐 Networking
- [HTTP/2에 대하여(feat.ios)](ComputerScience/http_2.md)
- [네트워킹 - 호스트파일이란, 내부망 설정하기](ComputerScience/networking_hostfile.md)
- [OSI 7 Layer](ComputerScience/osi_7layer.md)
- [OSI 7 Layer - 1. Physical Layer(물리계층)](ComputerScience/osi_7layer_010.Physical.md)
- [OSI 7 Layer - 1.5 여러 컴퓨터간 통신](ComputerScience/osi_7layer_011_internet.md)
- [OSI 7 Layer - 2. Data Link Layer(데이터 링크 계층)](ComputerScience/osi_7layer_020.DataLink.md)
- [OSI 7 Layer - 3. Network Layer(네트워크 계층)](ComputerScience/osi_7layer_030.Network.md)

## 🧮 Programming Paradigms
- [프로그래밍 패러다임 - Functional Programming(함수형 프로그래밍)](ComputerScience/programming_00_Functional_.md)
- [Functional Programming - 모나드 이해하기](ComputerScience/programming_00_Functional_Monade.md)
- [동기와 비동기](ComputerScience/synchronous_Asynchronous.md)

## 🎯 Design Patterns
- [Singleton Pattern 개요](ComputerScience/DesignPatterns/cs_dp_00_singleton_overview.md)
- [Factory Pattern 개요](ComputerScience/DesignPatterns/cs_dp_01_factory_overview.md)

## 🏛 Architecture Patterns

## 🛡 Security & Cryptography

## 🗄 Database

## 🧠 AI / Machine Learning
- [딥러닝이란](About-AI/DeepLearning.md)
- [딥러닝 - 신경망으로 숫자에서 패턴찾기](About-AI/DeepLearning_Neural.md)
- [요즘 핫한 GPT로 앱만들어보기](About-AI/MVVM_ReactorKit_Snapkit_RxSwift.md)
- [언어모델이란](About-AI/chatGPT.md)


<br><br>

---

# DevOps / Tools

### Tools
- [Postman 가이드](DevOps/Tools/Postman_Guide.md)

<br><br>


### CI/CD
- [CI/CD - GitHub Action 사용하기 : 초기 구현하기](CI_CD/GithubAction_A_tutorial00.md)
- [CI/CD - GitHub Action 사용하기2 : on 섹션 수정하기](CI_CD/GithubAction_A_tutorial01.md)
- [CI/CD - GitHub Action 사용하기3 : 실행할 스크립트 짜보기](CI_CD/GithubAction_A_tutorial02.md)

<br><br>

---

### Git
- [Git 브랜치 전략 3종 요약 (Git Flow / GitHub Flow / GitLab Flow)](Git/Git_030_BranchStrategy.md)
- [Git Actions - Permission to ....git denied to github-actions](Git/GitAction_tokenError.md)
- [Git - 튜토리얼(1) : 브랜치 생성하기. 리스트 확인, 브랜치 체크아웃](Git/Git_001_tutorial_checkout.md)
- [Git - 튜토리얼(2) : pull, fetch](Git/Git_002_pull.md)
- [Git - 튜토리얼(3) : status, add, restore, reset](Git/Git_003_add.md)
- [Git - 튜토리얼(4) : commit, push](Git/Git_004_commitPush.md)
- [Git - 푸시한 커밋의 Author 변경하기(username과 user email 수정하기)](Git/Git_010_tutorial_changeUsername.md)
- [GitHub - Various APIs](Git/Git_ContributionGraph.md)
- [GitLab SSH키 생성하기](Git/Git_SSHKey_INIT.md)
- [Git - 브랜치 삭제하기](Git/Git_branch_Delete.md)
- [브랜치 이름 변경하기](Git/Git_branch_rename.md)
- [푸시 에러 - 원격 저장소와 커밋 기록이 다른 경우](Git/Git_pushError_OtherCommit.md)
- [Git - 현재 깃폴더에 연동한 username 확인하고 변경하기](Git/Git_username.md)
- [공동작업을 위한 Git 버전관리](Git/TIL220422_GitControl.md)
- [git ignore를 사용하여 불필요한 업로드 줄이기](Git/TIL221108_how_to_make_ignore.md)
- [Git - Fork한 레포지토리 최신화 하기](Git/gitFork.md)
- [Git - 갑자기 터미널이 한글로 나온다면](Git/gitKorean.md)
- [Git - 깃 리모트 변경 하기](Git/gitRemoteChange.md)
- [Commit Template - 소스트리](Git/how_to_make_SourceTree_Commit_Template.md)
- [XcodeError - UserInterfaceState.xcuserState가 자꾸 뜰 때](Git/what_is_UserInterfaceState.md)


<br><br>

---

## 🧭 Personal Meta


### [Insight](#insight)
- [백만장자의 시크릿](Insight/220604_BookReview_Millionaire_Secret.md)
- [나에게 TIL이란](Insight/230408_About_TIL.md)
- [부의 추월차선: The Millionaire Fastlane](Insight/Economics_TheMillionaireFastlane.md)
- [부모님의 정원](Insight/TIL_220601_parentsGarden.md)
- [SuperNormal](Insight/superNormal.md)

### [Self-Review](#self-review)
- [어떻게 리뷰할 것인가](Self-Review/aboutReview.md)
- [22년 5월 회고 / 6월 목표](Self-Review/review_220530May.md)
- [22년 7월 회고 / 8월 목표](Self-Review/review_220806July.md)
- [23년 4월 회고 / 5월 목표](Self-Review/review_230428April.md)
- [23년 5월 회고 / 6월 목표](Self-Review/review_230526May.md)
- [23년 6월 회고 / 7월 목표](Self-Review/review_230625June.md)
- [23년 7월 회고 / 8월 목표](Self-Review/review_230730July.md)
- [23년 8월 회고 / 9월 목표](Self-Review/review_230830Aug.md)
- [23년 9월 회고 / 10월 목표](Self-Review/review_230930Sep.md)
- [23년 10월 회고 / 11월 목표](Self-Review/review_231031Oct.md)
- [23년 11월 회고 / 12월 목표](Self-Review/review_231130Nov.md)
- [23년 12월 회고 / 1월 목표](Self-Review/review_231231Dec.md)
- [24년 4월 회고 / 5월 목표](Self-Review/review_240430April.md)
- [24년 5월 회고 / 6월 목표](Self-Review/review_240531May.md)


# History
- 220314 : First Commit
- 250703 : 모바일 전체 구조 통일
