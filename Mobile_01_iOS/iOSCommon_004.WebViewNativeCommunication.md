# WebView - JavaScript와 Native 간 양방향 통신

iOS에서 웹 페이지(JavaScript)에서 앱으로 메시지를 보내려면, WKWebView의 `WKScriptMessageHandler`를 활용해야 합니다. 이 문서에서는 WKScriptMessageHandler를 등록하고, 메시지를 수신 및 처리하는 방법, 메모리 관리(LeakAvoider), Objective-C 적용법까지 다룹니다.

## 1. WKScriptMessageHandler란?

WKWebView에서 웹(JavaScript) → 앱(Native)으로 메시지를 전달할 때 사용하는 프로토콜입니다. 웹에서 `window.webkit.messageHandlers.<name>.postMessage(...)`로 메시지를 보낼 수 있으며, 앱에서는 이를 받아 처리할 수 있습니다.

## 2. 등록 방법

WKWebView를 생성할 때, WKUserContentController에 message handler를 등록합니다.

```swift
import WebKit

class MyWebViewController: UIViewController, WKScriptMessageHandler {
    var webView: WKWebView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let contentController = WKUserContentController()
        contentController.add(self, name: "myHandler")

        let config = WKWebViewConfiguration()
        config.userContentController = contentController

        webView = WKWebView(frame: self.view.bounds, configuration: config)
        self.view.addSubview(webView)
    }
}
```

## 3. 메시지 수신 및 처리

`WKScriptMessageHandler`의 필수 메서드인 `userContentController(_:didReceive:)`를 구현하여 메시지를 받을 수 있습니다.

```swift
extension MyWebViewController: WKScriptMessageHandler {
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        if message.name == "myHandler" {
            print("웹에서 보낸 메시지: \(message.body)")
        }
    }
}
```

### 웹(JavaScript)에서 메시지 보내기

```javascript
window.webkit.messageHandlers.myHandler.postMessage("Hello from Web!");
```

## 4. 메모리 관리: deinit에서 remove

등록한 handler는 해제 시 반드시 제거해야 합니다. 그렇지 않으면 retain cycle 등 메모리 누수가 발생할 수 있습니다.

```swift
deinit {
    webView.configuration.userContentController.removeScriptMessageHandler(forName: "myHandler")
}
```

## 5. LeakAvoider 패턴 (메모리 누수 방지)

WKScriptMessageHandler는 weak로 등록되지 않으므로, self(UIViewController 등)를 직접 handler로 등록하면 retain cycle이 발생할 수 있습니다. 이를 방지하려면 중간에 weak 참조를 가진 객체(LeakAvoider)를 두는 방법이 있습니다.

```swift
class LeakAvoider: NSObject, WKScriptMessageHandler {
    weak var delegate: WKScriptMessageHandler?

    init(delegate: WKScriptMessageHandler) {
        self.delegate = delegate
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        delegate?.userContentController(userContentController, didReceive: message)
    }
}

// 등록 시
contentController.add(LeakAvoider(delegate: self), name: "myHandler")
```

## 6. Objective-C 적용 방법

Objective-C에서도 WKScriptMessageHandler를 사용할 수 있습니다.

```objc
@interface MyWebViewController () <WKScriptMessageHandler>
@property (nonatomic, strong) WKWebView *webView;
@end

@implementation MyWebViewController
- (void)viewDidLoad {
    [super viewDidLoad];
    WKUserContentController *contentController = [[WKUserContentController alloc] init];
    [contentController addScriptMessageHandler:self name:@"myHandler"];

    WKWebViewConfiguration *config = [[WKWebViewConfiguration alloc] init];
    config.userContentController = contentController;

    self.webView = [[WKWebView alloc] initWithFrame:self.view.bounds configuration:config];
    [self.view addSubview:self.webView];
}

- (void)userContentController:(WKUserContentController *)userContentController didReceiveScriptMessage:(WKScriptMessage *)message {
    if ([message.name isEqualToString:@"myHandler"]) {
        NSLog(@"웹에서 보낸 메시지: %@", message.body);
    }
}

- (void)dealloc {
    [self.webView.configuration.userContentController removeScriptMessageHandlerForName:@"myHandler"];
}
@end
```

