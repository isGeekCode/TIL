# Flutter - 웹뷰구현 : webview_flutter 세팅

[릴리즈 노트](https://pub.dev/packages/webview_flutter)


**Flutter에서 웹뷰(WebView)** 를 이용해 앱을 켜자마자  
**네이버 홈페이지(https://www.naver.com)** 를 보여주는 가장 간단한 방법 

> 제한사항 : http 도메인이나 자바스크립트 등에 있어서 사용하기에 (커스텀하기)복잡하다.  그러니 간단한 거라면 추천
> 만약 커스텀이 필요하다면 inappWebView로 진행할 것



---

## 1단계: webview_flutter 패키지 설치하기

`pubspec.yaml` 파일을 열고 아래 내용을 `dependencies:` 아래에 추가:

```yaml
dependencies:
  flutter:
    sdk: flutter
  webview_flutter: ^4.4.2
```

※ 저장하면 자동으로 설치되거나, 안 되면 터미널에서 아래 명령어를 입력:

```bash
flutter pub get
```

---

## 2단계: Android & iOS 설정하기

### 📱 Android

`android/app/src/main/AndroidManifest.xml` 파일에서 `<application>` 안에 아래 코드 추가:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

### 🍎 iOS

`ios/Runner/Info.plist` 파일 안에 아래 내용 추가:

```xml
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
  <true/>
</dict>
```

---

## 3단계: main.dart 파일 구현

`lib/main.dart` 파일

```dart
import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: WebViewPage(),
    );
  }
}

class WebViewPage extends StatefulWidget {
  const WebViewPage({super.key});

  @override
  State<WebViewPage> createState() => _WebViewPageState();
}

class _WebViewPageState extends State<WebViewPage> {
  late final WebViewController _controller;

  @override
  void initState() {
    super.initState();
    _controller = WebViewController()
      ..loadRequest(Uri.parse('https://www.naver.com'));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: WebViewWidget(controller: _controller),
      ),
    );
  }
}
```


## History
- 250619: 초안작성
