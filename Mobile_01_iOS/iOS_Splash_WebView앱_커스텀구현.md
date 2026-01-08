# iOS - WebView 기반 앱 Splash Screen 커스텀 구현

WebView 기반 앱(React Native WebView, Ionic 등)에서 복잡한 레이아웃의 Splash Screen을 네이티브로 구현하는 방법입니다.

## 문제 상황

### 라이브러리의 한계
- `react-native-splash-screen` 같은 라이브러리는 단순한 중앙 이미지만 가능
- 복잡한 레이아웃 구현 불가능

### 실제 요구사항
고객사 요청:
- **중앙 로고**: 메인 브랜드 로고
- **하단 로고**: 파트너/제공사 로고
- **화면 비율 대응**: 다양한 디바이스 크기 자동 대응

→ **해결책: SplashViewController + Native Module 직접 구현**

---

## 전체 흐름

```
앱 실행
  ↓
LaunchScreen (시스템)
  ↓
SplashViewController (네이티브)
  ↓
React Native 부팅 중...
  ↓
WebView 로드 시작
  ↓
JS에서 SplashModule.hide() 호출
  ↓
Objective-C Bridge (SplashModule.m)
  ↓
Swift SplashModule.hide() 실행
  ↓
AppDelegate.hideSplashFromWebView() 호출
  ↓
SplashViewController dismiss
```

---

## 구현 단계

### 1. SplashModule.swift 생성

React Native에서 호출할 Native Module을 만듭니다.

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

**핵심:**
- `@objc`: Objective-C에서 접근 가능하도록
- `DispatchQueue.main.async`: UI 작업은 메인 스레드에서
- `hideSplashFromWebView()`: 목적이 명확한 메서드명

---

### 2. SplashModule.m (Objective-C Bridge)

JavaScript와 Swift를 연결하는 브릿지입니다.

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
AppDelegate.hideSplashFromWebView()
```

---

### 3. AppDelegate.swift 수정

앱 시작 시 Splash를 띄우고, JavaScript에서 요청하면 숨깁니다.

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

**핵심 포인트:**
- `modalPresentationStyle = .fullScreen`: iOS 13+ 대응 (카드 모달 방지)
- `animated: false`: 자연스러운 전환 (LaunchScreen → Splash)
- `hideSplashFromWebView()`: WebView 전용 메서드명으로 목적 명확화

---

### 4. SplashViewController 구현

복잡한 레이아웃을 Auto Layout으로 구현합니다.

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

**레이아웃 구조:**
```
┌─────────────────────────────┐
│                             │
│                             │
│        ┌──────────┐         │
│        │          │         │
│        │ 중앙 로고 │         │ ← centerYAnchor
│        │          │         │
│        └──────────┘         │
│                             │
│                             │
│        ┌──────────┐         │
│        │ 하단 로고 │         │ ← bottomAnchor (safe area)
│        └──────────┘         │
└─────────────────────────────┘
```

---

### 5. LaunchScreen과 동일하게 유지

**LaunchScreen.storyboard 또는 .xib**도 동일한 레이아웃으로 구성하여
앱 실행 시 깜빡임 없이 자연스럽게 이어지도록 합니다.

**자연스러운 전환:**
```
LaunchScreen (시스템)
  ↓ (동일한 레이아웃)
SplashViewController (네이티브)
  ↓ (fade out)
WebView 화면
```

---

## 실전 팁

### 1. 안전 영역 고려

```swift
// Safe Area 사용 (iPhone X 이상 대응)
bottomLogo.bottomAnchor.constraint(
  equalTo: view.safeAreaLayoutGuide.bottomAnchor,
  constant: -20
)
```

### 2. 다크모드 대응

```swift
// 시스템 배경색 사용
view.backgroundColor = UIColor.systemBackground

// 또는 Asset Catalog에서 Color Set으로 관리
view.backgroundColor = UIColor(named: "SplashBackground")
```

**Assets.xcassets에서 Color Set 추가:**
- Light Mode: #FFFFFF
- Dark Mode: #000000

### 3. 이미지 해상도

**Assets.xcassets 구조:**
```
main_logo.imageset/
  ├─ main_logo@1x.png (보통 사용 안함)
  ├─ main_logo@2x.png (iPhone 8, XR 등)
  └─ main_logo@3x.png (iPhone 12 Pro 등)
```

### 4. 애니메이션 추가 (선택)

```swift
func hideSplashFromWebView() {
  UIView.animate(withDuration: 0.3, animations: {
    self.splashViewController?.view.alpha = 0
  }) { _ in
    self.splashViewController?.dismiss(animated: false) {
      self.splashViewController = nil
    }
  }
}
```

---

## JavaScript 연동

React Native WebView에서 호출하는 방법은 다음 문서를 참고하세요:

**관련 문서:**
- [React Native - WebView 앱 Splash 구현](../Mobile_04_ReactNative/RN_Splash_001_네이티브_커스텀_구현.md)

**간단 예시:**
```javascript
import { NativeModules } from 'react-native';
const { SplashModule } = NativeModules;

// WebView 로드 시작 시
SplashModule.hide();
```

---

## 주의사항

### 1. 메모리 관리

```swift
// dismiss 후 반드시 nil 처리
splashViewController?.dismiss(animated: true) {
  self.splashViewController = nil  // ← 메모리 해제
}
```

### 2. Thread Safety

```swift
// UI 작업은 항상 메인 스레드에서
DispatchQueue.main.async {
  appDelegate.hideSplashFromWebView()
}
```

### 3. 앱 시작 순서

```
1. application(_:didFinishLaunchingWithOptions:)
   ├─ React Native 초기화
   ├─ Window 설정
   └─ showSplash() 호출
2. LaunchScreen → SplashViewController 전환
3. React Native Bundle 로드
4. JavaScript 실행
5. WebView 컴포넌트 렌더링
6. onLoadStart → SplashModule.hide()
7. Splash 제거
```

---

## 디버깅

### Splash가 안 사라질 때

```swift
// SplashModule.swift에 로그 추가
func hide() {
  print("🔵 SplashModule.hide() called")
  DispatchQueue.main.async {
    guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {
      print("🔴 AppDelegate not found")
      return
    }
    print("🟢 Calling hideSplashFromWebView()")
    appDelegate.hideSplashFromWebView()
  }
}
```

### JavaScript에서 확인

```javascript
// Module이 제대로 등록됐는지 확인
console.log('SplashModule:', NativeModules.SplashModule);

// hide 호출
NativeModules.SplashModule?.hide();
```

---

## 요약

**iOS WebView 앱 Splash 구현:**

1. **SplashViewController**: 복잡한 레이아웃 구현 (중앙 + 하단 로고)
2. **SplashModule.swift**: Native Module 생성
3. **SplashModule.m**: Objective-C Bridge
4. **AppDelegate**: Splash 표시/숨김 관리
5. **JavaScript**: `SplashModule.hide()` 호출

**핵심:**
- Auto Layout으로 다양한 화면 크기 대응
- Objective-C Bridge로 JavaScript ↔ Swift 연결
- `hideSplashFromWebView()` 메서드명으로 목적 명확화
- LaunchScreen과 동일한 레이아웃으로 자연스러운 전환

이 방식이 라이브러리보다 **안정적**이고 **커스터마이징**이 자유롭습니다.
