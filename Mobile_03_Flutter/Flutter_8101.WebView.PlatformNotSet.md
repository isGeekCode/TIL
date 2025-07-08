# Flutter_8102_WebView_PlatformNotSet – WebViewPlatform.instance 오류


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

WebView 테스트 중

<br><br>

## ❗️현상 (에러 로그)
```
Assertion failed: file:///Users/{유저명}/.pub-cache/hosted/pub.dev/webview_flutter_platform_interface-2.13.1/lib/src/
platform_webview_controller.dart:26:7
WebViewPlatform.instance != null
"A platform implementation for "webview_flutter" has not been set. Please ensure that an implementation of WebViewPlatform" has been set to "WebViewPlatform.instance" before use. For unit testing, "WebViewPlatform.instance' can be set with your own test implementation.
See also: https://docs.flutter.dev/testing/errors
```

<br><br>

---

## 🧪 원인
- WebViewPlatform의 구현체가 등록되지 않음
- WebViewPlatform.instance 가 등록되지않은 이유는 여러개가 있을 수 있다.    

<br><br>

---

## ✅ 해결 방법
1. 웹뷰를 사용할 수 없는 환경인 경우: 모바일 환경에서 실행하면 정상적으로 동작함을 확인할 수 있다.  

2. WebViewPlatform.instance 가 등록되지않아서 생긴 에러라면 아래와 같이 등록한다. 

```
WebViewPlatform.instance = MyCustomPlatform();
```


<br><br>

## History
- 250619 : 초안작성

