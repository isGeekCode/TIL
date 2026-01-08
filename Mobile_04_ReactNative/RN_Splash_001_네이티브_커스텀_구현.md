# React Native - Splash Screen 네이티브 커스텀 구현 (WebView 기반)

React Native WebView 기반 앱에서 복잡한 Splash Screen을 구현하는 방법입니다.
라이브러리로는 한계가 있는 커스텀 레이아웃을 네이티브에서 구현하고, WebView 로드 시점에 제어합니다.

## 전체 흐름

```
┌─────────────────────────────────────────────┐
│ 1. 앱 실행                                    │
│    ├─ iOS: LaunchScreen → SplashVC         │
│    └─ Android: MainActivity Splash Layout  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 2. React Native 부팅                         │
│    - JS Bundle 로드                         │
│    - WebView 컴포넌트 렌더링                  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 3. WebView 로드 시작 (onLoadStart)            │
│    → SplashModule.hide() 호출               │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 4. Native Module Bridge                      │
│    iOS: SplashModule.m → Swift              │
│    Android: SplashModule.kt                 │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 5. Native에서 Splash 제거                    │
│    - iOS: SplashVC dismiss                 │
│    - Android: Splash Layout 제거            │
└─────────────────────────────────────────────┘
```

---

## 문제 상황

### 라이브러리의 한계
- `react-native-splash-screen` 같은 라이브러리는 단순한 중앙 이미지만 가능
- iOS와 Android에서 동일한 복잡한 레이아웃 구현 불가능

### 실제 요구사항
고객사 요청:
- **중앙 로고**: 메인 브랜드 로고
- **하단 로고**: 파트너/제공사 로고
- **화면 비율 대응**: 다양한 디바이스 크기 자동 대응

→ **해결책: Native Module 직접 구현**

---

## React Native - WebView에서 Native Module 호출

### 1. WebView 로드 시작 시 Splash 숨김

```javascript
// App.js
import React from 'react';
import { NativeModules } from 'react-native';
import { WebView } from 'react-native-webview';

const { SplashModule } = NativeModules;

function App() {
  const handleLoadStart = () => {
    // WebView 로드가 시작되면 즉시 Splash 숨김
    SplashModule.hide();
  };

  return (
    <WebView
      source={{ uri: 'https://example.com' }}
      onLoadStart={handleLoadStart}  // ← 핵심!
      onLoad={() => console.log('WebView loaded')}
      onError={(error) => {
        console.error('WebView error:', error);
        SplashModule.hide();  // 에러 발생해도 Splash는 숨김
      }}
    />
  );
}

export default App;
```

**핵심 포인트:**
- `onLoadStart`: WebView가 로드를 **시작**할 때 호출 (빠른 반응)
- `SplashModule.hide()`: 네이티브 모듈 호출
- 에러 처리: WebView 로드 실패해도 Splash는 숨김

---

### 2. WebView 완전 로드 후 숨기기 (선택)

```javascript
// 웹 페이지가 완전히 로드된 후 숨기고 싶다면
function App() {
  const handleLoad = () => {
    // WebView 완전 로드 완료 시
    SplashModule.hide();
  };

  return (
    <WebView
      source={{ uri: 'https://example.com' }}
      onLoad={handleLoad}  // onLoadStart 대신 onLoad 사용
    />
  );
}
```

**차이점:**
- `onLoadStart`: 로드 시작 시 (빠름, 추천)
- `onLoad`: 완전 로드 완료 시 (느림, 페이지가 완전히 준비됨)

---

### 3. 타이밍 제어 (선택)

```javascript
// 최소 표시 시간 보장
const MINIMUM_SPLASH_TIME = 2000;  // 2초
let startTime = Date.now();

function App() {
  const handleLoadStart = () => {
    const elapsed = Date.now() - startTime;
    const remaining = Math.max(0, MINIMUM_SPLASH_TIME - elapsed);

    setTimeout(() => {
      SplashModule.hide();
    }, remaining);
  };

  return (
    <WebView
      source={{ uri: 'https://example.com' }}
      onLoadStart={handleLoadStart}
    />
  );
}
```

**사용 예:**
- 브랜드 로고를 최소 2초는 보여주고 싶을 때
- 너무 빨리 사라지는 것을 방지

---

### 4. 에러 처리

```javascript
function App() {
  const handleLoadStart = () => {
    // Module이 존재하는지 확인
    if (SplashModule && typeof SplashModule.hide === 'function') {
      SplashModule.hide();
    } else {
      console.error('SplashModule not found');
    }
  };

  const handleError = (syntheticEvent) => {
    const { nativeEvent } = syntheticEvent;
    console.error('WebView error:', nativeEvent);

    // 에러 발생해도 Splash는 숨김
    SplashModule?.hide();
  };

  return (
    <WebView
      source={{ uri: 'https://example.com' }}
      onLoadStart={handleLoadStart}
      onError={handleError}
    />
  );
}
```

---

## 네이티브 구현

React Native에서는 단순히 `SplashModule.hide()`를 호출하는 **인터페이스** 역할만 합니다.
실제 Splash 구현은 iOS와 Android 네이티브에서 이루어집니다.

### iOS 네이티브 구현

**상세 내용:**
- [iOS - WebView 앱 Splash Screen 커스텀 구현](../Mobile_01_iOS/iOS_Splash_WebView앱_커스텀구현.md)

