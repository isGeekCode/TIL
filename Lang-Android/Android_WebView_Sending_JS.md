# Android - WebView : 앱에서 웹으로 JavaScript 보내기

 웹뷰를 세팅할 때, 앱과 웹이 서로 소통하는 방법은 다양하다. 
 그중 웹에서 javascript를 세팅하고 그 함수를 앱에서 호출할 수가 있다.


## LoadUrl
기본적으로 WebView.loadUrl(String) 함수를 이용하고
다음과 같은 형태로 사용한다.



```kotlin
/// 웹뷰로 javascript 전송
webView.loadUrl("javascript:sum(1,2)")
```


## evaluateJavaScript : 반환값을 캐치 가능한 함수
```kotlin
// 반환 값이 필요 없는 경우
evaluateJavascript("javascript:sum(1,2)", null)

// 반환 값이 필요한 경우
evaluateJavascript("javascript:sum(1,2)") { value ->
    // handle value
}
```
  
[참고링크](https://developer-munny.tistory.com/9)  