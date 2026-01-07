# RN_Native_001_Native_Module_이해하기

## 🤔 이 문서를 읽기 전에
- **선수 지식**: React Native 기본, WebView 이해
- **예상 소요 시간**: 50분
- **준비물**: Android Studio, Xcode (실습 시)

## 🎯 이 문서에서 배울 것
1. Native Module이 무엇이고 왜 필요한지
2. Android (Kotlin)로 Native Module 만들기
3. iOS (Objective-C)로 Native Module 만들기
4. JavaScript에서 Native Module 호출하기
5. SplashModule 실전 분석

---

## 📖 본문

### 1. Native Module이 뭐야?

#### 한 줄 요약
**"JavaScript에서 네이티브 코드(Android/iOS)를 직접 호출할 수 있게 해주는 다리"**

#### 왜 필요한가?

React Native는 대부분의 기능을 제공하지만, 다음과 같은 경우 **네이티브 코드가 반드시 필요**합니다:

**1. React Native에 없는 기능**
```
❌ React Native에 없는 것들:
- 스플래시 화면 제어
- 생체 인증 (지문, Face ID)
- 카메라 커스터마이징
- 블루투스, NFC
- 앱 설정 변경
```

**2. 성능이 중요한 작업**
```
✅ 네이티브로 하면 더 빠른 것들:
- 이미지 처리 (필터, 압축)
- 대량 데이터 처리
- 암호화/복호화
- 센서 데이터 실시간 처리
```

**3. 플랫폼별 고유 기능**
```
iOS 전용:
- Apple Pay
- HealthKit

Android 전용:
- Google Play Billing
- Android Auto
```

---

### 2. Native Module 통신 구조

```
┌─────────────────────────────────────────────┐
│         JavaScript (React Native)            │
│                                              │
│  import { NativeModules } from 'react-native'│
│  NativeModules.SplashModule.hide();          │
└──────────────────┬──────────────────────────┘
                   │
                   │ React Native Bridge
                   │
     ┌─────────────┴──────────────┐
     │                            │
     ↓                            ↓
┌─────────────────┐   ┌──────────────────────┐
│  Android (Kotlin)│   │   iOS (Objective-C)  │
│                  │   │                      │
│  @ReactMethod    │   │  RCT_EXPORT_METHOD   │
│  fun hide() {    │   │  hide() {            │
│    // 네이티브   │   │    // 네이티브       │
│    // 코드 실행  │   │    // 코드 실행      │
│  }               │   │  }                   │
└──────────────────┘   └──────────────────────┘
```

---

## 3. Android Native Module 만들기

### 3.1 SplashModule 전체 코드 (Kotlin)

```kotlin
// android/app/src/main/java/com/example/myapp/SplashModule.kt

package com.example.myapp

import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.bridge.ReactContextBaseJavaModule
import com.facebook.react.bridge.ReactMethod

/**
 * React Native Bridge Module - Splash Screen 제어
 */
class SplashModule(reactContext: ReactApplicationContext)
    : ReactContextBaseJavaModule(reactContext) {

  private val appContext: ReactApplicationContext = reactContext

  /**
   * 1. 모듈 이름 정의
   * JavaScript에서 NativeModules.SplashModule로 접근
   */
  override fun getName(): String {
    return "SplashModule"
  }

  /**
   * 2. JavaScript에서 호출 가능한 메서드
   * @ReactMethod 어노테이션 필수!
   */
  @ReactMethod
  fun hide() {
    val activity = appContext.currentActivity as? MainActivity
    activity?.runOnUiThread {
      activity.hideSplashFromWebView()
    }
  }
}
```

### 3.2 Package 등록 (Kotlin)

```kotlin
// android/app/src/main/java/com/example/myapp/SplashPackage.kt

package com.example.myapp

import com.facebook.react.ReactPackage
import com.facebook.react.bridge.NativeModule
import com.facebook.react.bridge.ReactApplicationContext
import com.facebook.react.uimanager.ViewManager

/**
 * Native Module을 React Native에 등록하는 패키지
 */
class SplashPackage : ReactPackage {
  override fun createNativeModules(reactContext: ReactApplicationContext): List<NativeModule> {
    return listOf(SplashModule(reactContext))
  }

  override fun createViewManagers(reactContext: ReactApplicationContext): List<ViewManager<*, *>> {
    return emptyList()
  }
}
```

