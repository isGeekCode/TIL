# Cookie - ios에서 쿠키 다루기

## 여러 웹뷰에서 쿠키 공유하기

- [TIL : Cookie - 여러 웹뷰에서 쿠키 공유하기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_Cookie_sharing.md) 

## 쿠키 가져오기


### evaluateJavaScript 사용하기

- [TIL : Cookie - 현재 웹뷰로 쿠키 가져오기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_cookie_call.md) 
- [TIL : WebView - 앱에서 웹으로 JavaScript보내기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/WebView_Sending_JS.md) 

```swift

웹뷰이름.evaluateJavaScript(script 함수이름 string, completionHandler: { result , error in })

// script source  : document.cookie
```

### WKWebsiteDataStore 을 이용하는 방법 ( ios11 이상 )

- [TIL : WebView - WKWebsiteDataStore 사용하여 웹뷰의 데이터관리하기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_WebView_WKWebsiteDataStore.md) 

```swift
let storage = WKWebsiteDataStore.default().httpCookieStore
storage.getAllCookies { cookies in }
```


## 쿠키 생성하기
 
### WKWebsiteDataStore 을 이용하는 방법 ( ios11 이상 )

- [TIL : WebView - WKWebsiteDataStore 사용하여 웹뷰의 데이터관리하기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_WebView_WKWebsiteDataStore.md) 

```swift
let cookie = HTTPCookie(properties: [
    .domain: "example.com",
    .path: "/",
    .name: "cookie_name",
    .value: "cookie_value"
])!

websiteDataStore.httpCookieStore.setCookie(cookie) {
    print("Cookie added!")
}
```

## 쿠키 삭제하기

- [TIL : WebView - WKWebsiteDataStore 사용하여 웹뷰의 데이터관리하기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_WebView_WKWebsiteDataStore.md) 


### WKWebsiteDataStore 을 이용하는 방법 ( ios11 이상 )

```swift
let storage = WKWebsiteDataStore.default().httpCookieStore
storage.delete(cookie,completionHandler)
```

## 웹뷰간 쿠키공유하기
- [TIL : WKProcessPool - 여러 웹뷰에서 쿠키 공유하기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_Cookie_sharing.md) 
