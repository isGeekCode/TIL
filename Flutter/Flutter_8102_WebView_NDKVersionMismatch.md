# Flutter_8102_WebView_NDKVersionMismatch – Android NDK 버전 불일치


## 🧰 설치 환경
- Flutter: 3.32.4
- Dart: 3.8.1
- Platform: iOS / Android
- Plugin: webview_flutter 4.13.0
- IDE: VSCode / Android Studio / Xcode

<br><br>

## 📌 발생 상황
### 언제
`pub get` 이후 첫 빌드 시

<br><br>

### 어디서

WebView 초기화 시점

<br><br>

### 무엇을 하다가

WebView 테스트 중, 웹뷰가 동작은 하지만 에러로그 발생

<br><br>

## ❗️현상 (에러 로그)
```
Your project is configured with Android NDK 26.3.11579264, but the following plugin(s) depend on a different Android NDK version:
- webview_flutter_android requires Android NDK 27.0.12077973
Fix this issue by using the highest Android NDK version (they are backward compatible).
Add the following to /{프로젝트폴더}/android/app/build.gradle.kts:


android {
    ndkVersion = "27.0.12077973"
    ...
}
```

<br><br>

---

## 🧪 원인
- 현재 webview_flutter 의 안드로이드 NDK 최소 버전은 27.0.12077973 이기 때문에 해당 버전으로 최적화를 시키라는 것이다.  

<br><br>

---

## ✅ 해결 방법
Step1. NDK 최소버전을 맞춰서 설치한다.  

Step2. 설치한 NDK명을 명시한다.  

- 경로 : `/{프로젝트경로}/android/app/src/build.gradle.kts

```
//ASIS

android {
    namespace = "com.example.first_app_test"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = flutter.ndkVersion
}


//TOBE
android {
    namespace = "com.example.first_app_test"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = "29.0.13599879"
}

```

비슷한 상황으로는 바로 하단에 이부분도 수정해야하는 경우도 생긴다.   

```
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }

    kotlinOptions {
        jvmTarget = JavaVersion.VERSION_11.toString()
    }


```




<br><br>

## History
- 250619 : 초안작성


