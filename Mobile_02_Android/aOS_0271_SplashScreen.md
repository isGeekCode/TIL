# Android - 스플래시 화면 구현 가이드 (정적 & 동적)

이 문서는 Android 앱에서 스플래시 화면(Splash Screen)을 정적/동적으로 구현하는 방법을 설명합니다.  
Android 12 이상에서는 SplashScreen API가 기본 제공되며, 이전 버전에서는 테마 또는 Activity 기반 구현이 필요합니다.

<br>

## 1. 정적 스플래시 구현 (테마 기반)

앱 시작 시 표시되는 테마(Theme)를 활용해 스플래시 화면을 구성할 수 있습니다.

### 📌 구현 방법

1. **styles.xml 설정**
    ```xml
    <style name="LaunchTheme" parent="Theme.AppCompat.Light.NoActionBar">
        <item name="android:windowBackground">@drawable/splash_screen</item>
    </style>
    ```

2. **AndroidManifest.xml에 적용**
    ```xml
    <activity
        android:name=".MainActivity"
        android:theme="@style/LaunchTheme">
        ...
    </activity>
    ```

> 이 방식은 Java/Kotlin 코드 실행 전에 표시되는 순수 정적 UI입니다.

<br>

## 2. 동적 스플래시 구현 (Activity 기반)

실제 로직을 수행하거나 초기 데이터를 받아오기 위해 별도의 SplashActivity를 구성할 수 있습니다.

### 📌 구현 흐름

1. SplashActivity를 시작 Activity로 등록
2. onCreate에서 타이머 또는 비동기 작업 처리
3. 완료 후 MainActivity로 전환

```kotlin
class SplashActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        Handler(Looper.getMainLooper()).postDelayed({
            startActivity(Intent(this, MainActivity::class.java))
            finish()
        }, 1500)
    }
}
```

> 서버 통신, 로컬 초기화, 로그인 체크 등도 이 시점에 수행 가능

<br>

## 3. Android 12 이상 - SplashScreen API 활용

Android 12(API 31)부터는 SplashScreen API를 통해 공식적으로 지원됩니다.

### 📌 기본 구성

- `theme`에 `android:windowSplashScreen*` 속성 설정
- `onCreate()`에서 커스터마이징 가능

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    // SplashScreen 설치
    installSplashScreen()
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)
}
```

> 로고 애니메이션, 조건부 유지 시간 등도 API를 통해 제어할 수 있습니다.

<br>

## 전환 방식 요약 비교

| 구현 방식     | API 버전      | 설명                              |
|---------------|---------------|-----------------------------------|
| Theme 기반    | 전체          | 코드 실행 전 이미지 표시          |
| Activity 기반 | 전체          | SplashActivity에서 전환 제어      |
| SplashScreen API | Android 12+ | 공식 API 사용, 애니메이션 커스텀 |

<br><br>

## 4. WebView 앱 스플래시 구현 (React Native, Ionic 등)

WebView 기반 앱(React Native WebView, Ionic 등)에서는 복잡한 레이아웃의 Splash Screen을 네이티브로 구현합니다.

### 📌 WebView 앱의 특징

- 라이브러리의 한계: `react-native-splash-screen` 같은 라이브러리는 단순한 중앙 이미지만 가능
- 복잡한 레이아웃 필요: 중앙 로고 + 하단 파트너 로고 등
- 네이티브 구현 필요: MainActivity에 Splash Layout을 추가

<br>

### 4-1. MainActivity vs SplashActivity 선택

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
WebView 로드 시작 → Splash 제거
```

**MainActivity Splash의 장점:**
- ✅ **흰 화면 방지**: WebView 로드 중에도 Splash가 보임
- ✅ **시간 벌기**: WebView 로드는 시간이 걸림 (네트워크 요청)
- ✅ **자연스러운 전환**: 깜빡임 없이 Splash → WebView
- ✅ **로직 추가 가능**: Activity 생명주기에서 제어 가능

<br>

### 4-2. ViewModel 아키텍처 패턴

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

<br>

### 4-3. Splash Layout 생성

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
│        ┌──────────┐         │
│        │ 중앙 로고 │         │ ← constraintTop/Bottom (중앙)
│        └──────────┘         │
│                             │
│        ┌──────────┐         │
│        │ 하단 로고 │         │ ← constraintBottom (하단 20dp 여백)
│        └──────────┘         │
└─────────────────────────────┘
```

<br>

### 4-4. MainActivity 구현

```kotlin
// MainActivity.kt
package com.myapp

import android.os.Bundle
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private var splashView: View? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

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
(뒤에서 WebView 로드 중...)
  ↓
외부에서 hideSplash() 호출
  ↓
Splash View 제거
```

<br>

### 4-5. 실전 팁

**다크모드 대응:**
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

**이미지 해상도:**
```
res/
  ├─ drawable-mdpi/main_logo.png (160dpi)
  ├─ drawable-hdpi/main_logo.png (240dpi)
  ├─ drawable-xhdpi/main_logo.png (320dpi)
  ├─ drawable-xxhdpi/main_logo.png (480dpi)
  └─ drawable-xxxhdpi/main_logo.png (640dpi)
```

**또는 벡터 이미지:**
```
res/drawable/main_logo.xml (SVG)
```

**애니메이션 추가 (선택):**
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

**Navigation Bar 고려:**
```xml
<!-- 하단 로고가 Navigation Bar에 가려지지 않도록 -->
<ImageView
    android:id="@+id/bottomLogo"
    ...
    android:layout_marginBottom="40dp" />  <!-- 여유 있게 -->
```

<br>

### 4-6. React Native 연동

React Native WebView 앱에서 네이티브로 제어하는 방법은 별도 문서 참고:

**관련 문서:**
- [React Native - WebView 앱 Splash 구현](../Mobile_04_ReactNative/RN_Splash_001_네이티브_커스텀_구현.md)

<br>

### 4-7. MainActivity vs SplashActivity 비교

| 방식 | 장점 | 단점 | 적합한 경우 |
|------|------|------|-------------|
| **SplashActivity** | 명확한 구조 분리 | Activity 전환 시 흰 화면 발생 | 일반 네이티브 앱 |
| **MainActivity Splash** | 흰 화면 방지, WebView 로드 중 시간 벌기 | Activity 하나에 책임 증가 | WebView 기반 앱 |

**WebView 앱에서 MainActivity Splash를 선택한 이유:**
- Activity 전환 시 발생하는 짧은 흰 화면을 완전히 제거
- WebView 로드 시간을 Splash로 자연스럽게 커버
- 사용자는 끊김 없는 부드러운 화면 전환 경험

<br><br>

---

## HISTORY
- 260626: Android 초안 추가
- 260108: WebView 앱 스플래시 구현 섹션 추가