## 7. 앱 → 웹: JavaScript 호출 (evaluateJavaScript)

WKWebView에서 앱이 웹 측의 함수를 호출하거나 값을 전달하려면 `evaluateJavaScript(_:completionHandler:)`를 사용한다. 웹 페이지에 대상 함수가 존재해야 하며, DOM 로드 타이밍을 고려한다.

### 7.1 기본 호출

```swift
// 웹에 정의된 전역 함수: function showText(msg) { document.body.innerText = msg; }
webView.evaluateJavaScript("showText('Hello from iOS')", completionHandler: nil)
```

### 7.2 값 반환 받기

`completionHandler`의 `result`로 JS 평가 결과를 전달받을 수 있다. (숫자는 보통 `Double/NSNumber`, 객체는 `NSDictionary/Array`로 브릿지됨)

```swift
webView.evaluateJavaScript("2 + 3") { result, error in
    if let error = error { print("JS error:", error); return }
    if let num = result as? NSNumber {
        print("sum =", num.intValue) // 5
    }
}
```

Promise를 사용하는 경우, JS 측에서 `await` 없이 바로 값을 반환하지 않으면 `result`가 `undefined`가 될 수 있다. 필요 시 JS에 헬퍼를 두거나 `window.__bridgeResolve(id, value)`와 같은 콜백으로 웹→앱 응답을 받는 패턴을 사용한다.

### 7.3 안전하게 데이터 전달 (JSON 인코딩)

문자열을 직접 JS 코드에 삽입하면 따옴표/줄바꿈 등으로 문법 오류가 날 수 있다. **JSON 인코딩** 후 그대로 넘기는 방식을 권장한다.

```swift
let payload: [String: Any] = ["id": "req-1", "message": "안녕", "count": 3]
let data = try! JSONSerialization.data(withJSONObject: payload)
let json = String(data: data, encoding: .utf8)! 
// {"id":"req-1","message":"안녕","count":3}

let js = "window.fromApp && window.fromApp(\(json))"
webView.evaluateJavaScript(js, completionHandler: nil)
```

웹 측(예시):

```html
<script>
  window.fromApp = function (data) {
    // data: { id, message, count }
    console.log("fromApp:", data);
    // 화면 갱신 등 처리
  };
</script>
```

### 7.4 DOM 로드 타이밍 보장

대상 함수가 준비되기 전에 호출하면 실패한다. 다음 중 하나로 보장한다.

- **UserScript로 사전 주입**
  ```swift
  let scriptSrc = "window.fromApp = window.fromApp || function(d) { console.log('fromApp init', d); };"
  let userScript = WKUserScript(source: scriptSrc, injectionTime: .atDocumentStart, forMainFrameOnly: true)
  contentController.addUserScript(userScript)
  ```
- **로드 완료 후 호출**
  ```swift
  func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
      webView.evaluateJavaScript("showText('Loaded!')", completionHandler: nil)
  }
  ```

### 7.5 보안/주의사항 체크리스트

- 사용자 입력을 그대로 JS 코드 문자열에 삽입하지 말 것(반드시 JSON 인코딩).
- 민감정보는 JS로 전달하지 말고, 필요 시 네이티브에서 직접 처리하거나 서버와 통신할 것.
- 다중 호출/중복 실행 방지: 요청 `id`를 두고 웹 측에서 멱등 처리.
- `javaScriptEnabled`가 비활성화된 구성인지 확인.
- 웹이 없는 새 창/팝업 컨텍스트 여부 확인(`forMainFrameOnly`).

---

## History
- 230731 : 최초 작성
- 231006 : postMessage 추가
- 240203 : 예제 추가
- 250908 : 내용 수정