**구현 요약:**
```
JavaScript: SplashModule.hide()
  ↓
Objective-C Bridge (SplashModule.m)
  ↓
Swift: SplashModule.hide()
  ↓
AppDelegate.hideSplashFromWebView()
  ↓
SplashViewController dismiss
```

**핵심 파일:**
- `SplashModule.swift`: Native Module
- `SplashModule.m`: Objective-C Bridge
- `SplashViewController.swift`: 복잡한 레이아웃 구현
- `AppDelegate.swift`: Splash 표시/숨김 관리

---

### Android 네이티브 구현

**상세 내용:**
- [Android - WebView 앱 Splash Screen 커스텀 구현](../Mobile_02_Android/aOS_Splash_WebView앱_커스텀구현.md)

**구현 요약:**
```
JavaScript: SplashModule.hide()
  ↓
SplashModule.kt
  ↓
MainActivity.hideSplash()
  ↓
Splash Layout 제거
```

**핵심 파일:**
- `SplashModule.kt`: Native Module
- `SplashPackage.kt`: Module 등록
- `MainActivity.kt`: Splash 표시/제거
- `res/layout/splash_screen.xml`: ConstraintLayout 레이아웃

**특징:**
- MainActivity에서 Splash를 띄워 Activity 전환 시 흰 화면 방지
- WebView 로드 시간 동안 Splash로 시간 벌기

---

## 핵심 포인트

### 1. React Native의 역할

**단순 인터페이스:**
```javascript
// React Native는 네이티브 모듈을 호출만 함
SplashModule.hide();
```

**실제 구현은 네이티브에서:**
- iOS: Swift + Objective-C
- Android: Kotlin

---

### 2. WebView 기반 앱의 특징

```javascript
// WebView 로드 시작 시점에 Splash 제거
<WebView
  onLoadStart={() => SplashModule.hide()}
/>
```

**타이밍:**
- `onLoadStart`: 로드 시작 (추천)
- `onLoad`: 완전 로드 완료
- `onLoadEnd`: 로드 종료 (성공/실패 모두)

---

### 3. Native가 UI 담당

- **iOS**: SplashViewController로 복잡한 레이아웃
- **Android**: ConstraintLayout으로 복잡한 레이아웃

**레이아웃 예시:**
```
┌─────────────────────────────┐
│                             │
│        ┌──────────┐         │
│        │ 중앙 로고 │         │ ← centerYAnchor / constraint center
│        └──────────┘         │
│                             │
│        ┌──────────┐         │
│        │ 하단 로고 │         │ ← bottomAnchor / constraint bottom
│        └──────────┘         │
└─────────────────────────────┘
```

---

### 4. 화면 비율 대응

- **iOS**: Auto Layout Constraints
- **Android**: ConstraintLayout

**장점:**
- 다양한 화면 크기 자동 대응
- iPhone SE부터 iPad까지
- 작은 Android 폰부터 태블릿까지

---

## iOS vs Android 차이점

| 구분 | iOS | Android |
|------|-----|---------|
| **Module** | Swift + Objective-C Bridge | Kotlin |
| **UI** | SplashViewController | Splash Layout (ConstraintLayout) |
| **표시** | Present/Dismiss | addView/removeView |
| **Thread** | DispatchQueue.main | runOnUiThread |
| **레이아웃** | Auto Layout | ConstraintLayout |
| **특징** | LaunchScreen → SplashVC 자연스러운 전환 | MainActivity에서 Splash 띄워 흰 화면 방지 |

---

## 실전 팁

### 1. 최소 표시 시간 보장

```javascript
// 너무 빨리 사라지지 않도록
const MINIMUM_SPLASH_TIME = 2000;
```

### 2. 에러 처리

```javascript
try {
  await initializeApp();
  SplashModule?.hide();  // undefined 체크
} catch (error) {
  console.error('Init failed:', error);
  SplashModule?.hide();  // 에러 발생해도 Splash는 숨김
}
```

### 3. 디버깅

```javascript
// Module이 제대로 등록됐는지 확인
console.log('SplashModule:', NativeModules.SplashModule);

// 메서드 확인
console.log('hide method:', typeof NativeModules.SplashModule?.hide);
```

### 4. TypeScript 사용 시

```typescript
// types/SplashModule.d.ts
declare module 'react-native' {
  interface NativeModulesStatic {
    SplashModule: {
      hide: () => void;
    };
  }
}
```

---

## 결론

**WebView 기반 RN 앱의 Splash는 Native Module로 직접 구현**

**React Native 역할:**
- `SplashModule.hide()` 호출 (인터페이스)
- `onLoadStart` 이벤트 활용

**네이티브 역할:**
- 실제 Splash UI 구현 (복잡한 레이아웃)
- 표시/숨김 로직
- 자연스러운 전환

**장점:**
- 라이브러리보다 **안정적**
- **커스터마이징** 자유로움
- 플랫폼별 최적화 가능

**다음 단계:**
1. [iOS 네이티브 구현 보기](../Mobile_01_iOS/iOS_Splash_WebView앱_커스텀구현.md)
2. [Android 네이티브 구현 보기](../Mobile_02_Android/aOS_Splash_WebView앱_커스텀구현.md)

---

## 관련 문서

- [iOS - WebView 앱 Splash Screen 커스텀 구현](../Mobile_01_iOS/iOS_Splash_WebView앱_커스텀구현.md)
- [Android - WebView 앱 Splash Screen 커스텀 구현](../Mobile_02_Android/aOS_Splash_WebView앱_커스텀구현.md)
- [RN - Native Module 이해하기](./RN_Native_001_Native_Module_이해하기.md)
