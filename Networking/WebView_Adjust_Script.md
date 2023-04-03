# WebView - 웹뷰에 스크립트를 적용시키는 방법


## 1. WKUserContentController 사용

WKUserContentController는 웹 페이지가 로드될 때 콘텐츠 스크립트를 적용하기 위해 사용된다.

먼저 WKUserScript 객체를 생성한다. 
이 객체에는 적용할 스크립트, 적용 시점 및 대상 프레임에 대한 정보가 포함된다. 
그런 다음 생성 된 WKUserScript 객체를 WKUserContentController의 addUserScript() 메서드를 사용하여 추가한다.

예를 들어, 쿠키를 추가하려는 경우, WKUserScript를 사용하여 해당 쿠키를 스크립트로 만들고, 이를 WKUserContentController에 추가하여 적용할 수 있다.

하지만 이 방법은 앱이 시작될 때만 적용되며, 이후 웹 페이지가 변경될 때마다 다시 추가해야 한다.

```swift
let cookieScript = WKUserScript.init(source: script source string, injectionTime: .atDocumentStart, forMainFrameOnly: false)

self.userContentController.addUserScript(cookieScript)
```


## Evaluate JavaScript
- [TIL : WebView - 앱에서 웹으로 JavaScript보내기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/WebView_Sending_JS.md)  

evaluateJavaScript() 메서드를 사용하여 iOS 웹뷰에서 동적으로 스크립트를 실행할 수 있다.

이 방법은 웹 페이지가 로드될 때마다 스크립트를 실행할 수 있으며, WKUserContentController와는 달리 페이지가 변경될 때마다 추가하지 않아도 된다.

evaluateJavaScript() 메서드는 첫 번째 인수로 실행할 스크립트 문자열을 받는다. 

이 스크립트는 JavaScript 코드이며, iOS 웹뷰 내에서 실행된다.
두 번째 매개 변수로는 완료 핸들러를 전달하여 스크립트 실행 후 결과를 처리할 수 있다.

예를 들어, 쿠키를 추가하려면 JavaScript로 작성된 쿠키 생성 코드를 문자열로 작성하고 evaluateJavaScript()를 사용하여 해당 코드를 실행할 수 있습다.

```swift
// wv는 WKWebView 객체.

// 스크립트 실행 후 처리할 핸들러를 정의.
let handler: (Any?, Error?) -> Void = { result, error in
    if let error = error {
        print("Error: \(error.localizedDescription)")
    } else {
        print("Result: \(String(describing: result))")
    }
}

// 쿠키를 생성하는 JavaScript 코드를 문자열로 작성.
let cookieScript = """
    var cookieString = "key=value";
    document.cookie = cookieString;
"""

// evaluateJavaScript() 메서드를 사용하여 스크립트를 실행.
wv.evaluateJavaScript(cookieScript, completionHandler: handler)

```

## 두 방법의 차이점

주요 차이점은 WKUserContentController를 사용하는 경우, 앱이 시작될 때만 스크립트가 적용되며,

evaluateJavaScript()를 사용하는 경우, 웹 페이지가 로드될 때마다 스크립트가 실행된다.
 
따라서 적용하는 스크립트의 성격과 목적에 따라 적절한 방법을 선택해야 한다.