### 3.3 Application에 패키지 추가

```kotlin
// android/app/src/main/java/com/example/myapp/MainApplication.kt

class MainApplication : Application(), ReactApplication {

  override val reactNativeHost: ReactNativeHost =
    object : DefaultReactNativeHost(this) {
      override fun getPackages(): List<ReactPackage> =
        PackageList(this).packages.apply {
          // 여기에 커스텀 패키지 추가!
          add(SplashPackage())
        }
    }
}
```

---

## 4. iOS Native Module 만들기

### 4.1 헤더 파일 (Objective-C)

```objective-c
// ios/MyApp/SplashModule.h

#import <React/RCTBridgeModule.h>
#import <UIKit/UIKit.h>

/**
 * React Native Bridge Module - Splash Screen 제어 (iOS)
 */
@interface SplashModule : NSObject <RCTBridgeModule>
@end
```

### 4.2 구현 파일 (Objective-C)

```objective-c
// ios/MyApp/SplashModule.m

#import "SplashModule.h"
#import "MyApp-Swift.h"  // Swift 클래스 사용을 위한 자동 생성 헤더

@implementation SplashModule

/**
 * 1. 모듈 등록
 * JavaScript에서 NativeModules.SplashModule로 접근
 */
RCT_EXPORT_MODULE();

/**
 * 2. JavaScript에서 호출 가능한 메서드
 * RCT_EXPORT_METHOD 매크로 사용
 */
RCT_EXPORT_METHOD(hide)
{
  // UI 작업은 메인 스레드에서 실행
  dispatch_async(dispatch_get_main_queue(), ^{
    AppDelegate *appDelegate = (AppDelegate *)[[UIApplication sharedApplication] delegate];
    [appDelegate hideSplashFromWebView];
  });
}

/**
 * 3. 모듈 초기화 시 메인 큐 사용 여부
 */
+ (BOOL)requiresMainQueueSetup
{
  return NO;  // 백그라운드 스레드에서 초기화
}

@end
```

### 4.3 Swift와 Objective-C 브릿징

만약 AppDelegate가 Swift로 작성되어 있다면:

```swift
// ios/MyApp/AppDelegate.swift

@objc class AppDelegate: UIResponder, UIApplicationDelegate {

  // Objective-C에서 호출 가능하도록 @objc 표시
  @objc func hideSplashFromWebView() {
    UIView.animate(withDuration: 0.3, animations: {
      splashView?.alpha = 0
    }) { _ in
      splashView?.removeFromSuperview()
    }
  }
}
```

---

## 5. JavaScript에서 사용하기

### 5.1 기본 사용법

```typescript
// src/screens/WebShell.tsx

import { NativeModules } from 'react-native';

// 1. NativeModules에서 가져오기
const { SplashModule } = NativeModules;

// 2. 메서드 호출
if (SplashModule) {
  SplashModule.hide();
}
```

### 5.2 실전 사용 (WebView onLoadStart)

```typescript
// src/screens/WebShell.tsx

<WebView
  ref={ref}
  source={{ uri: START_URL }}
  onLoadStart={() => {
    setLoading(true);
    setErrorMsg(null);

    // 네이티브 스플래시 숨김 (Android & iOS)
    if (NativeModules.SplashModule) {
      NativeModules.SplashModule.hide();
    }
  }}
  ...
/>
```

### 5.3 TypeScript 타입 정의

```typescript
// src/types/nativeModules.d.ts

interface SplashModuleInterface {
  hide: () => void;
}

declare module 'react-native' {
  interface NativeModulesStatic {
    SplashModule: SplashModuleInterface;
  }
}
```

---

## 6. 파라미터와 콜백

### 6.1 파라미터 받기

**Android (Kotlin):**
```kotlin
@ReactMethod
fun showAlert(title: String, message: String) {
  val activity = appContext.currentActivity
  activity?.runOnUiThread {
    AlertDialog.Builder(activity)
      .setTitle(title)
      .setMessage(message)
      .setPositiveButton("확인", null)
      .show()
  }
}
```

