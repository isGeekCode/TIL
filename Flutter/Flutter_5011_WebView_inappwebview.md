# Flutter - 웹뷰구현 : inappwebview 세팅(권장)

**Flutter에서 고급 웹뷰(WebView)** 기능을 사용할 수 있도록 도와주는 방법

- [릴리즈노트](https://pub.dev/packages/flutter_inappwebview)

<br><br>

## 1단계: flutter_inappwebview 패키지 설치하기

`pubspec.yaml` 파일을 열고 아래 내용을 `dependencies:` 아래에 추가:

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_inappwebview: ^6.1.5
```


※ 저장하면 자동으로 설치되거나, 안 되면 터미널에서 아래 명령어를 입력:

```bash
flutter pub get
```


## 2단계: Android & iOS 설정하기

### 📱 Android

`android/app/src/main/AndroidManifest.xml`에 아래 항목들이 있는지 확인하고 추가해요:

```xml
<uses-permission android:name="android.permission.INTERNET"/>

<application
  android:usesCleartextTraffic="true"
  android:name="io.flutter.app.FlutterApplication"
  android:label="your_app_name"
  android:icon="@mipmap/ic_launcher">
```

`android/app/build.gradle` 파일에 `minSdkVersion 21` 이상인지 확인:

```gradle
defaultConfig {
  minSdkVersion 21
}
```

---

### 🍎 iOS

`ios/Runner/Info.plist` 파일 안에 아래 내용 추가:

```xml
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
  <true/>
</dict>
```


## 3단계: main.dart 파일 구현

`lib/main.dart` 파일 예시는 아래와 같이 구성:

```dart
import 'package:flutter/material.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: WebViewPage()
    );
  }
}

class WebViewPage extends StatefulWidget {
  const WebViewPage({super.key});
  @override
  State<WebViewPage> createState() => _WebViewPageState();
}

class _WebViewPageState extends State<WebViewPage> {

  InAppWebViewController? _webViewController;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('브라우저'),
      ),
      body: InAppWebView(
        initialUrlRequest: URLRequest(
          url: Uri.parse("http://www.radcns.com"),
        ),
        initialOptions: InAppWebViewGroupOptions(
          crossPlatform: InAppWebViewOptions(
            mediaPlaybackRequiresUserGesture: false,
          ),
          android: AndroidInAppWebViewOptions(
            useHybridComposition: true,
          ),
          ios: IOSInAppWebViewOptions(
            allowsInlineMediaPlayback: true,
          ),
        ),
        onWebViewCreated: (controller) {
          _webViewController = controller;
        },
      ),
    );
  }
}
```


v.6+ :  InAppWebViewSettings가 추가되었다. 

initialUrlRequest : 인앱웹뷰 호출 시 시작 페이지 설정
initialOptions : 인앱웹뷰 호출 시 초기 설정
pullToRefreshController : 당겨서 새로고침 컨트롤러 정의
onWebViewCreated : 인앱웹뷰 생성 시  수행될 코드 정의
onLoadStart : 페이지 로딩 시작 시  수행될 코드 정의
onLoadStop : 페이지 로딩이 정지 시  수행될 코드 정의
onLoadError : 페이지 로딩 중 오류 발생 시  수행될 코드 정의
onProgressChanged : 페이지 로딩 상태 변경 시 메서드 정의
androidOnPermissionRequest : 안드로이드 웹뷰에서 권한 관련 코드 정의
shouldOverriderUrlLoading : URL 로딩 시 제어할 코드 정의

```
import 'package:flutter/material.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: WebViewPage()
    );
  }
}

class WebViewPage extends StatefulWidget {
  const WebViewPage({super.key});
  @override
  State<WebViewPage> createState() => _WebViewPageState();
}

class _WebViewPageState extends State<WebViewPage> {
  InAppWebViewController? _webViewController;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: InAppWebView(
            initialSettings: getInAppWebViewSettings(),
            initialUrlRequest: URLRequest(url: WebUri('https://www.ost.co.kr/'))),
      )
    );
  }
}

