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
│ 4. Objective-C Bridge                        │
│    SplashModule.m → hideSplashFromWebView() │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 5. Native에서 Splash 제거                    │
│    - iOS: SplashVC dismiss                 │
│    - Android: Splash Layout 제거            │
└─────────────────────────────────────────────┘
```

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
```

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

### 3. 타이밍 제어 (선택)

```javascript
// 최소 표시 시간 보장
const MINIMUM_SPLASH_TIME = 2000;
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

---

## Part 2: iOS Native 구현

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
      // AppDelegate의 hideSplashFromWebView 호출
      appDelegate.hideSplashFromWebView()
    }
  }

  @objc
  static func requiresMainQueueSetup() -> Bool {
    return true
  }
}
```

### 2. SplashModule.m (Objective-C Bridge)

```objective-c
// SplashModule.m
#import <React/RCTBridgeModule.h>

@interface RCT_EXTERN_MODULE(SplashModule, NSObject)

RCT_EXTERN_METHOD(hide)

@end
```

**Bridge 역할:**
- JavaScript `SplashModule.hide()` 호출
- → Objective-C Bridge (SplashModule.m)
- → Swift 메서드 실행 (SplashModule.swift)
- → AppDelegate의 `hideSplashFromWebView()` 호출

### 3. AppDelegate.swift 수정

```swift
// AppDelegate.swift
import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

  var window: UIWindow?
  var splashViewController: SplashViewController?

  func application(_ application: UIApplication,
                  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    // React Native 초기화
    let bridge = RCTBridge(delegate: self, launchOptions: launchOptions)
    let rootView = RCTRootView(bridge: bridge!, moduleName: "MyApp", initialProperties: nil)

    let rootViewController = UIViewController()
    rootViewController.view = rootView

    self.window = UIWindow(frame: UIScreen.main.bounds)
    self.window?.rootViewController = rootViewController
    self.window?.makeKeyAndVisible()

    // Splash 표시
    showSplash()

    return true
  }

  func showSplash() {
    splashViewController = SplashViewController()

    if let rootVC = window?.rootViewController {
      splashViewController?.modalPresentationStyle = .fullScreen
      rootVC.present(splashViewController!, animated: false)
    }
  }

  // WebView에서 호출되는 메서드
  func hideSplashFromWebView() {
    splashViewController?.dismiss(animated: true) {
      self.splashViewController = nil
    }
  }
}
```

### 4. SplashViewController 구현

```swift
// SplashViewController.swift
import UIKit

class SplashViewController: UIViewController {

  override func viewDidLoad() {
    super.viewDidLoad()
    setupUI()
  }

  private func setupUI() {
    view.backgroundColor = .white

    // 중앙 로고
    let centerLogo = UIImageView(image: UIImage(named: "main_logo"))
    centerLogo.contentMode = .scaleAspectFit
    centerLogo.translatesAutoresizingMaskIntoConstraints = false
    view.addSubview(centerLogo)

    // 하단 로고
    let bottomLogo = UIImageView(image: UIImage(named: "partner_logo"))
    bottomLogo.contentMode = .scaleAspectFit
    bottomLogo.translatesAutoresizingMaskIntoConstraints = false
    view.addSubview(bottomLogo)

    // Auto Layout
    NSLayoutConstraint.activate([
      // 중앙 로고
      centerLogo.centerXAnchor.constraint(equalTo: view.centerXAnchor),
      centerLogo.centerYAnchor.constraint(equalTo: view.centerYAnchor),
      centerLogo.widthAnchor.constraint(equalToConstant: 200),
      centerLogo.heightAnchor.constraint(equalToConstant: 200),

      // 하단 로고
      bottomLogo.centerXAnchor.constraint(equalTo: view.centerXAnchor),
      bottomLogo.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor, constant: -20),
      bottomLogo.heightAnchor.constraint(equalToConstant: 40)
    ])
  }
}
```

### 5. LaunchScreen과 동일하게 유지

**LaunchScreen.storyboard 또는 .xib**도 동일한 레이아웃으로 구성하여
앱 실행 시 깜빡임 없이 자연스럽게 이어지도록 합니다.

---

## Part 3: Android Native 구현

### 왜 MainActivity에서 Splash를 띄우는가?

**일반적인 Android 앱:**
```
SplashActivity (Splash 표시)
  ↓
MainActivity (메인 화면)
```

**하지만 WebView 기반 RN 앱의 문제:**
```
SplashActivity 종료
  ↓
MainActivity 시작
  ↓
WebView 로드 중... 😱 흰 화면 깜빡임 발생!
  ↓
WebView 로드 완료
```

**해결: MainActivity에서 즉시 Splash를 띄우기**
```
MainActivity onCreate()
  ↓
즉시 Splash Layout을 ContentView 위에 추가
  ↓
(뒤에서 WebView 로드 진행 중...)
  ↓
WebView onLoadStart → Splash 제거
```

**장점:**
- ✅ **흰 화면 방지**: WebView 로드 중에도 Splash가 보임
- ✅ **시간 벌기**: WebView 로드는 시간이 걸림 (네트워크 요청)
- ✅ **자연스러운 전환**: 깜빡임 없이 Splash → WebView
- ✅ **로직 추가 가능**: Activity 생명주기에서 제어 가능

**핵심:**
- SplashActivity를 별도로 두면 Activity 전환 시 흰 화면 발생
- MainActivity에서 바로 Splash를 올리면 WebView 로드 동안 시간 벌기 가능

### ViewModel 아키텍처 패턴

**전통적인 방식: SplashVM + MainVM 분리**
```
MainActivity
  ├─ SplashViewModel (Splash 로직)
  └─ MainViewModel (메인 로직)
```

