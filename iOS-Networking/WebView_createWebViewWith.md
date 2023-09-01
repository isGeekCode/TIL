# WebView - createWebViewWith : blank로 새창열기

`webView(_ webView:createWebViewWith configuration:for navigationAction:, windowFeatures:)`
메서드에 대해 알아보자.  


이 메서드는 웹 페이지 내에서 새 창이나 팝업 창을 열 때 호출되는 경우에 사용된다.  

웹에서 blank 타겟을 이용하는 경우에도 이 메서드를 호출하게 된다.  


메서드는 아래와 같이 선언한다.  

```swift
func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {

    return nil
}
```

이 메서드에서 return nil을 한 경우, 이 메서드는 새 창이나 팝업 창을 열지 않고, 기본 동작으로서 해당 창이나 프레임 내에서 웹 페이지를 로드하게 된다.


일반적으로 웹 브라우저는 웹 페이지를 표시하기 위해 현재 창이나 프레임을 사용하려고 한다.

이때, createWebViewWith 메서드를 구현하여 새로운 창이나 팝업을 생성하거나 원하는 동작을 수행할 때만 해당 창이나 프레임이 아닌 다른 창을 열 수 있다. 


```

func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {

    // 원하는 동작을 수행하고, 새 창이나 팝업을 열 필요가 없는 경우
    
    // 예를 들어, 내부에서 웹 페이지를 로드하고 싶을 때
    webView.load(navigationAction.request)
    
    
    return nil
}
```

아래와 같이 현재 url과 requestURL을 분기처리하는 방법도 있다.

또한 아래처럼 외부로 사파리에서 열수도 있다. 
```swift

func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {

    guard let currentURL = webView.url?.absoluteString else { return nil }
    guard let requestURL = navigationAction.request.url?.absoluteString else { return nil }



    // 사파리로 열기   
    if let url = navigationAction.request.url, url.host != webView.url?.host {
    // 외부 도메인의 링크가 클릭되었을 때
    if UIApplication.shared.canOpenURL(url) {
        UIApplication.shared.open(url, options: [:], completionHandler: nil)
    }
}

}
```



## History
- 230901: 초안작성
