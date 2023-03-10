# WebView - 앱에서 웹으로 JavaScript보내기

 웹뷰를 세팅할 때, 앱과 웹이 서로 소통하는 방법은 다양하다. 
 그중 웹에서 javascript를 세팅하고 그 함수를 앱에서 호출할 수가 있다.
 그럴 때 아래코드와 같이 사용이 가능하다. 

```swift

/// 웹뷰로 javascript 전송
public func sendJavaScript(param prm: String) {
    let jsonfunc =  "showMyFavorite('\(prm)')"
    self.mainWebView.evaluateJavaScript(jsonfunc) { (result, error) in

        if let error = error {
            print("error :: \(error)")
        }

        if let result = result {
            print("result :: \(result)")
        }
    }
}

```
이렇게 javascript를 세팅해도 가끔씩 아래 에러가 나는 경우가 있다.

```
error :: Error Domain=WKErrorDomain Code=4 "A JavaScript exception occurred" UserInfo={WKJavaScriptExceptionLineNumber=0, WKJavaScriptExceptionMessage=TypeError: undefined is not a function, WKJavaScriptExceptionColumnNumber=0, NSLocalizedDescription=A JavaScript exception occurred}
```

이 에러는 웹에 javaScript함수가 세팅되지않았을 때 생긴다. 놀라지 말자. 
내가 함수를 잘못만들었거나 웹에서 아직 개발안된 것일 가능성이 높다. 얼른 개발하고 기다리는 중이라고 생색내면 된다. 
