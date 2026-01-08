# React Native - Splash Screen 네이티브 커스텀 구현 (WebView 기반)

React Native WebView 기반 앱에서 Splash Screen을 Native Module로 제어하는 방법입니다.

## 개요

WebView 기반 앱에서는 복잡한 Splash Screen 구현을 위해 네이티브 모듈을 직접 연동합니다.

**전체 흐름:**
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

## Part 1: React Native - WebView에서 Native Module 호출

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

### 5. TypeScript 사용 시

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

## Part 2: iOS Native Module 구현

React Native와 iOS를 연결하는 Bridge를 구현합니다.

### 1. SplashModule.swift 생성

```swift
// SplashModule.swift
import Foundation
import React

@objc(SplashModule)
class SplashModule: NSObject {

  @objc
  func hide() {
    DispatchQueue.main.async {
      guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {
        return
      }
      // AppDelegate의 hideSplash 호출
      appDelegate.hideSplash()
    }
  }

  @objc
  static func requiresMainQueueSetup() -> Bool {
    return true
  }
}
```

**핵심:**
- `@objc`: Objective-C에서 접근 가능하도록
- `DispatchQueue.main.async`: UI 작업은 메인 스레드에서
- `appDelegate.hideSplash()`: 실제 Splash 제거 로직 호출

---

### 2. SplashModule.m (Objective-C Bridge)

```objective-c
// SplashModule.m
#import <React/RCTBridgeModule.h>

@interface RCT_EXTERN_MODULE(SplashModule, NSObject)

RCT_EXTERN_METHOD(hide)

@end
```

**Bridge 역할:**
```
JavaScript: SplashModule.hide()
  ↓
Objective-C Bridge (SplashModule.m)
  ↓
Swift: SplashModule.hide()
  ↓
AppDelegate.hideSplash()
```

---

### iOS 네이티브 UI 구현

실제 Splash UI 구현 (SplashViewController, AppDelegate 등)은 별도 문서 참고:

**상세 내용:**
- [iOS - 스플래시 화면 구현 가이드 § 4. WebView 앱 스플래시 구현](../Mobile_01_iOS/iOSCommon_001.SplashScreen.md#4-webview-앱-스플래시-구현-react-native-ionic-등)

**구현 내용:**
- SplashViewController (복잡한 레이아웃)
- AppDelegate 연동 (showSplash/hideSplash)
- NIB/Storyboard vs 코드 구현
- LaunchScreen 연동

---

## Part 3: Android Native Module 구현

React Native와 Android를 연결하는 Native Module을 구현합니다.

### 1. SplashModule.kt 생성

```kotlin
// SplashModule.kt
package com.myapp

import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod

class SplashModule(reactContext: ReactApplicationContext) :
    ReactContextBaseJavaModule(reactContext) {

    override fun getName(): String {
        return "SplashModule"
    }

    @ReactMethod
    fun hide() {
        val activity = currentActivity as? MainActivity
        activity?.runOnUiThread {
            activity.hideSplash()
        }
    }
}
```

**핵심:**
- `@ReactMethod`: JavaScript에서 호출 가능한 메서드
- `runOnUiThread`: UI 작업은 메인 스레드에서
- `MainActivity.hideSplash()`: 실제 Splash 제거 로직 호출

---

### 2. SplashPackage.kt

```kotlin
// SplashPackage.kt
package com.myapp

import com.facebook.react.ReactPackage
import com.facebook.react.bridge.NativeModule
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.uimanager.ViewManager

class SplashPackage : ReactPackage {
    override fun createNativeModules(reactContext: ReactApplicationContext):
        List<NativeModule> {
        return listOf(SplashModule(reactContext))
    }

    override fun createViewManagers(reactContext: ReactApplicationContext):
        List<ViewManager<*, *>> {
        return emptyList()
    }
}
```

---

### 3. MainApplication.kt 등록

```kotlin
// MainApplication.kt
class MainApplication : Application(), ReactApplication {

  override fun getPackages(): List<ReactPackage> {
    return PackageList(this).packages.apply {
      // SplashPackage 추가
      add(SplashPackage())
    }
  }
}
```

---

### Android 네이티브 UI 구현

실제 Splash UI 구현 (MainActivity, Layout 등)은 별도 문서 참고:

**상세 내용:**
- [Android - 스플래시 화면 구현 가이드 § 4. WebView 앱 스플래시 구현](../Mobile_02_Android/aOS_0271_SplashScreen.md#4-webview-앱-스플래시-구현-react-native-ionic-등)

**구현 내용:**
- MainActivity에서 Splash 띄우기 (흰 화면 방지)
- ConstraintLayout 복잡한 레이아웃
- ViewModel 아키텍처 패턴 (MainVM + SplashUseCase)
- 실전 팁 (다크모드, 애니메이션 등)

---

## 핵심 포인트

### 1. React Native의 역할

**단순 인터페이스:**
```javascript
// React Native는 네이티브 모듈을 호출만 함
SplashModule.hide();
```

**실제 구현은 네이티브에서:**
- iOS: Swift + Objective-C Bridge
- Android: Kotlin Module

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

### 3. Bridge 구조

**iOS:**
```
JavaScript
  ↓
SplashModule.m (Objective-C Bridge)
  ↓
SplashModule.swift
  ↓
AppDelegate.hideSplash()
```

**Android:**
```
JavaScript
  ↓
SplashModule.kt
  ↓
MainActivity.hideSplash()
```

---

## 실전 팁

### 1. 디버깅

```javascript
// Module이 제대로 등록됐는지 확인
console.log('SplashModule:', NativeModules.SplashModule);

// 메서드 확인
console.log('hide method:', typeof NativeModules.SplashModule?.hide);
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

### 3. 최소 표시 시간 보장

```javascript
const MINIMUM_SPLASH_TIME = 2000;
```

---

## 결론

**WebView 기반 RN 앱의 Splash는 Native Module로 직접 구현**

**React Native 역할:**
- `SplashModule.hide()` 호출 (인터페이스)
- `onLoadStart` 이벤트 활용
- Bridge를 통한 네이티브 연동

**네이티브 역할:**
- 실제 Splash UI 구현 (복잡한 레이아웃)
- 표시/숨김 로직
- 자연스러운 전환

**장점:**
- 라이브러리보다 **안정적**
- **커스터마이징** 자유로움
- 플랫폼별 최적화 가능

---

## 관련 문서

- [iOS - 스플래시 화면 구현 가이드](../Mobile_01_iOS/iOSCommon_001.SplashScreen.md)
- [Android - 스플래시 화면 구현 가이드](../Mobile_02_Android/aOS_0271_SplashScreen.md)
