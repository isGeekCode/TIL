# Cookie - 현재 웹뷰로 쿠키 가져오기
앱에서는 현재 웹뷰에서 소유한 쿠키정보가 필요한 경우가 있다.  이때, 쿠키를 가져오려면 어떻게 해야하는지 알아보자.  



## 1. evaluateJavaScript 사용
- [TIL : WebView - 앱에서 웹으로 JavaScript보내기 참고](https://github.com/isGeekCode/TIL/blob/main/Networking/WebView_Sending_JS.md) 


웹에는 JavaScript코드로 document.cookie라는 메서드를 실행할 수 있다.  
이 메서드를 실행하면 현재 웹페이지의 쿠키를 가져올 수 있는데,  
웹뷰에서 javaScript 코드를 실행시킬때 사용하는 evaluateJavaScript를 통해 사용할 수 있다.  

다만 이 방식으로는 제한사항이 있다.  `document.cookie`가 모든 쿠키를 반환하지 않을 수 있다는 점이다.   
또한 일부 쿠키는 HTTPOnly 속성 때문에 JavaScript로 접근할 수 없을 수 있다.  


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

iOS11 이후부터는 WKWebsiteDataStore를 이용해 웹뷰의 configuration 속성에서 websiteDataStore에 접근하여 쿠키를 관리할 수 있다.  

이 방법을 사용하면 HTTPOnly 쿠키에도 접근할 수 있고, 쿠키를 추가하거나 삭제하는 등 더 많은 제어가 가능하게 된다.  

```swift
let storage = WKWebsiteDataStore.default().httpCookieStore

storage.getAllCookies { cookies in }
```


## Story

옛날 옛적에, iOS 개발자라는 용감한 마법사가 있었어요. 그는 ‘WKWebView’라는 마법의 창을 통해 웹의 세계를 탐험하고 싶었죠. 그의 목표는 웹 페이지들이 숨기고 있는 비밀, 바로 ‘쿠키’들을 찾아내는 것이었습니다.

개발자는 ‘evaluateJavaScript’라는 강력한 마법을 사용하기로 했어요. 이 마법은 ‘WKWebView’를 통해 웹 페이지에 숨겨진 JavaScript 마법을 실행시키는 데 사용되었죠. 그는 ‘document.cookie’라는 주문을 외워, 페이지 안에 숨겨진 쿠키들을 드러내려고 했습니다.

마법 주문을 외우자, 많은 쿠키들이 나타났어요. 하지만 일부 쿠키들은 ‘HTTPOnly’라는 강력한 보호 마법 때문에 숨겨져 있었죠. 이를 깨닫고, 용감한 개발자는 또 다른 방법을 찾기 시작했습니다.

그는 ‘WKWebsiteDataStore’라는 더 강력한 마법을 발견했어요. 이 마법을 사용하면, HTTPOnly 쿠키들도 포함하여 모든 쿠키들을 부를 수 있었죠. 개발자는 이 마법을 사용하여 모든 쿠키들과 만나고, 그들의 비밀스런 이야기를 들을 수 있었습니다.

이렇게 용감한 개발자는 ‘WKWebView’, ‘evaluateJavaScript’, 그리고 ‘WKWebsiteDataStore’의 마법을 통해 웹의 세계를 탐험하며 많은 지식을 얻었다고 합니다.

