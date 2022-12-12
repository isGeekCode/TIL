# WebView - 스와이프로 리프레시 세팅

웹뷰를 아래로 스와이프하면 리프레시 인디케이터가 생성된다. 
이때 scrollView delegate를 세팅해야하고 
특히 scrollView bounce는 false로 해두면 작동하지 않는다.


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
mainWebView.scrollView.showsVerticalScrollIndicator = false
mainWebView.scrollView.showsHorizontalScrollIndicator = false
```
