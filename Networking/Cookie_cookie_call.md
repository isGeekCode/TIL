# Cookie - 현재 웹뷰로 쿠키 가져오기

## 1. evaluateJavaScript 사용

- [TIL : WebView - 앱에서 웹으로 JavaScript보내기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/WebView_Sending_JS.md) 

- script source : document.cookie

```swift
let javascript = "document.cookie"
webView.evaluateJavaScript(javascript) { (result, error) in
    if let error = error {
        print("Error getting cookie: \(error.localizedDescription)")
    } else if let result = result as? String {
        print("Cookie: \(result)")
    }
}
```
 
## 2. WKWebsiteDataStore 을 이용하는 방법 ( ios11 이상 )

- [TIL : WebView - WKWebsiteDataStore 사용하여 웹뷰의 데이터관리하기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_WebView_WKWebsiteDataStore.md) 

```swift
let storage = WKWebsiteDataStore.default().httpCookieStore

storage.getAllCookies { cookies in }
```

