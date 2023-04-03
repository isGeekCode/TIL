# Cookie - 여러 웹뷰에서 쿠키 공유하기

WKProcessPool을 사용하면 앱의 여러 WKWebView 객체에서 쿠키를 공유할 수 있다. 

WKProcessPool은 웹 컨텐츠 프로세스를 관리하는 객체이며, 앱에서 여러 WKWebView 객체가 공유할 수 있도록 이 프로세스 풀을 사용하여 WKWebView를 초기화한다.

### WKProcessPool을 사용하여 여러 WKWebView에서 쿠키를 공유하는 방법

**Step 1. WKProcessPool 객체를 생성**
```swift
let processPool = WKProcessPool()

```

**Step 2. WKWebView 초기화**

WKWebView를 초기화할 때 processPool 매개 변수를 사용하여 WKProcessPool 객체를 전달한다.

```swift

let configuration = WKWebViewConfiguration()
configuration.processPool = processPool

let webView1 = WKWebView(frame: .zero, configuration: configuration)
let webView2 = WKWebView(frame: .zero, configuration: configuration)
```

**쿠키 공유 확인**

위와 같이 WKWebView를 초기화하면,
두 WKWebView가 같은 WKProcessPool을 사용하므로 쿠키가 자동으로 공유된다.

따라서 첫 번째 WKWebView에서 설정한 쿠키는 두 번째 WKWebView에서도 사용할 수 있다.

```swift
let cookieScript = """
                      var cookieString = "key=value";
                      document.cookie = cookieString;
                   """

// 첫 번째 WKWebView에서 쿠키 설정
webView1.evaluateJavaScript(cookieScript)

// 두 번째 WKWebView에서 쿠키 확인
webView2.configuration.websiteDataStore.httpCookieStore.getAllCookies { cookies in
    print("Cookies: \(cookies)")
}
```

