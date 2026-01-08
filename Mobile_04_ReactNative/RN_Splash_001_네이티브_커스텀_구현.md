# React Native - Splash Screen 네이티브 커스텀 구현

React Native에서 복잡한 Splash Screen을 구현하려면 Native Module을 직접 만들어야 합니다.
라이브러리로는 한계가 있는 커스텀 레이아웃을 네이티브에서 구현하고, RN에서 제어하는 방식입니다.

## 전체 흐름

```
┌─────────────────────────────────────────────┐
│ 1. 앱 실행                                    │
│    ├─ iOS: LaunchScreen → SplashVC         │
│    └─ Android: MainActivity Splash Layout  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 2. React Native 부팅 시작                    │
│    - JS Bundle 로드                         │
│    - 컴포넌트 초기화                          │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 3. RN 부팅 완료 후 호출                       │
│    SplashModule.hide()                      │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 4. Native에서 Splash 제거                    │
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

## Part 1: React Native - Native Module 호출

### 1. Native Module 인터페이스 사용

```javascript
// App.js
import React, { useEffect } from 'react';
import { NativeModules } from 'react-native';

const { SplashModule } = NativeModules;

function App() {
  useEffect(() => {
    // 앱 초기화 작업
    initializeApp().then(() => {
      // 초기화 완료 후 Splash 숨김
      SplashModule.hide();
    });
  }, []);

  const initializeApp = async () => {
    // API 호출, 데이터 로드 등
    await fetchInitialData();
    await loadUserSettings();
  };

  return (
    // 앱 컴포넌트
  );
}
```

### 2. 타이밍 제어

```javascript
// 최소 2초는 보여주기
const MINIMUM_SPLASH_TIME = 2000;

useEffect(() => {
  const startTime = Date.now();

  initializeApp().then(() => {
    const elapsed = Date.now() - startTime;
    const remaining = Math.max(0, MINIMUM_SPLASH_TIME - elapsed);

    setTimeout(() => {
      SplashModule.hide();
    }, remaining);
  });
}, []);
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
      appDelegate.hideSplash()
    }
  }

  @objc
  static func requiresMainQueueSetup() -> Bool {
    return true
  }
}
```

### 2. SplashModule.m (Bridge)

```objective-c
// SplashModule.m
#import <React/RCTBridgeModule.h>

@interface RCT_EXTERN_MODULE(SplashModule, NSObject)

RCT_EXTERN_METHOD(hide)

@end
```

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

  func hideSplash() {
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

### 1. RN은 제어만 담당
```javascript
// RN의 역할: 타이밍만 제어
SplashModule.hide();  // "이제 숨겨!"
```

### 2. Native가 UI 담당
- **iOS**: SplashViewController로 복잡한 레이아웃
- **Android**: ConstraintLayout으로 복잡한 레이아웃

### 3. 화면 비율 대응
- **iOS**: Auto Layout Constraints
- **Android**: ConstraintLayout

### 4. 자연스러운 전환
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

**복잡한 Splash는 Native Module로 직접 구현**

1. RN에서 `SplashModule.hide()` 호출
2. iOS/Android 각각 Native Module 구현
3. 복잡한 레이아웃은 네이티브로 구현
4. RN 부팅 완료 후 제어권은 RN이 가짐

이 방식이 라이브러리보다 **안정적**이고 **커스터마이징**이 자유롭습니다.

---

## 관련 문서

- [iOS - Splash Screen 구현](../../Mobile_01_iOS/iOS_Splash_구현.md) (예정)
- [Android - Splash Screen 구현](../../Mobile_02_Android/Android_Splash_구현.md) (예정)
- [RN - Native Module 이해하기](./RN_Native_001_Native_Module_이해하기.md)
