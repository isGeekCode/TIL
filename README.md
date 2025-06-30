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


# Mobile
## 📦 iOS - UIKit기반 앱

<details>
<summary>UIKit 펼쳐보기</summary>

<details open>
<summary>🔄 UIKit 앱의 구조와 각종 이벤트 흐름</summary>

- [UIKit - App Structure](#uikit---app-structure) : UIApplication, AppDelegate, SceneDelegate 기반 앱 구조
- [UIKit - Windows & Screens](#uikit---windows--screens) : UIWindow, UIScreen 구성
- [UIKit - App Lifecycle](#uikit---app-lifecycle) : AppDelegate와 SceneDelegate의 이벤트
- [UIKit - UIViewController Lifecycle](#uikit---uiviewcontroller-lifecycle) : ViewController의 Life-cycle
- [UIKit - UIView Drawing Cycle](#uikit---uiview-drawing-cycle) : UIView의 Drawing-Cycle
- [UIKit - Responder Chain](#uikit---responder-chain) : UIResponder 처리 흐름, event 전달 체계
</details>

<details open>
<summary>🧩 UI 구성 & View 설계</summary>

- [UIKit - Views & Controls](#uikit---views--controls) : UIView (Container / Content / Control / Text / Search)
- [UIKit - View Controllers](#uikit---view-controllers) : UIViewController (Content / Container)
- [UIKit - Appearance](#uikit---appearance) : 전역 스타일 커스터마이징
- [UIKit - Animation](#uikit---animation) : 애니메이션 처리
- [UIKit - Navigation](#uikit---navigation) : 화면 전환 (Modal, Present/Push 흐름)
</details>

<details open>
<summary>📐 레이아웃</summary>

- [UIKit - Layout & Autolayout](#uikit---layout--autolayout) : 프레임, 오토레이아웃, 스택뷰
- [UIKit - Storyboards](#uikit---storyboards) : 스토리보드의 개념과 역할
- [UIKit - Nib Files](#uikit---nib-files) : XIB 파일과 커스텀 뷰 분리
</details>

<details open>
<summary>🎯 이벤트 & 입력 처리</summary>

- [UIKit - Gestures & Touches](#uikit---gestures--touches) : 제스처 인식기, 터치 처리
- [UIKit - Menus & Shortcuts](#uikit---menus--shortcuts) : UIMenu, 키보드 단축키
- [UIKit - Drag & Drop](#uikit---drag--drop) : 드래그 앤 드롭 API
- [UIKit - Pointer & Pencil](#uikit---pointer--pencil) : 포인터, Apple Pencil 대응
- [UIKit - Focus Navigation](#uikit---focus-navigation) : 키보드 포커스 이동
- [UIKit - Accessibility](#uikit---accessibility) : VoiceOver, 접근성 대응 방법

</details>

<details open>
<summary>🖼 그래픽, 그리기, 텍스트</summary>

- [UIKit - Images & PDF](#uikit---images--pdf) : UIImage, PDF 렌더링
- [UIKit - Drawing](#uikit---drawing) : CoreGraphics 기반 드로잉
- [UIKit - Printing](#uikit---printing) : 인쇄 기능 구성
- [UIKit - Text & Fonts](#uikit---text--fonts) : UILabel, NSAttributedString
- [UIKit - TextKit](#uikit---textkit) : 고급 텍스트 처리 시스템
- [UIKit - Writing Tools](#uikit---writing-tools) : 필기 입력 도구
- [UIKit - Handwriting Recognition](#uikit---handwriting-recognition) : Apple Pencil 필기 인식
</details>

</details>

---


## 📦 iOS - SwiftUI앱
<details>
<summary>SwiftUI 펼쳐보기</summary>


<details open>
<summary>📁 SwiftUI 앱의 구조와 각종 이벤트 흐름</summary>

- [SwiftUI - App Structure](#swiftui---app-structure) : @main, App, Scene 구성과 앱 엔트리 포인트
- [SwiftUI - Lifecycle](#swiftui---lifecycle) : 앱 생명주기 관리 및 상태 전이 흐름
- [SwiftUI - State Management](#swiftui---state-management) : @State, @Binding, @ObservedObject, @EnvironmentObject
</details>

<details open>
<summary>🧩 UI 구성 & View 설계</summary>

- [SwiftUI - View Composition](#swiftui---view-composition) : View, ViewBuilder, 재사용 가능한 뷰 설계
- [SwiftUI - Components](#swiftui---components) : Text, Image, Button, List, VStack 등 기본 UI 요소
- [SwiftUI - Modifiers](#swiftui---modifiers) : .padding(), .font(), .background() 등 스타일링 체계
- [SwiftUI - Navigation](#swiftui---navigation) : NavigationStack, NavigationLink, path 기반 탐색 구조
- [SwiftUI - Modal & Presentation](#swiftui---modal--presentation) : sheet, fullScreenCover, popover 등 화면 전환
- [SwiftUI - Animation](#swiftui---animation) : withAnimation, animation(), transition(), matchedGeometryEffect 등
</details>

<details open>
<summary>🎯 이벤트 & 입력 처리</summary>

- [SwiftUI - Gestures](#swiftui---gestures) : TapGesture, LongPressGesture, DragGesture 등
- [SwiftUI - Input Events](#swiftui---input-events) : 키보드 입력, 포커스 상태 등 이벤트 대응
- [SwiftUI - Clipboard](#swiftui---clipboard) : 클립보드 복사/붙여넣기 처리
- [SwiftUI - Drag & Drop](#swiftui---drag--drop) : 드래그 앤 드롭 구현 방법
- [SwiftUI - Focus](#swiftui---focus) : 포커스 가능한 뷰 구성 및 이동 제어
- [SwiftUI - System Events](#swiftui---system-events) : 앱 상태 변경 등 시스템 이벤트 대응
</details>

---

<details open>
<summary>🔗 프레임워크 상호 연동 (UIKit ↔ SwiftUI)</summary>

- [SwiftUI - UIKit Integration](#swiftui---uikit-integration) : UIViewRepresentable, UIViewControllerRepresentable 활용
- [UIKit - SwiftUI Integration](#uikit---swiftui-integration) : UIHostingController로 SwiftUI View 연결
</details>


---

<details open>
<summary>🌐 네트워크 통신</summary>

- [Networking-restful](#networking-restful) : RESTful API 통신
- [JSON & Codable](#json--codable) : Codable을 활용한 데이터 직렬화 / 역직렬화  
- [WebView 기반 앱 구현](#webview-기반-앱-구현) : WKWebView 구성, JS 통신, 팝업 대응 등
- [Socket Communication](#socket-communication) : WebSocket, Socket.IO 등 실시간 통신 방식
- [Bluetooth / BLE](#bluetooth--ble) : CoreBluetooth 기반 주변기기 연결 및 데이터 송수신
</details>

---


<details open>
<summary>🎨 UI 스타일링 & 디자인 시스템</summary>

- [Design System](#design-system) : 폰트, 색상, 간격 등 재사용 가능한 스타일 가이드 설계
- [Dark Mode Support](#dark-mode-support) : 다크/라이트 모드 대응 전략 및 시스템 연동
- [Theming](#theming) : 사용자 정의 테마 적용 및 환경 연계 처리 (.environment, UIAppearance 등)
- [Assets & Resources](#assets--resources) : 이미지, 색상, 앱 아이콘 등 xcassets 리소스 구성
- [Localization](#localization) : 다국어 지원을 위한 .strings 파일 구성 및 지역 대응 전략  
</details>

---

<details open>
<summary> 🔌 내부 프레임워크 기능 활용 </summary>

- [Media & Camera](#media--camera) : 이미지, 비디오, 카메라 활용  
- [Sharing & Files](#sharing--files) : 공유 기능, 파일 다운로드 처리  
- [Contacts & Location](#contacts--location) : 연락처, 위치 권한 및 연동  
</details>


<details open>
<summary>🔗 외부 프레임워크 서비스 연동</summary>

- [Social Login](#social-login) : Kakao, Naver, Apple 로그인 연동  
- [Firebase Integration](#firebase-integration) : 인증, 실시간 DB, Analytics 등 활용  
- [Analytics & Tracking](#analytics--tracking) : GA4, Adjust 등 연동  
</details>

---

<details open>
<summary> 🧰 개발 보조 도구 및 구성 관리  </summary>

- [3rd Party Libraries](#3rd-party-libraries) : CocoaPods, Swift Package Manager 관리  
- [Environment Configuration](#environment-configuration) : .xcconfig, Scheme
- [Debugging & Performance](#debugging--performance) : 디버깅 도구 및 성능
- [Launch Performance](#launch-performance) : 런치 타임 최적화 전략 (lazy load, 초기 렌더 경량화) 최적화  
</details>


<details open>
<summary> 🛡 보안 및 데이터 저장 기술   </summary>

- [App Permissions](#app-permissions) : Info.plist 권한 설정, 마이크/카메라/위치 접근 처리
- [Privacy Manifest](#privacy-manifest) : 2024년부터 도입된 Apple의 민감 정보 접근 명세
- [Storage Options](#storage-options) : Keychain, UserDefaults, CoreData  
- [Biometrics](#biometrics) : Face ID / Touch ID 연동  
</details>

<details open>
<summary> 🔔 푸시 알림 및 백그라운드 처리 </summary>

- [Push Notification](#push-notification) : APNs 설정 및 메시지 처리  
- [Background Tasks](#background-tasks) : Background Fetch, Task 처리  
</details>


<details open>
<summary>  🧪 앱 테스트 구성 요소  </summary>

- [Unit & UI Test](#unit--ui-test) : XCTest 기반 단위 및 UI 테스트  
- [Snapshot Testing](#snapshot-testing) : UI 정합성 확인을 위한 스냅샷 테스트  
</details>


<details open>
<summary>🏗 아키텍처 및 모듈 설계</summary>

- [Model-View Patterns](#model-view-patterns) : MVC, MVP, MVVM
- [Clean Architecture 계열](#clean-architecture-계열) : VIPER, RIBs의 책임 기반 분리 설계
- [Unidirectional Architecture](#unidirectional-architecture) : Redux 스타일, TCA, ReactorKit 등 단방향 데이터 흐름  
- [Modularization](#modularization) : 모듈 단위 분리 전략  
</details>


<details open>
<summary>🔀 동시성 처리</summary>

- [Concurrency Overview](#concurrency-overview) : 비동기 및 동시성의 개념과 필요성  
- [GCD (Grand Central Dispatch)](#gcd-grand-central-dispatch) : DispatchQueue, QoS, main/asyncAfter 처리  
- [DispatchWorkItem](#dispatchworkitem) : 작업 단위 생성 및 cancel, notify 등  
- [Operation & OperationQueue](#operation--operationqueue) : 병렬 작업 구성 및 의존성 관리  
- [Swift Concurrency](#swift-concurrency) : async/await, Task, TaskGroup 기반의 구조화된 동시성  
</details>


<details open>
<summary>🚀 배포 및 운영 자동화 전략   </summary>

- [Build & Distribution](#build--distribution) : 앱 서명, 빌드, 스토어 배포  
- [Monitoring Tools](#monitoring-tools) : Firebase, Sentry 등 모니터링 연동  
- [App Store Submission](#app-store-submission) : 리뷰 대응, 정책 이해  
- [CI/CD Pipeline](#ci-cd-pipeline) : 자동화된 테스트 및 배포 흐름 

</details>

---

<details open>
<summary>🧯 운영 이슈 문제 해결 </summary>

- [Log Analysis](#log-analysis) : 로그 기반 이슈 추적 및 원인 분석  
- [Crash Handling](#crash-handling) : 크래시 수집 및 대응 전략  
</details>


<details open>
<summary>🧾 Sample App 모음</summary>

- [sample App - 투두리스트](Sample-App-List/sample_000todoList.md)
- [sample App - 그림판앱](Sample-App-List/sample_001pictureApp.md)
- [Sample App : 설정앱 - SwiftUI](Sample-App-List/sample_002SettingApp_SwiftUI.md)
- [Sample App : 설정앱 - UIKit(Code)](Sample-App-List/sample_002SettingApp_UIKit.md)
- [Sample App : 네트워킹과정 앱 - SwiftUI](Sample-App-List/sample_010networkingApp_SwiftUI.md)
- [Block6 앱 만들기](Sample-App-List/sample_blockSix.md)
</details>


<br><br>

---

## Android

<br><br>

---

## Flutter

<br><br>

---

# 🌐 Web  
- [HTML Samples](#web-html-sample)  
- [CSS Patterns](#web-css-patterns)  
- [React](#web-react)  
</details>

<br><br>

---  

# 📚 Programming Language Reference  

## 🧬 Languages
- [Lang-Swift](#lang-swift)
- [Lang-Objective-C](#lang-objective-c)
- [Lang-Ruby](#lang-ruby)
- [Lang-Dart](#lang-dart)
- [Lang-TypeScript](#lang-typescript)
- [Lang-JavaScript](#lang-javascript)
- [Lang-SQL](#lang-sql)


### Markup & Style
- [Lang-Markdown](#lang-markdown)
- [Lang-HTML](#lang-html)
- [Lang-CSS](#lang-css)


<br><br>

---

# 🧠 Computer Science
- [📚 Basics](#-basics) : 
- [⚙️ Hardware](#-hardware) : 
- [🧩 Software](#-software) : 
- [📐 Algorithms](#-algorithms) : 
- [📦 Data Structure](#-data-structure) : 
- [🌐 Networking](#-networking) : 
- [🧮 Programming Paradigms](#-programming-paradigms) : 
- [🛡 Security & Cryptography](#-security--cryptography) : 
- [🗄 Database](#-database) : 
- [🧠 AI / Machine Learning](#-ai--machine-learning) : 

### ⚙️ DevOps / Tools

- [CI_CD](#ci_cd)
- [Docs](#docs)
- [Git](#git)


## 🌐 Other Topics

- [About-IT](#about-it)
- [Conference](#conference)


## 🤖 AI & Errors

- [About-AI](#about-ai)
- [About-Error](#about-error)

---


## 🧭 Personal Meta


- [Self-Review](#self-review)
- [Insight](#insight)


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

### [About-AI](#about-ai)
- [딥러닝이란](About-AI/DeepLearning.md)
- [딥러닝 - 신경망으로 숫자에서 패턴찾기](About-AI/DeepLearning_Neural.md)
- [요즘 핫한 GPT로 앱만들어보기](About-AI/MVVM_ReactorKit_Snapkit_RxSwift.md)
- [언어모델이란](About-AI/chatGPT.md)

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

### 📐 Algorithms
- [문제풀이 인사이트](Algorithm/000_algorithm_a_problem_solving_insights.md)
- [복잡도 정리](Algorithm/algorithm_000_essential_TimeComplexity.md)
- [필수 알고리즘 - 그리디 (Greedy)](Algorithm/algorithm_006_esssential_Greedy.md)
- [구현 정리](Algorithm/strategy_001_basic_implementation.md)
- [그래프 정리 (stack, queue, 재귀, bfs, dfs)](Algorithm/strategy_002_basic_graph_search.md)
- [기본 자료 구조 - 배열](Algorithm/000_algorithm_dataStructure_essential_array.md)
- [기본 자료 구조 - 연결 리스트 (Linked List)](Algorithm/001_algorithm_dataStructure_essential_linkedList.md)
- [기본 자료 구조 - 스택 (Stack)](Algorithm/002_algorithm_dataStructure_essential_stack.md)
- [기본 자료 구조 - 큐 (Queue)](Algorithm/003_algoritym_dataStructure_essential_queue.md)
- [알고리즘이란](Algorithm/About_Algorithm.md)
- [자료구조를 왜 공부해야하는지](Algorithm/algorithm00_00_dataStructure.md)
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

### [CI_CD](#ci_cd)
- [CI/CD - GitHub Action 사용하기 : 초기 구현하기](CI_CD/GithubAction_A_tutorial00.md)
- [CI/CD - GitHub Action 사용하기2 : on 섹션 수정하기](CI_CD/GithubAction_A_tutorial01.md)
- [CI/CD - GitHub Action 사용하기3 : 실행할 스크립트 짜보기](CI_CD/GithubAction_A_tutorial02.md)

### [ComputerScience](#computerscience)
- [2진법,10진법,16진법](ComputerScience/221021_baseRadix.md)
- [트랜지스터의 원리](ComputerScience/221024_transister.md)
- [Data Structure - 다양한 데이터 구조, iOS에서 사용하는 데이터 구조](ComputerScience/DataStructure.md)
- [MVP: Minimum Viable Product](ComputerScience/MVP.md)
- [직렬화(Serialization)](ComputerScience/Serialization.md)
- [# 터미널 - 커스텀 함수 및 환경변수 설정하기](ComputerScience/Terminal_customization.md)
- [Terminal 기초 사용법](ComputerScience/Terminal_manual.md)
- [여러가지 버전관리정책](ComputerScience/VersionLint.md)
- [iOS의 Virtual Memory에 대하여](ComputerScience/VirtualMemory.md)
- [Virtual Memory - Page File Swap](ComputerScience/VirtualMemory_PageFileSwap.md)
- [Data Structure - Stack과 Queue](ComputerScience/cs_001_stackQeueue.md)
- [Dynamic Programming (DP): 동적프로그래밍](ComputerScience/dynamicProgramming.md)
- [iOS와 HTTP/2에 대하여](ComputerScience/http_2.md)
- [iOS에서 메모리구조 : Code / Data / Heap / Stack](ComputerScience/memoryStructure.md)
- [애자일 방법론 이해하기](ComputerScience/methodology_agile.md)
- [네트워킹 - 호스트파일이란, 내부망 설정하기](ComputerScience/networking_hostfile.md)
- [OSI 7 Layer](ComputerScience/osi_7layer.md)
- [OSI 7 Layer - 1. Physical Layer(물리계층)](ComputerScience/osi_7layer_010.Physical.md)
- [OSI 7 Layer - 1.5 여러 컴퓨터간 통신](ComputerScience/osi_7layer_011_internet.md)
- [OSI 7 Layer - 2. Data Link Layer(데이터 링크 계층)](ComputerScience/osi_7layer_020.DataLink.md)
- [OSI 7 Layer - 3. Network Layer(네트워크 계층)](ComputerScience/osi_7layer_030.Network.md)
- [프로그래밍 패러다임 - Functional Programming(함수형 프로그래밍)](ComputerScience/programming_00_Functional_.md)
- [Functional Programming - 모나드 이해하기](ComputerScience/programming_00_Functional_Monade.md)
- [동기와 비동기](ComputerScience/synchronous_Asynchronous.md)

### [Conference](#conference)
- [Let us: Go! 2022 가을 - 221105(미참석)](Conference/Conference2022_LetUsGo2022_3Fall.md)
- [iOS Daejeon Club - 230325(참석)](Conference/Conference2023_IOSDaejonCodingClub_230325.md)
- [Let us: Go! 2023 봄 - 2304(미참석)](Conference/Conference2023_LetUSGo2023_1Spring.md)


### [Mobile-Common](#mobile-common)
- [App 공통 구성 요소 : Intro](Mobile_000_Common/Mobile_common_0000_intro.md)

### [Mobile-iOS](#mobile-ios)
- [iOS - 스플래시 화면 구현 가이드 (정적 & 동적)](Mobile_01_iOS/iOS_0271_SplashScreen.md)


### [iOS-AppStore](#ios-appstore)
- [App Store Connect - 배포된 앱을 삭제하는 2가지 방법](iOS-AppStore/AppStore_AppDismiss.md)
- [AppStore - 앱 생성하기](iOS-AppStore/AppStore_AppInit.md)
- [AppStore - 수출 규정 준수 정보](iOS-AppStore/AppStore_AppUseNonExempt.md)
- [AppStore - 버전정보 수정하기](iOS-AppStore/AppStore_ChangeVersionInfo.md)
- [AppStore - 긴급 심사 요청(Request Expedited Review)](iOS-AppStore/AppStore_expeditedReview.md)
- [앱심사 - 수출 규정 관련 문서가 누락됨(Missing Compliance) / 우회처리](iOS-AppStore/AppStore_missing_Compliance.md)
- [리젝사유 - 2. Performance(성능)](iOS-AppStore/Reject_2_Performance.md)
- [리젝사유 - 4. Design(디자인)](iOS-AppStore/Reject_4_Design.md)
- [리젝사유 - 5. Legal(법률)](iOS-AppStore/Reject_5_Legal.md)
- [테스트플라잇 - 외부 테스팅 (External Testing)](iOS-AppStore/TestFlight_externalTester.md)

### [iOS-Architecture](#ios-architecture)
- [디자인패턴이란](iOS-Architecture/Architecture_100_De_Intro_.md)
- [Cocoa Design Pattern - Delegate 델리게이트 패턴](iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Delegate.md)
- [Cocoa Design Pattern - Observer 옵저버 패턴](iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Observer.md)
- [Cocoa Design Pattern - Singleton (싱글톤 패턴)](iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Singleton.md)
- [아키텍쳐패턴이란, 디자인패턴과 아키텍쳐의 차이](iOS-Architecture/Architecture_200_Arc_Intro.md)
- [MVC -> MVP -> MVVM : Caculator](iOS-Architecture/Architecture_301_MVCToMVPToMVVM_Calculator.md)
- [MVC -> MVP -> MVVM : ColorSelectApp](iOS-Architecture/Architecture_301_MVCToMVPToMVVM_ColorSwitchApp.md)
- [MVC to MVVM : 01. UTC 오늘, 현재, 내일 시간보기](iOS-Architecture/Architecture_301_MVCToMVVM_01_UTC.md)
- [MVC to MVVM : 02. TableVC 클릭시 텍스트 변경](iOS-Architecture/Architecture_301_MVCToMVVM_02_Task.md)
- [VC -> MVC : Custom UICollectionView](iOS-Architecture/Architecture_301_MVC_CollectionView.md)
- [Architecture - IOS MVC의 한계](iOS-Architecture/Architecture_301_MVC_Massive.md)
- [Architecture - MVC: 전통적인 MVC구조로 HTTP사용하기](iOS-Architecture/Architecture_301_MVC_traditional.md)
- [Architecture - 간단한 MVVM구조 예제](iOS-Architecture/Architecture_301_MVVM_simpleExample.md)
- [단방향 데이터 플로우(Unidirectial Data Flow, UDF)](iOS-Architecture/Architecture_401_UnidirectialDataFlow.md)
- [ReactorKit - 예제: CountApp](iOS-Architecture/Architecture_402_RxSwift_ReactorKit_CountApp.md)
- [Clean Architecture(클린 아키텍쳐)](iOS-Architecture/Architecture_601_CleanArchitecture.md)
- [데이터 바인딩이란](iOS-Architecture/Data_Binding_about.md)
- [Architecture - 비즈니스 로직이란](iOS-Architecture/aboutBusinessLogic.md)

### [iOS-Concurrency](#ios-concurrency)
- [프로그래밍에서 동기 비동기 개념에 대한 이해](iOS-Concurrency/About_000_Sync_vs_Async_Basics.md)
- [비동기처리가 필요한 이유](iOS-Concurrency/About_001_Async_vs_Concurrent_Concepts.md)
- [비동기(Async), 동시(Concurrent)의 개념](iOS-Concurrency/About_002_async_concurrent_2.md)
- [GCD - OperationQueue를 이용한 비동기 작업](iOS-Concurrency/Concurrency_020_OperationQueue.md)
- [GCD - performSelector를 이용한 비동기 작업](iOS-Concurrency/Concurrency_030_performSelector.md)
- [동시성 프로그래밍 : Concurrency 톺아보기](iOS-Concurrency/GCD_001_Overview.md)
- [GCD - DispatchGroup](iOS-Concurrency/GCD_010_DispatchGroup.md)
- [GCD - DispatchWorkItem](iOS-Concurrency/GCD_011_DispatchWorkItem.md)
- [Swift Concurrency - Async / Await / Task](iOS-Concurrency/SwiftConcurrency_Overview.md)

### [iOS-CustomLogic](#ios-customlogic)
- [Login Logic (feat. UserDefault)](iOS-CustomLogic/Login_Logic.md)
- [DynamicSplash 세팅하기](iOS-CustomLogic/splash_dynamicSplash.md)

### [iOS-Development](#ios-development)
- [Date - Date로 두 개의 시간차 구하기](iOS-Development/Date_getTimeInterval.md)
- [볼륨버튼 캐치하기](iOS-Development/Detect_SystemVolume.md)
- [External Link (외부링크) - 커스텀 앱스키마 만들기, 사용하기](iOS-Development/ExternalLink_CustomScheme.md)
- [KVC와 KVO](iOS-Development/KVC_KVO.md)
- [로컬라이징](iOS-Development/Localization.md)
- [AudioToolbox - 롱프레스와 햅틱진동 구현하기 (Feat.Long press)](iOS-Development/Third_AudioToolBox_HapticAndLongpress.md)
- [IOS에 있어서 Caching](iOS-Development/ios_caching.md)

### [iOS-Environment](#ios-environment)
- [Xcode - 빌드된 app파일은 어디에 있을까](iOS-Environment/Bundle_derivedData.md)
- [appStoreReceiptURL](iOS-Environment/DetectingDeploymentEnvironment.md)
- [.ipa 파일 만들기](iOS-Environment/How_to.make_ipa.md)
- [How to Set - 세로모드 고정 (Potrait)](iOS-Environment/How_to_set_potrait_mode.md)
- [Info.plist : (값 가져오기, 권한)](iOS-Environment/InfoPlist.md)
- [Info.plist - App Version 가져오기](iOS-Environment/InfoPlist_appVersion.md)
- [Xcode 주석사용법](iOS-Environment/PragmaMark.md)
- [XCode - 전처리문 사용하기](iOS-Environment/PreprocessorCommand.md)
- [Privacy - 여러가지 접근권한요청](iOS-Environment/PrivercyPermission_various.md)
- [Scheme - Debug / Release 빌드 분리하기](iOS-Environment/Scheme_Separate_BuildSet.md)
- [Xcode에서 디버그뷰 활성화하기 :Firebase, GA4](iOS-Environment/firebase_debugView.md)
- [iOS DeviceSupport - 테스트 디바이스 iOS 수동 업데이트](iOS-Environment/iOSDeviceSupport_Manually_update.md)

### [iOS-Extensions](#ios-extensions)
- [hex값을 UIcolor로 변환하는 방법](iOS-Extensions/TIL221025_convertHexToUIColor.md)
- [UIKit에서 SwiftUI처럼 만들어 사용하기](iOS-Extensions/UIKitLikeSwiftUI.md)

### [iOS-Foundation](#ios-foundation)
- [AVFoundation - AVPlayer 사용하기](iOS-Foundation/AVFoundation_AVPlayer.md)
- [AVFoundation - TTS : Text-To-Speech](iOS-Foundation/AVFoundation_AVSpeechSynthesizer.md)
- [AVFoundation - Barcode Scanner 구현하기](iOS-Foundation/AVFoundation_BarcodeScan.md)
- [userDefault](iOS-Foundation/AboutUserDefualt.md)
- [Calendar - 캘린더로 두 개의 날짜 비교하기](iOS-Foundation/Calendar_getDateInterval.md)
- [FileManager - 파일 다운로드하기](iOS-Foundation/FileManager_fileDownload.md)
- [FileManager - 사용하기](iOS-Foundation/FileManager_introduce.md)
- [Foundation - JSONSerialization(1): 직렬화 Intro](iOS-Foundation/Foundation_JSONSerialization00.md)
- [Foundation - JSONSerialization(3):  Decode JSONData](iOS-Foundation/Foundation_JSONSerialization_Decode.md)
- [Foundation - JSONSerialization(2): Encode JSONData](iOS-Foundation/Foundation_JSONSerialization_Encode.md)
- [String Protocol - String to Data](iOS-Foundation/StringProtocol_stringToData.md)
- [타임스탬프 구현하기](iOS-Foundation/TIL220914_TimeStamp.md)
- [CMTime](iOS-Foundation/cmtime.md)

### [iOS-Framework-CoreAnimation](#ios-framework-coreanimation)
- [Core Animation 프레임워크(작성중)](iOS-Framework-CoreAnimation/About_CA_000_.md)

### [iOS-Framework-CoreLocation](#ios-framework-corelocation)
- [CLLocation - 위치정보 사용하기](iOS-Framework-CoreLocation/CLLocation_a_howToUse.md)
- [CoreLocation - 비콘 조회하기](iOS-Framework-CoreLocation/CLLocation_beacon.md)
- [Bluetooth, BLE, Beacon, iBeacon](iOS-Framework-CoreLocation/CoreLocation_iBeacon.md)

### [iOS-Framework-Management](#ios-framework-management)
- [Framework란 무엇인가](iOS-Framework-Management/FrameworkM_00_about.md)
- [XCFramework 생성하기](iOS-Framework-Management/FrameworkM_00_initial.md)

### [iOS-Framework-Migration](#ios-framework-migration)
- [UIAlertView Deprecated in iOS 9, Replaced by UIAlertController in iOS 10.0](iOS-Framework-Migration/AlertView.md)
- [MPMoviePlayerController Deprecated in iOS 10, Replaced by AVPlayerViewController in iOS 7](iOS-Framework-Migration/MPMoviePlayer.md)
- [NSURLConnection Deprecated in iOS 9, Replaced by URLSession in iOS 7](iOS-Framework-Migration/NSURLConnection.md)
- ['setVolume:' is deprecated: first deprecated in iOS 7.0 - Use MPVolumeView for volume control.](iOS-Framework-Migration/mpmusicplayer.md)

### [iOS-Framework-PhotoKit](#ios-framework-photokit)
- [PhotoKit - Introduce](iOS-Framework-PhotoKit/photokit_000_intro.md)

### [iOS-Framework-SwiftUI](#ios-framework-swiftui)
- [Layout - SwiftUI: Text](iOS-Framework-SwiftUI/SwiftUI_001_Text.md)
- [Layout - SwiftUI: Image](iOS-Framework-SwiftUI/SwiftUI_002_Image.md)
- [Layout - SwiftUI: Button](iOS-Framework-SwiftUI/SwiftUI_003_Button.md)
- [Layout - SwiftUI: Spacer](iOS-Framework-SwiftUI/SwiftUI_004_Spacer.md)
- [Layout - SwiftUI: Padding](iOS-Framework-SwiftUI/SwiftUI_005_Padding.md)
- [Layout - SwiftUI: HStack, VStack, ZStack](iOS-Framework-SwiftUI/SwiftUI_010_Stack.md)
- [Layout - SwiftUI: NavigationView](iOS-Framework-SwiftUI/SwiftUI_011_NavigationView.md)
- [Layout - SwiftUI: TabView](iOS-Framework-SwiftUI/SwiftUI_012_TabView.md)
- [SwiftUI - Control에 대하여](iOS-Framework-SwiftUI/SwiftUI_020_Control.md)
- [SwiftUI - View 프로토콜](iOS-Framework-SwiftUI/SwiftUI_030_View.md)
- [Layout - SwiftUI: Color](iOS-Framework-SwiftUI/SwiftUI_Color.md)
- [Layout - SwiftUI: List](iOS-Framework-SwiftUI/SwiftUI_List.md)
- [Layout - SwiftUI: ScrollView](iOS-Framework-SwiftUI/SwiftUI_ScrollView.md)
- [Layout - SwiftUI: State와 바인딩](iOS-Framework-SwiftUI/SwiftUI_State.md)

### [iOS-Framework-SwiftUI_UIKit](#ios-framework-swiftui_uikit)
- [UIKit으로 구현된 화면에 SwiftUI View를 추가하기 : UIHostingController](iOS-Framework-SwiftUI_UIKit/PreviewProvider_UIHostingController.md)
- [UIKit에서 SwiftUI의 Preview 사용하기](iOS-Framework-SwiftUI_UIKit/PreviewProvier.md)
- [UIKit에서 SwiftUI의 Preview관련 함수 만들어 사용하기](iOS-Framework-SwiftUI_UIKit/PreviewProvier3.md)
- [SwiftUI에서 UIKit 사용하기 : UIViewRepresentable, UILabel, WebView](iOS-Framework-SwiftUI_UIKit/UIViewResentable_UIKit.md)

### [iOS-Framework-UIKit](#ios-framework-uikit)
- [UIKit - UIStoryboard](iOS-Framework-UIKit/About_UIKIt_010_UIStoryboard.md)
- [[Apple Document] - About App Development with UIKit](iOS-Framework-UIKit/About_UIKit_.md)
- [UIKit기반 앱의 간단한 화면 인터페이스 구조](iOS-Framework-UIKit/About_UIKit_050WindowsAnsScreens_Screens_SimpleUIKitInterface.md)
- [읽어야할 개발자 문서](iOS-Framework-UIKit/About__Document_Recommended.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(0) : Intro](iOS-Framework-UIKit/About__UIKit_Tutorial00_Today00.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(1) : Creating a list View](iOS-Framework-UIKit/About__UIKit_Tutorial00_Today01.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(2) : Adopting collection views](iOS-Framework-UIKit/About__UIKit_Tutorial00_Today02.md)
- [[iOS App Dev Tutorials] UIKit - Today앱 만들기(3) : Displaying cell info](iOS-Framework-UIKit/About__UIKit_Tutorial00_Today03.md)
- [Container ViewController Type - Navigation Controller](iOS-Framework-UIKit/Container_ViewController_NavigationController.md)
- [Layout - 오토레이아웃의 개념](iOS-Framework-UIKit/Layout_About_AutoLayout.md)
- [Layout - UIView에 대하여](iOS-Framework-UIKit/Layout_About_UIView.md)
- [Layout - CGRectMake는 뭘까](iOS-Framework-UIKit/Layout_CGRectMake.md)
- [Layout - CodeUI: CustomShadow(feat.CustomClass)](iOS-Framework-UIKit/Layout_CodeUI_CustomShadow.md)
- [Layout - CodeUI: UIView, UILabel](iOS-Framework-UIKit/Layout_CodeUI_UILabel_UIView.md)
- [Layout - CodeUI: UILabel 고정폭 지정 이유 및 방법](iOS-Framework-UIKit/Layout_CodeUI_UILabel_Width_Fix.md)  
- [Layout - 이미지 컨텐츠 모드 (ContentMode)](iOS-Framework-UIKit/Layout_ImageContentMode.md)
- [Layout - StoryboardUI: CornerRadius](iOS-Framework-UIKit/Layout_StoryboardUI_CornerRadius.md)
- [UIAlert 어디서든 띄우기](iOS-Framework-UIKit/Layout_UIAlert.md)
- [Layout - Hierarchy of UIView (feat. addSubView)](iOS-Framework-UIKit/Layout_addSubView.md)
- [현재기기의 화면크기 측정하기 + 콤바인을 이용한 반응형레이아웃 만들기](iOS-Framework-UIKit/Layout_currentDeviceCheck&useCombineReactiveAutoLayout.md)
- [MessageUI란](iOS-Framework-UIKit/MessageUI.md)
- [MessageUI - MFMailComposeVC : 문의메일 보내기](iOS-Framework-UIKit/MessageUI_sendMail.md)
- [MessageUI - MFMessageComposeVC : 문자메세지 보내기](iOS-Framework-UIKit/MessageUI_sendSMS.md)
- [NSDate - Timezone: UTC, GMT, KST](iOS-Framework-UIKit/NSObject_NSDate_UTC.md)
- [NSObject - Timer : 타이머 구현하기](iOS-Framework-UIKit/NSObject_Timer.md)
- [NSObject_UIBarItem_UIBarButtonItem & UITabBarItem : 네비게이션바 / 툴바 / 탭바를 표시하는 아이템](iOS-Framework-UIKit/NSObject_UIBarItem.md)
- [CGColor에 대하여](iOS-Framework-UIKit/NSObject_UIColorCgColor.md)
- [NSObject - UIFont](iOS-Framework-UIKit/NSObject_UIFont.md)
- [NSObjcect_GestureRecognizer_UILongPressGestureRecognizer](iOS-Framework-UIKit/NSObject_UIGestureRecognizer_LongPress.md)
- [NSObject_UIResponder : UIResponder와 Responder Chain](iOS-Framework-UIKit/NSObject_UIResponder_.md)
- [NSObject_UIResponder_UIViewController_UIActivityViewController : 공유하기 기능](iOS-Framework-UIKit/NSObject_UIResponder_UIViewController_UIActivityViewController.md)
- [NSObject_UIResponder_UIViewController : 소개](iOS-Framework-UIKit/NSObject_UIResponder_UIViewController_a_Functions.md)
- [NSObject_UIResponder_UIViewController : 생성자](iOS-Framework-UIKit/NSObject_UIResponder_UIViewController_a_howToMake.md)
- [NSObject_UIResponder_UIViewController : UIViewController's Life-cycle (뷰컨트롤러의 생명주기)](iOS-Framework-UIKit/NSObject_UIResponder_UIViewController_lifeCycle.md)
- [NSObject_UIResponder_UIView : UIView 클래스](iOS-Framework-UIKit/NSObject_UIResponder_UIView_.md)
- [UIView의 Drawing Cycle (Layout Cycle)](iOS-Framework-UIKit/NSObject_UIResponder_UIView_DrawingCycle.md)
- [NSObject_UIResponder_UIView_UIImageView - 경로를 통해 이미지 다운로드하여 세팅하기](iOS-Framework-UIKit/NSObject_UIResponder_UIView_UIImageView_setImageDownload.md)
- [NSObject_UIResponder_UIView : UIPickerView](iOS-Framework-UIKit/NSObject_UIResponder_UIView_UIPickerView.md)
- [NSObject_UIResponder_UIView_UIProgressView](iOS-Framework-UIKit/NSObject_UIResponder_UIView_UIProgressView.md)
- [NSObject_UIResponder_UIView_UIScrollView](iOS-Framework-UIKit/NSObject_UIResponder_UIView_UIScrollView.md)
- [NSObject_UIResponder_UIView : UITabBar](iOS-Framework-UIKit/NSObject_UIResponder_UIView_UITabBar.md)
- [UIView - Layer란 무엇인가(작성중)](iOS-Framework-UIKit/NSObject_UIResponder_UIView_layer.md)
- [NSObject_UIResponder_UIView_UIActivityIndicatorView : 사용법](iOS-Framework-UIKit/NsObject_UIResponder_UIView_UIActivityIndicatorView.md)
- [UIKit에서 RootViewController 찾기](iOS-Framework-UIKit/SearchingRootVC.md)
- [CGPoint, CGSize, CGRect](iOS-Framework-UIKit/UIKit_CGPoint_CGSize_CGRect.md)
- [UIDevice](iOS-Framework-UIKit/UIKit_UIDevice.md)
- [UIKit - UISearchBar](iOS-Framework-UIKit/UIKit_UITextField_UISearchBar.md)
- [UICollectionView - 프로퍼티 옵저버 didSet과 isSelected](iOS-Framework-UIKit/ios_CollectionViewCell.md)

### [iOS-Framework-UIKit-UIResponder-UIApplication](#ios-framework-uikit-uiresponder-uiapplication)
- [[Apple Document] - UIApplicationMain(::::)](iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_000UIApplicationMain.md)
- [[Apple Document] - UIApplication 싱글턴 객체](iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_001UIApplication.md)
- [[Apple Document] - AppDelegate, UIApplicationDelegate 프로토콜](iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_002UIApplicationDelegate.md)
- [[Apple Document] - Managing your app’s life cycle : 앱의 생명주기 관리](iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_003AppLifeCycle.md)
- [[Apple Document] - Responding to the launch of your app : 앱 실행에 대한 응답](iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_004LaunchStoryboard.md)
- [[Apple Document] - About the app launch sequence : 앱의 실행되는 순서에 관하여](iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_005AppLaunchSequnce.md)
- [앱의 구동에 관하여](iOS-Framework-UIKit-UIResponder-UIApplication/AppLaunching_About.md)
- [UIApplication_AppDelegate - 헷갈릴수 있는 두 함수(didReceive형제)](iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate-DifferenceNotification.md)
- [UIApplication_AppDelegate - userNotificationCenter](iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate_userNotificationCenter.md)
- [UIApplication_AppDelegate - UIApplicationDelegate : 앱의 상태 / 생명주기(Life-Cycle)](iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_StatusCycle_of_App.md)

### [iOS-Framework-UIKit-UIResponder-UIView-UIControl](#ios-framework-uikit-uiresponder-uiview-uicontrol)
- [[Apple Document] - UIControl.Event 살펴보기](iOS-Framework-UIKit-UIResponder-UIView-UIControl/About_UIControl_030_event.md)
- [UIKit - UIAlertController : 장문의 얼럿 만들기](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UIAlertController_NSMutableAttributedString.md)
- [NSObject_UIResponder_UIView_UIControl : UIButton](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UIButton.md)
- [NSObject_UIResponder_UIView_UIControl : UIDatePicker](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UIDatePicker.md)
- [NSObject_UIResponder_UIView_UIControl : UIRefreshControl](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UIRefreshControl.md)
- [NSObject_UIResponder_UIView_UIControl : UISegmentedControl](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UISegmentedControl.md)
- [NSObject_UIResponder_UIView_UIControl : UISlider](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UISlider.md)
- [NSObject_UIResponder_UIView_UIControl : UISwitch](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UISwitch.md)
- [NSObject_UIResponder_UIView_UIControl : UITextField](iOS-Framework-UIKit-UIResponder-UIView-UIControl/NSObject_UIResponder_UIView_UIControl_UITextField.md)

### [iOS-Framework-UIKit-UIResponder-UIView-UIScrollView](#ios-framework-uikit-uiresponder-uiview-uiscrollview)
- [NSObject_UIResponder_UIView_UIScrollView_UICollectionView : 사용법](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_00_howToMake.md)
- [UICollectionView with DiffableDataSource](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_30_Diffable.md)
- [UICellAccessory : UICollectionView에 사용하는 악세서리 Struct](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_41_-UICellAccessory.md)
- [UITableView - 템플릿](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_00_Template.md)
- [UITableView - 기본 UITableView 생성](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_01_basic.md)
- [UITableView - 커스텀 UITableViewCell](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_02_CustomTableViewCell.md)
- [UITableView - Section 구현하기](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_03_Section.md)
- [UITableView - 셀 선택, 삭제 및 상호작용](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_04_select_UI.md)
- [UITableView - 동적 셀 높이](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_05_AutomaticDimension.md)
- [UITableView : 편집스타일 설정하기 - editingStyle](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_10_editingStyle.md)
- [[Apple Document] - NSObject_UIResponder_UIView_UITableViewCell](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_40_UITableViewCell.md)
- [NSObject_UIResponder_UIView_UITableViewCell : accessoryType](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_41_UITableViewCell_Delegate_AccessoryType.md)
- [NSObject_UIResponder_UIView_UIScrollView_UITableView : 셀 경계선없는 테이블뷰](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_50_excludeOutline.md)
- [NSObject_UIResponder_UIView_UIScrollView_UITableView : 셀 클릭시 높이가 변경되는 테이블뷰](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_80_FlexibleTableViewCell.md)
- [NSObject_UIResponder_UIView_UIScrollView_UITableView : SwiftUI로 셀 구현하기](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_81_SwiftUI_Configuration.md)

### [iOS-Framework-UIKit-UIResponder-UIViewController](#ios-framework-uikit-uiresponder-uiviewcontroller)
- [PHPickerController 사용하기-iOS14이상](iOS-Framework-UIKit-UIResponder-UIViewController/PHPickerViewController.md)
- [UIImagePickerController 사용하기-iOS14미만](iOS-Framework-UIKit-UIResponder-UIViewController/UIImagePickerController.md)
- [NSObject_UIResponder_UIViewController_UITableViewController : 테이블뷰 전용 ViewController](iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableViewController.md)

### [iOS-Hierachy](#ios-hierachy)
- [iOS_Hierachy - Foundation](iOS-Hierachy/IOS_Hierachy_Foundation.md)
- [iOS_Hierachy - UIKit](iOS-Hierachy/IOS_Hierachy_UIKit.md)

### [iOS-Integrity](#ios-integrity)
- [Integrity - 앱 설치환경 체크](iOS-Integrity/Integrity_Build_Environment.md)
- [Integrity - 인증서(.p8, .p12 / Development, Distribution / Producation SSL, Development SSL)](iOS-Integrity/Integrity_Certificate.md)
- [Integrity - 인증서와 프로비저닝 프로파일 (Certificate & Provisioning Profile) 관리하기](iOS-Integrity/Integrity_Certificate_Provisioning.md)
- [Integrity - DeviceCheck](iOS-Integrity/Integrity_DeviceCheck.md)
- [Integrity_개인정보 보호 매니페스트 PrivacyInfo.xcprivacy 만들기](iOS-Integrity/Integrity_PrivacyInfo.md)
- [Integrity - UUID / UDID / IDFA / IDFV](iOS-Integrity/Integrity_UUID_UDID_IDFA.md)
- [Integrity - APN 인증키(.p8) 발급받기](iOS-Integrity/Integrity_apn_p8.md)
- [Integrity - 중간자 공격(man-in-the-middle attack)](iOS-Integrity/Integrity_manInTheMiddleAttack.md)
- [Integrity - 리플레이 공격(Replay attack)](iOS-Integrity/Integrity_replayAttack.md)

### [iOS-Library](#ios-library)
- [iOS - 패키지 의존성 관리 도구: CocoaPods, Carthage, SPM](iOS-Library/About_A_iOS_Package.md)
- [About Swift PackageManager](iOS-Library/About_SPM.md)
- [CocoaPods 사용하기](iOS-Library/About_cocoaPods_basic.md)
- [About CocoaPods Error 방지하기](iOS-Library/About_cocoaPods_error.md)
- [Convention - SwiftLint 세팅하기](iOS-Library/Convention_SwiftLint.md)
- [Convention - SwiftLint 세부설정하기](iOS-Library/Convention_SwiftLintCustomRule.md)
- [라이브러리 - 카카오 SDK 사용하기](iOS-Library/Library_A_kakaoSDK.md)
- [라이브러리 - GIFu 사용하기](iOS-Library/Library_Gifu.md)
- [Library - Hero](iOS-Library/Library_Hero.md)
- [라이브러리 - Kingfisher 사용하기](iOS-Library/Library_Kingfisher.md)
- [라이브러리 - swiftSoup](iOS-Library/Library_SwiftSoup.md)
- [Push - 핑거푸시](iOS-Library/Push_fingerPush.md)
- [ReactiveX: RxSwift Introduce](iOS-Library/RxSwift_Introduce.md)
- [SNS Login - Kakao](iOS-Library/SNSLogin_kakao.md)
- [SNS Login - Naver](iOS-Library/SNSLogin_naver.md)

### [iOS-Networking](#ios-networking)
- [네트워크 통신의 이해](iOS-Networking/About_Networking.md)
- [NSObject - URLSession](iOS-Networking/About_URLSession.md)
- [Notifications - IOS에서 사용하는 알림의 종류](iOS-Networking/Apple_Notification.md)
- [개념 - 페이로드(Payload)](iOS-Networking/Concept_payload.md)
- [Cookie - ios에서 쿠키 다루기](iOS-Networking/Cookie_AdjustCookie.md)
- [Cookie - WKProcessPool를 사용해 여러 웹뷰에서 쿠키 공유하기](iOS-Networking/Cookie_Cookie_sharing.md)
- [WebView - WKWebsiteDataStore 사용하여 웹뷰의 데이터관리하기](iOS-Networking/Cookie_WebView_WKWebsiteDataStore.md)
- [Cookie란](iOS-Networking/Cookie_about.md)
- [Cookie - cookieAcceptPolicy (쿠키수락정책)](iOS-Networking/Cookie_cookieAcceptPolicy.md)
- [Cookie - 현재 웹뷰로 쿠키 가져오기](iOS-Networking/Cookie_cookie_call.md)
- [Network Programming - RESTful APIs 사용하기](iOS-Networking/Network_RestfulAPI.md)
- [네트워킹 - 각종 URL의 유효성 검사](iOS-Networking/URL_ValidationCheck.md)
- [WebView - PC에서 사용중인 내부망을 Iphone으로 연결시키는 방법](iOS-Networking/WebViewZ_intranet.md)
- [WKWebView 사용하기, 구성 요소 살펴보기](iOS-Networking/WebView_00_INTRO.md)
- [WebView - 웹뷰에 스크립트를 적용시키는 방법](iOS-Networking/WebView_Adjust_Script.md)
- [WebView - 웹에서 앱으로 보내는 JavaScript 수신하기 : WKScriptMessageHandler](iOS-Networking/WebView_CatchingJS.md)
- [WebView - Delegate method](iOS-Networking/WebView_Delegate.md)
- [WebView - 앱에서 웹소스의 JavaScript 메서드 호출하기 : evaluateJavaScript()](iOS-Networking/WebView_Sending_JS.md)
- [WebView - App에서 웹페이지를 여는 3가지 방법](iOS-Networking/WebView_basic_use.md)
- [WebView - 네비게이션컨트롤러 목록으로 웹뷰 관리하는 방법](iOS-Networking/WebView_catchNavigation.md)
- [WebView - Safari로 웹뷰 디버깅하는 방법](iOS-Networking/WebView_commute_with_Web.md)
- [WebView - createWebViewWith : blank로 새창열기](iOS-Networking/WebView_createWebViewWith.md)
- [WebView - 자주 사용하는 메서드](iOS-Networking/WebView_often_use_delegate_method.md)
- [WebView - 스와이프로 리프레시 세팅](iOS-Networking/WebView_swipe_refresh.md)
- [webview - 바운스 효과 제거하기](iOS-Networking/Webview_how_to_stop_bounce.md)

### [iOS-RelatedImage](#ios-relatedimage)
- [dp와 pt에 대하여 (Feat. 포인트란)](iOS-RelatedImage/DP_PT.md)
- [화면캡처 - 특정화면을 이미지로 저장하기](iOS-RelatedImage/imageSave.md)
- [PNG와 JPG에 대하여](iOS-RelatedImage/png_jpg.md)

### [iOS-ScreenTranport](#ios-screentranport)
- [정리 : iOS에서의 화면관리 및 전환](iOS-ScreenTranport/A_Various_switchingScene.md)
- [기본적인 iOS 앱의 구조 / 탭바컨트롤러 / 네비게이션컨트롤러](iOS-ScreenTranport/Application_BasicStructure.md)
- [화면전환 - UINavigationController 이해하기](iOS-ScreenTranport/navigationController.md)
- [present - CodeUI to StoryBoard](iOS-ScreenTranport/presentCodeUIToStoryboard.md)
- [present - UIKit to SwiftUI](iOS-ScreenTranport/present_UIKitToSwiftUI.md)
- [Segue를 이용한 화면이동](iOS-ScreenTranport/segue.md)
- [Show는 push와 present의 추상화 메서드](iOS-ScreenTranport/showPushPresent.md)
- [화면전환 - UITabBarController 이해하기](iOS-ScreenTranport/tabbarController.md)

### [iOS-TDD](#ios-tdd)
- [Testable한 코드 만들기1 - VC -> MVC -> MVP](iOS-TDD/testable_mvc_mvp.md)

### [Mobile-Android](#mobile-android)
- [Android Studio 완전삭제](Mobile_02_Android/AndroidStudio_delete.md)
- [Android - Basic : 안드로이드의 기본 앱구조](Mobile_02_Android/Android_Basic_AppStructure.md)
- [Android - WebView : 앱에서 웹으로 JavaScript 보내기](Mobile_02_Android/Android_WebView_Sending_JS.md)

### [Mobile-Flutter](#mobile-flutter)
- [Flutter - 문서 구조 가이드](Mobile_03_Flutter/Flutter_0000_Document_Guide.md)
- [Flutter - 설치 및 환경 세팅 가이드](Mobile_03_Flutter/Flutter_0100_Setup.md)
- [Flutter - Splash 구현](Mobile_03_Flutter/Flutter_0271_SplashScreen_basic.md)
- [Flutter - 위젯 개요](Mobile_03_Flutter/Flutter_1000_Widget_Overview.md)
- [Flutter - 기본 위젯 4종 (Text, Icon, Image, Box)](Mobile_03_Flutter/Flutter_1001_Basic_4_Widget.md)
- [Flutter - 레이아웃의 이해](Mobile_03_Flutter/Flutter_1400_Widget_Layout_Guide.md)
- [Flutter - Drawer : GNB / 사이드바](Mobile_03_Flutter/Flutter_1410_Drawer.md)
- [Flutter - ListView](Mobile_03_Flutter/Flutter_1100_ListView.md)
- [Flutter - Toggle Switch](Mobile_03_Flutter/Flutter_1501_ToggleSwitch.md)
- [Flutter - 삼각형 View 그리기](Mobile_03_Flutter/Flutter_1990_View_Triangle.md)
- [Flutter - 네트워크 통신 기초 (RESTful API 중심)](Mobile_03_Flutter/Flutter_2000_Networking_Basics.md)
- [Flutter - 화면 전환(Navigator)](Mobile_03_Flutter/Flutter_4000_Navigator_Basics.md)
- [Flutter - 웹뷰구현 : inappwebview 세팅(권장)](Mobile_03_Flutter/Flutter_5011_WebView_inappwebview.md)
- [Flutter - 웹뷰구현 : webview_flutter 세팅](Mobile_03_Flutter/Flutter_5012_WebView_inappwebview.md)
- [Flutter – Flavor를 이용한 빌드 환경 분리](Flutter_6012_BuildFlavor_Setup_Guide.md)
- [Flutter - iOS 릴리즈 빌드 및 .ipa 생성](Flutter_6101_iOS_IPA_Build_Manual.md)
- [Flutter Error - Trouble Shooting Template](Mobile_03_Flutter/Flutter_8000_TroubleShoot_template.md)
- [Flutter Error - WebView_PlatformNotSet : WebViewPlatform.instance 오류](Mobile_03_Flutter/Flutter_8101_WebView_PlatformNotSet.md)
- [Flutter Error - WebView_NDKVersionMismatch : Android NDK 버전 불일치](Mobile_03_Flutter/Flutter_8102_WebView_NDKVersionMismatch.md)
- [Flutter Error - Entrypoint doesn't contain...](Mobile_03_Flutter/Flutter_8103_EntryPoint.md)

## [🌐 Web Development](#web-development)



## [Languages](#languages)

### [Lang-Ruby](#lang-ruby)
- [Install: Ruby](Lang-Ruby/Install_Ruby.md)
- [RubyGems - Package Manager :　gem 관리하기](Lang-Ruby/ManageGem.md)
- [Ruby - 버전관리 : RVM, Rbenv 사용법](Lang-Ruby/ManageRuby.md)

### [Lang-Swift](#lang-swift)
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


### [Lang-Dart](#ios-dart)
- [Flutter - Dart: Intro](Lang-Dart/Flutter_0000_Dart_Intro.md)



### [Docs](#docs)
- [마크다운 - HTML사용하기](Docs/Docs_MarkDown_CSS.md)
- [마크다운에서 Toggle(Expander control) 기능 사용하기](Docs/HTML_Toggle.md)
- [마크다운 - 이미지 사이즈 세팅하기](Docs/MarkDown_Image.md)
- [마크다운 - TOC기능 만들기 (Table Of Contents)](Docs/MarkDown_TOC.md)
- [마크다운 - 표 만들기 (Table)](Docs/MarkDown_Table.md)



### [Git](#git)
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
- [푸시 에러 : 원격 저장소와 커밋 기록이 다른 경우](Git/Git_pushError_OtherCommit.md)
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
