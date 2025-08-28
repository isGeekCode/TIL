 # Flutter_0000_Document_Guide – 문서 구조 가이드


이 문서는 Flutter 학습 문서를 카테고리별로 정리하기 위한 번호 체계를 정의합니다.  

번호는 `0000`, `0100`, `0200`처럼 네 자리 숫자로 구분되며,  
README 정렬 및 검색 편의를 위해 사용됩니다.

<br><br>

---


## 📁 카테고리 번호 체계

| 번호     | 카테고리                                         | 설명                                                               |
| ------ | -------------------------------------------- | ---------------------------------------------------------------- |
| `0000` | [문서 구조 / 가이드 문서](#0000번대--문서-구조-및-가이드-문서)    | 이 문서 포함, 전체 구조 정의용 문서                                            |
| `0100` | [개발 환경 세팅 / 설치 / 시작](#0100번대--개발-환경-세팅--설치)  | Flutter 설치, IDE 설정, FVM 구성 등                                     |
| `0200` | [모바일 공통 기능](#0200번대--모바일-공통-기능)              | Splash 등                                                         |
| `1000` | [위젯 (Widgets)](#1000번대--위젯-widgets)          | 기본 UI 요소, 레이아웃, 입력 등 다양한 위젯                                      |
| `1300` | [라우팅 & 내비게이션](#1300번대--라우팅--내비게이션)           | 화면 전환, 탭바, 라우터 구성 등                                              |
| `2000` | [네트워크 & 비동기](#2000번대--네트워크--비동기)             | HTTP 요청, async/await, Dio 등                                      |
| `3000` | [데이터 유틸리티 정리](#3000번대--데이터-유틸리티-정리)          | JSON 파싱, 모델 변환, 포맷 유틸 함수 등 데이터 처리 중심                             |
| `4000` | [상태관리 / 앱 구조](#4000번대--상태관리--앱-구조)           | 상태 변경 흐름, setState, Provider 등 구성                                |
| `5000` | [플랫폼 기능 연동](#5000번대--플랫폼-기능-연동)              | WebView, 카메라, 갤러리, 공유, 푸시 알림, 위치 정보, 파일 접근 등 디바이스 연동 기능 및 패키지 활용 |
| `6000` | [배포 및 빌드 환경](#6000번대--배포-및-빌드-환경)            | iOS, Android 앱 배포를 위한 릴리즈 빌드, 서명, 업로드 가이드 등                      |
| `7000` | [앱 아키텍처](#7000번대--앱-아키텍처)                    | MVC, MVP, MVVM, 클린 아키텍처, 레이어 구성, DI 등                            |
| `8000` | [트러블슈팅 및 에러 정리](#8000번대--트러블슈팅-및-에러-정리)      | 기능/플러그인/OS 관련 에러 및 해결법 정리 전용 영역                                  |
| `9000` | [실험 / 기타](#9000번대--실험--기타)                   | 명확히 분류되지 않은 테스트 코드, 샌드박스, 일회성 정리 등                               |
|        | [학습 로드맵 가이드](#학습-로드맵-가이드)                    | 공식문서 기반 로드맵                                                      |

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

| 번호      | 설명                                                            |
| --------- | --------------------------------------------------------------- |
| `1000`    | 위젯 개요 (Widget 개념, 구조, 빌드 함수 등 기본 소개)           |
| 1-12      | Widget Catalog – 위젯 분류별 전체 목록                          |
| `1001`    | Basics – 가장 기초적인 위젯 구성 요소들 (Text, Button 등)       |
| `1001.01` | Drawer – Scaffold 내 사이드 내비게이션 메뉴 구성용 위젯         |
| `1002`    | Layout – 레이아웃 구성용 위젯 (Row, Column, Stack 등)           |
| `1002.01` | Single-child : Center                                           |
| `1002.21` | Multi-child : Column                                            |
| `1003`    | Text – 텍스트 표시 및 스타일링 관련 위젯                        |
| `1004`    | Input – 사용자 입력을 위한 위젯 (TextField, Button, Form 등)    |
| `1005`    | Assets, Images, and Icons – 이미지, 아이콘, 에셋 관련 구성 요소 |
| `1006`    | Scrolling – 스크롤 가능한 콘텐츠를 구성하는 위젯                |
| `1007`    | Interaction Models – 제스처 및 터치 반응 처리 위젯              |
| `1008`    | Styling – 테마, 반응형 구성, 패딩 등 스타일링 위젯              |
| `1009`    | Painting and Effects – 시각적 효과 및 그리기 관련 위젯          |
| `1010`    | Animation and Motion – 애니메이션 효과와 트랜지션 처리          |
| `1011`    | Async – 비동기 상태를 다루기 위한 위젯 (Future, Stream 등)      |
| `1012`    | Accessibility – 앱의 접근성을 향상시키는 도구 제공              |
| -         |                                                                 |
| `1150`    | Sliver – 고급 스크롤 레이아웃을 구성하는 Sliver 위젯 개요       |
| `1151`    | CustomScrollView – 여러 슬리버를 하나의 ScrollView로 결합       |
| `1152`    | SliverAppBar – 스크롤 시 접히는 AppBar 구성                     |
| `1153`    | SliverList & SliverGrid – 리스트/그리드형 스크롤 구성           |
| `1154`    | SliverToBoxAdapter – 일반 위젯을 Sliver에 포함시키기            |
| `1155`    | SliverFillRemaining – 스크롤 남은 공간을 채우는 위젯            |
| `1156`    | SliverPersistentHeader – 스크롤 고정 헤더 구성                  |
| `1159`    | Sliver 실전 예제 – 복합 Sliver UI 레이아웃 설계 실습            |


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
| `7000` | MVVM, 클린 아키텍처, 레이어 구성, DI 등 |

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


## 동시성 관련 로드맵

기초 (입문 · 핵심 개념)
- Flutter_2000.Networking.Basics.md → 네트워크 기초 
- Flutter_2001.Async.Overview.md → 비동기 개념 지도(Future/Stream/Isolate, 언제 무엇을 쓰나)
- Flutter_2001.1.Future.AsyncAwait.Basics.md → Future 기본, async/await 규칙, 반환 타입 정리
- Flutter_2002.Dio.Basics.md → Dio 기본
- Flutter_2003.Future.ThenVsAwait.md → then 체인 vs async/await 비교, 가독성/예외처리 차이
- Flutter_2004.Async.ErrorHandling.md → try/on/catch/finally, StackTrace, rethrow 패턴

응용 (패턴 · 실전 코드)
- Flutter_2004_Sequential_vs_Parallel.md — 순차(await) vs 병렬(Future.wait), 성능/주의점
- Flutter_2005_Stream_Basics.md — 단발성(Future) vs 다발성(Stream), await for, listen
- Flutter_2006_StreamController_Broadcast.md — StreamController, 단일/브로드캐스트, 변환(map, where)
- Flutter_2007_FutureBuilder_Recipes.md — FutureBuilder 상태 설계(로딩/성공/실패), 실수 패턴 교정
- Flutter_2008_StreamBuilder_Recipes.md — StreamBuilder 지속 업데이트 UI, 구독/해제 주의점
- Flutter_2009_EventLoop_Microtask.md — 이벤트 루프, microtask vs event queue, scheduleMicrotask

고급 (성능 · 구조 · 테스트)
- Flutter_2010_Timeout_Cancel_Retry.md — timeout, 취소 토큰(대안), 재시도(backoff) 패턴
- Flutter_2011_Async_in_Widget_Lifecycle.md — initState/dispose에서의 비동기, 메모리릭·race 방지
- Flutter_2012_Isolates_and_compute.md — Isolate/compute로 메인 스레드 블로킹 방지
- Flutter_2013_Async_Performance_Tips.md — jank 방지, 배치 처리, 디바운스/스로틀
- Flutter_2014_Testing_Async.md — 비동기 유닛/위젯 테스트, pump/pumpAndSettle, fake async

연계 (네트워크/상태관리)
- Flutter_2015_Dio_with_Async_Patterns.md — Dio + async 베스트 프랙티스(Interceptor/에러모델)
- Flutter_2016_Result_Either_ErrorModel.md — 성공/실패 타입 모델링(Result/Either) + UI 연동
- Flutter_2017_Async_with_Provider_Riverpod.md — FutureProvider/StreamProvider, cancel-safe 설계
- Flutter_2018_Async_File_IO.md — 파일 읽기/쓰기 비동기 패턴, isolate로 파싱 오프로딩
- Flutter_2019_Concurrency_Race_Conditions.md — 중복 클릭·중복 요청, 최신만 반영 패턴(switchMap 유사)

⸻

보조 링크(카탈로그 교차참조)
- 1011 Async 위젯과 상호 링크: FutureBuilder, StreamBuilder 문서는 1000번대(위젯 카탈로그)에도 요약 카드로 두고, 자세한 내용은 2007/2008로 점프하도록 앵커 연결.


## 동시성 로드맵 – 실행 가이드 (메타 + 체크박스 + 미션)

> 체크박스 상태: [ ] 예정  [~] 작성 중  [x] 완료

### 기초 (입문 · 핵심 개념)
- [ ] **Flutter_2000.Networking.Basics.md**
  - **목표**: HTTP/REST 개념, `http`/Dio 개요, JSON 구조(Map/List) 분기 이해
  - **키워드**: REST, HTTP 메서드, JSON, `http` 패키지
  - **예상소요**: 40m
  - **선행지식**: Dart 기본, 비동기 기초(Future 개념)
  - **실습(필수)**: JSON 객체/리스트 응답 각각 파싱, 상태코드 분기 처리
  - **실습(심화)**: 모델 `fromJson/toJson` 작성 후 리스트 매핑
  - **링크**: 2002 Dio Basics ↔ 3000 JSON 파싱, 2007 FutureBuilder

- [ ] **Flutter_2001.Async.Overview.md**
  - **목표**: Future/Stream/Isolate 개념 지도와 선택 기준 확립
  - **키워드**: 단발성/다발성, 메인스레드, 오프로딩
  - **예상소요**: 30m
  - **실습(필수)**: `Future.delayed(300ms)` → "hello" 로그  
  - **실습(심화)**: `Stream.periodic` 5회 카운트 → 콘솔  
  - **링크**: 2001.1 Async/Await Basics, 2005 Stream Basics(예고)

- [ ] **Flutter_2001.1.Future.AsyncAwait.Basics.md**
  - **목표**: async/await 규칙, `Future<T>` 반환/호출 패턴 이해
  - **키워드**: async 필요조건, await/then 비교, 불필요한 await
  - **예상소요**: 40m
  - **실습(필수)**: `Future<int>` 500ms 뒤 42 리턴 → 버튼 클릭 출력
  - **실습(심화)**: try/catch로 실패 흐름 가짜 처리
  - **링크**: 2007 FutureBuilder, 2003 ThenVsAwait

- [ ] **Flutter_2002.Dio.Basics.md**
  - **목표**: Dio 기본 사용(GET/POST), BaseOptions, LogInterceptor, 커스텀 Interceptor, 싱글턴
  - **키워드**: Dio, BaseOptions, InterceptorsWrapper, LogInterceptor, Singleton
  - **예상소요**: 60m
  - **실습(필수)**: `GET /images/search` 1·5건 호출 후 URL 추출
  - **실습(심화)**: `ApiClient` 싱글턴으로 공통 헤더·타임아웃 구성, 로그 커스터마이즈
  - **링크**: 2015 Dio with Async Patterns, 2007 FutureBuilder

- [ ] **Flutter_2003.Future.ThenVsAwait.md**
  - **목표**: then 체인 vs await 가독성/예외 처리 비교
  - **키워드**: 콜백 체인, catchError, 가독성
  - **예상소요**: 25m
  - **실습(필수)**: 동일 기능을 then/await 2버전으로 작성, 로그 순서 비교
  - **실습(심화)**: 에러 발생 시 두 방식의 스택트레이스 차이 캡처

- [ ] **Flutter_2004.Async.ErrorHandling.md**
  - **목표**: try/on/catch/finally, rethrow, StackTrace
  - **키워드**: 도메인에러→UI메시지 매핑
  - **예상소요**: 35m
  - **실습(필수)**: `risky()`에서 Exception 던지고 UI에 안전 표시  
  - **실습(심화)**: `finally`에서 로딩 off 보장하는 미니 헬퍼

---

### 응용 (패턴 · 실전 코드)

- [ ] **Flutter_2004_Sequential_vs_Parallel.md**
  - **목표**: 순차(await 체인) vs 병렬(Future.wait) 체감
  - **벤치마크**: `DateTime.now()`로 총 소요 로그
  - **실습(필수)**: 500ms/700ms 작업 순차 vs 병렬 시간 비교
  - **실습(심화)**: 일부 실패 시 부분성공 전략(성공만 필터)

- [ ] **Flutter_2005_Stream_Basics.md**
  - **목표**: Future↔Stream 차이, await for, listen
  - **실습(필수)**: 300ms 간격 카운터 1..5 `await for` 출력
  - **실습(심화)**: `listen`으로 구독 시작/해제 버튼

- [ ] **Flutter_2006_StreamController_Broadcast.md**
  - **목표**: 단일 vs broadcast, 변환(map, where)
  - **실습(필수)**: Controller → 두 위젯 동시 구독
  - **실습(심화)**: `where`로 짝수만 UI 반영

- [ ] **Flutter_2007_FutureBuilder_Recipes.md**
  - **목표**: 로딩/성공/실패 3상태 안전 패턴
  - **안티패턴**: `future` 재생성, 빌드 내 무한 재호출 방지
  - **실습(필수)**: 성공/실패 토글되는 목 API로 카드 UI

- [ ] **Flutter_2008_StreamBuilder_Recipes.md**
  - **목표**: 실시간 업데이트/구독수명 관리
  - **실습(필수)**: 타이머 스트림 + 일시정지/재개
  - **주의**: dispose에서 구독 해제

- [ ] **Flutter_2009_EventLoop_Microtask.md**
  - **목표**: event queue vs microtask, scheduleMicrotask
  - **실습(필수)**: `print` 순서 실험(then vs scheduleMicrotask)

---

### 고급 (성능 · 구조 · 테스트)

- [ ] **Flutter_2010_Timeout_Cancel_Retry.md**
  - **목표**: timeout, 취소(대안), 지수 백오프
  - **실습(필수)**: `Future.any`/타임아웃 가드

- [ ] **Flutter_2011_Async_in_Widget_Lifecycle.md**
  - **목표**: initState/dispose 중 비동기 안전처리
  - **실습(필수)**: mounted 체크, late cancel 패턴

- [ ] **Flutter_2012_Isolates_and_compute.md**
  - **목표**: compute/Isolate로 무거운 파싱 오프로딩
  - **벤치마크**: 메인 프레임 드랍 vs 오프로딩 비교

- [ ] **Flutter_2013_Async_Performance_Tips.md**
  - **목표**: jank 방지, 디바운스/스로틀/배치
  - **실습(필수)**: 입력 디바운스 검색 리스트

- [ ] **Flutter_2014_Testing_Async.md**
  - **목표**: fakeAsync, pump/pumpAndSettle
  - **실습(필수)**: FutureBuilder 위젯테스트

---

### 연계 (네트워크/상태관리)

- [ ] **Flutter_2015_Dio_with_Async_Patterns.md**
  - **목표**: Interceptor, 공통 에러모델, 재시도
  - **실습(필수)**: 성공/실패/타임아웃 3케이스 UI 바인딩

- [ ] **Flutter_2016_Result_Either_ErrorModel.md**
  - **목표**: 성공/실패 타입(Result/Either)로 UI 단순화
  - **실습(필수)**: `when(success:..., failure:...)` 렌더

- [ ] **Flutter_2017_Async_with_Provider_Riverpod.md**
  - **목표**: FutureProvider/StreamProvider, cancel-safe
  - **실습(필수)**: 탭 전환 중 중복요청 차단

- [ ] **Flutter_2018_Async_File_IO.md**
  - **목표**: 파일 IO 비동기 + isolate 파싱
  - **실습(필수)**: 대용량 JSON 파싱 오프로딩

- [ ] **Flutter_2019_Concurrency_Race_Conditions.md**
  - **목표**: 최신값만 반영(switchLatest 유사), 중복 클릭 방지
  - **실습(필수)**: 빠른 연타에도 마지막 요청만 UI 반영


<br><br>


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
            - 3.1.1.1. Introduction
            - 3.1.1.2. Think declaratively
            - 3.1.1.3. Ephemeral vs app state
            - 3.1.1.4. Simple app state management
            - 3.1.1.5. Options
        - 3.1.2. Networking & http
            - 3.1.2.1. Overview
            - 3.1.2.2. Fetch data from the internet
            - 3.1.2.3. Make authenticated requests
            - 3.1.2.4. Send data  to the internet
            - 3.1.2.5. update data over the internet
            - 3.1.2.6. Dele data on ther internet
            - 3.1.2.7. Communicate with WebSockets
        - 3.1.3. Serialization
            - 3.1.3.1. JSON serialization
            - 3.1.3.2. Parse JSON in the background
        - 3.1.4. Persistence
            - 3.1.4.1. Store key-value data on disk
            - 3.1.4.2. Read and write files
            - 3.1.4.3. Persist data with SQList
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


### 카테고리 분류

| 아이콘 | 설명                     | 비고 |
|--------|--------------------------|------|
| 📘     | Dart 문법 및 기본 구조      | 변수, 제어문, 클래스, async 등 |
| 🎨     | UI 구성 / 위젯           | Layout, Sliver, Text 등        |
| 🧠     | 상태관리 / 앱 구조        | setState, Provider, MVVM 등    |
| 🧭     | 라우팅 & 내비게이션       | Navigator, go_router 등        |
| 🖱️     | 입력 / 제스처            | TextField, Form, Gesture 등    |
| 🌐     | 네트워크 / 비동기 처리    | Dio, Future, JSON 등           |
| 💾     | 저장소 / 로컬 데이터      | SharedPreferences 등           |
| 🔌     | 플랫폼 연동 기능          | WebView, Push, 권한 등         |
| 🔍     | 앱 정보 / 시스템 인터페이스 | 앱 버전, OS 정보 등            |
| 📷     | 카메라 / 스캔 기능        | QR/Barcode 스캐너 등           |
| 💬     | 로컬라이징 / 언어 설정        | intl, 다국어 대응              |

### 로드맵
| TIL | BLOG | CATE | LEV |  소단계  |           학습 포인트            |                   실습 예제                    |                          관련 위젯 / 키워드                          |
| :-: | :--: | :--: | :-: | :---: | :-------------------------: | :----------------------------------------: | :-----------------------------------------------------------: |
|  ✅  |  ✅   |  📘  |  1  |  1.1  |     Dart - 변수 선언과 타입 이해     |                                            |                       var, final, const                       |
|  ✅  |  ✅   |  📘  |  1  |  1.2  |      Dart - 제어문과 흐름 제어      |      if/else, switch, for, while 반복문       |                        if, switch, for                        |
|  ✅  |  ✅   |  📘  |  1  |  1.3  |      Dart - 함수 정의 및 활용      |            기본 함수, 람다식, 매개변수 전달             |                        함수, 파라미터, 익명함수                         |
|  ❌  |  ❌   |  📘  |  1  |  1.4  |       Dart - 클래스와 생성자       |            class, 생성자, this 키워드            |                   class, constructor, this                    |
|  ✅  |  ✅   |  🎨  |  1  |  1.5  |     Flutter 프로젝트 구조 이해      |     main.dart 분석, MaterialApp 구조 살펴보기      |                 runApp, Widget, BuildContext                  |
|  ❌  |  ❌   |  📘  |  2  |  2.0  |      Dart - 상속과 추상 클래스      |          extends, abstract 클래스 실습          |                   abstract, super, extends                    |
|  ✅  |  ✅   |  🎨  |  2  |  2.1  |          위젯 개념 입문           |       Text, Icon, ElevatedButton 배치        |                 StatelessWidget, Build method                 |
|  ✅  |  ✅   |  🎨  |  2  |  2.2  |           레이아웃 기초           | Row, Column, Center, Padding, SizedBox 연습  |                 MainAxisAlignment, SizedBox 등                 |
|  ✅  |  ❌   |  🎨  |  2  |  2.3  |           레이아웃 실전           |                아이폰 설정앱 클론코딩                |                   Container, BoxDecoration                    |
|  ✅  |  ❌   |  🎨  |  2  | 2.35  |      SafeArea와 상태바 처리       |      기기별 상태바 영역 대응을 위해 SafeArea 사용 실습      |                     SafeArea, MediaQuery                      |
|  ❌  |  ❌   |  🎨  |  2  |  2.4  |         앱 아이콘 설정 실습         |            native 프로젝트에 아이콘 지정             |                    flutter_launcher_icons                     |
|  ❌  |  ❌   |  🎨  |  2  |  2.5  |         스플래시 화면 구현          |           native 프로젝트에 런치이미지 구성            |                 flutter_native_splash, Timer                  |
|  ❌  |  ❌   |  🎨  |  2  |  2.6  |        다크모드 & 테마 구성         |         라이트/다크모드 토글 및 ThemeData 적용         |                ThemeData, ThemeMode, Provider                 |
|  ✅  |  ✅   |  🧠  |  3  |  3.0  |         App의 시작 흐름          |            main함수로 시작하여 첫화면 띄우기            |               main,   MaterialApp, CupertinoApp               |
|  ✅  |  ✅   |  🧠  |  3  |  3.1  |        상태관리 기본 구조 이해        |            Stateless 와 Stateful            |                      setState, initState                      |
|  ✅  |  ✅   |  🧠  |  3  | 3.11  |   StatefulWidget 생명주기 이해    | initState, build, dispose 등의 호출 순서와 역할 이해  | createState, initState, didChangeDependencies, build, dispose |
|  ✅  |  ✅   |  🧠  |  3  | 3.12  |        상태관리 기본 구조 이해        |         StatefulWidget의 LifeCycle          |                      setState, initState                      |
|  ❌  |  ❌   |  🧠  |  3  |  3.2  |          상태 변경 실습           |              버튼 클릭 시 텍스트 변경하기              |                ElevatedButton, Text, setState                 |
|  ❌  |  ❌   |  🧠  |  3  |  3.3  |            도전과제             |               내부 변수로 배경색 바꾸기               |                    Color, Container, 변수 제어                    |
|  ✅  |  ✅   |  🧭  |  4  |  4.1  |          네비게이션 1.0          |          Navigator.push()로 화면 이동           |                 Navigator, MaterialPageRoute                  |
|  ❌  |  ❌   |  🧭  |  4  |  4.2  |          네비게이션 2.0          |          Navigator 2.0 방식 이해와 비교           |                 Page, RouteInformationParser                  |
|  ❌  |  ❌   |  🧭  |  4  |  4.3  |        go_router 실습         |          go_router로 로그인 → 홈 화면 이동          |                           go_router                           |
|  ✅  |  ❌   |  🧭  |  4  |  4.4  |       조건부 다이얼로그 네비게이션       |      AlertDialog에서 OK 누르면 첫 화면으로 pop       |                AlertDialog, Navigator.popUntil                |
|  ❌  |  ❌   |  🧭  |  4  |  4.5  |    Drawer를 활용한 사이드 메뉴 구성    |    Scaffold의 drawer 속성과 ListTile 구성 방식     |                       Drawer, Scaffold                        |
|  ❌  |  ❌   |  🧭  |  4  |  4.5  |   BottomNavigationBar 구성    |     하단 탭 UI와 탭 유지 전략 (IndexedStack 등)      |                 BottomNavigationBar, Scaffold                 |
|  ❌  |  ❌   |  🧭  |  4  |  4.5  |          TabBar 구성          |   TabController와 TabBarView를 활용한 상단 탭 구성   |          TabBar, TabController, DefaultTabController          |
|  ❌  |  ❌   |  🧠  |  5  |  5.1  |         상태관리 중급: 콜백         |                부모 위젯에 콜백 전달                |                   Function 타입, callback 구조                    |
|  ❌  |  ❌   |  🧠  |  5  |  5.2  |     InheritedWidget 이해      |                색상 테마 위젯 만들기                |                 of(context), InheritedWidget                  |
|  ❌  |  ❌   |  🧠  |  5  |  5.3  |          위젯 생성자 활용          |           생성자 통해 초기값 전달 및 조건 분기            |                   required, final, this.변수명                   |
|  ❌  |  ❌   | 🖱️  |  6  |  6.1  |        사용자 입력 기초 개념         |              입력 필드 만들고 값 출력하기              |                     TextField, onChanged                      |
|  ❌  |  ❌   | 🖱️  |  6  |  6.2  |           제스처 입력            |            스와이프, 탭 등 UX 제스처 테스트            |                 GestureDetector, Dismissible                  |
|  ❌  |  ❌   |  🎨  |  6  | 6.25  |     SnackBar와 Toast 알림      |           사용자 동작에 따른 피드백 메시지 띄우기           |                ScaffoldMessenger, fluttertoast                |
|  ❌  |  ❌   |  📘  |  6  |  6.3  |       Dart - 예외 처리 문법       |      try/catch, throw, finally 기본 구조       |                  try, catch, throw, finally                   |
|  ❌  |  ❌   |  🌐  |  7  |  7.0  |     Dart - 비동기 프로그래밍 기초     |    Future, async/await, Stream 개념 및 실습     |                 Future, async, await, Stream                  |
|  ❌  |  ❌   |  🌐  |  7  |  7.1  |           네트워크 요청           |            Dio로 GET 요청, JSON 보기            |                        Dio, jsonDecode                        |
|  ❌  |  ❌   |  🌐  |  7  |  7.2  |      HTTP CRUD 흐름 익히기       |     Create, Read, Update, Delete 버튼 구현     |                      Dio, PATCH, DELETE                       |
|  ❌  |  ❌   |  📘  |  8  |  8.1  |         JSON 직렬화 기초         |        User 모델 만들기, fromJson/toJson        |                       fromJson, toJson                        |
|  ❌  |  ❌   |  🌐  |  8  |  8.2  |    FutureBuilder로 UI 바인딩    |          API 요청 결과를 ListView로 출력           |                FutureBuilder, ListView.builder                |
|  ❌  |  ❌   |  🌐  |  8  |  8.3  |       다이나믹 스플래시 화면 구현       |         API로 받은 이미지 URL로 splash 구성         |           Dio, Image.network, FutureBuilder, Timer            |
|  ❌  |  ❌   | 🖱️  |  9  |  9.1  |     사용자 입력 심화 - 텍스트 그룹      |        TextField, Form, RichText 조합        |                  Form, GlobalKey, validator                   |
|  ❌  |  ❌   | 🖱️  |  9  |  9.2  |        입력 위젯 - 옵션 그룹        |       DropdownMenu, Slider, Chip 실습        |                value, onChanged, group widgets                |
|  ❌  |  ❌   | 🖱️  |  9  |  9.3  |         입력 위젯 - 토글류         |        Checkbox, Switch, Radio 등 실습        |                   onChanged, value, toggle                    |
|  ❌  |  ❌   |  🎨  |  9  |  9.4  |          설정 페이지 구현          |        SwitchListTile로 사용자 설정 화면 구성        |               SwitchListTile, ListView, Divider               |
|  ❌  |  ❌   |  🎨  |  9  | 9.41  |      설정 페이지에 프로필 사진 표시      |             원형 이미지로 사용자 아바타 표시             |               CircleAvatar, Image.asset/network               |
|  ❌  |  ❌   |  🔍  |  9  | 9.42  |       앱 버전 및 기기 정보 표시       |         앱의 버전, OS 정보 등을 설정 페이지에 표시         |              package_info_plus, device_info_plus              |
|  ❌  |  ❌   |  💾  |  9  | 9.43  |           로컬 저장소            |       SharedPreferences로 간단한 데이터 저장        |                      getString, setBool                       |
|  ❌  |  ❌   |  💾  |  9  | 9.44  |        설정 상태 저장 및 복원        |               앱 재실행 시 설정 유지                |                SharedPreferences, async/await                 |
|  ❌  |  ❌   |  🎨  |  9  | 9.45  |      회원번호 바코드 생성 및 표시       |        사용자 고유 ID를 바코드 이미지로 변환하여 표시         |               flutter_barcode_sdk, qr_flutter 등               |
|  ❌  |  ❌   |  🔌  |  9  | 9.46  |        내 정보 공유 기능 구현        |         바코드 + ID를 캡처하거나 공유하기 기능 구현         |                 Share, ScreenshotController 등                 |
|  ❌  |  ❌   |  💾  |  9  | 9.47  |        내 친구 보기 기능 구현        |          설정 페이지에서 친구 목록 리스트 확인 가능          |             ListView, SharedPreferences, local DB             |
|  ❌  |  ❌   |  📷  |  9  | 9.48  |     친구 추가 - 바코드 스캐너 구현      |        친구 바코드를 스캔하여 회원번호를 친구 목록에 저장        |             qr_code_scanner, flutter_barcode_sdk              |
|  ❌  |  ❌   |  💾  |  9  | 9.49  |       친구 목록 영구 저장 처리        | 앱 삭제 후에도 유지되도록 로컬 DB 또는 secure storage 사용  |                SharedPreferences, sqlite, hive                |
|  ❌  |  ❌   |  💬  |  9  |  9.5  |        언어/다국어 설정 지원         |          앱 내 언어 변경 및 intl 로케일 적용           |                  intl, flutter_localizations                  |
|  ❌  |  ❌   | 🖱️  |  9  |  9.6  |          날짜/시간 입력           |     DatePickerDialog, TimePickerDialog     |                   showDatePicker, DateTime                    |
|  ❌  |  ❌   |  📘  | 10  | 10.0  |     Dart - 캡슐화와 접근 제어자      |         private, getter/setter 실습          |                         `_`, get, set                         |
|  ❌  |  ❌   |  🧠  | 10  | 10.1  |        상태관리 심화 - 구조화        |        ChangeNotifier + Provider 기초        |                notifyListeners, context.watch                 |
|  ❌  |  ❌   |  🧠  | 10  | 10.2  |        ValueNotifier        |               UI 자동 갱신 상태 감시               |             ValueNotifier, ValueListenableBuilder             |
|  ❌  |  ❌   |  🎨  | 10  | 10.3  |      Sliver로 설정 페이지 구현      | 기존 설정 UI를 SliverList/SliverAppBar로 변환하여 구성 |          CustomScrollView, SliverList, SliverAppBar           |
|  ❌  |  ❌   |  🧠  | 10  | 10.35 |        가벼운 상태 분리 예제         |      숫자 증가 버튼 만들기: UI와 로직을 파일로 분리해보기       |                            구조 나누기                             |
|  ❌  |  ❌   |  🧠  | 10  | 10.4  |         MVVM 구조 맛보기         |         ViewModel 분리, Provider 바인딩         |                      Provider, Consumer                       |
|  ❌  |  ❌   |  🧠  | 10  | 10.5  |          설정 상태 관리           |     Provider, ChangeNotifier로 설정 상태 관리     |                Provider, ChangeNotifier, 상태저장                 |
|  ❌  |  ❌   |  🧠  | 11  | 11.1  |     상태관리 심화 - Provider      |        ChangeNotifier + Provider 기초        |                notifyListeners, context.watch                 |
|  ❌  |  ❌   |  🧠  | 12  | 12.1  |         Riverpod 기초         |      ref.watch로 상태 관찰, StateProvider       |                flutter_riverpod, ProviderScope                |
|  ❌  |  ❌   |  🧠  | 12  | 12.2  |          파생 상태 관리           |        FutureProvider, Computed 구성         |               ref.read, ref.watch, async/await                |
|  ❌  |  ❌   |  🧠  | 12  | 12.3  |          상태 공유/모듈화          |            여러 화면에서 상태 공유 및 리팩터링            |                  ref.listen, ConsumerWidget                   |
|  ❌  |  ❌   |  🧠  | 12  | 12.4  |   Provider → Riverpod 전환    |            기존 Provider 예제 리팩터링             |                    리팩터링 전략, best practice                     |
|  ❌  |  ❌   |  🔌  | 13  | 13.1  |         푸시 알림 기초 세팅         |        Firebase Messaging 연동, 권한 요청        |                   firebase_messaging, 권한 처리                   |
|  ❌  |  ❌   |  🔌  | 13  | 13.2  |        푸시 알림 수신 및 처리        |       Foreground/Background 알림 구분 처리       |                onMessage, onBackgroundMessage                 |
|  ❌  |  ❌   |  🔌  | 13  | 13.3  |       알림 클릭 시 라우팅 처리        |             알림 클릭 → 특정 페이지 이동              |                initialMessage, push navigation                |
|  ❌  |  ❌   |  🔌  | 14  | 14.1  |        WebView 기본 구성        |          웹 페이지를 띄우는 WebView 화면 구성          |                InAppWebView, initialUrlRequest                |
|  ❌  |  ❌   |  🔌  | 14  | 14.2  |      WebView 설정 커스터마이징      |        자바스크립트 허용, 유저에이전트 등 세부 옵션 구성        |                  settings, javaScriptEnabled                  |
|  ❌  |  ❌   |  🔌  | 14  | 14.3  |       WebView 히스토리 제어       |         뒤로 가기 버튼으로 WebView 히스토리 제어         |                canGoBack, goBack, WillPopScope                |
|  ❌  |  ❌   |  🔌  | 14  | 14.4  |   자바스크립트 → Flutter 메시지 수신   |    JS에서 메시지 전송 → Flutter에서 메시지 수신 및 처리     |           addJavaScriptHandler, onJsMessageReceived           |
|  ❌  |  ❌   |  🔌  | 14  | 14.5  |          커스텀 스킴 처리          |        웹 링크 내 커스텀 스킴 감지하여 특정 동작 수행         |            shouldOverrideUrlLoading, custom scheme            |
|  ❌  |  ❌   |  🔌  | 14  | 14.6  |          새 창 열기 처리          |       `target="_blank"` 등 새 창 요청 대응        |                        onCreateWindow                         |
|  ❌  |  ❌   |  🔌  | 14  | 14.7  |      푸시 링크로 WebView 열기      |         푸시 알림 클릭 시 링크로 WebView 열기          |              initialMessage, WebView navigation               |
|  ❌  |  ❌   |  🔌  | 14  | 14.8  |      설정에서 푸시 허용 여부 동기화      |    설정 스위치로  푸시 허용 여부 조작 + 시스템 푸시 권한  반영    |    SwitchListTile, firebase_messaging, permission_handler     |
|  ❌  |  ❌   |  🔌  | 14  | 14.9  |     Flutter → JS 메시지 전송     |           Flutter 코드에서 JS 함수 호출            |             evaluateJavascript, WebViewController             |
|  ❌  |  ❌   |  🔌  | 14  | 14.10 |    JS Channel 양방향 통신 정리     |      JS → Flutter, Flutter → JS 콜백 흐름      |               callHandler, addJavaScriptHandler               |
|  ❌  |  ❌   |  🔌  | 14  | 14.11 |          로딩 진행률 표시          |        웹 페이지 로딩 상태를 ProgressBar로 표현        |          onProgressChanged, LinearProgressIndicator           |
|  ❌  |  ❌   |  🔌  | 14  | 14.12 |          에러 페이지 대응          |            페이지 로드 실패 시 에러 화면 표시            |                 onLoadError, onLoadHttpError                  |
|  ❌  |  ❌   |  🔌  | 14  | 14.13 |          파일 업로드 처리          |            웹에서 파일 업로드 input 대응             |             androidOnShowFileChooser, file picker             |
|  ❌  |  ❌   |  🔌  | 14  | 14.14 |     Pull to Refresh 구성      |           페이지를 아래로 당겨 새로고침 기능 구현           |                    pullToRefreshController                    |
|  ❌  |  ❌   |  🔌  | 15  | 15.1  |          애플 로그인 연동          |         Apple Sign-In 구현, 권한 요청 처리         |                      sign_in_with_apple                       |
|  ❌  |  ❌   |  🔌  | 15  | 15.2  |         카카오 로그인 연동          |      Kakao SDK 로그인, 토큰 → Firebase 커넥팅      |               kakao_flutter_sdk, firebase_auth                |
|  ❌  |  ❌   |  🔌  | 15  | 15.3  |         네이버 로그인 연동          |       Naver Login SDK 활용, 사용자 정보 처리        |                  naver_login, firebase_auth                   |
|  ❌  |  ❌   |  🔌  | 15  | 15.4  |   구글 로그인 연동 (Firebase 기반)   |      GoogleSignIn 플러그인 + Firebase 연동       |                 firebase_auth, google_sign_in                 |
|  ❌  |  ❌   |  🔌  | 15  | 15.5  | Firebase Authentication 로그인 |             이메일 로그인 흐름, 권한 처리              |                         firebase_auth                         |
|  ❌  |  ❌   |  🔌  | 15  | 15.6  |      Remote Config 구성       |          앱 기능 동적 제어 (예: 버튼 숨기기 등)          |                    firebase_remote_config                     |
|  ❌  |  ❌   |  🔌  | 15  | 15.7  |      Crashlytics 에러 추적      |            예외 발생 시 자동 리포팅 흐름 구성            |                     firebase_crashlytics                      |
|  ❌  |  ❌   |  🔌  | 15  | 15.8  |    Firebase Analytics 적용    |             사용자 이벤트 추적 및 분석 설정             |                 firebase_analytics, logEvent                  |
|  ❌  |  ❌   |  🔌  | 15  | 15.9  |     Firestore 데이터베이스 기초     |           문서/컬렉션 구조 만들기, CRUD 실습           |                     cloud_firestore, CRUD                     |
|  ❌  |  ❌   |  🔌  | 15  | 15.10 |    Firebase Storage 업로드     |            이미지/파일 업로드 & 다운로드 흐름            |                   firebase_storage, 이미지 업로드                   |
|  ❌  |  ❌   |  🔌  | 15  | 15.11 |    결제 연동 (WebView 스킴 처리)    |         웹에서 결제 연동 또는 전용 페이지 이동 처리          |        shouldOverrideUrlLoading, intent scheme, 결제 URL        |