InAppWebViewSettings getInAppWebViewSettings() {
  return InAppWebViewSettings(
    // JavaScript 활성화 (javaScriptEnabled = true)
    javaScriptEnabled: true,

    // 이미지 자동 로드 (loadsImagesAutomatically = true)
    loadsImagesAutomatically: true,

    // 페이지를 화면 크기에 맞게 로드 (loadWithOverviewMode = true)
    loadWithOverviewMode: true,

    // 넓은 뷰포트 사용 (useWideViewPort = true)
    useWideViewPort: true,

    // 파일 시스템 접근 허용 (allowFileAccess = true)
    // Android에서는 allowFileAccess 속성으로 직접 제어
    allowFileAccess: true, // Android स्पेसिफिक

    // DOM Storage API 사용 활성화 (domStorageEnabled = true)
    domStorageEnabled: true,

    // 데이터베이스 저장소 API 사용 활성화 (databaseEnabled = true)
    databaseEnabled: true, // Web SQL, IndexedDB에 영향

    // 다중 창 지원 (setSupportMultipleWindows(false))
    // JavaScript가 자동으로 창을 열 수 있도록 허용 (javaScriptCanOpenWindowsAutomatically = true)
    // 이 두 가지는 supportMultipleWindows와 javaScriptCanOpenWindowsAutomatically로 각각 제어
    supportMultipleWindows: false, // 기본값은 false일 수 있음, 확인 필요
    javaScriptCanOpenWindowsAutomatically: true,

    // 텍스트 확대/축소 비율 설정 (textZoom = 100)
    // InAppWebView에서는 textZoom으로 직접 제어
    textZoom: 100,

    // 캐시 모드 설정 (cacheMode = WebSettings.LOAD_NO_CACHE)
    // cacheMode를 사용하여 동일한 WebSettings 상수를 사용
    cacheMode: CacheMode.LOAD_NO_CACHE, // Android CacheMode 열거형 사용

    // 가로 스크롤바 비활성화 (isHorizontalScrollBarEnabled = false)
    horizontalScrollBarEnabled: false,

    // 세로 스크롤바 비활성화 (isVerticalScrollBarEnabled = false)
    verticalScrollBarEnabled: false,

    // 스크롤바 오버레이 설정 (setVerticalScrollbarOverlay, setHorizontalScrollbarOverlay)
    // InAppWebView에는 직접적인 overlay 설정이 없을 수 있으며,
    // scrollbarFadingEnabled 와 안드로이드 플랫폼별 옵션으로 유사하게 제어 가능
    // 또는 기본 동작에 의존. 필요 시 플랫폼 채널로 네이티브 코드 직접 호출 고려.
    // scrollbarFadingEnabled: true, // 예시 (네이티브 동작과 다를 수 있음)

    // 혼합 콘텐츠 처리 설정 (mixedContentMode = WebSettings.MIXED_CONTENT_ALWAYS_ALLOW)
    // mixedContentMode를 사용하여 동일한 WebSettings 상수를 사용
    mixedContentMode: MixedContentMode.MIXED_CONTENT_ALWAYS_ALLOW, // Android MixedContentMode 열거형 사용

    // 쿠키 허용 (CookieManager.getInstance().setAcceptCookie(true))
    // InAppWebView는 기본적으로 쿠키를 허용하는 경향이 있으며,
    // CookieManager를 통해 더 세부적으로 제어 가능.
    // 명시적인 전역 설정은 CookieManager를 통해야 할 수 있음.
    // allow troisième-party cookies는 Android 특화 옵션으로 제어 가능.
    // (cookieManager.setAcceptThirdPartyCookies(this, true))
    // initialSettings에 직접적인 전역 쿠키 활성화 옵션은 없을 수 있음.
    // 다만, WebView 자체는 기본적으로 쿠키를 사용하려고 함.
    // 서드파티 쿠키는 아래 android specific 옵션에서 설정
    // androidSpecific: AndroidInAppWebViewSettings(
    //   // 서드파티 쿠키 허용
    //   thirdPartyCookiesEnabled: true,
    //   // allowFileAccess는 여기에 있었으나, 최신 버전에서는 상위 레벨로 이동했을 수 있음.
    //   // allowFileAccessFromFileURLs: true, // 필요 시
    //   // allowUniversalAccessFromFileURLs: true, // 필요 시
    //
    //   // 다운로드 리스너 관련 설정은 InAppWebView의 onDownloadStart 콜백으로 처리
    //   // 별도의 설정 옵션은 아님
    // ),

    // iOS 특화 설정 (필요한 경우)
    // iosSpecific: IOSInAppWebViewSettings(
    //   allowsInlineMediaPlayback: true,
    // ),

    // 다른 유용한 설정들:
    // 사용자 에이전트 설정
    // userAgent: "Custom User Agent String",

    // 미디어 재생을 사용자의 제스처 없이 허용 (주의해서 사용)
    mediaPlaybackRequiresUserGesture: false,

    // 뷰포트 설정 (HTML 메타 태그를 더 우선시할 수 있음)
    // useWideViewPort가 true일 때 이 설정이 보조적으로 작용
    // initialScale: 100, // % 단위가 아닌 double 값 (예: 1.0)

    // 기본 글꼴 크기
    // defaultFontSize: 16,

    // 기본 고정 폭 글꼴 크기
    // defaultFixedFontSize: 13,

    // 개발자 도구 활성화 (디버그 빌드에서만)
    // debuggingEnabled: true, // kDebugMode ? true : false,
  );
}
```
