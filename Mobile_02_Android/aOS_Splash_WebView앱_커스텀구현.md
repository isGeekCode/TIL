# Android - WebView 기반 앱 Splash Screen 커스텀 구현

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

→ **해결책: MainActivity에 Splash Layout + Native Module 직접 구현**

---

## 왜 MainActivity에서 Splash를 띄우는가?

### 일반적인 Android 앱

```
SplashActivity (Splash 표시)
  ↓
MainActivity (메인 화면)
```

### 하지만 WebView 기반 RN 앱의 문제

```
SplashActivity 종료
  ↓
MainActivity 시작
  ↓
WebView 로드 중... 😱 흰 화면 깜빡임 발생!
  ↓
WebView 로드 완료
```

**문제:**
- Activity 전환 시 짧은 흰 화면 노출
- WebView 로드는 시간이 걸림 (네트워크 요청)
- 사용자 경험 저하

### 해결: MainActivity에서 즉시 Splash를 띄우기

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

---

## ViewModel 아키텍처 패턴

### 전통적인 방식: SplashVM + MainVM 분리

```
MainActivity
  ├─ SplashViewModel (Splash 로직)
  └─ MainViewModel (메인 로직)
```

### 최근 권장 방식: MainVM 내부에 SplashUseCase

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

## 구현 단계

### 1. SplashModule.kt 생성

React Native에서 호출할 Native Module을 만듭니다.

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
- `MainActivity` 타입 캐스팅으로 `hideSplash()` 호출

---

### 2. SplashPackage.kt

Native Module을 React Native에 등록합니다.

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

### 4. Splash Layout 생성

ConstraintLayout으로 복잡한 레이아웃을 구현합니다.

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

**레이아웃 구조:**
```
┌─────────────────────────────┐
│                             │
│                             │
│        ┌──────────┐         │
│        │          │         │
│        │ 중앙 로고 │         │ ← constraintTop/Bottom (중앙)
│        │          │         │
│        └──────────┘         │
│                             │
│                             │
│        ┌──────────┐         │
│        │ 하단 로고 │         │ ← constraintBottom (하단 20dp 여백)
│        └──────────┘         │
└─────────────────────────────┘
```

---

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

**핵심 로직:**

1. **onCreate()**: Activity 시작 시 즉시 Splash 추가
2. **showSplash()**: ContentView 위에 Splash Layout 추가
3. **hideSplash()**: Splash Layout 제거 + 메모리 해제

**동작 순서:**
```
MainActivity 시작
  ↓
onCreate() 실행
  ↓
showSplash() → ContentView에 splash_screen.xml 추가
  ↓
(뒤에서 React Native 부팅 중...)
  ↓
WebView 로드 시작
  ↓
JavaScript에서 SplashModule.hide() 호출
  ↓
hideSplash() → Splash View 제거
```

---

## 실전 팁

### 1. 다크모드 대응

```xml
<!-- res/values/colors.xml -->
<color name="splash_background">#FFFFFF</color>

<!-- res/values-night/colors.xml -->
<color name="splash_background">#000000</color>
```

```xml
<!-- splash_screen.xml -->
<androidx.constraintlayout.widget.ConstraintLayout
    android:background="@color/splash_background">
```

### 2. 이미지 해상도

**res/ 디렉토리 구조:**
```
res/
  ├─ drawable-mdpi/main_logo.png (160dpi)
  ├─ drawable-hdpi/main_logo.png (240dpi)
  ├─ drawable-xhdpi/main_logo.png (320dpi)
  ├─ drawable-xxhdpi/main_logo.png (480dpi)
  └─ drawable-xxxhdpi/main_logo.png (640dpi)
```

**또는 벡터 이미지 사용:**
```
res/drawable/main_logo.xml (SVG)
```

### 3. 애니메이션 추가 (선택)

```kotlin
fun hideSplash() {
    splashView?.let { view ->
        view.animate()
            .alpha(0f)
            .setDuration(300)
            .withEndAction {
                val rootView = findViewById<ViewGroup>(android.R.id.content)
                rootView.removeView(view)
                splashView = null
            }
    }
}
```

### 4. Navigation Bar 고려

```xml
<!-- 하단 로고가 Navigation Bar에 가려지지 않도록 -->
<ImageView
    android:id="@+id/bottomLogo"
    ...
    android:layout_marginBottom="40dp" />  <!-- 여유 있게 -->
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

```kotlin
fun hideSplash() {
    splashView?.let { view ->
        val rootView = findViewById<ViewGroup>(android.R.id.content)
        rootView.removeView(view)
        splashView = null  // ← 메모리 해제
    }
}
```

### 2. Thread Safety

```kotlin
// UI 작업은 항상 메인 스레드에서
activity?.runOnUiThread {
    activity.hideSplash()
}
```

### 3. Null Safety

```kotlin
// Activity가 null일 수 있음
val activity = currentActivity as? MainActivity
activity?.runOnUiThread {
    activity.hideSplash()
}
```

---

## 디버깅

### Splash가 안 사라질 때

```kotlin
// SplashModule.kt에 로그 추가
@ReactMethod
fun hide() {
    Log.d("SplashModule", "🔵 hide() called")
    val activity = currentActivity as? MainActivity
    if (activity == null) {
        Log.e("SplashModule", "🔴 MainActivity not found")
        return
    }
    Log.d("SplashModule", "🟢 Calling hideSplash()")
    activity.runOnUiThread {
        activity.hideSplash()
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

### Logcat 필터

```
adb logcat | grep SplashModule
```

---

## MainActivity vs SplashActivity 비교

| 방식 | 장점 | 단점 | 적합한 경우 |
|------|------|------|-------------|
| **SplashActivity** | 명확한 구조 분리 | Activity 전환 시 흰 화면 발생 | 일반 네이티브 앱 |
| **MainActivity Splash** | 흰 화면 방지, WebView 로드 중 시간 벌기 | Activity 하나에 책임 증가 | WebView 기반 앱 |

**WebView 앱에서 MainActivity Splash를 선택한 이유:**
- Activity 전환 시 발생하는 짧은 흰 화면을 완전히 제거
- WebView 로드 시간을 Splash로 자연스럽게 커버
- 사용자는 끊김 없는 부드러운 화면 전환 경험

---

## 요약

**Android WebView 앱 Splash 구현:**

1. **MainActivity.onCreate()**: 즉시 Splash Layout 추가
2. **SplashModule.kt**: Native Module 생성
3. **SplashPackage.kt**: Module 등록
4. **splash_screen.xml**: ConstraintLayout으로 복잡한 레이아웃 구현
5. **JavaScript**: `SplashModule.hide()` 호출

**핵심:**
- MainActivity에서 Splash를 띄워 Activity 전환 시 흰 화면 방지
- ConstraintLayout으로 다양한 화면 크기 대응
- `addView()`/`removeView()`로 Splash 제어
- MainVM + SplashUseCase 패턴으로 깔끔한 아키텍처

**MainActivity Splash의 핵심 가치:**
- WebView 로드 중 발생하는 흰 화면을 완벽히 차단
- 시간을 벌어서 자연스러운 사용자 경험 제공

이 방식이 라이브러리보다 **안정적**이고 **커스터마이징**이 자유롭습니다.
