# WebView - 스와이프로 리프레시 세팅

웹뷰를 아래로 스와이프하면 새로고침 되는 경험이 있을 것이다. 

아이폰의 웹뷰에는 scrollView가 있고 여기에는  refresh control이라 부르는 것을  세팅할 수 있다. 

이때 scrollView delegate를 세팅해야하고 특히 scrollView bounce는 false로 해두면 작동하지 않는다.

```swift
let mainWebView = WKWebView()
let refreshControl = UIRefreshControl()

self.mainWebView.scrollView.addSubview(refreshControl)

refreshControl.addTarget(self, action: #selector(reloadWebView(_:)), for: .valueChanged)

/// 웹뷰 리프레시
    @objc func reloadWebView(_ sender: UIRefreshControl) {
        self.mainWebView.reload()
        sender.endRefreshing()
    }

mainWebView.scrollView.delegate = self
mainWebView.scrollView.bounces = true
mainWebView.scrollView.alwaysBounceVertical = false
```
