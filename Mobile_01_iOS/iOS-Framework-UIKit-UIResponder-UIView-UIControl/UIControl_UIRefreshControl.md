# UIRefreshControl

웹뷰나 테이블뷰 등을 스크롤하면서 로딩 인디케이터가 나오고 일정 이상 드래그하면 새로고침이 되는 것을 본적이 있을것이다. 이 때 사용하는 것이 UIRefreshControl객체이다. 

이 사례는 웹뷰에서 사용하기 위해 정리하는 내용이다. 

절차는 아래와 같다. 

## Step1. refreshControl init

```swift
let refreshControl = UIRefreshControl()

```

## Step2. refreshControl에 넣어줄 함수 세팅

```swift
/// 웹뷰 리프레시
@objc func reloadWebView(_ sender: UIRefreshControl) {
    print("refresh")
    self.mainWebView.reload()
    sender.endRefreshing()
}
```

## Step3. refreshControl에 넣어줄 함수 addTarget

```swift
refreshControl.addTarget(self, action: #selector(reloadWebView(_:)), for: .valueChanged)

```

## Step4. 완성한 refreshControl을 넣어줄 refreshControl 변수에 넣어준다.

→ 웹뷰에는 scrollView가 포함되어있고 scrollView는 refreshControl 변수를 가지고 있다.

```swift
mainWebView.scrollView.refreshControl = refreshControl
```

## Step5. 웹뷰인경우는 ScrollView의 delegate와  bounce를 확인

 

```swift
mainWebView.scrollView.delegate = self
mainWebView.scrollView.bounces = true
mainWebView.scrollView.alwaysBounceVertical = false

```

# 전체코드

```swift
let refreshControl = UIRefreshControl()

refreshControl.addTarget(self, action: #selector(reloadWebView(_:)), for: .valueChanged)
mainWebView.scrollView.refreshControl = refreshControl
// 필수
mainWebView.scrollView.bounces = true

/// 웹뷰 리프레시
@objc func reloadWebView(_ sender: UIRefreshControl) {
    print("refresh")
    self.mainWebView.reload()
    sender.endRefreshing()
}

mainWebView.scrollView.delegate = self
mainWebView.scrollView.bounces = true
mainWebView.scrollView.alwaysBounceVertical = false
```
