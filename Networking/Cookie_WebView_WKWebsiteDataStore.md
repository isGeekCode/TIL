# WebView - WKWebsiteDataStore 사용하여 웹뷰의 데이터관리하기

## WKWebsiteDataStore란
WKWebsiteDataStore는 웹사이트 데이터를 저장하는 객체로,

WKWebView에서 사용되는 쿠키, 캐시, 로컬스토리지 등의 데이터를 관리하는 역할을 한다.

주요 기능은 아래와 같다. 

- 1. 쿠키, 캐시, 로컬스토리지 등의 데이터 관리
WKWebsiteDataStore를 사용하면 웹뷰에서 사용되는 쿠키, 캐시, 로컬스토리지 등의 데이터를 직접 관리할 수 있다.

이를 통해, 웹뷰에서 사용하는 데이터를 정확하게 관리할 수 있다.


- 2. 데이터 분리
WKWebsiteDataStore를 사용하여, 하나의 앱에서 여러 개의 WKWebView를 사용하는 경우,

각각의 WKWebView에서 사용되는 데이터를 분리할 수 있다.

이를 통해, 각각의 WKWebView에서 사용하는 데이터를 구분하여 정확하게 관리할 수 있다.


- 3. 보안
WKWebsiteDataStore를 사용하여, 웹뷰에서 사용하는 데이터를 직접 관리할 수 있기 때문에 보안 측면에서도 유리하다.

WKWebsiteDataStore를 사용하여 데이터를 관리하면, 데이터 누출을 방지할 수 있다.


- 4. 성능 개선
WKWebsiteDataStore를 사용하여, 웹뷰에서 사용하는 데이터를 관리하면 성능을 개선할 수 있다. 

WKWebsiteDataStore는 쿠키, 캐시, 로컬스토리지 등의 데이터를 메모리나 디스크에 저장하고 관리하기 때문에, 웹뷰에서 데이터를 로드할 때 성능이 향상된다.

## WKWebsiteDataStore에서 관리할 수 있는 데이터
웹 뷰에서 필요한 기능에 따라 다양하게 사용된다. 

쿠키를 통해 다양한 정보를 관리할 수 있기때문에, 일반적으로는 쿠키를 관리하는 데 사용한다.

- HTTP 쿠키
- 캐시 데이터
- 인증 자격 증명
- 스토리지 데이터
- WebSQL 데이터베이스 데이터
- IndexedDB 데이터
- 서버 작업자 데이터
- 로컬 스토리지 데이터
- 콘텐츠 색인 데이터


## WKWebsiteDataStore 사용법

### WKWebsiteDataStore 객체를 생성하기

```swift
let websiteDataStore = WKWebsiteDataStore.default()
```

### WKWebViewConfiguration 객체를 생성하기

```swift
let configuration = WKWebViewConfiguration()
```

### WKWebViewConfiguration 객체에 WKWebsiteDataStore 객체를 할당

```swift
configuration.websiteDataStore = websiteDataStore

```

### WKWebView 객체를 생성할 때 변수로 사용하기

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)

```


### httpCookieStore 속성을 사용하여 쿠키를 추가하기

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

### 특정쿠키 삭제하기
```swift
// 삭제할 쿠키 생성
let cookie = HTTPCookie(properties: [
    .domain: "example.com",
    .path: "/",
    .name: "cookie_name",
    .value: "cookie_value"
])!

// 쿠키 삭제
webView.configuration.websiteDataStore.httpCookieStore.delete(cookie) {
    print("쿠키 삭제 완료")
}

//혹은

let cookieName = "cookie_name"

WKWebsiteDataStore.default().httpCookieStore.getAllCookies { cookies in
    let targetCookies = cookies.filter { $0.name == cookieName }
    for cookie in targetCookies {
        WKWebsiteDataStore.default().httpCookieStore.delete(cookie) {
            print("쿠키 삭제 완료: \(cookie.name)")
        }
    }
}
```

### 모든쿠키 삭제하기
```swift
let storage = WKWebsiteDataStore.default().httpCookieStore

    for cookie in cookies {
        WKWebsiteDataStore.default().httpCookieStore.delete(cookie) {
            print("쿠키 삭제 완료: \(cookie.name)")
        }
    }

```
