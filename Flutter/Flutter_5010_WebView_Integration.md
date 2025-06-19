# Flutter - WebView 생성하기

**Flutter에서 웹뷰(WebView)** 를 이용해 앱을 켜자마자  
**네이버 홈페이지(https://www.naver.com)** 를 보여주는 가장 간단한 방법 

---

## 1단계: webview_flutter 패키지 설치하기

`pubspec.yaml` 파일을 열고 아래 내용을 `dependencies:` 아래에 추가해요:

```yaml
dependencies:
  flutter:
    sdk: flutter
  webview_flutter: ^4.4.2
```

※ 저장하면 자동으로 설치되거나, 안 되면 터미널에서 아래 명령어를 입력해요:

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

---

## ✅ 4단계: 실행하기

이제 아래 명령어로 앱을 실행해요:

```bash
flutter run
```

기기가 연결돼 있다면 바로 네이버가 뜰 거예요!  
시뮬레이터에서도 잘 보여요.

---

## 📝 마무리

이렇게 하면 별다른 버튼 없이,  
**앱을 켜자마자 웹페이지가 바로 뜨는 Flutter 앱**이 완성돼요!

다음 글에서는 이 웹뷰에 뒤로가기 버튼을 달거나, 로딩 중 표시를 넣는 방법도 소개할게요 :)
