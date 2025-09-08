# WKWebView 사용하기, 구성 요소 살펴보기


간단한 WKWebView사용법과 구성 요소들을 살펴보자.

## 간단한 사용법

- import WebKit

- WKWebViewConfiguration 객체를 생성하고 웹 페이지 환경 및 설정을 구성.

- WKWebView를 생성하고 구성된 WKWebViewConfiguration 객체를 전달하여 초기화.

- WKWebView를 화면에 추가하거나 서브뷰로 사용합니다.


```swift
import UIKit
import WebKit

class ViewController: UIViewController {
    var webView: WKWebView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 1. WKWebView 및 WKWebViewConfiguration 객체 가져오기
        let configuration = WKWebViewConfiguration()
        
        // 2. WKWebViewConfiguration 객체를 통해 웹 페이지 환경 설정
        // 예를 들어, 웹 페이지 내에서 오디오 및 비디오 미디어를 재생하는 경우
        config.allowsInlineMediaPlayback = true
        
        // 3. WKWebView 생성 및 구성된 WKWebViewConfiguration 객체 전달하여 초기화
        webView = WKWebView(frame: view.bounds, configuration: configuration)
        
        // WKWebView의 네비게이션 델리게이트 설정 (선택 사항)
        webView.navigationDelegate = self
        
        // 4. WKWebView를 화면에 추가하거나 서브뷰로 사용
        view.addSubview(webView)
        
        // 웹 페이지 로드 예시
        let url = URL(string: "https://www.example.com")
        let request = URLRequest(url: url!)
        webView.load(request)
    }
    

} 


// WKNavigationDelegate 메서드 (선택 사항)

exention ViewController: WKNavigationDelegate {

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        // 웹 페이지 로딩이 완료된 후 실행할 코드
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
    
        guard let requestUrl = navigationAction.request.url,
              let urlHost = requestUrl.host else {

            decisionHandler(.cancel)
            return
        }
              
        decisionHandler(.allow)
    }
}

```

## 구성요소

- WkWebView
    - configuration: WKWebViewConfiguration
        - preferences: WKPreferences
            - javaScriptCanOpenWindowsAutomatically: Bool
        - userContentControler: WKUserContentController
        - processPool: WKProcessPool
        - allowsInlineMediaPlayaback: Bool
        - ignoresViewportScaleLimits: Bool




### configuration 

- 웹 페이지 환경 설정: 
    - WKWebView는 웹 페이지를 표시하기 위한 환경을 구현해야한다. WKWebViewConfiguration을 사용하여 웹 페이지의 기본 환경을 설정할 수 있다.
    - 예를 들어, 사용자 에이전트 문자열, 자바스크립트 활성화 여부, 쿠키 및 캐시 관리 등의 설정을 구성할 수 있다.

- JavaScript 환경 설정
    - WKWebView는 웹 페이지에서 JavaScript를 실행하고 상호 작용하는 데 사용된다.
    - avaScript messageHandler를 추가하여 네이티브 코드와의 통신을 설정할 수 있다.

- 웹 페이지 데이터 공유
    - 웹 뷰에서 사용하는 캐시, 쿠키 및 데이터 저장소를 관리할 수 있다. 이를 통해 웹 페이지 간 데이터 공유 및 관리가 가능

- 웹 페이지 컨텐츠 커스터마이징
    - WKWebView를 사용하여 웹 페이지 내용을 조작하고 커스터마이징할 수 있다. 
    - 사용자 정의 스타일 시트, 스크립트 등을 적용할 수 있다.

- 웹 페이지 컨텐츠 로딩 및 페이지 네비게이션 제어
    - 웹 페이지 컨텐츠의 로딩 및 페이지 네비게이션을 관리하고 컨트롤할 수 있다.



### preferences
웹 페이지 환경 설정을 구성하는 속성. 예를 들어, 사용자 에이전트 문자열을 설정하고 JavaScript 활성화 여부를 조절할 수 있다.  


### userContentController
WKUserContentController 객체를 할당하여 웹 페이지와 네이티브 코드 간의 통신 및 JavaScript 메시지 핸들링을 설정할 수 있다.

### processPool
WKProcessPool 객체를 설정하여 WKWebView 인스턴스 간에 데이터 및 쿠키를 공유하는 데 사용된다.
웹 페이지 데이터를 공유하거나 웹 뷰 간에 상태를 공유하려는 경우에 유용합니다. 이를 통해 다양한 WKWebView 인스턴스가 동일한 쿠키, 캐시, 데이터 스토어를 공유할 수 있다.

```swift
let processPool = WKProcessPool()
let configuration = WKWebViewConfiguration()
configuration.processPool = processPool

```


### websiteDataStore
WKWebsiteDataStore 객체를 설정하여 웹 페이지 데이터를 관리하고 로컬 스토리지, 캐시, 쿠키 등을 관리한다.

### allowsInlineMediaPlayback
- WKWebViewConfiguration 클래스의 속성 중 하나.

- `true`로 설정하면 웹 페이지 내에서 오디오 및 비디오 미디어를 인라인으로 웹 페이지 내부에 포함하여 재생할 수 있다.

- `false`로 설정하면 미디어 요소가 기본적으로 별도의 미디어 플레이어나 팝업 창에서 열리며, 웹 페이지 내에서 인라인으로 재생되지 않는다.

```swift
let configuration = WKWebViewConfiguration()
configuration.allowsInlineMediaPlayback = true

```

### ignoresViewportScaleLimits

- WKWebViewConfiguration 클래스의 속성 중 하나.

- `true`로 설정하면 웹 페이지가 설정된 뷰포트 스케일 제한을 무시하고 사용자가 웹 페이지를 확대하거나 축소할 수 있게 된다. 이렇게 하면 사용자가 웹 페이지의 화면 배율을 원하는 대로 조정할 수 있으며, 모바일 디바이스에서 웹 페이지를 보다 편리하게 확대 또는 축소할 수 있다.

- `false`로 설정하면 웹 페이지는 설정된 뷰포트 스케일 제한을 따라야 한다. 이 경우, 웹 페이지의 레이아웃 및 확대/축소가 뷰포트 스케일 제한에 따라 제한된다.

- 이 속성은 사용자 경험과 웹 페이지 레이아웃에 영향을 미치는 중요한 설정 중 하나이며, 웹 페이지가 모바일 디바이스에서 어떻게 표시되는지에 대한 제어를 제공한다.

```swift
let configuration = WKWebViewConfiguration()
configuration.ignoresViewportScaleLimits = true

```