**iOS (Objective-C):**
```objective-c
RCT_EXPORT_METHOD(showAlert:(NSString *)title message:(NSString *)message)
{
  dispatch_async(dispatch_get_main_queue(), ^{
    UIAlertController *alert = [UIAlertController
      alertControllerWithTitle:title
      message:message
      preferredStyle:UIAlertControllerStyleAlert];

    [alert addAction:[UIAlertAction
      actionWithTitle:@"확인"
      style:UIAlertActionStyleDefault
      handler:nil]];

    [rootViewController presentViewController:alert animated:YES completion:nil];
  });
}
```

**JavaScript:**
```typescript
NativeModules.AlertModule.showAlert('제목', '메시지 내용');
```

---

### 6.2 콜백으로 결과 받기

**Android (Kotlin):**
```kotlin
import com.facebook.react.bridge.Callback

@ReactMethod
fun getDeviceInfo(callback: Callback) {
  val deviceInfo = HashMap<String, String>()
  deviceInfo["model"] = android.os.Build.MODEL
  deviceInfo["version"] = android.os.Build.VERSION.RELEASE

  callback.invoke(deviceInfo)
}
```

**iOS (Objective-C):**
```objective-c
RCT_EXPORT_METHOD(getDeviceInfo:(RCTResponseSenderBlock)callback)
{
  NSDictionary *deviceInfo = @{
    @"model": [[UIDevice currentDevice] model],
    @"version": [[UIDevice currentDevice] systemVersion]
  };

  callback(@[deviceInfo]);
}
```

**JavaScript:**
```typescript
NativeModules.DeviceModule.getDeviceInfo((info: any) => {
  console.log('모델:', info.model);
  console.log('버전:', info.version);
});
```

---

### 6.3 Promise로 결과 받기 (권장!)

**Android (Kotlin):**
```kotlin
import com.facebook.react.bridge.Promise

@ReactMethod
fun getUserLocation(promise: Promise) {
  try {
    // 위치 조회 (간소화)
    val location = getCurrentLocation()

    val result = HashMap<String, Double>()
    result["latitude"] = location.latitude
    result["longitude"] = location.longitude

    promise.resolve(result)
  } catch (e: Exception) {
    promise.reject("LOCATION_ERROR", e.message)
  }
}
```

**iOS (Objective-C):**
```objective-c
RCT_REMAP_METHOD(getUserLocation,
                 resolver:(RCTPromiseResolveBlock)resolve
                 rejecter:(RCTPromiseRejectBlock)reject)
{
  @try {
    CLLocation *location = [self getCurrentLocation];

    NSDictionary *result = @{
      @"latitude": @(location.coordinate.latitude),
      @"longitude": @(location.coordinate.longitude)
    };

    resolve(result);
  } @catch (NSException *exception) {
    reject(@"LOCATION_ERROR", exception.reason, nil);
  }
}
```

**JavaScript:**
```typescript
try {
  const location = await NativeModules.LocationModule.getUserLocation();
  console.log('위도:', location.latitude);
  console.log('경도:', location.longitude);
} catch (error) {
  console.error('위치 조회 실패:', error);
}
```

---

## 7. 주의사항 및 Best Practices

### 7.1 UI 스레드 주의

**❌ 잘못된 코드 (Android):**
```kotlin
@ReactMethod
fun updateUI() {
  // ❌ React Method는 백그라운드 스레드에서 실행됨!
  // UI 작업을 직접 하면 크래시!
  textView.text = "Hello"
}
```

**✅ 올바른 코드:**
```kotlin
@ReactMethod
fun updateUI() {
  val activity = appContext.currentActivity
  activity?.runOnUiThread {
    // ✅ UI 스레드에서 실행
    textView.text = "Hello"
  }
}
```

**iOS도 마찬가지:**
```objective-c
RCT_EXPORT_METHOD(updateUI)
{
  // ✅ 메인 큐에서 실행
  dispatch_async(dispatch_get_main_queue(), ^{
    label.text = @"Hello";
  });
}
```

---

### 7.2 null 체크

**JavaScript:**
```typescript
// ✅ 모듈 존재 여부 체크
if (NativeModules.SplashModule) {
  NativeModules.SplashModule.hide();
} else {
  console.warn('SplashModule이 없습니다');
}
```

---

### 7.3 메서드 이름 컨벤션

**권장:**
```kotlin
@ReactMethod
fun getUserProfile() { }  // ✅ camelCase

@ReactMethod
fun get_user_profile() { }  // ❌ snake_case (JavaScript 스타일 아님)
```

