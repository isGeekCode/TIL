# App 공통 기능: Splash Screen

## ✅ 개요
Splash Screen은 앱 실행 시 사용자에게 **가장 먼저 노출되는 화면**입니다.
앱의 **브랜드 아이덴티티를 전달하고**, 초기화 과정을 자연스럽게 감싸는 역할을 합니다.


<br><br>

---

## 🎯 목적 및 역할

| 역할 | 설명 |
|------|------|
| 로딩 중 사용자 이탈 방지 | 앱 초기 데이터 세팅 시간 동안 사용자에게 빈 화면 대신 안정적인 인상을 제공 |
| 브랜드 노출 | 로고, 색상, 모션 등을 통해 브랜드 인지도 강화 |
| 초기화 | 내부적으로 버전체크, 토큰 검사 등 사전 설정 로직 실행 가능 |

<br><br>

---

## 🧱 일반 구조

1. **App Launch → Splash Screen 표시**
2. 내부 초기화 로직 (예: 버전체크, 토큰 확인, 권한 체크 등)
3. 다음 화면(Navigation)으로 전환


<br><br>

---

## 📱 플랫폼별 기본 제공 방식

| 플랫폼 | 제공 방식 | 동적 Splash 지원 | 커스터마이징 방법 |
|---------|------------|-----------------|------------------|
| **iOS** | LaunchScreen.storyboard (정적) | 불가 (정적은 시스템 제어) | Xcode에서 설정 (정적), 동적 Splash가 필요할 경우 LaunchScreen과 동일한 모양의 ViewController를 직접 구성 |
| **Android** | theme 기반 SplashActivity (정적) | 가능 (Activity로 구현 가능) | `theme.splash` 또는 `SplashActivity`에서 설정 |
| **Flutter** | 별도 구현 필요 | 가능 (첫 화면에서 자유 구성) | `flutter_native_splash` 패키지 또는 커스텀 화면 구현 |

> 각 플랫폼은 시스템 차원에서 **정적 Splash**를 지원하며, **동적 Splash는 앱 내부에서 직접 구성**해야 합니다.


<br><br>

---

## 🌀 확장 예시

| 확장 기능 | 설명 |
|-----------|------|
| 버전체크 | 최소 버전 이상 여부 확인 후 업데이트 유도 |
| 다이나믹 이미지/영상 출력 | API로 받은 이미지 또는 동영상을 splash처럼 표시 |
| 애니메이션 | 로딩 중 애니메이션 또는 인터랙션 요소 삽입 |


<br><br>

---

## 🔗 연결 문서
- [Flutter 구현 보기](Mobile_03_Flutter/Flutter_0271_SplashScreen_basic.md)
- [iOS 구현 보기](Mobile_01_iOS/iOS_0001_SplashScreen.md) *(예정)*
- [Android 구현 보기](Mobile_02_Android/Android_0001_SplashScreen.md) *(예정)*



# 🟦 App 공통 기능: Splash Screen (개요)

## ✅ 정의
Splash Screen은 앱 실행 시 가장 먼저 사용자에게 노출되는 화면으로,  
앱의 브랜드 인식을 강화하고 초기 설정 또는 로딩 시간 동안 이탈을 방지하는 목적을 가집니다.

---

## 📌 역할 요약

| 역할 | 설명 |
|------|------|
| 사용자 이탈 방지 | 초기 로딩 시간 동안 사용자에게 안정적인 UX 제공 |
| 브랜드 노출 | 로고, 색상, 전용 애니메이션 등을 통해 브랜드 이미지 전달 |
| 초기화 처리 | 버전체크, 토큰 검사 등 앱 내부 설정 수행 가능 |

---

## 📱 플랫폼별 기본 동작 방식 (정리)

| 플랫폼 | 기본 제공 방식 | 동적 Splash 지원 | 비고 |
|--------|----------------|------------------|------|
| **iOS** | LaunchScreen.storyboard (정적) | ❌ 시스템 제어로 동적 불가 | 동적 처리는 ViewController 생성 필요 |
| **Android** | Android 12 이상: SplashScreen API (정적)<br>이하 버전: theme 기반 SplashActivity | ⭕ Activity로 커스터마이징 가능 | Android 12 이상은 아이콘 기반 splash 자동 제공 |
| **Flutter** | 별도 구현 필요 | ⭕ 첫 화면에서 자유 구현 가능 | `flutter_native_splash` 사용 가능 |

---

## 🌀 확장 사례 (문서별 설명 예정)

- 버전 체크 및 업데이트 유도
- 다이나믹 이미지 / 동영상 기반 스플래시
- 사용자 타입 분기 후 이동
- 애니메이션 또는 브랜드 모션 활용

---

## 🔗 구현 문서 (세부 내용은 아래에서 다룸)

- [공통 개념 정리 (이 문서)](./Mobile_common_001_splash.md)
- [Flutter 구현](../Mobile_03_Flutter/Flutter_0271_SplashScreen_basic.md)
- [iOS 구현](../Mobile_01_iOS/iOS_0001_SplashScreen.md) *(예정)*
- [Android 구현](../Mobile_02_Android/Android_0001_SplashScreen.md) *(예정)*