**최근 권장 방식: MainVM 내부에 SplashUseCase**
```
MainActivity
  └─ MainViewModel
       ├─ SplashUseCase (Splash 관련 로직)
       └─ 기타 UseCase들
```

**MainVM + SplashUseCase 방식이 더 나은 이유:**
- ✅ **단일 책임**: MainActivity는 하나의 ViewModel만 관리
- ✅ **응집도**: Splash는 Main 화면의 일부 → UseCase로 관리하는 것이 자연스러움
- ✅ **생명주기 관리 단순화**: ViewModel 하나만 observe하면 됨
- ✅ **테스트 용이**: UseCase 단위로 테스트 가능

**참고:** 별도 SplashVM을 두는 경우도 있지만, Splash가 단순히 "로딩 상태"라면 UseCase로 분리하는 것이 더 깔끔합니다.

---

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

### 4. Splash Layout 생성

```xml
<!-- res/layout/splash_screen.xml -->
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/splashLayout"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/white">

    <!-- 중앙 로고 -->
    <ImageView
        android:id="@+id/centerLogo"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:src="@drawable/main_logo"
        android:contentDescription="@string/main_logo"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />

    <!-- 하단 로고 -->
    <ImageView
        android:id="@+id/bottomLogo"
        android:layout_width="wrap_content"
        android:layout_height="40dp"
        android:src="@drawable/partner_logo"
        android:contentDescription="@string/partner_logo"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        android:layout_marginBottom="20dp" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

### 5. MainActivity.kt 구현

```kotlin
// MainActivity.kt
package com.myapp

import android.os.Bundle
import android.view.View
import android.view.ViewGroup
import com.facebook.react.ReactActivity
import com.facebook.react.ReactActivityDelegate
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint
import com.facebook.react.defaults.DefaultReactActivityDelegate

class MainActivity : ReactActivity() {

    private var splashView: View? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        showSplash()
    }

    private fun showSplash() {
        splashView = layoutInflater.inflate(R.layout.splash_screen, null)

        val rootView = findViewById<ViewGroup>(android.R.id.content)
        rootView.addView(splashView)
    }

    fun hideSplash() {
        splashView?.let { view ->
            val rootView = findViewById<ViewGroup>(android.R.id.content)
            rootView.removeView(view)
            splashView = null
        }
    }

    override fun getMainComponentName(): String = "MyApp"

    override fun createReactActivityDelegate(): ReactActivityDelegate =
        DefaultReactActivityDelegate(this, mainComponentName, DefaultNewArchitectureEntryPoint.fabricEnabled)
}
```

---

## 핵심 포인트

### 1. WebView 기반 앱의 특징
```javascript
// WebView 로드 시작 시점에 Splash 제거
<WebView
  onLoadStart={() => SplashModule.hide()}
/>
```

### 2. Objective-C Bridge를 통한 호출
```
JavaScript (RN)
  ↓
SplashModule.m (Objective-C Bridge)
  ↓
SplashModule.swift
  ↓
AppDelegate.hideSplashFromWebView()
  ↓
SplashViewController dismiss
```

### 3. Native가 UI 담당
- **iOS**: SplashViewController로 복잡한 레이아웃
- **Android**: ConstraintLayout으로 복잡한 레이아웃

### 4. 화면 비율 대응
- **iOS**: Auto Layout Constraints
- **Android**: ConstraintLayout

### 5. 자연스러운 전환
- LaunchScreen → SplashVC: 동일한 레이아웃으로 깜빡임 없음
- MainActivity: ContentView에 Splash 추가/제거

---

## iOS vs Android 차이점

| 구분 | iOS | Android |
|------|-----|---------|
| **Module** | Swift + Objective-C Bridge | Kotlin |
| **UI** | SplashViewController | Splash Layout (ConstraintLayout) |
| **표시** | Present/Dismiss | addView/removeView |
| **Thread** | DispatchQueue.main | runOnUiThread |
| **레이아웃** | Auto Layout | ConstraintLayout |

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

### 3. 안전 영역 고려
- **iOS**: safeAreaLayoutGuide 사용
- **Android**: 하단 Navigation Bar 고려

### 4. 다크모드 대응
```swift
// iOS
view.backgroundColor = UIColor.systemBackground

// 또는 Asset Catalog에서 Color Set으로 관리
```

```xml
<!-- Android -->
<!-- res/values-night/colors.xml -->
<color name="splash_background">#000000</color>
```

---

## 결론

**WebView 기반 RN 앱의 Splash는 Native Module로 직접 구현**

1. **WebView 로드 시작** 시점에 `SplashModule.hide()` 호출
2. **Objective-C Bridge** 통해 네이티브 메서드 호출
3. iOS: `hideSplashFromWebView()` / Android: `hideSplash()`
4. 복잡한 레이아웃(중앙 + 하단 로고)은 네이티브로 구현

**핵심:**
- WebView 기반 앱은 `onLoadStart` 이벤트 활용
- Bridge 구조: JS → Objective-C (.m) → Swift
- 메서드 명명: `hideSplashFromWebView` (목적이 명확)

이 방식이 라이브러리보다 **안정적**이고 **커스터마이징**이 자유롭습니다.

---

## 관련 문서

- [iOS - Splash Screen 구현](../../Mobile_01_iOS/iOS_Splash_구현.md) (예정)
- [Android - Splash Screen 구현](../../Mobile_02_Android/Android_Splash_구현.md) (예정)
- [RN - Native Module 이해하기](./RN_Native_001_Native_Module_이해하기.md)
