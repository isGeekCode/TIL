# NSObject_UIResponder_UIView_UIActivityIndicatorView_만들기

앱을 구현할 때, 로직상 기다려야하는 경우, 사용자에게 로딩을 알려주는 객체가 있다.
아래 그림을 보면 iOS, Android 사용자들은 각자의 사용자 경험을 떠올려보자. 

![activityindicators-default](https://user-images.githubusercontent.com/76529148/215659312-7da24c9c-5691-4536-a3d1-aa19c1c6c1a2.png)

로직상 작업이 시작되는 부분에서 로딩뷰를 시작하고, 끝나는 부분에서 사라지게 하면 된다. 


## 객체 생성하기
웹뷰에 세팅을 하는 경우
```swift

class MainViewController {

    var indicator = UIActivityIndicatorView()

    // 세팅
    func setIndicator(wkWebView: WKWebView, indicator: UIActivityIndicatorView) {
        wkWebView.addSubview(indicator)
        indicator.translatesAutoresizingMaskIntoConstraints = false

        NSLayoutConstraint.activate([
            indicator.centerXAnchor.constraint(equalTo: wkWebView.centerXAnchor),
            indicator.centerYAnchor.constraint(equalTo: wkWebView.centerYAnchor),
        ])

        indicator.style = .large
    }



}

```
## 싱글톤 객체 생성하기
- 여러곳에서 전역적으로 인디케이터를 사용해야할 때가 있다. 그때마다 객체를 만들수 없기때문에 싱글톤을 생성한다. 
- 탑뷰가 아니라 특정뷰, 특히 웹뷰에 대한 로딩을 해야할 상황이 있다. 이때 웹뷰의 바로위에 로딩뷰를 배치하기 위해선 두번째 함수를 사용한다. 
```
class CustomIndicator {
    private var activityIndicatorView = UIActivityIndicatorView()
    
    static var shared = CustomIndicator()

    private init() { }
    
    /// 로딩뷰를 시작하는 함수
    func startAnimating(view: UIView = (UIApplication.topViewController()?.view)!) {
        view.addSubview(activityIndicatorView)
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false

        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])

        activityIndicatorView.style = .large
        activityIndicatorView.startAnimating()
    }
    /// 로딩비률 해당 웹뷰 바로위에만 둬야하는경우
    func startAnimating(webView: WkWebView, view: UIView = (UIApplication.topViewController()?.view)!) {
        webView.addSubview(activityIndicatorView)
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false

        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: webView.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: webView.centerYAnchor),
        ])

        activityIndicatorView.style = .large
        activityIndicatorView.startAnimating()
    }
    
    /// 로딩뷰를 종료하는 함수
    func stopAnimating() {
        activityIndicatorView.stopAnimating()
        activityIndicatorView.removeFromSuperview()
    }
    
    
}

```


### 사용하기
- `startAnimating()`를 통해 시작
- `stopAnimating()`를 통해 정지

만약 웹뷰에서 사용한다면 로딩이 시작하는 부분에 startAnimating, 로딩이 끝날 부분에 stopAnimating를 넣어준다.
- 주의할 점은 에러가 날때도 stopAnimating이 선언되어야한다는 것이다.

```

        /// 웹뷰가 메인 프레임에 대한 콘텐츠를 받기 시작할 때 호출되는 메서드
    func webView(_ webView: WKWebView, didCommit navigation: WKNavigation!) {
        
        guard let url = webView.url else { return }
        indicator.startAnimating()
    }
    
    
    /// 웹뷰가 콘텐츠 받기(navigation)를 완료했을 때 호출되는 메서드
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        
        guard let url = webView.url else { return }
        indicator.stopAnimating()
    }
```
