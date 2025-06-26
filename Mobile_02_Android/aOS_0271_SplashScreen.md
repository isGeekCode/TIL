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

## HISTORY
- 260626: Android 초안 추가
