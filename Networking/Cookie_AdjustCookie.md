# Cookie - ios에서 쿠키 다루기

## 여러 웹뷰에서 쿠키 공유하기

- [TIL : Cookie - 여러 웹뷰에서 쿠키 공유하기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/Cookie_Cookie_sharing.md) 

## 쿠키 가져오기


## 쿠키 생성하기
 
### 1. evaluateJavaScript 사용하기

- [TIL : WebView - 앱에서 웹으로 JavaScript보내기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/WebView_Sending_JS.md) 

```swift

웹뷰이름.evaluateJavaScript(script 함수이름 string, completionHandler: { result , error in })

// script source  : document.cookie
```

### 2. WKWebsiteDataStore 을 이용하는 방법 ( ios11 이상 )

```swift
let storage = WKWebsiteDataStore.default().httpCookieStore
storage.getAllCookies { cookies in }
```
 

## 쿠키 삭제하기

### WKWebsiteDataStore 을 이용하는 방법 ( ios11 이상 )

```swift
let storage = WKWebsiteDataStore.default().httpCookieStore
storage.delete(cookie,completionHandler)
```
