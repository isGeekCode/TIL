# webview - 바운스 효과 제거하기


iOS의 웹뷰에서 바운스효과가 기본값으로 들어가있다.
바운스효과란 가장자리까지 드래그를 했을 때, ScrollView의 움직임에 반동이 생기는 것을 말한다.

webview안에는 scrollView가 들어있어서 접근할 수 있게된다. 

```swift
let mainWebView = WKWebView()

mainWebView.scrollView.bounces = false
mainWebView.scrollView.alwaysBounceVertical = false
```