---

## 💡 직접 해보기

### 실습 1: ToastModule 만들기

**목표:** Android Toast, iOS Alert를 Native Module로 만들기

**Android (Kotlin):**
```kotlin
class ToastModule(reactContext: ReactApplicationContext)
    : ReactContextBaseJavaModule(reactContext) {

  override fun getName(): String = "ToastModule"

  @ReactMethod
  fun show(message: String) {
    val activity = reactApplicationContext.currentActivity
    activity?.runOnUiThread {
      Toast.makeText(activity, message, Toast.LENGTH_SHORT).show()
    }
  }
}
```

**iOS (Objective-C):**
```objective-c
@implementation ToastModule

RCT_EXPORT_MODULE();

RCT_EXPORT_METHOD(show:(NSString *)message)
{
  dispatch_async(dispatch_get_main_queue(), ^{
    UIAlertController *alert = [UIAlertController
      alertControllerWithTitle:nil
      message:message
      preferredStyle:UIAlertControllerStyleAlert];

    // 2초 후 자동 닫기
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC),
                   dispatch_get_main_queue(), ^{
      [alert dismissViewControllerAnimated:YES completion:nil];
    });

    [rootViewController presentViewController:alert animated:YES completion:nil];
  });
}

@end
```

**JavaScript:**
```typescript
NativeModules.ToastModule.show('안녕하세요!');
```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: @ReactMethod 빠뜨림

```kotlin
❌ 잘못된 코드
fun hide() {
  // @ReactMethod 없으면 JavaScript에서 호출 불가!
}

✅ 올바른 코드
@ReactMethod
fun hide() {
  // JavaScript에서 호출 가능
}
```

### ❌ 실수 2: 모듈 이름 불일치

```kotlin
❌ 잘못된 코드
override fun getName(): String = "Splash"

// JavaScript
NativeModules.SplashModule.hide()  // ❌ 모듈 이름이 다름!

✅ 올바른 코드
override fun getName(): String = "SplashModule"

// JavaScript
NativeModules.SplashModule.hide()  // ✅
```

### ❌ 실수 3: Package 등록 안 함

```kotlin
❌ 잘못된 코드
// SplashModule.kt 만들었지만 MainApplication.kt에 등록 안 함
// → JavaScript에서 undefined

✅ 올바른 코드
// MainApplication.kt
override fun getPackages(): List<ReactPackage> =
  PackageList(this).packages.apply {
    add(SplashPackage())  // 반드시 등록!
  }
```

---

## 🔗 참고 자료

### 공식 문서
- [React Native - Native Modules (Android)](https://reactnative.dev/docs/native-modules-android)
- [React Native - Native Modules (iOS)](https://reactnative.dev/docs/native-modules-ios)

### 프로젝트 파일
- `android/app/src/main/java/.../SplashModule.kt`
- `ios/MyApp/SplashModule.h`
- `ios/MyApp/SplashModule.m`

---

## ✅ 체크리스트

이 문서를 다 읽었다면 체크해보세요:

- [ ] Native Module이 무엇인지 이해했다
- [ ] Android에서 @ReactMethod로 메서드를 노출하는 방법을 알겠다
- [ ] iOS에서 RCT_EXPORT_METHOD로 메서드를 노출하는 방법을 알겠다
- [ ] NativeModules로 JavaScript에서 호출하는 방법을 알겠다
- [ ] UI 스레드 주의사항을 이해했다
- [ ] Promise로 비동기 결과를 받는 방법을 알겠다

---

## 📌 핵심 요약

1. **Native Module = JavaScript ↔ Native 통신 다리**
2. **Android:** `@ReactMethod` + `ReactContextBaseJavaModule`
3. **iOS:** `RCT_EXPORT_METHOD` + `RCTBridgeModule`
4. **UI 작업:** 반드시 메인 스레드에서 (`runOnUiThread`, `dispatch_async`)
5. **비동기:** Callback보다 Promise 권장
6. **필수 등록:** Package (Android), Xcode 프로젝트 (iOS)

---

**다음 문서:** `RN_Firebase_001_FCM_푸시_알림_기초.md`로 이어집니다!

**작성일**: 2026-01-07
**난이도**: 🟠 중고급
