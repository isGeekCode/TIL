# Flutter WebView window.open() 테스트

본 문서는 Flutter 앱 내에서 `InAppWebView`를 사용하여 `window.open()` 호출 시 새 창을 처리하는 방법을 테스트한 예제에 대한 설명입니다.  
주요 패키지는 `flutter_inappwebview`이며, 웹뷰 내에서 A 태그, 버튼 클릭, iframe 방식으로 외부 링크를 여는 동작을 각각 확인할 수 있습니다.

## 주요 기능 요약

- `InAppWebView`를 이용한 웹뷰 구성  
- `window.open()` 호출 시 `onCreateWindow` 콜백을 활용하여 새 창을 처리  
- A 태그, 버튼 클릭 (window.open), iframe 방식 테스트  

## HTML 테스트 코드

```html
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>테스트</title>
  </head>
  <body>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 16px;">
      <div><strong>A 태그 방식</strong></div>
      <a href="https://flutter.dev" target="_blank">Open Flutter Website (A tag)</a>
      <br>
      <div><strong>window.open() 방식</strong></div>
      <button onclick="window.open('https://flutter.dev', '_blank')">Open Flutter Website (window.open)</button>
      <br>
      <div><strong>iframe 방식</strong></div>
      <iframe src="https://flutter.dev" width="100%" height="600"></iframe>
    </div>
  </body>
</html>
```

## Flutter 코드 주요 구성

이 예제에서는 `InAppWebView` 위젯을 사용하여 웹뷰를 구성하고 있습니다.  
웹뷰 내에서 `window.open()` 호출이 발생하면 `onCreateWindow` 콜백이 호출되며, 이를 통해 새 창을 Flutter 내에서 처리하도록 구현했습니다.  
웹뷰 설정(`WebViewSettings`)에서는 JavaScript 실행 허용, 다중 창 지원, 미디어 재생 설정 등을 포함하여 다양한 환경을 구성하고 있습니다.

아래는 참고용으로 사용된 Flutter 전체 코드 구현입니다.
## 전체 코드 예제

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
      title: 'Flutter WebView window.open Test',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const WebViewTestPage(),
    );
  }
}

class WebViewTestPage extends StatefulWidget {
  const WebViewTestPage({Key? key}) : super(key: key);

  @override
  State<WebViewTestPage> createState() => _WebViewTestPageState();
}

class _WebViewTestPageState extends State<WebViewTestPage> {
  late InAppWebViewController webViewController;
  InAppWebViewController? newWindowController;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter WebView window.open Test'),
      ),
      body: Column(
        children: [
          Expanded(
            child: InAppWebView(
              initialUrlRequest: URLRequest(
                url: Uri.dataFromString('''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>테스트</title>
  </head>
  <body>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 16px;">
      <div><strong>A 태그 방식</strong></div>
      <a href="https://flutter.dev" target="_blank">Open Flutter Website (A tag)</a>
      <br>
      <div><strong>window.open() 방식</strong></div>
      <button onclick="window.open('https://flutter.dev', '_blank')">Open Flutter Website (window.open)</button>
      <br>
      <div><strong>iframe 방식</strong></div>
      <iframe src="https://flutter.dev" width="100%" height="600"></iframe>
    </div>
  </body>
</html>
''', mimeType: 'text/html'),
              ),
              initialSettings: getInAppWebViewSettings(),
              onWebViewCreated: (controller) {
                webViewController = controller;
              },
              onCreateWindow: (controller, createWindowRequest) async {
                // 새 창 요청이 들어오면 새 InAppWebView를 띄워서 처리
                showDialog(
                  context: context,
                  builder: (context) {
                    return AlertDialog(
                      content: SizedBox(
                        width: double.infinity,
                        height: 600,
                        child: InAppWebView(
                          initialUrlRequest: URLRequest(
                            url: createWindowRequest.request.url,
                          ),
                          initialSettings: getInAppWebViewSettings(),
                          onWebViewCreated: (newController) {
                            newWindowController = newController;
                          },
                        ),
                      ),
                      actions: [
                        TextButton(
                          onPressed: () {
                            Navigator.of(context).pop();
                          },
                          child: const Text('닫기'),
                        ),
                      ],
                    );
                  },
                );
                return true;
              },
            ),
          ),
        ],
      ),
    );
  }
}


InAppWebViewSettings getInAppWebViewSettings() {
  return InAppWebViewSettings(
    javaScriptEnabled: true,
    javaScriptCanOpenWindowsAutomatically: true,
    supportMultipleWindows: true,
    useOnDownloadStart: true,
    mediaPlaybackRequiresUserGesture: false,
    allowsInlineMediaPlayback: true,
  );
}
```
